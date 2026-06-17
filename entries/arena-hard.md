---
id: arena-hard
name: Arena-Hard-Auto
aliases: [Arena-Hard, Arena-Hard-Auto v2, Arena-Hard v2.0]
homepage: https://github.com/lmarena/arena-hard-auto
year: 2024
domain: [general, instruction-following, reasoning, code, creative-writing]
genre: online-leaderboard

authority:
  maintainers: [LMSYS / LMArena(lmarena-ai)]
  institution_count: 0
  update_cadence: irregular     # 版本演进 v1(2024-04)→ v2.0(2025-04)
  online: true

popularity:
  hf_space: https://huggingface.co/datasets/lmarena-ai/arena-hard-auto
  trending: true
  as_of: "2026-06-17"

methodology:
  evaluation: [llm-judge, pairwise]
  contamination_controls: "提示词从真实的 Chatbot Arena 用户对话中新挑、定期更新;v2 加入风格控制(style control)以削弱'答得长/排版好'就赢的偏置。"
  notes: "Arena-Hard-Auto 是 LMArena 出的**自动**基准:用强 LLM 当裁判做成对比较(pairwise),目标是**廉价、快速地预测 LMArena(人类投票)排名**。v2.0(2025-04-23)含 500 道高难真实用户提示(开放式工程/数学等)+ 250 道创意写作;官方称与人类偏好排名相关性约 98.6%、对模型的区分度约为 MT-Bench 的 3 倍。"

models_ranked:
  - { model: 前沿对话模型(多家), rank: 1, axis: instruction-following, license: closed, note: "随版本与裁判模型变动;设计目标是逼近 LMArena 的人类投票排名,而非独立真值" }

citations:
  - { title: "From Live Data to High-Quality Benchmarks: The Arena-Hard Pipeline(LMSYS 博客,2024-04-19)", url: "https://www.lmsys.org/blog/2024-04-19-arena-hard/", accessed: "2026-06-17" }
  - { title: "Arena-Hard-Auto 论文(arXiv 2406.11939)", url: "https://arxiv.org/abs/2406.11939", accessed: "2026-06-17" }
  - { title: "Arena-Hard-Auto — 代码与榜(lmarena/arena-hard-auto, GitHub)", url: "https://github.com/lmarena/arena-hard-auto", accessed: "2026-06-17" }
  - { title: "arena-hard-auto — 数据集(lmarena-ai, HuggingFace)", url: "https://huggingface.co/datasets/lmarena-ai/arena-hard-auto", accessed: "2026-06-17" }

as_of: "2026-06-17"
freshness:
  status: fresh
  last_checked: "2026-06-17"
  note: "v2.0 仍是当前版本;作为 LMArena 的廉价自动代理在用。注意它是'预测人类投票'的代理指标,不是独立真值。"

agent_summary:
  author: agent
  generated: "2026-06-17"

moa:
  capability_axes: [instruction-following, reasoning, code, creative-writing]
  modalities: [text]
  access: [api, open-weights]
  recommended_for:
    - "想用便宜、可复现的自动跑分**预估**一个模型在 LMArena(人类投票)上的大致位置,而不必等真实对战量"
    - "迭代调模型时做快速回归:它对模型差异的区分度高于 MT-Bench"
  caveats:
    - "LLM-as-judge 有自我/同源偏好与风格偏置(v2 的 style control 只是削弱、非消除)"
    - "设计目标就是**预测 LMArena**,与 [lmarena] 高度相关——两者一起看是冗余,不是两个独立证据"
    - "它是人类偏好的**代理**,不等于任务真值;高分=更讨裁判/用户喜欢,未必=更正确"

tags: [general, llm-judge, arena-proxy, near-duplicate]
---

## Agent summary

Arena-Hard-Auto(LMArena/LMSYS 出品)是一个**自动**对话基准:用一个强 LLM 当**裁判**对模型输出做**成对比较**,
目标是**廉价、快速地预测 LMArena(Chatbot Arena 人类投票)的排名**,省去攒大量真实对战的成本。提示词从真实
Arena 用户对话里挑出**高难**的那批。**v2.0**(2025-04-23)含 **500 道高难真实提示**(开放式工程、数学等)
外加 **250 道创意写作**;官方报告与人类偏好排名相关性约 **98.6%**、对模型的**区分度约为 MT-Bench 的 3 倍**,
并引入**风格控制(style control)**来压制"答得长、排版漂亮就赢"的偏置。

要点(对选型关键):它本质是 **LLM-as-judge 的代理指标**——好处是便宜、可复现、区分度高;但 (1) 裁判会有
自我/同源偏好与风格偏置,style control 只能削弱不能消除;(2) 它的**设计目标就是预测 LMArena**,所以和
[lmarena] 条目**高度相关**,两者一起看是冗余而非两份独立证据;(3) 它是**人类偏好的代理**,不是任务真值,
高分意味着"更讨裁判/用户喜欢",未必等于"更正确"。

<!-- 仅事实;来源:LMSYS 博客、arXiv 2406.11939、GitHub 仓库、HF 数据集。
     这是之前刻意略过的近重复项(与 LMArena 重叠),应需求补入 census;重叠已在 caveats/summary 标注。 -->

## Expert verdict

<!-- 人工署名(chenhao)。值得回答:
     1) 它和 LMArena 高度相关——在你的证据体系里,Arena-Hard 是给 LMArena 的"廉价预演",还是该被 LMArena 直接取代?
     2) "98.6% 相关、3x 区分度"是和人类投票比的;你信这个自动代理到什么程度才敢据它在 MoA 里选对话冠军?
     3) LLM-judge 的风格/同源偏置 + style control 的残留——会不会让你坚持对自家关键场景再做一轮人评或私域对战? -->
