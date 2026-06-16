---
id: omnibench
name: OmniBench
aliases: [M-A-P OmniBench]
homepage: https://m-a-p.ai/OmniBench/
year: 2024
domain: [general, multimodal, omni, audio-visual]
genre: online-leaderboard

authority:
  maintainers: [Yizhi Li / Ge Zhang et al. (M-A-P / multimodal-art-projection)]
  institution_count: 0
  update_cadence: irregular
  online: true

popularity:
  trending: false
  as_of: "2026-06-16"             # 被 Qwen3-Omni tech report 引用(cross-report 频次)

methodology:
  evaluation: [automated, human]
  contamination_controls: "人工标注的三模态题目,设计成必须同时用上三种输入——单模态走捷径会失败。"
  notes: "1,142 道人工标注问答对,需要对 image + audio + text 同时推理。音频分三类:speech、sound events、music。"

citations:
  - { title: "OmniBench: Towards The Future of Universal Omni-Language Models (Li, Zhang et al., 2024)", url: "https://arxiv.org/abs/2409.15272", accessed: "2026-06-16" }
  - { title: "OmniBench — code (multimodal-art-projection/OmniBench)", url: "https://github.com/multimodal-art-projection/OmniBench", accessed: "2026-06-16" }
  - { title: "m-a-p/OmniBench — dataset (HuggingFace)", url: "https://huggingface.co/datasets/m-a-p/OmniBench", accessed: "2026-06-16" }

as_of: "2026-06-16"
freshness:
  status: fresh
  last_checked: "2026-06-16"
  note: "2024 年的三模态基准;仍是 omni-modal 整合的参考,经 Qwen3-Omni 报告浮现。"

agent_summary:
  author: agent
  generated: "2026-06-16"

moa:
  capability_axes: [tri-modal-reasoning, audio-visual-understanding]
  modalities: [image, audio, text]
  access: [api, open-weights]
  recommended_for:
    - "测试真正的 omni-modal 整合——题目需要 image + audio + text 一起用,不能靠单模态兜底"
    - "音视频推理,大多数(单模态)榜会漏掉的切片"
  caveats:
    - "规模小(1,142 题)——统计功效有限"
    - "从 omni-model tech report 浮现;跨报告出现是人气,不是 authority"
---

## Agent summary

OmniBench(M-A-P / multimodal-art-projection,2024)评测**三模态**理解——image、audio、text
**同时**——也是 Qwen3-Omni 报告所用的音视频基准之一,即经 tech-report 发现法浮现。它有 **1,142 道
人工标注问答对**,设计成正确作答必须对**三种**输入做整合推理;单模态走捷径会失败。它的音频涵盖
**speech、sound events、music**。这使它成为对真正*omni-modal 整合*的一个少见测试,而非大多数榜所
孤立考察的单模态技能。

局限:它规模小(1,142 题,功效低),且它在各厂商 omni 报告里的出现是 **cross-report 频次**信号
(人气),不是中立权威。适合作为"模型是否真正融合多模态"这一聚焦维度。

<!-- 仅事实;来源为所引 arXiv 论文、GitHub 与 HF 数据集。 -->

## Expert verdict

<!-- 人工署名(chenhao)。值得回答:三模态整合是不是一个独立的 MoA 选型维度,还是被各单模态分数所涵盖?
     n=1,142 是否足以给权重,还是只能作为方向性信号? -->
