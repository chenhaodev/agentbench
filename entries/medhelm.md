---
id: medhelm
name: MedHELM
aliases: [Holistic Evaluation of Language Models for Medical Tasks]
homepage: https://medhelm.org/
year: 2025
domain: [medical, clinical-tasks]
genre: online-leaderboard

authority:
  maintainers: [Stanford CRFM / BMIR, Stanford Health Care, Microsoft Health & Life Sciences, community-led (2026)]
  institution_count: 0          # multi-institutional; clinicians from 15 medical specialties (not a fixed count)
  update_cadence: irregular
  online: true                  # HELM-style public leaderboard

methodology:
  evaluation: [automated, human]
  contamination_controls: "由真实临床工作流构建、经临床医生验证的任务分类,而非复用考试题。"
  notes: "121 个临床任务,组织成经临床医生验证的任务分类:5 大类（Clinical Decision Support、Patient Communication、Clinical Note Generation、Medical Research Assistance、Administration & Workflow)、22 个子类、35 个 benchmark。同行评议、多机构;来自 15 个专科的临床医生。2026 年转为独立的社区主导项目。"

citations:
  - { title: "MedHELM — Holistic Evaluation of Language Models for Medical Tasks", url: "https://medhelm.org/", accessed: "2026-06-16" }
  - { title: "MedHELM (CRFM HELM documentation)", url: "https://crfm-helm.readthedocs.io/en/latest/medhelm/", accessed: "2026-06-16" }

as_of: "2026-06-16"
freshness:
  status: fresh
  last_checked: "2026-06-16"
  note: "2025 年初公布;2026 年起社区主导。"

agent_summary:
  author: agent
  generated: "2026-06-16"

expert_verdict:
  signed_by: chenhao
  signed_date: "2026-06-16"
  confidence: medium          # low / medium / high
  one_liner: "子榜单很经典很全面。然而，模型不太全、更新不太频繁"

moa:
  capability_axes: [clinical-decision-support, patient-communication, clinical-note-generation, medical-research-assistance, admin-workflow]
  modalities: [text]
  access: [api, open-weights]
  recommended_for:
    - "为某个 SPECIFIC 临床工作流挑模型,而不是看单一的‘医疗 IQ’数字"
    - "跨 5 大任务族做整体对比,带逐类拆解"
  caveats:
    - "设计上就是整体/多指标——没有单一头条排名;要逐类读"
    - "治理 2026 年从 Stanford+Microsoft 转为社区主导"
---

## Agent summary

HELM 是 Stanford（斯坦福）做的一套统一评测框架,给各家大模型用同一套标准打分。MedHELM（Holistic Evaluation of Language Models）就是把这套框架搬到医疗领域的版本。

它给模型出了 121 个临床任务的“考卷”,并按一套经临床医生核对过的分类把这些任务归了类:5 大类（Clinical Decision Support 临床决策支持、Patient Communication 医患沟通、Clinical Note Generation 病历书写、Medical Research Assistance 医学研究辅助、Administration & Workflow 行政与流程）,其下又分 22 个子类、35 个 benchmark（基准测试,给 AI 出的标准考卷）。

这套东西在 2025 年初由 Stanford 生物医学信息研究中心（BMIR）、Stanford Health Care 与 Microsoft（微软）Health & Life Sciences 合作公布,参与的临床医生覆盖 15 个医学专科。2026 年起,它转为独立的社区主导项目。

它有一个很特别的做法:不给出一个总排名数字,而是按大类、按任务分别报告每个模型的表现,让读者根据自己实际的工作场景去挑模型。

<!-- 仅事实;来源为 medhelm.org 与 CRFM HELM 文档。 -->

## Expert verdict

人工署名(chenhao)。值得回答: 逐任务的整体评测是否让 MedHELM 成为医疗榜里最强的 MoA 选型输入? 我认为不是，因为它最新不太频、且模型类别不全。
"没有单一排名" 对一个非领域工程师是帮助还是妨碍? 我认为很难讲。没有单一排名的话，某个场景我选任意模型应该都可以；当然，其他榜单可能会补充该信息的。
