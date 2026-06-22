---
id: ocrbench
name: OCRBench
aliases: [Multimodal OCR Benchmark]
homepage: https://github.com/Yuliang-Liu/MultimodalOCR
year: 2023
domain: [general, multimodal, ocr]
genre: online-leaderboard

authority:
  maintainers: [Yuliang Liu / Xiang Bai et al. (华中科技大学 等)]
  institution_count: 0
  update_cadence: irregular
  online: true

popularity:
  trending: false
  as_of: "2026-06-17"             # 多模态 OCR 的常用基准,见于 VLM tech report

methodology:
  evaluation: [automated]
  contamination_controls: "1000 条问答全部人工核对/校正;汇编自 29 个数据集,覆盖面广。"
  notes: "评测多模态大模型的 OCR 能力,5 个组成:文本识别、场景文本 VQA、文档型 VQA、关键信息抽取(KIE)、手写数学公式识别(HMER)。汇编 29 个数据集、1000 条人工核验问答。GitHub 上有 leaderboard(并有 OCRBench v2)。"

citations:
  - { title: "OCRBench: On the Hidden Mystery of OCR in Large Multimodal Models (Liu et al., 2023)", url: "https://arxiv.org/abs/2305.07895", accessed: "2026-06-17" }
  - { title: "OCRBench — code & leaderboard (Yuliang-Liu/MultimodalOCR)", url: "https://github.com/Yuliang-Liu/MultimodalOCR", accessed: "2026-06-17" }

as_of: "2026-06-17"
freshness:
  status: fresh
  last_checked: "2026-06-17"
  note: "多模态 OCR 的常用基准;有 OCRBench v2 接续。前沿 VLM 攀升中。"

agent_summary:
  author: agent
  generated: "2026-06-17"

moa:
  capability_axes: [ocr, text-recognition, key-information-extraction]
  modalities: [image, text]
  access: [api, open-weights]
  recommended_for:
    - "评测多模态模型的 OCR/识别能力(识别 > 理解,与 DocVQA 互补)"
    - "覆盖场景文本、文档、KIE、手写公式等多种文本视觉任务"
  caveats:
    - "仅 1000 条(虽人工核验)——统计功效有限"
    - "聚焦识别/抽取,不等于文档级推理或长文理解"
---

## Agent summary

OCRBench 是一套给 AI 出的标准考卷(benchmark),专门考多模态大模型的 OCR 能力。OCR(把图片里的文字识别成可读文本)是基本功;多模态大模型(MLLM,能同时看图读文的大模型)能不能把图里的字看准、看全,就靠这类测试来检验。它由 Yuliang Liu、Xiang Bai 等人在 2023 年发布(arXiv 2305.07895),自称是覆盖面最广的 OCR 评测之一。

它分 5 个部分:文本识别、场景文本 VQA(看图回答问题,这里是回答图中文字相关的问题)、文档型 VQA、关键信息抽取(KIE,从图里挑出指定信息,比如发票上的金额)、手写数学公式识别(HMER)。题目汇编自 29 个数据集,一共 1000 条问答,全部经过人工核验。代码和排行榜放在 GitHub 上,后续还有升级版 OCRBench v2。它常出现在各家视觉语言模型(VLM)的技术报告里,本条目也是顺着技术报告查到的。

它和另一套测试 DocVQA 正好互补:OCRBench 偏"识别和抽取"(字看得准不准),DocVQA 偏"理解和问答"(看懂了没有)。它的局限也很明显,只有 1000 条题,虽然人工核验过,但题量小,结论的统计说服力有限;而且它考的是识别和抽取,不等于文档级的推理,也不代表能读懂长文。

<!-- 仅事实;来源为所引 arXiv 论文与 Yuliang-Liu/MultimodalOCR 仓库。 -->

## Expert verdict

<!-- 人工署名(chenhao)。值得回答:为文档处理选模型时,OCRBench(识别)与 DocVQA(理解)各占多少权重?
     1000 条规模够不够支撑选型,还是只作方向性参考? -->
