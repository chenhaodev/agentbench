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

Open LLM Leaderboard 是 HuggingFace(一个托管开源 AI 模型的平台)维护的一份排行榜,专门给"开源模型"（open-weights，指权重公开、谁都能下载来自己部署的模型）的通用能力打分。它曾是这一类里最受关注的统一基准测试（benchmark，可以理解成给 AI 出的标准考卷),所有模型用同一套工具 EleutherAI lm-evaluation-harness 跑同样的题、出可比的分。

第一代 v1（2023）由 6 套考卷组成:ARC、HellaSwag、MMLU、TruthfulQA、Winogrande、GSM8K。后来出了两个问题:一是模型分数都逼近满分,题目区分不出高下(饱和);二是有些模型出现了数据污染,也就是训练时提前见过类似的题,靠背答案把分刷虚高。于是这一代在 2024 年 6 月被归档(sunset/archived,即停更封存)。接替它的 v2(2024-06)换了 6 套更难、更难靠死记硬背蒙混的考卷:MMLU-Pro、GPQA、MuSR、MATH、IFEval、BBH,分别测知识、推理、数学、follow 指令等。此后整个榜也已收尾,不再更新。

所以它今天主要有两个用处:一是当历史标尺,回看某个开源模型当年在统一工具下的成绩;二是当一份活教材,说明"考卷会被刷饱和、必须不断加难"这件事(正好呼应本仓库关心的去饱和主题)。但它不适合用来做今天的选型。另外,它只看自动跑分的对错,不涉及对话质量、安全,也不测模型会不会用工具。

<!-- 仅事实;来源为 HF Space 与官方归档文档。 -->

## Expert verdict

<!-- 人工署名(chenhao)。值得回答:一个已归档的榜还该不该收录?它"v1 饱和→v2 加难"的演化,对你判断
     其他榜的寿命有何启发?自动跑分的天花板在哪? -->
