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

MEDIQA 是医学 NLP 圈长期举办的 **shared task(同台竞赛)系列**,挂靠 ClinicalNLP / BioNLP workshop(NAACL/ACL),
近两年也借 CLEF/ImageCLEF 办多模态场。它的价值不是"在线排行榜",而是**每年给临床真实任务出一套带标注的新题**,
研究者同场竞赛、组织方发 overview 论文。本条专门补 **2023 之后**的同族(此前漏在 name-search 之外):

- **MEDIQA-CORR 2024** —— 病历**错误检测与纠正**(给临床文本找错、改对)。
- **MEDIQA-M3G 2024** —— **多语言多模态**医学答案生成,皮肤科消费者健康图文问答。
- **MEDIQA-MAGIC 2024/2025** —— 远程医疗的多模态 QA,含皮损区域**分割**与封闭式问答(办在 CLEF/ImageCLEF)。
- **MEDIQA-WV 2025** —— **伤口护理**图文 VQA,英/中双语,延续 M3G 的皮肤科方向。
- **MEDIQA-OE 2025** —— 从**医患对话**中抽取**医嘱(orders)**。

要点:这些任务用**新构造、逐年更换**的数据,天然抗旧训练集泄漏,且贴近临床实务(真实文本/对话/图像,
而非刷满的 MCQ recall)。但代价是**每届题量小、领域窄**,单届成绩统计力有限,只能当"年度临床任务风向标",
不能外推成通用医学能力总评。与已有的 **MEDIQA-Chat 2023**(见 [mediqa-chat] 条目)同源。

<!-- 仅事实;来源:MEDIQA 官方站 + 各届 ClinicalNLP overview 论文(ACL Anthology)。 -->

## Expert verdict

<!-- 人工署名(chenhao)。值得回答:
     1) 这种"逐年换题、贴临床实务"的 shared task,在你的信任标尺里能不能补 HealthBench/MedQA 这类大榜测不到的真实性?权重给多少?
     2) 题量小(常数百例)→ 单届排名波动大;你会把它当"任务/数据来源"还是当"模型排名依据"?
     3) 哪一两届(CORR 纠错 / OE 医嘱抽取 / WV 图文)对你的临床 MoA 最有选型价值,为什么? -->
