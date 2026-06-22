#!/usr/bin/env python3
"""Static-site renderer — turns PUBLISHABLE (expert-signed) entries into a
GitHub-Pages-friendly static site under site/.

Design (per CLAUDE.md):
- Renders ONLY publishable entries (reuses bin/check_publish.py — unsigned drafts
  never reach the page; "草稿可提交,发布需签字").
- Separates the three signals visually — authority(权威) / popularity(人气·非质量)
  / capability(能力)— so a reader never mistakes likes for quality.
- Foregrounds the expert verdict + confidence, the layer aggregators can't give.

Zero extra deps beyond pyyaml. Minimal inline Markdown (bold/italic/code/paragraphs).
Usage: python3 bin/render_site.py   →   writes site/index.html, site/<id>.html, site/style.css
"""
import html
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "bin"))
OUT = os.path.join(ROOT, "site")


def load():
    try:
        import yaml
    except ImportError:
        print("FATAL: pip install pyyaml", file=sys.stderr)
        sys.exit(2)
    import check_publish as cp
    schema = __import__("json").load(open(os.path.join(ROOT, "schema", "entry.schema.json")))
    return yaml, cp, schema


def split_body(text):
    """Return (agent_summary_html, expert_verdict_html) from the markdown body."""
    def section(name):
        m = re.search(rf"^## {name}\s*\n(.*?)(?=^## |\Z)", text, re.S | re.M)
        if not m:
            return ""
        body = re.sub(r"<!--.*?-->", "", m.group(1), flags=re.S).strip()
        return md(body)
    return section("Agent summary"), section("Expert verdict")


def md(s):
    """Tiny Markdown → HTML for the subset used (paragraphs, **bold**, *italic*, `code`)."""
    out = []
    for para in re.split(r"\n\s*\n", s.strip()):
        if not para.strip():
            continue
        t = html.escape(para.strip())
        t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
        t = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", t)
        t = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", t)
        t = t.replace("\n", " ")
        out.append(f"<p>{t}</p>")
    return "\n".join(out)


def chips(items, cls="chip"):
    return "".join(f'<span class="{cls}">{html.escape(str(i))}</span>' for i in (items or []))


def lst(items):
    if not items:
        return ""
    return "<ul>" + "".join(f"<li>{html.escape(str(i))}</li>" for i in items) + "</ul>"


def conf_badge(c):
    c = (c or "").lower()
    return f'<span class="conf conf-{html.escape(c)}">{html.escape(c) or "—"}</span>'


def page(title, body, depth_to_root="."):
    return f"""<!doctype html>
<html lang="zh"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<link rel="stylesheet" href="{depth_to_root}/style.css"></head>
<body><a id="top"></a><main>{body}</main>
<footer>AgentBench · 主观榜单评议。别的榜告诉你“谁排第几”,这里告诉你“这个榜该不该信”。</footer>
</body></html>"""


def render_entry(e, body_md):
    fm = e
    agent_html, verdict_html = split_body(body_md)
    ev = fm.get("expert_verdict") or {}

    # --- authority ---
    auth = fm.get("authority", {})
    cites = fm.get("citations", []) or []
    cite_html = "".join(
        f'<li><a href="{html.escape(c.get("url",""))}" target="_blank" rel="noopener">{html.escape(c.get("title",""))}</a>'
        f' <span class="muted">· {html.escape(c.get("accessed",""))}</span></li>'
        for c in cites)
    auth_rows = [("维护方 maintainers", ", ".join(auth.get("maintainers", []) or [])),
                 ("机构数 institutions", auth.get("institution_count", "—")),
                 ("更新节奏 cadence", auth.get("update_cadence", "—")),
                 ("在线榜 online", "是" if auth.get("online") else "否")]
    cc = auth.get("citation_count")
    if cc:
        auth_rows.append(("引用数 citations", f'{cc.get("value")} ({html.escape(cc.get("source",""))}, {html.escape(cc.get("as_of",""))})'))
    auth_tbl = "".join(f"<tr><th>{html.escape(k)}</th><td>{html.escape(str(v))}</td></tr>" for k, v in auth_rows)

    # --- popularity ---
    pop = fm.get("popularity") or {}
    social = pop.get("social", []) or []
    soc_html = "".join(
        f'<li><a href="{html.escape(s.get("url",""))}" target="_blank" rel="noopener">'
        f'{html.escape(s.get("platform","").upper())}{" · "+html.escape(s.get("handle","")) if s.get("handle") else ""}</a>'
        f' <span class="muted">{html.escape(s.get("note",""))}</span></li>' for s in social)
    pop_bits = []
    if pop.get("hf_space"):
        pop_bits.append(f'<a href="{html.escape(pop["hf_space"])}" target="_blank" rel="noopener">HF Space</a>')
    if "hf_likes" in pop:
        pop_bits.append(f'❤ {pop["hf_likes"]}')
    if pop.get("trending"):
        pop_bits.append("trending")
    pop_inner = (" · ".join(pop_bits) or "<span class='muted'>无显著人气数据</span>") + (f"<ul>{soc_html}</ul>" if soc_html else "")

    # --- capability ---
    ranks = fm.get("models_ranked", []) or []
    if ranks:
        rows = "".join(
            f'<tr><td>{html.escape(str(r.get("model","")))}</td><td>{html.escape(str(r.get("axis","")))}</td>'
            f'<td>{html.escape(str(r.get("rank","")))}</td><td>{html.escape(str(r.get("license","")))}</td>'
            f'<td class="muted">{html.escape(str(r.get("note","")))}</td></tr>' for r in ranks)
        cap_html = f'<table class="rank"><tr><th>模型</th><th>轴 axis</th><th>名次</th><th>许可</th><th>备注</th></tr>{rows}</table>'
    else:
        cap_html = '<p class="muted">无榜内排名（本身不是排名榜 / 数据集）。</p>'

    moa = fm.get("moa", {})
    fresh = fm.get("freshness", {})
    one = ev.get("one_liner")

    body = f"""
<p><a href="./index.html">← 返回总览</a></p>
<h1>{html.escape(fm.get("name",""))} {conf_badge(ev.get("confidence"))}</h1>
<p class="badges">{chips([fm.get("genre","")], "chip genre")}{chips(fm.get("domain",[]))}{chips((moa or {}).get("modalities",[]), "chip mod")}</p>
<p class="muted">{html.escape(fm.get("year","") and str(fm.get("year")) or "")} · <a href="{html.escape(fm.get("homepage",""))}" target="_blank" rel="noopener">{html.escape(fm.get("homepage",""))}</a>
 · freshness: <b>{html.escape(fresh.get("status","—"))}</b> <span class="muted">{html.escape(fresh.get("note",""))}</span></p>

<section class="verdict">
  <h2>专家判语 Expert verdict {conf_badge(ev.get("confidence"))}</h2>
  {f'<p class="oneliner">“{html.escape(one)}”</p>' if one else ''}
  {verdict_html or '<p class="muted">(未署名)</p>'}
  <p class="sig">— 署名 {html.escape(ev.get("signed_by","?"))} · {html.escape(ev.get("signed_date",""))}</p>
</section>

<section><h2>它是什么 Agent summary <span class="tag">事实 · AI 整理</span></h2>{agent_html}</section>

<div class="signals">
  <section class="sig-auth"><h3>① 权威 Authority<br><span class="muted">学术/机构/引用</span></h3><table>{auth_tbl}</table>
    {f'<h4>引用</h4><ul class="cites">{cite_html}</ul>' if cite_html else ''}</section>
  <section class="sig-pop"><h3>② 人气 Popularity<br><span class="muted warn">≠ 质量</span></h3>{pop_inner}</section>
  <section class="sig-cap"><h3>③ 能力 Capability<br><span class="muted">榜内排名</span></h3>{cap_html}</section>
</div>

<section class="moa"><h2>拿它挑模型用（MoA 选型输入）<br><span class="muted">如果你要把几个模型搭成团队,这里是从这个榜能取到的参考</span></h2>
  <p><b>能力轴</b> {chips(moa.get("capability_axes",[]))}</p>
  <p><b>模态</b> {chips(moa.get("modalities",[]),"chip mod")} &nbsp; <b>部署</b> {chips(moa.get("access",[]),"chip acc")}</p>
  <h4>适合 recommended for</h4>{lst(moa.get("recommended_for",[]))}
  <h4>注意 caveats</h4>{lst(moa.get("caveats",[]))}
</section>
<p class="backtop"><a href="#top">↑ 返回顶部</a> · <a href="./index.html">← 返回总览</a></p>
"""
    return page(fm.get("name", "entry") + " · AgentBench", body)


GENRE_ZH = {
    "online-leaderboard": "在线排行榜",
    "shared-task": "公开评测任务",
    "paper-bound": "随论文发布",
    "aggregator": "榜中榜（聚合器）",
    "dataset": "数据集",
}


def render_index(entries):
    rows = []
    for fm, _ in entries:
        ev = fm.get("expert_verdict") or {}
        med_row = "medical" in (fm.get("domain") or [])
        dom = "medical" if med_row else "non-medical"
        dom_label = "医疗" if med_row else "非医疗"
        genre = fm.get("genre", "")
        one = (ev.get("one_liner") or "").strip()
        rows.append(
            f'<tr data-domain="{dom}" data-genre="{html.escape(genre)}"'
            f' data-conf="{html.escape((ev.get("confidence") or ""))}" data-year="{html.escape(str(fm.get("year","") or ""))}"'
            f' data-name="{html.escape((fm.get("name","") or "").lower())}">'
            f'<td><a href="./{html.escape(fm["id"])}.html">{html.escape(fm.get("name",""))}</a> <span class="muted">{html.escape(str(fm.get("year","") or ""))}</span></td>'
            f'<td><span class="chip genre">{html.escape(GENRE_ZH.get(genre, genre))}</span></td>'
            f'<td>{dom_label}</td>'
            f'<td>{chips((fm.get("moa") or {}).get("modalities",[]),"chip mod")}</td>'
            f'<td>{conf_badge(ev.get("confidence"))}</td>'
            f'<td class="muted">{html.escape(one)}</td></tr>')
    med = sum(1 for fm, _ in entries if "medical" in (fm.get("domain") or []))
    body = f"""
<h1>AgentBench · 主观榜单评议</h1>
<p class="lede">市面上有一堆“AI 排行榜”在比谁的模型更强。这个站做的是另一件事:请一位专家逐个点评<strong>这些榜本身值不值得信</strong>,以及看榜时最容易踩的坑。</p>

<details class="explainer" open>
  <summary>一分钟看懂（不需要 AI 背景）</summary>
  <p>AI 排行榜（leaderboard）有点像手机跑分:让很多 AI 模型做同一套题,按得分排名次。
  麻烦在于,分高不等于真好用——题目可能早被模型“背”过,有的榜还是某家公司自己办、给自家产品打广告。</p>
  <p>所以这里不排“谁第几名”,而是请专家回答三件事:这个榜<b>可不可信</b>、高分到底<b>换来了什么真本事</b>、
  要不要照着它<b>挑模型用</b>。每条都标了专家的<b>信心</b>（高 / 中 / 低）,你可以只信你愿意信的那部分。</p>
</details>

<details class="explainer">
  <summary>先认识几个词</summary>
  <ul class="glossary">
    <li><b>榜单 / leaderboard</b>:给 AI 模型打分排名的网页或论文。</li>
    <li><b>判语</b>:专家看完一个榜后写下的主观结论。它是本站的核心,由真人署名,不是 AI 代写。</li>
    <li><b>聚合器 / aggregator</b>:把很多榜的结果汇到一起的“榜中榜”。它告诉你谁在榜上,但不替你判断该不该信。</li>
    <li><b>MoA</b>:把好几个 AI 模型像团队一样搭着用,各管自己擅长的一块。要决定让谁进这个团队,就用得上这些榜做参考。</li>
  </ul>
</details>

<p class="muted">已收录 {len(entries)} 条 · 医疗 {med} / 非医疗 {len(entries)-med} · 只显示专家已署名的条目。</p>

<div class="filters">
  <label>领域 <select id="f-domain"><option value="">全部</option><option value="medical">医疗</option><option value="non-medical">非医疗</option></select></label>
  <label>类型 <select id="f-genre"><option value="">全部</option>
    <option value="online-leaderboard">在线排行榜</option><option value="shared-task">公开评测任务</option><option value="paper-bound">随论文发布</option>
    <option value="aggregator">榜中榜（聚合器）</option><option value="dataset">数据集</option></select></label>
  <label>排序 <select id="f-sort">
    <option value="default">默认（名称）</option>
    <option value="conf">专家信心 高→低</option>
    <option value="year">年份 新→旧</option>
  </select></label>
  <input id="f-text" placeholder="搜索名称…">
</div>

<table id="grid"><thead><tr><th>榜单</th><th>类型</th><th>领域</th><th>能处理什么</th><th>专家信心</th><th>一句话判语</th></tr></thead>
<tbody>{''.join(rows)}</tbody></table>

<script>
const g=document.getElementById('grid'),fd=document.getElementById('f-domain'),
fg=document.getElementById('f-genre'),fs=document.getElementById('f-sort'),ft=document.getElementById('f-text');
const CONF={{high:3,medium:2,low:1,'':0}};
function flt(){{const d=fd.value,ge=fg.value,t=ft.value.toLowerCase();
for(const r of g.tBodies[0].rows){{
 const ok=(!d||r.dataset.domain===d)&&(!ge||r.dataset.genre===ge)&&(!t||r.dataset.name.includes(t));
 r.style.display=ok?'':'none';}}}}
function srt(){{const tb=g.tBodies[0],rs=[...tb.rows],m=fs.value;
 rs.sort((a,b)=>{{
  if(m==='conf') return (CONF[b.dataset.conf]||0)-(CONF[a.dataset.conf]||0)||a.dataset.name.localeCompare(b.dataset.name);
  if(m==='year') return (+b.dataset.year||0)-(+a.dataset.year||0)||a.dataset.name.localeCompare(b.dataset.name);
  return a.dataset.name.localeCompare(b.dataset.name);}});
 rs.forEach(r=>tb.appendChild(r));}}
[fd,fg].forEach(e=>e.onchange=flt);ft.oninput=flt;fs.onchange=srt;
</script>
"""
    return page("AgentBench · 主观榜单评议", body)


CSS = """
html{scroll-behavior:smooth}
:root{--ink:#1a1a1a;--muted:#666;--line:#e3e3e3;--accent:#2b6cb0;
--auth:#2f855a;--pop:#b7791f;--cap:#2b6cb0;--bg:#fbfbfa}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);
font:16px/1.65 -apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Microsoft YaHei",sans-serif}
main{max-width:920px;margin:0 auto;padding:28px 20px 60px}
footer{max-width:920px;margin:0 auto;padding:20px;color:var(--muted);font-size:13px;border-top:1px solid var(--line)}
a{color:var(--accent);text-decoration:none}a:hover{text-decoration:underline}
h1{font-size:1.9rem;margin:.2em 0}.lede{font-size:1.15rem}
.explainer{background:#fff;border:1px solid var(--line);border-radius:8px;padding:6px 16px;margin:12px 0}
.explainer[open]{padding-bottom:12px}
.explainer summary{cursor:pointer;font-weight:600;padding:8px 0}
.explainer p{margin:.5em 0}
.glossary{padding-left:18px;margin:.4em 0}.glossary li{margin:.35em 0}
.muted{color:var(--muted);font-size:.9em}.warn{color:var(--pop);font-weight:600}
.badges{margin:.2em 0}.tag{font-size:.7rem;background:#eef;color:#446;padding:2px 7px;border-radius:10px;vertical-align:middle}
.chip{display:inline-block;background:#eee;border-radius:11px;padding:1px 9px;margin:2px;font-size:.8rem}
.chip.genre{background:#e6effa;color:#234e80}.chip.mod{background:#eaf6ee;color:#246b40}
.chip.acc{background:#faf0e6;color:#7a4a14}
.conf{font-size:.72rem;padding:2px 9px;border-radius:11px;vertical-align:middle;font-weight:700}
.conf-high{background:#d7f0dd;color:#1d6b37}.conf-medium{background:#fdeecb;color:#86600f}
.conf-low{background:#eee;color:#555}
table{border-collapse:collapse;width:100%;margin:.6em 0;font-size:.93rem}
th,td{border:1px solid var(--line);padding:7px 9px;text-align:left;vertical-align:top}
#grid td:first-child{font-weight:600}
.verdict{background:#fff;border:1px solid var(--line);border-left:5px solid var(--accent);
border-radius:8px;padding:14px 18px;margin:18px 0}
.verdict .oneliner{font-size:1.15rem;font-weight:600;margin:.2em 0}
.verdict .sig{color:var(--muted);font-size:.85rem;text-align:right;margin:.4em 0 0}
.signals{display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px;margin:16px 0}
.signals section{border:1px solid var(--line);border-radius:8px;padding:10px 12px;background:#fff}
.signals h3{margin:.1em 0 .5em;font-size:.95rem}
.sig-auth{border-top:4px solid var(--auth)}.sig-pop{border-top:4px solid var(--pop)}
.sig-cap{border-top:4px solid var(--cap)}
.signals table th{width:46%;font-weight:600;background:#fafafa}
.cites{padding-left:18px;font-size:.85rem}.rank{font-size:.82rem}
.moa{background:#fff;border:1px solid var(--line);border-radius:8px;padding:10px 18px;margin:16px 0}
.filters{display:flex;gap:14px;flex-wrap:wrap;align-items:center;margin:14px 0}
.filters select,.filters input{padding:5px 8px;font-size:.9rem}
.backtop{margin:22px 0 0;font-size:.9rem;border-top:1px solid var(--line);padding-top:12px}
@media(max-width:680px){.signals{grid-template-columns:1fr}}
"""


def main():
    yaml, cp, schema = load()
    os.makedirs(OUT, exist_ok=True)
    import glob
    entries = []
    for path in sorted(glob.glob(os.path.join(ROOT, "entries", "*.md"))):
        if os.path.basename(path).startswith("_"):
            continue
        if cp.check_entry(path, schema, yaml, __import__("jsonschema").Draft202012Validator):
            continue  # not publishable → skip (unsigned/invalid)
        text = open(path, encoding="utf-8").read()
        fm = yaml.safe_load(re.match(r"^---\n(.*?)\n---", text, re.S).group(1))
        entries.append((fm, text))

    if not entries:
        print("no publishable entries — nothing rendered (sign some first).")
        return 0

    open(os.path.join(OUT, "style.css"), "w", encoding="utf-8").write(CSS)
    open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(render_index(entries))
    for fm, text in entries:
        open(os.path.join(OUT, fm["id"] + ".html"), "w", encoding="utf-8").write(render_entry(fm, text))
    print(f"rendered {len(entries)} entries → {os.path.relpath(OUT, ROOT)}/ (index.html + {len(entries)} pages + style.css)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
