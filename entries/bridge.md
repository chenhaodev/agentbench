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
  note: "实时 leaderboard;模型覆盖数字（99 个 LLM）为截至 2025-11-04。"

agent_summary:
  author: agent
  generated: "2026-06-16"

expert_verdict:
  signed_by: chenhao
  signed_date: "2026-06-16"
  confidence: high          # low / medium / high
  one_liner: "Harvard, MGH等权威机构，且榜单比较新"

moa:
  capability_axes: [clinical-text-understanding, multilingual-clinical]
  modalities: [text]
  access: [api, open-weights]
  recommended_for:
    - "多语种、真实临床文本理解（不是考试 QA)"
    - "考察临床文档上 few-shot 与 chain-of-thought 的表现差异"
  caveats:
    - "聚焦临床文本理解——不涉及对话安全或患者沟通"
    - "比 MCQ 榜更贴近部署文本,但偏任务抽取形态,不是端到端诊疗"
---

## Agent summary

BRIDGE（arXiv 2504.19467,2025;由 YLab-Open 维护）是一份给 AI 出的标准考卷（benchmark,基准测试）,专门考多种语言下对真实临床文本的理解。它有 87 个临床文本任务,覆盖 9 种语言、超过 1,000,000 条样本。每个模型会在三种答题设置下打分:zero-shot（不给例子直接答）、few-shot（先看几道带答案的例题再答）、chain-of-thought（让模型把推理一步步写出来再给结论）。

配套的 HuggingFace Space 上有一个在线榜单（leaderboard）,已经系统地考过 99 个前沿大模型（LLM,即没做专门改造的通用大模型那一类）,数字截至 2025-11-04。

它跟很多医疗考卷不一样的地方在于:题目取自真实临床文档,而不是考试式的选择题（MCQ）题库。这让它更贴近实际部署里处理临床文档的场景,代价是它不考多轮对话、安全和与患者的沟通。

<!-- 仅事实;来源为所引 arXiv 论文与 HF Space。 -->

## Expert verdict

人工署名(chenhao)。"真实临床文本" 的真实性, 是否足以让人信任 BRIDGE 用于路由? 我认为是的。
9 语种覆盖对非英语部署有什么价值? 在中国没有价值。
