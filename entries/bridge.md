---
id: bridge
name: BRIDGE
aliases: [BRIDGE Medical Leaderboard]
homepage: https://huggingface.co/spaces/YLab-Open/BRIDGE-Medical-Leaderboard
year: 2025
domain: [medical, clinical-text, multilingual]
genre: online-leaderboard

authority:
  maintainers: [YLab-Open]
  institution_count: 0
  update_cadence: live          # leaderboard grows as models are submitted/evaluated
  online: true

popularity:
  hf_space: https://huggingface.co/spaces/YLab-Open/BRIDGE-Medical-Leaderboard
  as_of: "2026-06-16"

methodology:
  evaluation: [automated]
  contamination_controls: "取自真实临床实践文本,而非考试式 MCQ 题库。"
  notes: "87 个真实临床文本任务,横跨 9 种语言、超过 1,000,000 条样本;报告 zero-shot、few-shot 与 chain-of-thought 三种设置;截至 2025-11-04 已评测 99 个 LLM。"

citations:
  - { title: "BRIDGE: Benchmarking Large Language Models for Understanding Real-world Clinical Practice Text", url: "https://arxiv.org/abs/2504.19467", accessed: "2026-06-16" }
  - { title: "BRIDGE Medical Leaderboard (HuggingFace Space)", url: "https://huggingface.co/spaces/YLab-Open/BRIDGE-Medical-Leaderboard", accessed: "2026-06-16" }

as_of: "2026-06-16"
freshness:
  status: fresh
  last_checked: "2026-06-16"
  note: "实时 leaderboard;模型覆盖数字(99 个 LLM)为截至 2025-11-04。"

agent_summary:
  author: agent
  generated: "2026-06-16"

moa:
  capability_axes: [clinical-text-understanding, multilingual-clinical]
  modalities: [text]
  access: [api, open-weights]
  recommended_for:
    - "多语种、真实临床文本理解(不是考试 QA)"
    - "考察临床文档上 few-shot 与 chain-of-thought 的表现差异"
  caveats:
    - "聚焦临床文本理解——不涉及对话安全或患者沟通"
    - "比 MCQ 榜更贴近部署文本,但偏任务抽取形态,不是端到端诊疗"
---

## Agent summary

BRIDGE(arXiv 2504.19467,2025;由 YLab-Open 维护)是一个**真实世界临床实践文本的多语种基准**。
它包含 **87 个临床文本任务,横跨 9 种语言、超过 1,000,000 条样本**,并在 **zero-shot、few-shot、
chain-of-thought** 三种设置下报告模型成绩。配套的 HuggingFace Space leaderboard 系统性评测了
**99 个前沿 LLM**(截至 2025-11-04)。它的独特之处在于从*真实临床文档*取材,而非考试式选择题库,
这使它更接近部署中的文档级临床 NLP——代价是不测试多轮对话、安全或患者沟通。

<!-- 仅事实;来源为所引 arXiv 论文与 HF Space。 -->

## Expert verdict

<!-- 人工署名(chenhao)。值得回答:"真实临床文本"的真实性,是否足以让人信任 BRIDGE 用于路由?
     9 语种覆盖对非英语部署有什么价值? -->
