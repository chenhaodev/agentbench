---
id: leaderboard-of-leaderboards
name: Leaderboard of Leaderboards (HF aggregators)
aliases: [MAYA-AI all-leaderboard, OpenEvals every-leaderboards, find-a-leaderboard]
homepage: https://huggingface.co/spaces/MAYA-AI/all-leaderboard
year: 2025                        # approximate — community HF Spaces of the 2025–2026 era
domain: [meta, ai-benchmarks, leaderboard-discovery]
genre: aggregator

authority:
  maintainers: [MAYA-AI, OpenEvals]   # independent community HuggingFace Spaces
  institution_count: 0
  update_cadence: live             # HF Spaces, refresh as the underlying boards change
  online: true

popularity:
  hf_space: https://huggingface.co/spaces/MAYA-AI/all-leaderboard
  trending: false
  as_of: "2026-06-16"

methodology:
  evaluation: [automated]
  contamination_controls: "N/A——它不做评测,只索引其他 leaderboard。"
  notes: "是聚合器,不是评测器。MAYA-AI 的'Leaderboard of Leaderboards'让你浏览/对比 HF 上托管的 benchmark leaderboard,按类别筛选,并按 likes 或 trending 排序。OpenEvals 的'every-leaderboards'在 11 个 HF benchmark 上给出统一视图(按模型名/规模/任务筛选);'find-a-leaderboard'是发现式搜索。"

citations:
  - { title: "Leaderboard of Leaderboards (HuggingFace Space, MAYA-AI)", url: "https://huggingface.co/spaces/MAYA-AI/all-leaderboard", accessed: "2026-06-16" }
  - { title: "Official Benchmarks Leaderboard 2026 — every-leaderboards (OpenEvals)", url: "https://huggingface.co/spaces/OpenEvals/every-leaderboards", accessed: "2026-06-16" }
  - { title: "Find a leaderboard (OpenEvals)", url: "https://huggingface.co/spaces/OpenEvals/find-a-leaderboard", accessed: "2026-06-16" }

as_of: "2026-06-16"
freshness:
  status: fresh
  last_checked: "2026-06-16"
  note: "实时 HF Spaces;覆盖范围取决于查看时 HF 上托管了什么。"

agent_summary:
  author: agent
  generated: "2026-06-16"

expert_verdict:
  signed_by: chenhao
  signed_date: "2026-06-16"
  confidence: low          # low / medium / high
  one_liner: "榜单的榜单，所以要深入一层挖掘一下"

moa:
  capability_axes: [benchmark-discovery, leaderboard-comparison]
  modalities: [text]
  access: [api, open-weights, local]
  recommended_for:
    - "深入之前,先找出某能力到底有哪些 leaderboard 存在"
    - "本仓库的 OBJECTIVE 对照面——它们列榜,我们评榜"
  caveats:
    - "按 likes / trending 排序——是 POPULARITY,不是质量(正是 AgentBench 要对抗的陷阱)"
    - "主要索引 HF 托管的榜;漏掉 shared task、论文内置榜与区域榜(见 docs/SOURCING.md)"
    - "没有专家判断:回答'谁在榜上',从不回答'该不该信这个榜'"
---

## Agent summary

本条目覆盖 **aggregator** 体裁:HuggingFace 上的"榜中榜"应用——它们索引、搜索、排序*其他*
leaderboard,而不亲自评测模型。**MAYA-AI 的"Leaderboard of Leaderboards"**让你浏览并对比 HF 上
托管的 benchmark leaderboard,按类别筛选,并**按 likes 或 trending 排序**。**OpenEvals 的
"every-leaderboards"**在 **11 个 HF benchmark** 上给出统一视图(按模型名、规模、任务筛选),其
**"find-a-leaderboard"**是发现式搜索。

它们是 **AgentBench 的客观对照面**:回答*"有哪些榜、谁在上面"*——自动、且快得无可匹敌;而本仓库回答
*"该不该信这个榜,高分到底买到了什么"*。它们默认的 **likes/trending 排序是人气信号,不是质量信号**,
且主要覆盖 HF 托管的榜,因此对 workshop shared task、论文内置榜与区域榜代表不足。这个缺口正是本项目
按 `genre` × 来源普查(`docs/SOURCING.md`)、而不依赖聚合器索引的原因。

<!-- 仅事实;来源为所引 HuggingFace Spaces。 -->

## Expert verdict

人工署名(chenhao)。聚合器是否让 AgentBench 多余, 还是恰恰证明需要一层判断? 我认为，此榜单不够全面。
"按likes排序" 在哪里会主动误导一个起草 MoA 的非领域工程师? 全面的榜单很难在专一领域最权威，故只是用来初筛罢了。
