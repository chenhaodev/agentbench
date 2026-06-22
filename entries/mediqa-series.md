---
id: mediqa-series
name: MEDIQA Shared Tasks(2024–2025 系列)
aliases: [MEDIQA-CORR, MEDIQA-M3G, MEDIQA-MAGIC, MEDIQA-WV, MEDIQA-OE]
homepage: https://sites.google.com/view/mediqa-shared-tasks
year: 2024
domain: [medical, clinical, multimodal]
genre: shared-task

authority:
  maintainers: [MEDIQA 组织方(ClinicalNLP / BioNLP workshop 系列;NAACL / ACL / CLEF)]
  institution_count: 0
  update_cadence: yearly        # 每年一届,随 workshop 出题
  online: false

methodology:
  evaluation: [automated, human]
  contamination_controls: "每届用新构造/新标注的数据(临床错误、皮肤科图文、伤口护理、医嘱抽取等),逐年换题,天然抗旧训练集泄漏;但题量小、领域窄,统计力有限。"
  notes: "shared task=研究者在固定数据集上同台竞赛,组织方给官方 overview。本条覆盖 2023 之后的同族:MEDIQA-CORR 2024(病历错误检测与纠正)、MEDIQA-M3G 2024(多语言多模态医学答案生成,皮肤科)、MEDIQA-MAGIC 2024/2025(远程医疗多模态 QA + 皮损分割,办在 CLEF/ImageCLEF)、MEDIQA-WV 2025(伤口护理图文 VQA,英/中双语)、MEDIQA-OE 2025(从医患对话中抽取医嘱)。早期还有 MEDIQA 2019/2021 与 MEDIQA-Chat/-Sum 2023。"

citations:
  - { title: "MEDIQA Shared Tasks 官方站(历届任务总入口)", url: "https://sites.google.com/view/mediqa-shared-tasks", accessed: "2026-06-17" }
  - { title: "Overview of the MEDIQA-CORR 2024 Shared Task on Medical Error Detection and Correction (ClinicalNLP 2024)", url: "https://aclanthology.org/2024.clinicalnlp-1.57/", accessed: "2026-06-17" }
  - { title: "Overview of the MEDIQA-M3G 2024 Shared Task on Multilingual & Multimodal Medical Answer Generation (ClinicalNLP 2024)", url: "https://aclanthology.org/2024.clinicalnlp-1.55/", accessed: "2026-06-17" }
  - { title: "Overview of the MEDIQA-WV 2025 Shared Task on Woundcare Visual Question Answering (ClinicalNLP 2025)", url: "https://aclanthology.org/2025.clinicalnlp-1.3/", accessed: "2026-06-17" }
  - { title: "Overview of the MEDIQA-OE 2025 Shared Task on Medical Order Extraction (ClinicalNLP 2025)", url: "https://aclanthology.org/2025.clinicalnlp-1.2/", accessed: "2026-06-17" }

as_of: "2026-06-17"
freshness:
  status: fresh
  last_checked: "2026-06-17"
  note: "系列仍在持续办(2025 届有 WV/OE/MAGIC);但每届是独立 shared task、题量小,作为'年度临床任务风向标'用,不是常更新的在线排行榜。"

agent_summary:
  author: agent
  generated: "2026-06-17"

expert_verdict:
  signed_by: chenhao
  signed_date: "2026-06-17"
  confidence: medium          # low / medium / high

moa:
  capability_axes: [clinical-qa, medical-error-correction, multimodal-medical-vqa, clinical-note-generation, medical-order-extraction]
  modalities: [text, image]
  access: [api, open-weights]
  recommended_for:
    - "找临床真实场景(病历纠错、皮肤科图文问答、医嘱抽取)的评测任务与标注数据——比饱和的医学 MCQ 更贴实务"
    - "做去医疗偏斜的 census 锚点:覆盖 shared-task 这一最易被 name-search 漏掉的体裁"
  caveats:
    - "每届题量小、领域窄,单届成绩统计力弱,不能当通用医学能力的总评"
    - "是一次性竞赛的 overview,不是持续更新的在线榜;'谁领先'的口径随届变化"
    - "与已有 [mediqa-chat] 条目同源(2023 届);本条专记 2023 之后的同族任务"

tags: [medical, clinical, shared-task, census-anchor]
---

## Agent summary

MEDIQA 是医学 NLP(用计算机处理医学文本的研究方向)圈子里办了很多年的一系列 shared task(公开评测竞赛:大家在同一套题、同一套数据上比成绩)。它挂在 ClinicalNLP / BioNLP 这两个学术研讨会下面(隶属 NAACL/ACL 这些会议),近两年还借 CLEF/ImageCLEF 办了带图像的赛题。它的价值不在于做一个长期更新的在线排行榜,而是每年针对临床真实任务出一套新题、配好标注答案,让研究者上场比拼,主办方再写一篇 overview(总结)论文。本条专门补上 2023 之后的同系列赛题(这些之前靠按名字搜索容易漏掉):

- MEDIQA-CORR 2024:病历错误检测与纠正,也就是给一段临床文本挑错、再改对。
- MEDIQA-M3G 2024:多语言、多模态(同时处理文字和图像)的医学答案生成,场景是皮肤科的大众健康图文问答。
- MEDIQA-MAGIC 2024/2025:远程医疗里的图文问答,还要把皮肤病变的区域圈出来(分割)并回答封闭式问题(办在 CLEF/ImageCLEF)。
- MEDIQA-WV 2025:伤口护理的图文 VQA(看图回答问题,Visual Question Answering),英文和中文双语,接着 M3G 的皮肤科方向往下做。
- MEDIQA-OE 2025:从医患对话里抽取医嘱(orders,医生开的检查、用药等指令)。

几个要点。这些题用的都是新做、逐年更换的数据,所以旧的训练集很难提前"背"到答案,而且贴近临床实务(真实的文本、对话、图像,而不是那种刷到饱和的 MCQ(选择题)死记考点)。代价是每届题量小、领域窄,单届成绩的统计意义有限,只能当作"今年临床任务往哪走"的风向标,不能拿来推断一个模型的通用医学能力。它和已有的 MEDIQA-Chat 2023(见 [mediqa-chat] 条目)出自同一系列。

<!-- 仅事实;来源:MEDIQA 官方站 + 各届 ClinicalNLP overview 论文(ACL Anthology)。 -->

## Expert verdict

人工署名(chenhao)。值得回答:
1) 这种"逐年换题、贴临床实务"的 shared task, 在你的信任标尺里能不能补 HealthBench/MedQA 这类大榜测不到的真实性? 权重给多少? 只要够新（2年内），比HealthBench这种肯定要高，高出20%吧
2) 题量小(常数百例)→ 单届排名波动大;你会把它当"任务/数据来源"还是当"模型排名依据"? 不存在这类分法，一切以用户为中心；题型虽小但是若有名气、比较新，则可以参考的
3) 哪一两届(CORR 纠错 / OE 医嘱抽取 / WV 图文) 对你的临床 MoA 最有选型价值,为什么? CORR、OE最有用。因为MoA一般是全流程、要注意幻觉率的

