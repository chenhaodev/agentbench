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

expert_verdict:
  signed_by: chenhao
  signed_date: "2026-06-16"
  confidence: low          # low / medium / high

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

OmniBench 是一份给 AI 出的标准考卷(benchmark),由 M-A-P(multimodal-art-projection)团队在 2024 年做出来。它要考的是 tri-modal,也就是同时给图、音、文三种输入(image、audio、text),看模型能不能一起用上。Qwen3-Omni 的技术报告里也用了它当音视频测试,我们正是顺着这类报告发现它的。

整份卷子有 1,142 道人工标注的问答对。题目特意设计成:要答对,就得把三种输入整合起来推理,只看其中一种(单模态)、想走捷径,就会答错。音频也分了三类:语音(speech)、环境声响(sound events)、音乐(music)。所以它能测出一件大多数考卷测不到的事:模型是不是真把多种模态融到一起用,而不是分头各考一种单模态本事。

它也有短板。一是题量小,只有 1,142 题,样本太少,统计上说服力有限。二是它能被人注意到,主要是因为多家厂商的 omni 模型报告里反复提到它(cross-report 频次),这只能算人气,不等于中立的权威背书。把它当成一个聚焦的检验角度还行:用来看模型到底有没有真正融合多模态。

<!-- 仅事实;来源为所引 arXiv 论文、GitHub 与 HF 数据集。 -->

## Expert verdict

人工署名(chenhao)。值得回答: 
三模态整合是不是一个独立的 MoA 选型维度, 还是被各单模态分数所涵盖? 只有在世界模型、环境交互中需要被考虑。
n=1,142 是否足以给权重,还是只能作为方向性信号? 只能作为启发式思考
