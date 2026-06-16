# AgentBench · 主观榜单评议 (subjective leaderboard review)

> 不是再做一个排行榜,而是给现有的 AI 榜单写**专家判语**:这个榜可不可信、高分到底买到了什么、要不要据此在 MoA(Mixture-of-Agents)里选模型。

## 一分钟看懂(无需 AI 背景)

市面上有几百个 AI"排行榜"(leaderboard)——谁的模型在医疗、情商、推理上更强。问题是:**榜单本身良莠不齐**。有的有几百位医生背书,有的只是网友点赞;有的题目早被模型背熟(饱和),有的还在区分高下。

AgentBench 不重复排名。它对每个值得关注的榜单出一份**人签字的主观判语**:
- 这个榜**谁在做**、**怎么测**、**现在谁领先**(客观事实,由 AI 整理);
- 然后一位**专家**(本仓库:chenhao)写下**该不该信、信到什么程度**(主观判语,只能人来写)。

产物是一个 GitHub 页面,给两类人看:① 非 AI 人士科普查阅;② 跨领域的 AI 工程师快速判断"选哪个榜的冠军进我的系统"。

## 它和 HuggingFace 的"榜中榜"有什么不同

HuggingFace 上**已经有**客观的榜单聚合器(leaderboard of leaderboards),能按 likes/trending 排序、按类别筛选,例如
[OpenEvals/every-leaderboards](https://huggingface.co/spaces/OpenEvals/every-leaderboards)、
[MAYA-AI/all-leaderboard](https://huggingface.co/spaces/MAYA-AI/all-leaderboard)。

> **聚合器回答"谁在榜上";AgentBench 回答"该不该信这个榜"。** 我们的差异化是**专家判语层**,不是再聚合一次排名——那会输给自动更新的 Space。

## 一个榜单值不值得信:看什么 metric

不同"排序"是**三条不同的轴**,本仓库的 schema 把它们显式分开,避免读者把人气当质量:

| 轴 | 含义 | schema 字段 |
|---|---|---|
| **人气** HF likes / downloads / trending | 采用度,**会被刷,≠好** | `popularity` |
| **学术权威** 引用数(Google Scholar / Semantic Scholar) | 被同行引用的程度 | `authority.citation_count` |
| **能力** 榜内 rank / score | 模型在该榜的成绩 | `models_ranked` |

**医疗榜单尤其要注意**:最有名的医疗榜(HealthBench、MedBench、MedHELM)**不是靠 HF likes 出名的**——它们多半连 HF Space 的点赞都没有。它们的权威货币是:

1. **临床参与度** — HealthBench 有 262 位医生写评分标准;MedHELM 覆盖 15 个专科的临床医生;MedBench v4 由 500+ 机构的医生审核;
2. **背书机构** — OpenAI / Stanford / 国家级医疗 AI 基地;
3. **引用数**;
4. **临床真实度** — 真实病历文本/多轮对话 > 选择题知识背诵(MultiMedQA 类已**饱和**)。

> 结论:在医疗领域,`popularity` 是弱信号,真正决定"值不值得信"的是 `authority`(机构/医生/引用)+ **临床真实度**。

## 已收录的榜单(草稿)

| 榜单 | 领域 | 权威信号 | 状态 |
|---|---|---|---|
| [MedBench](entries/medbench.md) | 中文医疗(LLM/多模态/Agent) | 500+ 机构、动态防污染 | draft(待签) |
| [HealthBench](entries/healthbench.md) | 医疗安全/健康对话 | 262 位医生评分标准(OpenAI) | draft(待签) |
| [MedHELM](entries/medhelm.md) | 121 项临床任务(整体评估) | Stanford,临床验证的任务分类 | draft(待签) |
| [BRIDGE](entries/bridge.md) | 多语种真实临床文本 | 87 任务/9 语种/百万样本 | draft(待签) |
| [Open Medical-LLM Leaderboard](entries/open-medical-llm-leaderboard.md) | 开源医疗 QA | HF 社区榜,**已饱和** | draft(待签) |
| [RCQ](entries/rcq.md) | 真实临床提问(n=100,盲评) | Nature Medicine,NYU+UT Austin | draft(待签) |
| [MEDIQA-Chat](entries/mediqa-chat.md) | 医患对话→病历摘要(shared task) | ACL ClinicalNLP 2023,Microsoft | draft(待签) |
| [MedQA](entries/medqa.md) | 医疗 QA 原始数据集(USMLE 式) | Jin et al. 2020,MIT,**已饱和** | draft(待签) |
| [Leaderboard of Leaderboards](entries/leaderboard-of-leaderboards.md) | 榜中榜聚合器(meta) | HF MAYA-AI / OpenEvals | draft(待签) |
| [LMArena](entries/lmarena.md) | 通用对话·人类盲投 Elo(**非医疗锚点**) | Berkeley/LMSYS,arXiv 2403.04132 | draft(待签) |
| [MMMU](entries/mmmu.md) | 多模态推理(**非医疗·多模态锚点**) | Yue et al. CVPR 2024,11.5K 题 | draft(待签) |
| [OmniBench](entries/omnibench.md) | 图+音+文 三模态(omni) | M-A-P,arXiv 2409.15272 | draft(待签) |
| [Video-MME](entries/video-mme.md) | 视频理解(长达 1 小时) | MME-Benchmarks,CVPR 2025 | draft(待签) |
| [VoiceBench](entries/voicebench.md) | 语音助手(口语指令+安全) | NUS,arXiv 2410.17196 | draft(待签) |

> 还可一键起草:EQ-Bench(情商)、MTEB(向量检索)、Open LLM Leaderboard;及 Qwen3-Omni 报告里的 MathVista / DocVQA / GPQA 等。
>
> 当前 14 条中 **6 条非医疗**,模态覆盖 文/图/音/视频。"用 tech report 当发现源"见 [docs/SOURCING.md](docs/SOURCING.md)。

### 怎么找榜单:按"体裁 × 来源"普查,不靠名字搜

每个条目带一个 `genre` 字段——`online-leaderboard` / `shared-task` / `paper-bound` / `aggregator` / `dataset`。这是为了**让整类缺口可见**:按名字搜只能找到你叫得出、且在网络搜索里靠前的榜,会**系统性漏掉** workshop shared task(如 MEDIQA-Chat)、论文内置榜(如 RCQ)、区域榜。检索方法与已知缺口见 **[docs/SOURCING.md](docs/SOURCING.md)**。

## 人在环中:草稿 → 签字 → 发布

整个流程把**人和 AI 的笔分开**(详见 [CLAUDE.md](CLAUDE.md) 的"Integrity rules"):

1. **草稿**:AI 把 `## Agent summary`(纯事实)写好,`## Expert verdict` 留空。
2. **签字**:**专家在自己的编辑器里**写 `## Expert verdict` 判语,并填 `expert_verdict` frontmatter(`signed_by` / `signed_date` / `confidence` / `one_liner`)。
   - 这一步不是工具调用,所以 `hooks/guard_verdict.py` 不会拦你;但它会**拦住 AI** 写进判语区。
3. **发布**:`python3 bin/check_publish.py` 只放行**已签字**的条目进 GitHub 页面("草稿可提交,发布需签字")。

```bash
python3 bin/check_publish.py            # 发布门禁:未签字 = 拦截
```

## 数据契约与项目结构

数据优先:**schema 就是契约**,渲染与工具都薄。

```
SKILL.md                   技能清单(本 repo 即 Skill;触发后教 agent 走整套工作流)
schema/entry.schema.json   一个榜单条目的契约(popularity / authority / models_ranked / expert_verdict / moa)
entries/<id>.md            一个榜单 = frontmatter + 「## Agent summary」+「## Expert verdict」
entries/_TEMPLATE.md       起草模板
bin/check_publish.py       发布门禁(--schema-only 为 CI 硬门禁)
bin/render_site.py         静态站点渲染(只渲染已签字条目)
hooks/guard_verdict.py     PreToolUse:禁止 AI 代写专家判语
hooks/validate_entry.py    PostToolUse:写入即按 schema 校验(草稿放行)
.github/workflows/pages.yml CI:schema 门禁 → 渲染 → 部署 GitHub Pages
docs/SOURCING.md           按"体裁×来源"普查的发现法
CLAUDE.md                  决策、完整性规则、语言约定、hook 与门禁说明
```

依赖:`pip install pyyaml jsonschema`(仅用于校验/门禁;无运行时框架)。

## 作为 Skill 使用

本 repo 即一个 [Claude Code Skill](SKILL.md)(开放 `SKILL.md` 格式)。安装:`ln -s "$PWD" ~/.claude/skills/agentbench`。触发后,它教 agent 走完整工作流:**发现(按体裁×来源普查)→ 起草(先核实再写,判语留空)→ 校验 → 交专家签字 → 渲染/部署**,并强制"AI 写事实、专家签判语"的边界。已上线示例:<https://chenhaodev.github.io/agentbench/>。

## 设计取舍

- **CLI/docs-as-data,不做 TUI**:Skill 的交互界面是 agent 对话,TUI agent 驱动不了。若日后需要高频比对式人工评审,再在同一份数据上加一个轻量 TUI 视图。
- **无自建 CLI 编排**:本仓库只渲染**策展文本**(不像 `med-agent-verifier` 要跑评测),故首版用现成静态站点生成器 + CI 校验,不造 CLI。
