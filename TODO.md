# TODO

后续要做的事。已完成的设计与约定见 [CLAUDE.md](CLAUDE.md);收录方法见 [docs/SOURCING.md](docs/SOURCING.md)。

## 1. 签字(人在环中 · 最高优先)
> 最新计数与待签清单见文末**进度快照**(本节早期计数已过时)。
- 流程提醒:在自己的编辑器里改(不是工具调用,`guard_verdict.py` 不拦你);判语写在 `<!-- -->` 之外;`signed_date` 加引号;`confidence` ∈ {low,medium,high};改完 `python3 bin/check_publish.py entries/<id>.md` 应翻成 OK。

## 2. 渲染:静态站点
- [x] **`bin/render_site.py`** —— 零额外依赖渲染器,**只渲染已签发(publishable)条目**(复用 check_publish);输出 `site/`(index + 每条详情 + style.css)。三轴信号(权威/人气/能力)视觉分离,专家判语置顶。本地预览:`python3 bin/render_site.py && python3 -m http.server -d site`。
- [x] **GitHub Pages 部署 workflow**:`.github/workflows/pages.yml` —— push 时 `check_publish --schema-only`(硬门禁)→ `render_site`(只发已签字)→ 部署 `site/`(`configure-pages enablement:true` 自启用)。新草稿不会弄垮构建,只是不上线。
- [x] **已上线**:<https://chenhaodev.github.io/agentbench/>(repo: chenhaodev/agentbench,public)。build ✓ + deploy ✓,14 条全部在线。
- [x] Actions 升到支持 Node 24 的主版本(checkout@v6/setup-python@v6/configure-pages@v6/upload-pages-artifact@v5/deploy-pages@v5);CI 已验证绿。
- [x] 首页按 confidence / year 排序;详情页"返回顶部" + 平滑滚动。

## 3. 广度:继续去医疗偏斜(当前 6/14 非医疗)
- [ ] 非医疗锚点(事实已备好):**EQ-Bench**(情商,原始 brief 点名)、**MTEB**(向量检索)、**Open LLM Leaderboard**(通用,v1→v2)。
- [ ] Qwen3-Omni 报告里的多模态候选:**MathVista / DocVQA / OCRBench / GPQA / AIME25 / BFCL-v3 / Arena-Hard** 等(见 SOURCING.md 的"tech report"来源)。

## 4. 覆盖缺口(来自 docs/SOURCING.md)
- [ ] `aggregator`、`dataset` 已各 1 条,但仍单薄;每个 `genre` 至少多覆盖一个领域。
- [x] **MEDIQA 系列 2023 之后**的年份 / 同族 shared task → `mediqa-series`(待签)。
- [ ] 跑 genre / 去偏斜报告作为常规体检(脚本已在会话中验证可用,可固化进 Makefile/CI)。

## 5. 工具与门禁增强(可选)
- [x] `bin/check_publish.py` 增加 **stale `as_of` 告警**(> 365 天,非阻断 WARN)反映"判语会过期"。
- [ ] 把 **cross-report 引用频次**做成结构化的 `popularity` 子信号(比 HF likes 更严谨)。
- [ ] 引用 URL 的**可解析性**目前只查形状(不联网);如需联网校验,单独做 CI step,勿放进 hook。
- [ ] 评估是否需要 `Makefile`(对标 med-agent-verifier 的可发现 target 约定)。

## 6. 收尾
- [ ] 待 `TASK.md` 意图被 CLAUDE.md 完全吸收后,**删除 `TASK.md`**(沿用 med-agent-verifier 约定)。
- [x] 把本仓库打包成 **Skill**(`SKILL.md`,开放格式;scripts=`bin/`,resources=`schema/`+`entries/_TEMPLATE.md`+`docs/`)。安装:`ln -s "$PWD" ~/.claude/skills/agentbench`。
  - [ ] 可选:发布到 skill.sh / agentskill.sh;或做成 plugin(`.claude-plugin/`)。

## 已知限制(非待办,记录)
- LinkedIn 帖子 **permalink 无法干净抓取**(URN 不在可读 DOM);只能记作者+反应数+论文线索。
- 社交信号(X/Reddit/LinkedIn)一律是 **sentiment,不是 authority**,永不进 `expert_verdict`。

---

## 进度快照(2026-06-17,本节为最新口径,前面各节旧计数已被超越)

**已完成**:**29 条入库 · 15 条已签发并上线 · 14 条待签** · 静态站点 + GitHub Pages 自动部署(<https://chenhaodev.github.io/agentbench/>)· 打包并安装为 Skill · `check_publish --schema-only` CI 硬门禁 · 去医疗偏斜 **22/29** · `check_publish.py` 非阻断 stale `as_of` 告警(>365 天)· [docs/VERDICT_RUBRIC.md](docs/VERDICT_RUBRIC.md) 判语 rubric · Actions 已升 Node 24 主版本 · 首页排序(信心/年份)+ 详情页"返回顶部" · `TASK.md` 已删(意图入 CLAUDE.md)。

### A. 最高优先 —— 签字 14 条草稿(已入库,schema-valid,未上线)
专家(chenhao)逐条签:**mteb · open-llm-leaderboard · gpqa · mathvista · docvqa · ocrbench · bfcl · swe-bench · mediqa-series · aime-2025 · arena-hard · mle-bench · re-bench · signalmc-med**。
- 每条已写好 `## Expert verdict` 留白 + 2–3 个针对性问题;在 `<!-- -->` 外作答。
- 加 `expert_verdict` 块(`signed_by`/`signed_date` 带引号/`confidence`∈{low,medium,high}/可选 `one_liner`)。
- 签好 `python3 bin/check_publish.py entries/<id>.md` 翻 OK → commit + push → CI 自动上线。
- 提醒:`aime-2025`/`arena-hard` 是刻意补的近重复(增量有限),`signalmc-med` 是很新的预印本且测编码器非 LLM——这几条判 `low` 或暂不签都合理。

### B. 广度(已补的新轴)
- [x] **代码/agentic**:`swe-bench`(issue→patch,可执行评测)。
- [x] **ML 工程 / AI-R&D**(此前完全空白):`mle-bench`(Kaggle 式 ML 工程,OpenAI)、`re-bench`(METR,带人类专家对照)。
- [x] **bio-signal**(census 锚点):`signalmc-med`(ECG+PPG 生物信号 FM 评测,2026 新预印本)。
- [x] 刻意略过的近重复:`aime-2025`(数学,与现有重叠)、`arena-hard`(与 LMArena 重叠)—— 应需求已补,重叠已标注。
- [x] **MEDIQA 2023+ 系列**:`mediqa-series`(CORR/M3G/MAGIC/WV/OE,2024–2025)。
- [ ] 仍可补:**SWE-bench Pro**、graph/GNN(OGB)、cybersecurity(CyberSecEval)、bio-signal 的 EEG-FM-Bench / 多模态 LLM 读 ECG(PULSE)等——按需。

### C. 工具/体验
- [x] `check_publish.py` 非阻断 stale `as_of` 告警(>365 天)。
- [x] 判语信任标尺写成 [docs/VERDICT_RUBRIC.md](docs/VERDICT_RUBRIC.md)。
- [x] Actions 升 Node 24 主版本(checkout@v6 / setup-python@v6 / configure-pages@v6 / upload-pages-artifact@v5 / deploy-pages@v5);CI 已验证绿。
- [x] 首页排序(默认/信心/年份)+ 详情页"返回顶部" + 平滑滚动。
- [ ] **cross-report 引用频次** 结构化为 `popularity` 子信号。
- [ ] 跑 genre / 去偏斜报告作为常规体检,固化进 Makefile/CI(脚本已验证可用)。

### D. 收尾
- [x] `TASK.md` 意图已进 CLAUDE.md → **已删除 `TASK.md`**。
- [ ] 可选:发布 Skill 到 skill.sh / agentskill.sh,或做成 plugin。
