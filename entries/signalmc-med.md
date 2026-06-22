---
id: signalmc-med
name: SignalMC-MED
aliases: [SignalMC MED]
homepage: https://arxiv.org/abs/2603.09940
year: 2026
domain: [medical, bio-signal, ecg, ppg, multimodal]
genre: dataset

authority:
  maintainers: [Fredrik K. Gustafsson, Xiao Gu, ... David A. Clifton 等（Oxford 等）]
  institution_count: 0
  update_cadence: frozen         # 论文随附的固定 benchmark
  online: false

methodology:
  evaluation: [automated]
  contamination_controls: "新构造的临床数据集（同步 ECG+PPG,22,256 次就诊）,非网络公开题库,泄漏风险低;但来自有限来源/队列,跨机构外推性待验。"
  notes: "评测**生物信号 foundation model（信号编码器）**、不是 LLM。数据为 22,256 次就诊、每次 10 分钟重叠的**单导联 ECG + PPG**;含 **20 个临床任务**:人口学预测、急诊去向（ED disposition)、化验值回归、既往 ICD-10 诊断检出。主要发现:领域专用生物信号模型优于通用时间序列模型;**ECG+PPG 多模态融合**优于单信号。arXiv 2026-03。"

citations:
  - { title: "SignalMC-MED: A Multimodal Benchmark for Evaluating Biosignal Foundation Models on Single-Lead ECG and PPG(arXiv 2603.09940)", url: "https://arxiv.org/abs/2603.09940", accessed: "2026-06-17" }

as_of: "2026-06-17"
freshness:
  status: fresh
  last_checked: "2026-06-17"
  note: "很新（2026-03),尚未成为社区标准;作为‘生物信号 FM 评测’这一稀缺体裁的 census 锚点收入,权威性待时间检验。"

agent_summary:
  author: agent
  generated: "2026-06-17"

moa:
  capability_axes: [biosignal-encoding, ecg-interpretation, ppg, clinical-prediction, multimodal-fusion]
  modalities: [tabular]
  access: [open-weights, local]
  recommended_for:
    - "为‘读生理波形（ECG/PPG)’的临床任务找评测——这是 census 里基本空白的 bio-signal 体裁"
    - "判断生物信号**编码器**该不该进可穿戴/床旁监护类 pipeline（多模态融合是否值）"
  caveats:
    - "测的是信号 **foundation model（编码器）**,不是 LLM —— 对纯 LLM 的 MoA 选型只是**间接**输入"
    - "单导联 + 有限队列来源,跨机构/人群外推性待验"
    - "非常新（2026-03),还不是公认标准;别当成熟基准用,作 census 锚点为主"

tags: [medical, bio-signal, ecg, ppg, census-anchor]
---

## Agent summary

SignalMC-MED 是一份少见的生物信号（physiological waveform,指心电、脉搏这类随时间起伏的生理波形）考卷,也就是给 AI 出的标准测试（benchmark）。它补上了本库里基本空白的 bio-signal 这一类。

先说清楚一件容易混的事:它考的是生物信号 foundation model,也就是把 ECG/PPG 波形读进来、压成一组数字表示的“信号编码器”,而不是我们平时说的聊天用大模型（LLM）。所以对一个主要靠挑 LLM 来组队的 MoA（把多个模型组队、各管一块来用）来说,它只能算间接参考:它回答的是“这种信号编码器值不值得放进流程里”,不是“哪个聊天模型更强”。

数据来自 22,256 次就诊,每次取 10 分钟、互相重叠的单导联 ECG（心电图）加 PPG（脉搏波）,在上面定义了 20 个临床任务,比如预测人口学信息、判断急诊去向（ED disposition,即病人从急诊后续往哪儿走）、回归化验数值、检出过去的 ICD-10 诊断（ICD-10 是国际通用的疾病编码）。主要结论有两条。一是专门为这个领域做的生物信号模型,表现好过通用的时间序列模型。二是把 ECG 和 PPG 两种信号合在一起（多模态融合,即同时用多种信号）,效果好过只用单一信号。

也得如实说它的短板。它非常新（arXiv 2026-03）,还没成为社区公认的标准;而且只用了单导联、病例来源有限,换一家机构、换一批人群能不能照样管用,还没验证过。所以这里只是把它当作 bio-signal 这个稀缺类别的一个 census 锚点（census 指按类别逐项普查、而非只搜得到名字的东西）先收进来,权威性留给时间和专家去判断。

<!-- 仅事实;来源:arXiv 2603.09940 摘要。这是新近预印本,单一一手来源,权威性待验,已在 caveats/freshness 标注。 -->

## Expert verdict

<!-- 人工署名(chenhao)。值得回答:
     1) 它测的是信号编码器、不是 LLM——在你的 MoA(以 LLM 选型为主)里,bio-signal FM 该作为独立模块还是先不纳入?
     2) 非常新、单一队列、单导联:你给一个 2026-03 预印本基准多少信任?是否要等多机构复现/同行评审再算数?
     3) "ECG+PPG 融合更好"这类结论,对你判断可穿戴/床旁监护的 MoA 设计有没有实际选型价值? -->
