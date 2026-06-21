---
id: mteb
name: MTEB
aliases: [Massive Text Embedding Benchmark]
homepage: https://huggingface.co/spaces/mteb/leaderboard
year: 2022
domain: [general, embeddings, retrieval]
genre: online-leaderboard

authority:
  maintainers: [Niklas Muennighoff et al. (Hugging Face / Cohere 等社区)]
  institution_count: 0
  update_cadence: live           # HF leaderboard,持续接受模型提交
  online: true

popularity:
  hf_space: https://huggingface.co/spaces/mteb/leaderboard
  trending: false
  as_of: "2026-06-17"

methodology:
  evaluation: [automated]
  contamination_controls: "覆盖 8 类任务/数百数据集,单一任务过拟合难以拉高总分;但公开数据集仍有训练泄漏风险。"
  notes: "8 类文本嵌入任务(Bitext mining、classification、clustering、pair classification、reranking、retrieval、STS、summarization),58 个数据集,覆盖 112 种语言。是比较文本嵌入/检索模型事实上的标准榜。"

citations:
  - { title: "MTEB: Massive Text Embedding Benchmark (Muennighoff et al., 2022)", url: "https://arxiv.org/abs/2210.07316", accessed: "2026-06-17" }
  - { title: "MTEB Leaderboard (HuggingFace Space)", url: "https://huggingface.co/spaces/mteb/leaderboard", accessed: "2026-06-17" }

as_of: "2026-06-17"
freshness:
  status: fresh
  last_checked: "2026-06-17"
  note: "live;嵌入模型选型的标准参考。注意子榜/语种很多,需按任务读。"

agent_summary:
  author: agent
  generated: "2026-06-17"

expert_verdict:
  signed_by: chenhao
  signed_date: "2026-06-22"
  confidence: medium          # low / medium / high

moa:
  capability_axes: [text-embeddings, retrieval, reranking, semantic-similarity]
  modalities: [text]
  access: [api, open-weights]
  recommended_for:
    - "为 RAG/检索/聚类选嵌入模型——这是该领域事实上的标准榜"
    - "多语种(112 语)嵌入能力对比"
  caveats:
    - "总分会掩盖任务差异;按你的任务(如 retrieval)读子榜,别只看 overall"
    - "公开数据集存在训练泄漏风险;高分未必迁移到你的私有语料"
---

## Agent summary

MTEB(Massive Text Embedding Benchmark;Muennighoff 等,2022,arXiv 2210.07316)是比较**文本
嵌入模型**事实上的标准榜,托管在 HuggingFace。它覆盖 **8 类嵌入任务**——bitext mining、分类、
聚类、pair classification、reranking、检索(retrieval)、STS、摘要——共 **58 个数据集、112 种
语言**,以统一口径给嵌入模型打分并排名。对 RAG / 检索 / 语义相似度选型,它是最直接的入口。

要点:它是**通用嵌入**榜,`overall` 总分会掩盖任务间差异——做 retrieval 就读 retrieval 子榜,别只
看综合分;而且底层是公开数据集,存在训练泄漏风险,高分未必迁移到你的私有语料。

<!-- 仅事实;来源为所引 arXiv 论文与 HF 榜。 -->

## Expert verdict

为 RAG 选嵌入模型时我只看 retrieval 子榜,不信 overall 综合分;112 语覆盖对中文、尤其中文医疗检索的迁移性有限,加上公开数据集泄漏风险,最终一定要配自建的中文(医疗)私域检索评测来定。
