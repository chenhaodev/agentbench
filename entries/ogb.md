---
id: ogb
name: Open Graph Benchmark (OGB)
aliases: [OGB, OGB-LSC]
homepage: https://ogb.stanford.edu
year: 2020
domain: [general, graph, gnn, machine-learning, representation-learning]
genre: online-leaderboard

authority:
  maintainers: [Weihua Hu, Matthias Fey, Marinka Zitnik, Yuxiao Dong, Hongyu Ren, Bowen Liu, Michele Catasta, Jure Leskovec (Stanford SNAP 等)]
  institution_count: 0
  update_cadence: irregular       # 各数据集独立榜,持续接收提交但无统一节律
  online: true

methodology:
  evaluation: [automated]
  contamination_controls: "用**有应用意义的、非随机的数据划分**(如按时间、按分子骨架 scaffold split)而非随机切分,以逼近真实泛化、抑制平凡记忆;但训练/测试同源于公开图数据,LLM 时代的'题面进训练集'式污染不是它的主要设计目标(它评的是从头训练的 GNN,不是预训练 LLM)。"
  notes: "图机器学习事实上的标准基准。统一的 loader / 划分 / 评测协议覆盖三类任务:**节点分类(node)、链接预测(link)、图属性预测(graph)**,跨社交网/生物网/分子图/源码 AST/知识图谱等域,含 small→large 多个规模。每个数据集自带 application-specific 的划分与指标,排行榜按数据集分列。另有 **OGB-LSC**(Large-Scale Challenge,百万–十亿级图,配 KDD Cup)。NeurIPS 2020。"

models_ranked:
  - { model: "(各数据集 SOTA 不同,无统一冠军)", rank: 1, axis: graph-learning, license: open-source, note: "OGB 不产单一总名次:每个数据集一张榜,领先者多为各类 GNN(GCN/GAT/GraphSAGE/SGC 及各任务专用变体)。这里 models_ranked 仅占位说明,不代表跨数据集排名。" }

citations:
  - { title: "Open Graph Benchmark: Datasets for Machine Learning on Graphs (Hu et al., NeurIPS 2020, arXiv 2005.00687)", url: "https://arxiv.org/abs/2005.00687", accessed: "2026-06-19" }
  - { title: "OGB 官方站(各数据集排行榜、loader、评测协议)", url: "https://ogb.stanford.edu", accessed: "2026-06-19" }
  - { title: "OGB-LSC: A Large-Scale Challenge for Machine Learning on Graphs (Hu et al., arXiv 2103.09430)", url: "https://arxiv.org/abs/2103.09430", accessed: "2026-06-19" }

as_of: "2026-06-19"
freshness:
  status: aging
  last_checked: "2026-06-19"
  note: "基准本身成熟、广被引用且榜仍接收提交,但 2020 年立、属 GNN 时代的标准件;作为 census 里**图/GNN 这一全新体裁的锚点**收入,与 LLM 选型只是间接相关(见 caveats)。"

agent_summary:
  author: agent
  generated: "2026-06-19"

moa:
  capability_axes: [graph-learning, node-classification, link-prediction, graph-property-prediction, representation-learning]
  modalities: [tabular]
  access: [open-weights, local]
  recommended_for:
    - "为'结构化图/关系数据'(社交网、分子、知识图谱、AST)的任务选**图编码器/GNN**——这是该能力事实上的标准榜,本 census 此前完全空白的图体裁"
    - "需要可复现横比时:它的统一 loader + 非随机划分 + 固定指标,比自切数据集更可信"
  caveats:
    - "评的是从头训练的 **GNN/图模型,不是 LLM** —— 对以 LLM 选型为主的 MoA 是**间接**输入(类似 signalmc-med 之于 bio-signal)"
    - "无单一总名次:每个数据集一张榜,'谁最强'要按你的具体任务/图类型看,不能跨数据集横比"
    - "2020 年立,部分小数据集已接近饱和;前沿研究多转向 OGB-LSC 大规模赛道"

tags: [graph, gnn, machine-learning, census-anchor, executable-eval]
---

## Agent summary

Open Graph Benchmark(OGB,Hu、Leskovec 等,Stanford SNAP,**NeurIPS 2020**,arXiv 2005.00687)是**图机器学习事实上的标准基准**,
补本 repo 此前完全空白的 **图 / GNN 体裁**。它提供一套**统一的数据加载、数据划分与评测协议**,让图模型的横比可复现——
在它之前,图 ML 论文各用各的小数据集和切分,结果难比。

**它测什么。** 三类任务:**节点分类(node property)、链接预测(link property)、图属性预测(graph property)**,
覆盖社交网络、生物网络、分子图、源码 AST、知识图谱等多个域,数据规模从小到大都有。关键设计是**有应用意义的、非随机划分**
(例如分子任务按 scaffold 切、时序图按时间切),逼近真实泛化场景而非平凡记忆。每个数据集**各自一张排行榜**、各自的指标。
另有 **OGB-LSC**(Large-Scale Challenge,百万到十亿级大图,配 KDD Cup),把战线推到工业规模。

**怎么读名次。** OGB **不产单一总冠军**——领先模型按数据集而异,多为各类 GNN(GCN、GAT、GraphSAGE、SGC 及任务专用变体)。
所以"OGB 第一名"这种说法没有意义,要落到具体数据集 + 任务类型。

**对 MoA 的定位(三信号分离)。** 权威性高(Stanford、NeurIPS、广被引用,且榜仍活),但要点醒:它评的是**从头训练的图模型,不是 LLM**——
对以 LLM 选型为主的 MoA,它和 signalmc-med 一样是**间接**输入,回答"图编码器值不值得进 pipeline / 选哪类 GNN",而不是"哪个聊天模型强"。
引用数本条**未核实具体数值**(其量级很大但不臆造)。

<!-- 仅事实;来源:arXiv 2005.00687(NeurIPS 2020)、ogb.stanford.edu、arXiv 2103.09430(OGB-LSC)。"无单一名次"为该基准设计事实。 -->

## Expert verdict

<!-- 人工署名(chenhao)。在本注释之外用中文作答:
     1) OGB 评的是 GNN/图编码器、不是 LLM。在你的 MoA(以 LLM 选型为主)里,图模型该作为独立模块纳入,还是先不收?什么任务会让你真去查这张榜?
     2) 它无单一总名次、按数据集分列:这种"必须落到具体任务才有意义"的榜,对非图领域的 AI 工程师可用性如何?该不该在站点里特别提示读法?
     3) 2020 年的成熟基准、部分饱和:你给它 fresh 还是 aging?作为图体裁的 census 锚点,它够不够,还是该再配一个更新的图 LLM/图推理基准? -->
