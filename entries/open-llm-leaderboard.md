---
id: open-llm-leaderboard
name: Open LLM Leaderboard
aliases: [HF Open LLM Leaderboard, Open LLM Leaderboard v2]
homepage: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard
year: 2023
domain: [general, llm-reasoning]
genre: online-leaderboard

authority:
  maintainers: [Hugging Face]
  institution_count: 0
  update_cadence: frozen          # v1 于 2024-06 归档;v2 接替后该项目亦已收尾
  online: true

popularity:
  hf_space: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard
  trending: false
  as_of: "2026-06-17"

methodology:
  evaluation: [automated]
  contamination_controls: "v1 因饱和+污染被归档;v2 换上更难、更抗记忆的题集(GPQA、MMLU-Pro 等)。"
  notes: "用 EleutherAI lm-evaluation-harness 统一跑分。v1(2023):ARC、HellaSwag、MMLU、TruthfulQA、Winogrande、GSM8K——2024-06 因基准饱和与污染归档。v2(2024-06):MMLU-Pro、GPQA、MuSR、MATH、IFEval、BBH(更难)。"

citations:
  - { title: "Open LLM Leaderboard (HuggingFace Space)", url: "https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard", accessed: "2026-06-17" }
  - { title: "Open LLM Leaderboard v1 archive (HuggingFace docs)", url: "https://huggingface.co/docs/leaderboards/en/open_llm_leaderboard/archive", accessed: "2026-06-17" }

as_of: "2026-06-17"
freshness:
  status: stale
  last_checked: "2026-06-17"
  note: "v1 已于 2024-06 归档;v2 接替后该榜整体已收尾。作为历史标尺有价值,当前选型请用活跃榜。"

agent_summary:
  author: agent
  generated: "2026-06-17"

moa:
  capability_axes: [general-knowledge, reasoning, instruction-following, math]
  modalities: [text]
  access: [open-weights]
  recommended_for:
    - "理解'开源模型通用能力'这一类榜的演化(v1 饱和 → v2 加难)"
    - "回溯历史:某开源模型在统一 harness 下的旧成绩"
  caveats:
    - "v1 已归档(饱和+污染);整体项目已收尾——别用它做当前选型"
    - "纯自动跑分,不测对话质量、安全或工具使用"
---

## Agent summary

Open LLM Leaderboard 是 HuggingFace 维护的**开源 LLM 通用能力**榜,曾是该领域最受关注的统一基准,
用 **EleutherAI lm-evaluation-harness** 跑分。**v1**(2023)由 6 个基准组成——ARC、HellaSwag、
MMLU、TruthfulQA、Winogrande、GSM8K——但因模型逼近**饱和**、且部分模型出现**污染**(训练见过类似
题),于 **2024 年 6 月归档**。**v2**(2024-06)换上更难、更抗记忆的 6 个基准——MMLU-Pro、GPQA、
MuSR、MATH、IFEval、BBH。此后该榜整体已收尾。

它今天的价值更多是**历史标尺**与"榜会饱和、需要不断加难"的活教材(正与本仓库的去饱和主题呼应),而非
当前选型依据。它也只测自动跑分,不涉及对话质量、安全或工具使用。

<!-- 仅事实;来源为 HF Space 与官方归档文档。 -->

## Expert verdict

<!-- 人工署名(chenhao)。值得回答:一个已归档的榜还该不该收录?它"v1 饱和→v2 加难"的演化,对你判断
     其他榜的寿命有何启发?自动跑分的天花板在哪? -->
