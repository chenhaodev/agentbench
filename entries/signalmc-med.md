---
id: signalmc-med
name: SignalMC-MED
aliases: [SignalMC MED]
homepage: https://arxiv.org/abs/2603.09940
year: 2026
domain: [medical, bio-signal, ecg, ppg, multimodal]
genre: dataset

authority:
  maintainers: [Fredrik K. Gustafsson, Xiao Gu, ... David A. Clifton 等(Oxford 等)]
  institution_count: 0
  update_cadence: frozen         # 论文随附的固定 benchmark
  online: false

methodology:
  evaluation: [automated]
  contamination_controls: "新构造的临床数据集(同步 ECG+PPG,22,256 次就诊),非网络公开题库,泄漏风险低;但来自有限来源/队列,跨机构外推性待验。"
  notes: "评测**生物信号 foundation model(信号编码器)**、不是 LLM。数据为 22,256 次就诊、每次 10 分钟重叠的**单导联 ECG + PPG**;含 **20 个临床任务**:人口学预测、急诊去向(ED disposition)、化验值回归、既往 ICD-10 诊断检出。主要发现:领域专用生物信号模型优于通用时间序列模型;**ECG+PPG 多模态融合**优于单信号。arXiv 2026-03。"

citations:
  - { title: "SignalMC-MED: A Multimodal Benchmark for Evaluating Biosignal Foundation Models on Single-Lead ECG and PPG(arXiv 2603.09940)", url: "https://arxiv.org/abs/2603.09940", accessed: "2026-06-17" }

as_of: "2026-06-17"
freshness:
  status: fresh
  last_checked: "2026-06-17"
  note: "很新(2026-03),尚未成为社区标准;作为'生物信号 FM 评测'这一稀缺体裁的 census 锚点收入,权威性待时间检验。"

agent_summary:
  author: agent
  generated: "2026-06-17"

moa:
  capability_axes: [biosignal-encoding, ecg-interpretation, ppg, clinical-prediction, multimodal-fusion]
  modalities: [tabular]
  access: [open-weights, local]
  recommended_for:
    - "为'读生理波形(ECG/PPG)'的临床任务找评测——这是 census 里基本空白的 bio-signal 体裁"
    - "判断生物信号**编码器**该不该进可穿戴/床旁监护类 pipeline(多模态融合是否值)"
  caveats:
    - "测的是信号 **foundation model(编码器)**,不是 LLM —— 对纯 LLM 的 MoA 选型只是**间接**输入"
    - "单导联 + 有限队列来源,跨机构/人群外推性待验"
    - "非常新(2026-03),还不是公认标准;别当成熟基准用,作 census 锚点为主"

tags: [medical, bio-signal, ecg, ppg, census-anchor]
---

## Agent summary

SignalMC-MED 是少见的**生物信号(physiological waveform)评测基准**,补 repo 里基本空白的 bio-signal 体裁。
要先说清:它评的是**生物信号 foundation model(把 ECG/PPG 波形编码成表示的"信号编码器")**,**不是 LLM**——
对以 LLM 选型为主的 MoA,它是**间接**输入(回答"信号编码器值不值得进 pipeline",而非"哪个聊天模型强")。

数据是 **22,256 次就诊**、每次 10 分钟重叠的**单导联 ECG + PPG**,定义了 **20 个临床任务**:人口学预测、
急诊去向(ED disposition)、化验值回归、既往 ICD-10 诊断检出。主要发现:**领域专用**生物信号模型优于通用时间序列模型;
**ECG+PPG 多模态融合**优于单信号输入。

诚实标注:它**非常新**(arXiv 2026-03),尚未成为社区公认标准;且是单导联 + 有限队列,跨机构外推性待验。
这里把它作为 **bio-signal 这一稀缺体裁的 census 锚点**收入——权威性留给时间和专家判断。

<!-- 仅事实;来源:arXiv 2603.09940 摘要。这是新近预印本,单一一手来源,权威性待验,已在 caveats/freshness 标注。 -->

## Expert verdict

<!-- 人工署名(chenhao)。值得回答:
     1) 它测的是信号编码器、不是 LLM——在你的 MoA(以 LLM 选型为主)里,bio-signal FM 该作为独立模块还是先不纳入?
     2) 非常新、单一队列、单导联:你给一个 2026-03 预印本基准多少信任?是否要等多机构复现/同行评审再算数?
     3) "ECG+PPG 融合更好"这类结论,对你判断可穿戴/床旁监护的 MoA 设计有没有实际选型价值? -->
