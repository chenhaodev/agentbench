---
id: docvqa
name: DocVQA
aliases: [Document Visual Question Answering]
homepage: https://rrc.cvc.uab.es/?ch=17
year: 2020
domain: [general, multimodal, document-understanding]
genre: dataset

authority:
  maintainers: [Minesh Mathew, Dimosthenis Karatzas, C.V. Jawahar (IIIT Hyderabad / CVC)]
  institution_count: 0
  update_cadence: frozen          # 静态数据集 + Robust Reading 竞赛
  online: true                    # RRC 上有竞赛排行榜

methodology:
  evaluation: [automated]
  contamination_controls: "真实文档图像 + 人工标注问答;公开多年,存在训练泄漏风险。"
  notes: "50,000 个问题,定义在 12,000+ 张文档图像上。要求模型在视觉上理解文档(表格、表单、版式)并作答。WACV 2021;在 RRC(Robust Reading Competition)设有竞赛榜。"

citations:
  - { title: "DocVQA: A Dataset for VQA on Document Images (Mathew et al., 2020; WACV 2021)", url: "https://arxiv.org/abs/2007.00398", accessed: "2026-06-17" }
  - { title: "Document Visual Question Answering (Robust Reading Competition)", url: "https://rrc.cvc.uab.es/?ch=17", accessed: "2026-06-17" }

as_of: "2026-06-17"
freshness:
  status: aging
  last_checked: "2026-06-17"
  note: "文档 VQA 的奠基数据集;前沿 VLM 已高分,作为标准对标项仍被广泛引用但区分力下降。"

agent_summary:
  author: agent
  generated: "2026-06-17"

expert_verdict:
  signed_by: chenhao
  signed_date: "2026-06-17"
  confidence: low          # low / medium / high

moa:
  capability_axes: [document-understanding, visual-qa, layout-reading]
  modalities: [image, text]
  access: [api, open-weights]
  recommended_for:
    - "评测文档图像理解(表格/表单/版式)的视觉问答——文档处理类应用的核心"
    - "VLM 文档能力的标准对标项之一"
  caveats:
    - "它是 DATASET(+竞赛榜),不是模型自带排名;公开多年,污染/饱和风险高"
    - "聚焦文档 VQA,不测多页推理、长文档或生成"
---

## Agent summary

DocVQA(全称 Document Visual Question Answering,意思是"看着文档图片回答问题")是这一类测试的奠基考卷,由 Mathew、Karatzas、Jawahar 三人在 2020 年发布(论文见 arXiv 2007.00398,正式发表于 WACV 2021)。它包含 50,000 个问题,出在 12,000 多张文档图片上。要做对题,AI 不能只读纯文字,得真的"看懂"图片里的版面:表格长什么样、表单填在哪、文字排在哪个位置。这套题目在 RRC(Robust Reading Competition,一个长期举办的文字识别竞赛)上设有公开排行榜,各家在介绍自己多模态大模型(能同时看图读文的 AI)时,也常拿它来对比文档能力。我们这条记录就是在翻看这些技术报告时发现的。

要注意两点。第一,它本质是一套数据集(外加一个竞赛榜),不是某个模型自带的排名,得有人拿模型去跑才会出分。第二,这套题公开太多年,如今主流的多模态大模型普遍都能拿高分,既有数据污染的风险(模型可能提前见过这些题、靠背答案虚高),也已经接近满分饱和,拉不开差距了。它只测单张文档的看图回答,不涉及跨多页推理、长文档,也不测让模型自己写一段话。

<!-- 仅事实;来源为所引 arXiv 论文与 RRC 竞赛页。 -->

## Expert verdict

值得回答:已饱和的文档 VQA 还值不值得引用, 作为门槛还是弃用? 我认为是作为门槛
它与 OCRBench的分工(理解 vs 识别) 在你选文档处理模型时怎么用? 确实有交集，但OCRbench更新更频繁一些，多专注于表格处理; VQA领域更广，但由于已饱和且少连续复杂推理，一般作为入门级别。
