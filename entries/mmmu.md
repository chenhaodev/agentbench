---
id: mmmu
name: MMMU
aliases: [Massive Multi-discipline Multimodal Understanding]
homepage: https://mmmu-benchmark.github.io/
year: 2023
domain: [general, multimodal, vision-language, reasoning]
genre: online-leaderboard

authority:
  maintainers: [Xiang Yue / Yuansheng Ni et al. (academic collaboration)]
  institution_count: 0
  update_cadence: irregular       # leaderboard updated as models are submitted
  online: true

popularity:
  trending: false
  as_of: "2026-06-16"             # very high cross-report citation frequency — see summary

methodology:
  evaluation: [automated]
  contamination_controls: "大学水平的专家题目;更难的 MMMU-Pro 变体用于对抗走捷径与饱和。"
  notes: "11.5K 道多模态题目,取自大学考试、测验与教科书,覆盖 6 个学科(Art & Design、Business、Science、Health & Medicine、Humanities & Social Science、Tech & Engineering)、30 个科目、183 个子领域,以及 30 种异构图像类型(图表、示意图、地图、表格、乐谱、化学结构式)。需要大学水平的学科知识 + 审慎推理。"

citations:
  - { title: "MMMU: A Massive Multi-discipline Multimodal Understanding and Reasoning Benchmark for Expert AGI (Yue et al., 2023; CVPR 2024)", url: "https://arxiv.org/abs/2311.16502", accessed: "2026-06-16" }
  - { title: "MMMU benchmark — official site & leaderboard", url: "https://mmmu-benchmark.github.io/", accessed: "2026-06-16" }
  - { title: "MMMU/MMMU — dataset (HuggingFace)", url: "https://huggingface.co/datasets/MMMU/MMMU", accessed: "2026-06-16" }

as_of: "2026-06-16"
freshness:
  status: aging
  last_checked: "2026-06-16"
  note: "前沿 VLM 现已得分很高;MMMU-Pro 维持其区分度。仍是 tech report 里默认的多模态推理锚点。"

agent_summary:
  author: agent
  generated: "2026-06-16"

expert_verdict:
  signed_by: chenhao
  signed_date: "2026-06-16"
  confidence: low

moa:
  capability_axes: [multimodal-reasoning, visual-knowledge, document-chart-understanding]
  modalities: [image, text]
  access: [api, open-weights]
  recommended_for:
    - "事实上的多模态推理锚点——几乎每份 VLM/omni tech report 都会对标(如 Qwen3-Omni)"
    - "跨多学科、多图像类型的大学水平视觉推理"
  caveats:
    - "选择题 → 有记忆/走捷径风险;要更难的信号请看 MMMU-Pro"
    - "它在厂商 tech report 里的普遍性是 cross-report 频次(popularity),不是中立权威——厂商只报自己擅长的榜"
    - "含一个 Health & Medicine 子集,但整体是通用榜,不是医疗 benchmark"
---

## Agent summary

MMMU(Yue et al., 2023;CVPR 2024)是**默认的多模态推理基准**——一个通用视觉-语言锚点,
也是本仓库里**用 tech-report 发现法**找到的最典型例子(几乎每份 VLM/omni 报告都引它,包括
Qwen3-Omni)。它包含 **11.5K** 道多模态题目,取自大学考试、测验与教科书,横跨 **6 个学科**
(Art & Design、Business、Science、Health & Medicine、Humanities & Social Science、
Tech & Engineering)、**30 科目 / 183 子领域**,以及 **30 种异构图像类型**(图表、示意图、
地图、乐谱、化学结构式……)。它要求大学水平的知识加审慎推理,并提供官方 leaderboard;更难的
**MMMU-Pro** 变体用于对抗饱和。

它在前沿 tech report 里近乎普遍的出现,是一种 **cross-report 引用频次**信号——比 HF likes 或
社交热度更严谨的人气代理,但仍是 **popularity,不是 authority**:厂商只报自己赢的榜。它是选择题
(因此有记忆/走捷径倾向)且面向通用领域;内嵌的 Health & Medicine 子集并不使它成为医疗 benchmark。

<!-- 仅事实;来源为所引 arXiv 论文、官网与 HF 数据集。 -->

## Expert verdict

Human-signed (chenhao). Worth answering: "reported in every tech report" 
is just consensus. Cross-report frequency is weighted as popularity. MMMU 在 MoA 选型里权重很低
