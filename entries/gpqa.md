---
id: gpqa
name: GPQA
aliases: [Graduate-Level Google-Proof Q&A, GPQA Diamond]
homepage: https://github.com/idavidrein/gpqa
year: 2023
domain: [general, reasoning, science-QA]
genre: dataset

authority:
  maintainers: [David Rein et al. (NYU 等;Samuel R. Bowman)]
  institution_count: 0
  update_cadence: frozen          # 静态数据集
  online: false                   # 数据集,非自有排行榜;广泛被各榜/报告引用

methodology:
  evaluation: [automated]
  contamination_controls: "'Google-proof':熟练非专家可联网 30+ 分钟仍仅 34%;专家级、难检索的题目设计降低走捷径。"
  notes: "448 道由领域专家(生物/物理/化学博士)编写的多选题。博士专家 65%(剔除明显失误后 74%),熟练非专家联网仅 34%,发布时最强 GPT-4 基线 39%。目的是支持可扩展监督(scalable oversight)。常用更难的 GPQA-Diamond 子集。"

citations:
  - { title: "GPQA: A Graduate-Level Google-Proof Q&A Benchmark (Rein et al., 2023)", url: "https://arxiv.org/abs/2311.12022", accessed: "2026-06-17" }
  - { title: "GPQA — data & code (idavidrein/gpqa)", url: "https://github.com/idavidrein/gpqa", accessed: "2026-06-17" }

as_of: "2026-06-17"
freshness:
  status: fresh
  last_checked: "2026-06-17"
  note: "仍是前沿推理能力的常用硬基准(尤其 Diamond 子集),被各模型 tech report 广泛对标。"

agent_summary:
  author: agent
  generated: "2026-06-17"

expert_verdict:
  signed_by: chenhao
  signed_date: "2026-06-22"
  confidence: medium          # low / medium / high

moa:
  capability_axes: [hard-reasoning, scientific-knowledge]
  modalities: [text]
  access: [api, open-weights]
  recommended_for:
    - "区分前沿模型的硬科学推理(选择题里少数仍未饱和的高难基准)"
    - "作为推理强度的快速门槛(GPQA-Diamond)"
  caveats:
    - "它是 DATASET 不是排行榜——分数取决于谁、怎么跑(few-shot/CoT/采样)"
    - "仅生物/物理/化学,且为选择题;不测开放式推理或事实正确性"
---

## Agent summary

GPQA(Graduate-Level Google-Proof Q&A;Rein 等,2023,arXiv 2311.12022;含 Bowman)是一套
**研究生级硬推理**数据集:**448 道**由生物/物理/化学博士编写的多选题。它的标志是"**Google-proof**"
——熟练的非专家即使联网平均 30 多分钟仍只有 **34%**,而对应领域的博士专家约 **65%**(剔除明显失误后
74%);发布时最强 GPT-4 基线仅 **39%**。设计初衷是支持**可扩展监督**(让人类专家可靠地从超越人类的
AI 获取真信息)。实践中常用更难的 **GPQA-Diamond** 子集,它已成为各前沿模型 tech report 的标配硬指标。

它是*数据集*而非自有排行榜:任何分数都取决于跑法(few-shot/CoT/采样);且仅覆盖三门理科、为选择题,
不测开放式推理或事实正确性。

<!-- 仅事实;来源为所引 arXiv 论文与 idavidrein/gpqa 仓库。 -->

## Expert verdict

硬推理可作一个参考维度,但 GPQA 的选择题(MCQ)形式会高估真实推理——蒙对/排除法都拉高分,而领域专家自己也只有 ~65%。所以我对 GPQA 分打折看,不当作可直接据以选型的独立硬指标。
