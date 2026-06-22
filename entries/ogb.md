---
id: ogb
name: Open Graph Benchmark (OGB)
aliases: [OGB, OGB-LSC]
homepage: https://ogb.stanford.edu
year: 2020
domain: [general, graph, gnn, machine-learning, representation-learning]
genre: online-leaderboard

authority:
  maintainers: [Weihua Hu, Matthias Fey, Marinka Zitnik, Yuxiao Dong, Hongyu Ren, Bowen Liu, Michele Catasta, Jure Leskovec (Stanford SNAP 等）]
  institution_count: 0
  update_cadence: irregular       # 各数据集独立榜,持续接收提交但无统一节律
  online: true

methodology:
  evaluation: [automated]
  contamination_controls: "用**有应用意义的、非随机的数据划分**（如按时间、按分子骨架 scaffold split）而非随机切分,以逼近真实泛化、抑制平凡记忆;但训练/测试同源于公开图数据,LLM 时代的‘题面进训练集’式污染不是它的主要设计目标（它评的是从头训练的 GNN,不是预训练 LLM)。"
  notes: "图机器学习事实上的标准基准。统一的 loader / 划分 / 评测协议覆盖三类任务:**节点分类（node)、链接预测（link)、图属性预测（graph)**,跨社交网/生物网/分子图/源码 AST/知识图谱等域,含 small→large 多个规模。每个数据集自带 application-specific 的划分与指标,排行榜按数据集分列。另有 **OGB-LSC**(Large-Scale Challenge,百万–十亿级图,配 KDD Cup)。NeurIPS 2020。"

models_ranked:
  - { model: "（各数据集 SOTA 不同,无统一冠军）", rank: 1, axis: graph-learning, license: open-source, note: "OGB 不产单一总名次:每个数据集一张榜,领先者多为各类 GNN(GCN/GAT/GraphSAGE/SGC 及各任务专用变体）。这里 models_ranked 仅占位说明,不代表跨数据集排名。" }

citations:
  - { title: "Open Graph Benchmark: Datasets for Machine Learning on Graphs (Hu et al., NeurIPS 2020, arXiv 2005.00687)", url: "https://arxiv.org/abs/2005.00687", accessed: "2026-06-19" }
  - { title: "OGB 官方站（各数据集排行榜、loader、评测协议）", url: "https://ogb.stanford.edu", accessed: "2026-06-19" }
  - { title: "OGB-LSC: A Large-Scale Challenge for Machine Learning on Graphs (Hu et al., arXiv 2103.09430)", url: "https://arxiv.org/abs/2103.09430", accessed: "2026-06-19" }

as_of: "2026-06-19"
freshness:
  status: aging
  last_checked: "2026-06-19"
  note: "基准本身成熟、广被引用且榜仍接收提交,但 2020 年立、属 GNN 时代的标准件;作为 census 里**图/GNN 这一全新体裁的锚点**收入,与 LLM 选型只是间接相关（见 caveats)。"

agent_summary:
  author: agent
  generated: "2026-06-19"

moa:
  capability_axes: [graph-learning, node-classification, link-prediction, graph-property-prediction, representation-learning]
  modalities: [tabular]
  access: [open-weights, local]
  recommended_for:
    - "为‘结构化图/关系数据’（社交网、分子、知识图谱、AST）的任务选**图编码器/GNN**——这是该能力事实上的标准榜,本 census 此前完全空白的图体裁"
    - "需要可复现横比时:它的统一 loader + 非随机划分 + 固定指标,比自切数据集更可信"
  caveats:
    - "评的是从头训练的 **GNN/图模型,不是 LLM** —— 对以 LLM 选型为主的 MoA 是**间接**输入（类似 signalmc-med 之于 bio-signal)"
    - "无单一总名次:每个数据集一张榜,'谁最强‘要按你的具体任务/图类型看,不能跨数据集横比"
    - "2020 年立,部分小数据集已接近饱和;前沿研究多转向 OGB-LSC 大规模赛道"

tags: [graph, gnn, machine-learning, census-anchor, executable-eval]
---

## Agent summary

先说图（graph）是什么:由“节点 + 连线”构成的数据,比如社交网络里的人和好友关系,或者分子里的原子和化学键。处理这类数据的 AI 模型叫图神经网络（GNN）。Open Graph Benchmark（OGB,由 Hu、Leskovec 等人在斯坦福 SNAP 实验室做出,发表于 **NeurIPS 2020**,论文 arXiv 2005.00687）是这一行当公认的标准考卷（benchmark）,也填上了本 repo 之前完全空白的图 / GNN 这一类。它给出一套统一的数据加载、数据划分和评分规则,让不同图模型能放在同样的条件下比较,而且别人能复现结果。在它出现之前,做图机器学习的论文各用各的小数据集、各切各的训练测试集,谁强谁弱根本比不清楚。

它测三类任务:节点分类（node property,猜某个节点的属性）、链接预测（link property,猜两个节点之间是否有连线）、图属性预测（graph property,判断整张图的属性）。测试数据覆盖社交网络、生物网络、分子图、源代码的语法树（AST）、知识图谱等多个领域,图的规模从小到大都有。它有个关键设计:划分训练集和测试集时不用随机切,而是按真实场景里有意义的方式切（比如分子任务按分子骨架 scaffold 切,带时间的图按时间先后切）,这样更接近“模型遇到没见过的新情况”时的真实表现,而不是让模型靠死记硬背蒙混过关。每个数据集都有自己的一张排行榜（leaderboard）和自己的评分指标。此外还有 OGB-LSC（Large-Scale Challenge,大规模挑战赛,图的规模到百万乃至十亿级,配套 KDD Cup 比赛）,把难度推到了工业级别。

怎么看排名?OGB 不评单一总冠军。领先的模型因数据集而异,大多是各种 GNN（GCN、GAT、GraphSAGE、SGC,以及为具体任务定制的变体）。所以说“OGB 第一名”是没有意义的,必须落到某个具体数据集加某种任务类型上才能谈。

它对 MoA（把多个模型组队、各管一块来用）的位置:这里要把三种信号分开看。权威性很高（斯坦福出品、NeurIPS 发表、被大量引用,排行榜至今还在收新成绩）。但要提醒一句,它考的是从头训练的图模型,不是 LLM（大语言模型）。所以对以挑选 LLM 为主的 MoA 来说,它和 signalmc-med 一样只是间接参考,回答的是“图编码器值不值得加进 pipeline、该选哪类 GNN”,而不是“哪个聊天模型更强”。引用数本条没有核实具体数值（量级很大,但不凭空编造）。

<!-- 仅事实;来源:arXiv 2005.00687（NeurIPS 2020）、ogb.stanford.edu、arXiv 2103.09430（OGB-LSC）。“无单一名次”为该基准设计事实。 -->

## Expert verdict

<!-- 人工署名(chenhao)。在本注释之外用中文作答:
     1) OGB 评的是 GNN/图编码器、不是 LLM。在你的 MoA(以 LLM 选型为主)里,图模型该作为独立模块纳入,还是先不收?什么任务会让你真去查这张榜?
     2) 它无单一总名次、按数据集分列:这种"必须落到具体任务才有意义"的榜,对非图领域的 AI 工程师可用性如何?该不该在站点里特别提示读法?
     3) 2020 年的成熟基准、部分饱和:你给它 fresh 还是 aging?作为图体裁的 census 锚点,它够不够,还是该再配一个更新的图 LLM/图推理基准? -->
