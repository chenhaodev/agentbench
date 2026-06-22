---
id: video-mme
name: Video-MME
aliases: [VideoMME]
homepage: https://video-mme.github.io/
year: 2024
domain: [general, video, multimodal]
genre: online-leaderboard

authority:
  maintainers: [Chaoyou Fu et al. (MME-Benchmarks)]
  institution_count: 0
  update_cadence: irregular
  online: true

popularity:
  trending: false
  as_of: "2026-06-16"             # 被当作"行业标准"(如 GPT-4.1)并在 VLM tech report 中引用

methodology:
  evaluation: [automated, human]
  contamination_controls: "视频经人工挑选与专家标注;时长跨短→长以抵抗抽帧走捷径。"
  notes: "900 个人工挑选/标注的视频,合计 254 小时 → 2,700 个问答对;6 个主要视觉领域、30 个子领域;时长 11 秒–1 小时(短/中/长);输入含视频帧加字幕与音频。CVPR 2025。"

citations:
  - { title: "Video-MME: The First-Ever Comprehensive Evaluation Benchmark of Multi-modal LLMs in Video Analysis (Fu et al., 2024; CVPR 2025)", url: "https://arxiv.org/abs/2405.21075", accessed: "2026-06-16" }
  - { title: "Video-MME — code & leaderboard (MME-Benchmarks/Video-MME)", url: "https://github.com/MME-Benchmarks/Video-MME", accessed: "2026-06-16" }

as_of: "2026-06-16"
freshness:
  status: fresh
  last_checked: "2026-06-16"
  note: "实时 leaderboard;在视频-LLM 评测中被广泛引用。顶部前沿模型攀升中(Gemini 级约 80 多分)。"

agent_summary:
  author: agent
  generated: "2026-06-16"

expert_verdict:
  signed_by: chenhao
  signed_date: "2026-06-16"
  confidence: medium          # low / medium / high

moa:
  capability_axes: [video-understanding, long-context-multimodal, temporal-reasoning]
  modalities: [video, text]
  access: [api, open-weights]
  recommended_for:
    - "对比视频 LLM,含长视频(可达 1 小时)的时序推理"
    - "一个事实上的行业标准视频榜(被 GPT-4.1 当作参考)"
  caveats:
    - "选择题形式;分数随是否提供字幕/音频而变"
    - "通用视频理解——不针对具体领域"
---

## Agent summary

Video-MME(Fu et al., 2024;CVPR 2025;MME-Benchmarks)是一套给 AI 出的标准考卷(benchmark),专门考能看视频并读文字的大模型(多模态 MLLM)。它自称是面向视频的首个综合评测基准,也是我们在各家厂商技术报告里翻到、而不是靠搜索名字找到的视频考卷之一。整套题目用了 900 个人工挑选、专家标注的视频,合计 254 小时,出成 2,700 道问答题,覆盖 6 个领域、30 个子领域。

它有个特别之处:视频时长从 11 秒到 1 小时都有,按短、中、长(short/medium/long video)分级。要答对长视频的题,模型得跟着画面理清前后发生了什么(时序推理),不能只看几帧蒙一下。喂给模型的也不只是画面帧,还配了字幕和音频。

现在这套题被很多论文当参考,GPT-4.1 就把它当成衡量"看长视频"能力的行业标准。

它的局限也清楚:题目是选择题(MCQ),给不给字幕、音频两种条件下分数会变;而且只考通用视频理解,不针对某个具体领域。如果要把多个模型组队、各管一块来用(MoA),它适合用来挑视频理解、长上下文这一块的模型。

<!-- 仅事实;来源为所引 arXiv 论文与 Video-MME 仓库。 -->

## Expert verdict

人工署名(chenhao)。值得回答: 
长视频时序推理是否值得一个独立的 MoA 维度? 不值得，因为现在和人类专家差距过大，整体业界还不成熟。
"分数依赖字幕/音频" 在多大程度上削弱了跨模型可比性? 我认为影响比较大。
