---
id: mathvista
name: MathVista
aliases: []
homepage: https://mathvista.github.io/
year: 2023
domain: [general, multimodal, math, vision-language]
genre: online-leaderboard

authority:
  maintainers: [Pan Lu et al. (UCLA / Microsoft Research 等)]
  institution_count: 0
  update_cadence: irregular
  online: true

popularity:
  trending: false
  as_of: "2026-06-17"             # 视觉数学的标准基准,广泛见于 VLM tech report

methodology:
  evaluation: [automated]
  contamination_controls: "汇编自 28 个既有多模态数学数据集 + 3 个新建(IQTest、FunctionQA、PaperQA),覆盖面降低单源过拟合。"
  notes: "6,141 道视觉数学题,需理解图表、函数图、几何图形等做空间/图示推理。发布时(2023-10)评测 12 个基础模型,最强 GPT-4V 总体 49.9%(领先第二名 Bard 15.1 个百分点)。"

citations:
  - { title: "MathVista: Evaluating Mathematical Reasoning of Foundation Models in Visual Contexts (Lu et al., 2023)", url: "https://arxiv.org/abs/2310.02255", accessed: "2026-06-17" }
  - { title: "MathVista — site & leaderboard", url: "https://mathvista.github.io/", accessed: "2026-06-17" }
  - { title: "MathVista — data & code (lupantech/MathVista)", url: "https://github.com/lupantech/MathVista", accessed: "2026-06-17" }

as_of: "2026-06-17"
freshness:
  status: fresh
  last_checked: "2026-06-17"
  note: "视觉数学推理的常用基准;前沿 VLM 已远超 2023 年的 49.9%,但仍是标配对标项。"

agent_summary:
  author: agent
  generated: "2026-06-17"

moa:
  capability_axes: [visual-math-reasoning, diagram-understanding, spatial-reasoning]
  modalities: [image, text]
  access: [api, open-weights]
  recommended_for:
    - "评测看图做数学(图表/函数图/几何)的视觉数学推理"
    - "区分 VLM 在图示理解+推理上的差距"
  caveats:
    - "题型偏数学+图示;不代表通用视觉理解"
    - "汇编自多个既有数据集,部分可能进入训练语料"
---

## Agent summary

MathVista(Pan Lu 等,2023,arXiv 2310.02255)是**视觉数学推理**的标准基准:**6,141 道**需要看懂
图表、函数图、几何图形的数学题,考察空间推理与图示解读。它汇编自 **28 个**既有多模态数学数据集,
外加 **3 个新建**子集(IQTest、FunctionQA、PaperQA)。发布时(2023-10)评测 12 个基础模型,最强
**GPT-4V 总体 49.9%**、领先第二名 Bard 15.1 个百分点——可见当年难度。它常出现在 VLM tech report
的对标表里(本条目即经 tech-report 发现法浮现)。

它聚焦"看图做数学",不代表通用视觉理解;且因汇编自多个既有数据集,部分内容可能已进入训练语料。

<!-- 仅事实;来源为所引 arXiv 论文、官网与 lupantech/MathVista 仓库。 -->

## Expert verdict

<!-- 人工署名(chenhao)。值得回答:视觉数学是否值得做 MoA 的独立维度,还是被'多模态推理'(如 MMMU)
     涵盖?汇编自既有数据集的污染风险,该让你给它的分数打几折? -->
