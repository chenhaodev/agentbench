---
id: bfcl
name: BFCL (Berkeley Function-Calling Leaderboard)
aliases: [Berkeley Function Calling Leaderboard, BFCL v3, Gorilla BFCL]
homepage: https://gorilla.cs.berkeley.edu/leaderboard.html
year: 2024
domain: [general, tool-use, agentic, function-calling]
genre: online-leaderboard

authority:
  maintainers: [Shishir Patil et al. (UC Berkeley — Gorilla 项目）]
  institution_count: 0
  update_cadence: live           # 持续加入模型;版本演进 V1 → V3
  online: true

popularity:
  hf_space: https://huggingface.co/datasets/gorilla-llm/Berkeley-Function-Calling-Leaderboard
  trending: false
  as_of: "2026-06-17"

methodology:
  evaluation: [automated]
  contamination_controls: "用抽象语法树（AST）核对工具调用结构、而非真跑每个工具,可扩展到上千函数;V3 引入有状态多轮场景,降低记忆刷分。"
  notes: "可执行的函数调用评测:覆盖串行/并行调用、多种编程语言,用 AST 结构核对。V3 聚焦多轮、多步、有状态的 agentic 设置,并考察模型在该场景下的‘弃答与推理’能力。ICML 2025。"

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
    - "区分单轮工具调用 vs 多轮、有状态、长链路 agentic 能力（V3)"
  caveats:
    - "AST 结构核对≠真实执行成功;结构对但语义错的调用可能被算对"
    - "聚焦函数调用;不测一般对话质量或领域正确性"
---

## Agent summary

BFCL（Berkeley Function-Calling Leaderboard）出自 UC Berkeley 的 Gorilla 项目,Patil 等人,发表于 ICML 2025。它是一份给 AI 出的标准考卷（benchmark）,专门考大模型（LLM）会不会按格式调用外部函数、工具,也就是“function/tool calling”。这件事现在公认要看它的分。它的考法是真去跑代码:覆盖一次只调一个工具、一次并排调好几个工具的情况,也覆盖多种编程语言。最关键的一招,是它不真把每个工具都执行一遍,而是用“抽象语法树（AST,可以理解成把代码拆成一棵结构树）”去核对每次调用写得对不对,这样才扛得住上千个函数的规模。

到了 V3 版本,考的范围从“调一次工具”扩到了能自己分步骤、调工具干活的 AI（agent/智能体）场景:要多轮来回、分多步、还要记住前面发生过什么。它还顺带考一件事:模型什么时候该承认自己答不了、又该怎么一步步推理。结论挺有用:最前沿的模型在“调一次工具”上已经很强了,但记忆、临场决策、长链条推理还是难关。

有两点要留神。第一,AST 只核对调用的结构对不对,不等于真跑成功;有些调用结构没错、意思却错了,也可能被算对。第二,它只考函数调用这一件事,不管日常对话好不好、也不管具体领域答得对不对。

<!-- 仅事实;来源为所引 ICML 论文、Gorilla 仓库与 HF 数据集。 -->

## Expert verdict

BFCL 的 AST 结构匹配分对衡量 function-calling 已经够用,我不强求再叠一层真跑执行的私域评测;选 agent 模型时多轮 agentic(V3)分可比单轮稍高权重,但二者都直接信 BFCL 自身分即可。
