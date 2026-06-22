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
  contamination_controls: "提示词从真实的 Chatbot Arena 用户对话中新挑、定期更新;v2 加入风格控制（style control）以削弱‘答得长/排版好’就赢的偏置。"
  notes: "Arena-Hard-Auto 是 LMArena 出的**自动**基准:用强 LLM 当裁判做成对比较（pairwise),目标是**廉价、快速地预测 LMArena（人类投票）排名**。v2.0(2025-04-23）含 500 道高难真实用户提示（开放式工程/数学等）+ 250 道创意写作;官方称与人类偏好排名相关性约 98.6%、对模型的区分度约为 MT-Bench 的 3 倍。"

models_ranked:
  - { model: 前沿对话模型（多家）, rank: 1, axis: instruction-following, license: closed, note: "随版本与裁判模型变动;设计目标是逼近 LMArena 的人类投票排名,而非独立真值" }

citations:
  - { title: "From Live Data to High-Quality Benchmarks: The Arena-Hard Pipeline(LMSYS 博客,2024-04-19)", url: "https://www.lmsys.org/blog/2024-04-19-arena-hard/", accessed: "2026-06-17" }
  - { title: "Arena-Hard-Auto 论文（arXiv 2406.11939)", url: "https://arxiv.org/abs/2406.11939", accessed: "2026-06-17" }
  - { title: "Arena-Hard-Auto — 代码与榜（lmarena/arena-hard-auto, GitHub)", url: "https://github.com/lmarena/arena-hard-auto", accessed: "2026-06-17" }
  - { title: "arena-hard-auto — 数据集（lmarena-ai, HuggingFace)", url: "https://huggingface.co/datasets/lmarena-ai/arena-hard-auto", accessed: "2026-06-17" }

as_of: "2026-06-17"
freshness:
  status: fresh
  last_checked: "2026-06-17"
  note: "v2.0 仍是当前版本;作为 LMArena 的廉价自动代理在用。注意它是‘预测人类投票’的代理指标,不是独立真值。"

agent_summary:
  author: agent
  generated: "2026-06-17"

moa:
  capability_axes: [instruction-following, reasoning, code, creative-writing]
  modalities: [text]
  access: [api, open-weights]
  recommended_for:
    - "想用便宜、可复现的自动跑分**预估**一个模型在 LMArena（人类投票）上的大致位置,而不必等真实对战量"
    - "迭代调模型时做快速回归:它对模型差异的区分度高于 MT-Bench"
  caveats:
    - "LLM-as-judge 有自我/同源偏好与风格偏置（v2 的 style control 只是削弱、非消除）"
    - "设计目标就是**预测 LMArena**,与 [lmarena] 高度相关——两者一起看是冗余,不是两个独立证据"
    - "它是人类偏好的**代理**,不等于任务真值;高分=更讨裁判/用户喜欢,未必=更正确"

tags: [general, llm-judge, arena-proxy, near-duplicate]
---

## Agent summary

Arena-Hard-Auto 是 LMArena/LMSYS 做的一套自动跑分（benchmark,给 AI 出的标准考卷）。它的做法是让另一个很强的 AI 当“阅卷老师”（LLM-as-judge,让一个 AI 给别的 AI 打分）,把两个模型的回答两两放在一起比,谁答得好就给谁一分。这么设计是为了省钱、省时间地猜出 LMArena 排名——LMArena 是靠大量真人投票排出的模型榜单,攒够真人对战很慢很贵,所以用 AI 评判来当便宜的替身。考题（提示词）是从 LMArena 上真实用户的对话里挑出来的难题。v2.0 版本（2025-04-23）有 500 道高难度的真实问题（开放式工程、数学等）,再加 250 道创意写作题。官方说,它排出的名次和真人偏好的名次相关性约 98.6%,把模型之间拉开差距的能力约是 MT-Bench（另一套早期对话跑分）的 3 倍。它还加了一个“风格控制”（style control）的机制,用来压住“答得长、排版漂亮就容易赢”这种跑偏。

挑模型时要记住几件事。它说到底是个由 AI 评判产生的替身指标:好处是便宜、能重复跑、区分度高。但也有三个坑。第一,当裁判的 AI 会偏心,容易给和自己同源的模型或风格讨喜的答案打高分,风格控制只能削弱这种偏向,消不掉。第二,它生来就是为了猜 LMArena 的名次,所以和 [lmarena] 这条目重合度很高,两个一起看属于重复,不算两份独立证据。第三,它衡量的是真人喜不喜欢这种“偏好”,不是题目本身的对错;分高只说明更讨裁判或用户喜欢,不代表答得更正确。

<!-- 仅事实;来源:LMSYS 博客、arXiv 2406.11939、GitHub 仓库、HF 数据集。
     这是之前刻意略过的近重复项（与 LMArena 重叠）,应需求补入 census;重叠已在 caveats/summary 标注。 -->

## Expert verdict

<!-- 人工署名(chenhao)。值得回答:
     1) 它和 LMArena 高度相关——在你的证据体系里,Arena-Hard 是给 LMArena 的"廉价预演",还是该被 LMArena 直接取代?
     2) "98.6% 相关、3x 区分度"是和人类投票比的;你信这个自动代理到什么程度才敢据它在 MoA 里选对话冠军?
     3) LLM-judge 的风格/同源偏置 + style control 的残留——会不会让你坚持对自家关键场景再做一轮人评或私域对战? -->
