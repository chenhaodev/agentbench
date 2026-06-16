# TODO

后续要做的事。已完成的设计与约定见 [CLAUDE.md](CLAUDE.md);收录方法见 [docs/SOURCING.md](docs/SOURCING.md)。

## 1. 签字(人在环中 · 最高优先)
当前 **2/14 已签发**(MMMU、HealthBench)。其余待专家(chenhao)审阅并签字:
- [ ] **LMArena** —— 之前那次编辑没存上,需重签(`expert_verdict` 块 + 判语正文)。
- [ ] 其余 11 条逐条签字:bridge、medbench、medhelm、open-medical-llm-leaderboard、medqa、mediqa-chat、rcq、leaderboard-of-leaderboards、omnibench、video-mme、voicebench。
- 流程提醒:在自己的编辑器里改(不是工具调用,`guard_verdict.py` 不拦你);判语写在 `<!-- -->` 之外;`signed_date` 加引号;`confidence` ∈ {low,medium,high};改完 `python3 bin/check_publish.py entries/<id>.md` 应翻成 OK。

## 2. 渲染:静态站点
- [x] **`bin/render_site.py`** —— 零额外依赖渲染器,**只渲染已签发(publishable)条目**(复用 check_publish);输出 `site/`(index + 每条详情 + style.css)。三轴信号(权威/人气/能力)视觉分离,专家判语置顶。本地预览:`python3 bin/render_site.py && python3 -m http.server -d site`。
- [x] **GitHub Pages 部署 workflow**:`.github/workflows/pages.yml` —— push 时 `check_publish --schema-only`(硬门禁)→ `render_site`(只发已签字)→ 部署 `site/`(`configure-pages enablement:true` 自启用)。新草稿不会弄垮构建,只是不上线。
- [x] **已上线**:<https://chenhaodev.github.io/agentbench/>(repo: chenhaodev/agentbench,public)。build ✓ + deploy ✓,14 条全部在线。
- [ ] 可选:把 Actions 升到支持 Node 24 的版本(checkout/setup-python/configure-pages/upload-pages-artifact/deploy-pages 当前跑在 Node 20,仅弃用告警,不影响运行)。
- [ ] 可选:首页加按 confidence / year 排序;详情页加"返回顶部"。

## 3. 广度:继续去医疗偏斜(当前 6/14 非医疗)
- [ ] 非医疗锚点(事实已备好):**EQ-Bench**(情商,原始 brief 点名)、**MTEB**(向量检索)、**Open LLM Leaderboard**(通用,v1→v2)。
- [ ] Qwen3-Omni 报告里的多模态候选:**MathVista / DocVQA / OCRBench / GPQA / AIME25 / BFCL-v3 / Arena-Hard** 等(见 SOURCING.md 的"tech report"来源)。

## 4. 覆盖缺口(来自 docs/SOURCING.md)
- [ ] `aggregator`、`dataset` 已各 1 条,但仍单薄;每个 `genre` 至少多覆盖一个领域。
- [ ] **MEDIQA 系列 2023 之后**的年份 / 同族 shared task 未调研。
- [ ] 跑 genre / 去偏斜报告作为常规体检(脚本已在会话中验证可用,可固化进 Makefile/CI)。

## 5. 工具与门禁增强(可选)
- [ ] `bin/check_publish.py` 增加 **stale `as_of` 告警**(如 > 12 个月)反映"判语会过期"。
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
