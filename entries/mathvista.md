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

MathVista(Pan Lu 等,2023,arXiv 2310.02255)是给 AI 出的一套"看图做数学"考卷,专门测它能不能
同时看图读文(多模态)地解数学题。整套题共 6,141 道,都需要先看懂图表、函数图、几何图形,再做空间
推理和图示解读。这些题不是新出的,而是从 28 个现成的多模态数学数据集里汇编而来,另外补了 3 个新建
子集(IQTest、FunctionQA、PaperQA)。2023 年 10 月发布时,作者拿 12 个基础模型来考,成绩最好的是
GPT-4V,总体只答对 49.9%,比第二名 Bard 高出 15.1 个百分点。这个分数也说明当年这套题有多难。如今它
常被写进各家视觉语言模型(VLM)的技术报告里当对标项,本条目也是顺着这些技术报告找到的。

它只盯着"看图做数学"这一块,不能代表 AI 的通用看图能力。另外,因为题目是从多个现成数据集拼起来的,
有些内容可能早已进了模型的训练语料,也就是说模型可能提前见过考题、靠背答案虚高(数据污染)。

<!-- 仅事实;来源为所引 arXiv 论文、官网与 lupantech/MathVista 仓库。 -->

## Expert verdict

<!-- 人工署名(chenhao)。值得回答:视觉数学是否值得做 MoA 的独立维度,还是被'多模态推理'(如 MMMU)
     涵盖?汇编自既有数据集的污染风险,该让你给它的分数打几折? -->
