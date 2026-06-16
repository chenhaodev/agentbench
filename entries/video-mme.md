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

Video-MME(Fu et al., 2024;CVPR 2025;MME-Benchmarks)自称是面向**视频**多模态 LLM 的首个综合
评测基准,也是经 tech-report 发现法浮现的视频基准之一。它包含 **900 个人工挑选、专家标注的视频**,
合计 **254 小时**,产生 **2,700 个问答对**,横跨 **6 个领域 / 30 个子领域**。关键是,时长从 **11 秒
到 1 小时**(短/中/长),使它成为对**长上下文时序推理**的测试,且输入不仅有帧,还有**字幕与音频**。
它已成为被广泛引用的参考——GPT-4.1 把它框定为多模态长上下文能力的"行业标准"。

局限:它是选择题(分数随是否提供字幕/音频而变)且面向通用。适合作为 MoA 中的视频 / 长上下文维度。

<!-- 仅事实;来源为所引 arXiv 论文与 Video-MME 仓库。 -->

## Expert verdict

<!-- 人工署名(chenhao)。值得回答:长视频时序推理是否值得一个独立的 MoA 维度?"分数依赖字幕/音频"
     在多大程度上削弱了跨模型可比性? -->
