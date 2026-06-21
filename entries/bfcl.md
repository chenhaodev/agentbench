---
id: bfcl
name: BFCL (Berkeley Function-Calling Leaderboard)
aliases: [Berkeley Function Calling Leaderboard, BFCL v3, Gorilla BFCL]
homepage: https://gorilla.cs.berkeley.edu/leaderboard.html
year: 2024
domain: [general, tool-use, agentic, function-calling]
genre: online-leaderboard

authority:
  maintainers: [Shishir Patil et al. (UC Berkeley — Gorilla 项目)]
  institution_count: 0
  update_cadence: live           # 持续加入模型;版本演进 V1 → V3
  online: true

popularity:
  hf_space: https://huggingface.co/datasets/gorilla-llm/Berkeley-Function-Calling-Leaderboard
  trending: false
  as_of: "2026-06-17"

methodology:
  evaluation: [automated]
  contamination_controls: "用抽象语法树(AST)核对工具调用结构、而非真跑每个工具,可扩展到上千函数;V3 引入有状态多轮场景,降低记忆刷分。"
  notes: "可执行的函数调用评测:覆盖串行/并行调用、多种编程语言,用 AST 结构核对。V3 聚焦多轮、多步、有状态的 agentic 设置,并考察模型在该场景下的'弃答与推理'能力。ICML 2025。"

citations:
  - { title: "The Berkeley Function Calling Leaderboard (BFCL): From Tool Use to Agentic Evaluation of LLMs (Patil et al., ICML 2025)", url: "https://proceedings.mlr.press/v267/patil25a.html", accessed: "2026-06-17" }
  - { title: "BFCL — code & leaderboard (ShishirPatil/gorilla)", url: "https://github.com/ShishirPatil/gorilla/blob/main/berkeley-function-call-leaderboard/README.md", accessed: "2026-06-17" }
  - { title: "Berkeley-Function-Calling-Leaderboard — dataset (HuggingFace)", url: "https://huggingface.co/datasets/gorilla-llm/Berkeley-Function-Calling-Leaderboard", accessed: "2026-06-17" }

as_of: "2026-06-17"
freshness:
  status: fresh
  last_checked: "2026-06-17"
  note: "live;函数调用/工具使用的标准榜,V3 已扩到多轮 agentic。持续加入新模型。"

agent_summary:
  author: agent
  generated: "2026-06-17"

expert_verdict:
  signed_by: chenhao
  signed_date: "2026-06-22"
  confidence: medium          # low / medium / high

moa:
  capability_axes: [function-calling, tool-use, multi-turn-agentic, planning]
  modalities: [text]
  access: [api, open-weights]
  recommended_for:
    - "为 agent/工具调用选模型——这是 function-calling 事实上的标准榜"
    - "区分单轮工具调用 vs 多轮、有状态、长链路 agentic 能力(V3)"
  caveats:
    - "AST 结构核对≠真实执行成功;结构对但语义错的调用可能被算对"
    - "聚焦函数调用;不测一般对话质量或领域正确性"
---

## Agent summary

BFCL(Berkeley Function-Calling Leaderboard;UC Berkeley 的 Gorilla 项目,Patil 等,ICML 2025)是
评测 LLM **函数调用 / 工具使用**事实上的标准榜。它是**可执行**评测,覆盖串行/并行调用与多种编程语言,
关键创新是用**抽象语法树(AST)**核对每次工具调用的*结构*、而非真跑每个工具,从而能扩展到上千函数。
**V3** 把范围从单次工具调用推进到**多轮、多步、有状态的 agentic 场景**,并考察模型在其中"何时该弃答、
如何推理"。它的结论很有用:前沿模型在单轮调用上已很强,但**记忆、动态决策与长链路推理仍是难点**。

要点:AST 结构核对**不等于真实执行成功**——结构正确但语义错误的调用可能被判对;且它只测函数调用,
不涉及一般对话质量或领域正确性。

<!-- 仅事实;来源为所引 ICML 论文、Gorilla 仓库与 HF 数据集。 -->

## Expert verdict

BFCL 的 AST 结构匹配分对衡量 function-calling 已经够用,我不强求再叠一层真跑执行的私域评测;选 agent 模型时多轮 agentic(V3)分可比单轮稍高权重,但二者都直接信 BFCL 自身分即可。
