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

GPQA(Graduate-Level Google-Proof Q&A;Rein 等,2023,arXiv 2311.12022;作者含 Bowman)是一份研究生级的难推理"考卷",由生物、物理、化学三个方向的博士出题,一共 448 道选择题(MCQ,即选择题)。它的特点叫 "Google-proof",意思是连用搜索引擎现查也很难做对:让本来在行、又能联网的熟练非专家平均花 30 多分钟去答,正确率也只有 34%;而对应领域的博士专家约 65%(把明显的笔误剔掉后是 74%)。发布时最强的 GPT-4 模型,在没专门改造的情况下也只考了 39%。出这套题的初衷是支持"可扩展监督"(scalable oversight),也就是让人类专家能可靠地从比自己更强的 AI 那里拿到真实信息。实际用的时候,大家常用更难的 GPQA-Diamond 子集,它已经成了各家前沿模型技术报告(tech report)里的标配难题。

要注意,GPQA 是一份数据集,不是它自己运营的排行榜。同一份题,谁来跑、怎么跑(给几个例题、要不要让模型先写推理过程、怎么采样),分数都会不一样。而且它只覆盖三门理科,题型又全是选择题,既不考开放式的推理,也不查事实对不对。

<!-- 仅事实;来源为所引 arXiv 论文与 idavidrein/gpqa 仓库。 -->

## Expert verdict

硬推理可作一个参考维度,但 GPQA 的选择题(MCQ)形式会高估真实推理——蒙对/排除法都拉高分,而领域专家自己也只有 ~65%。所以我对 GPQA 分打折看,不当作可直接据以选型的独立硬指标。
