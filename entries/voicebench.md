---
id: voicebench
name: VoiceBench
aliases: []
homepage: https://matthewcym.github.io/VoiceBench/
year: 2024
domain: [general, audio, speech, voice-assistant]
genre: online-leaderboard

authority:
  maintainers: [Yiming Chen / Xianghu Yue et al. (NUS — Haizhou Li group)]
  institution_count: 0
  update_cadence: irregular
  online: true

popularity:
  trending: false
  as_of: "2026-06-16"             # 在 omni tech report(如 Qwen3-Omni)的语音基准中被引用

methodology:
  evaluation: [automated]
  contamination_controls: "注入真实口语变异(口音、混响、内容复杂度),使模型无法靠干净文本走捷径。"
  notes: "6,783 条合成与真实口语指令,横跨 8 个任务。评估三个能力维度——general knowledge、instruction-following、safety——在真实说话人与环境变异下进行。发表于 TACL 2026。"

citations:
  - { title: "VoiceBench: Benchmarking LLM-Based Voice Assistants (Chen, Yue et al., 2024; TACL)", url: "https://arxiv.org/abs/2410.17196", accessed: "2026-06-16" }
  - { title: "VoiceBench — code & leaderboard (MatthewCYM/VoiceBench)", url: "https://github.com/MatthewCYM/VoiceBench", accessed: "2026-06-16" }
  - { title: "VoiceBench Leaderboard", url: "https://matthewcym.github.io/VoiceBench/", accessed: "2026-06-16" }

as_of: "2026-06-16"
freshness:
  status: fresh
  last_checked: "2026-06-16"
  note: "活跃的 leaderboard;端到端语音助手评测的标准参考。"

agent_summary:
  author: agent
  generated: "2026-06-16"

moa:
  capability_axes: [voice-assistant, spoken-instruction-following, speech-robustness, spoken-safety]
  modalities: [audio, text]
  access: [api, open-weights]
  recommended_for:
    - "在真实语音条件(口音、混响)下评测端到端语音助手"
    - "口语指令遵循 + safety——超越单纯的 ASR 转写准确率"
  caveats:
    - "部分语音是合成(TTS)——可能不完全反映真实用户音频"
    - "聚焦语音助手,通用领域"
---

## Agent summary

VoiceBench(Chen、Yue et al.,NUS,2024;TACL)是面向 **LLM 语音助手**的首个多维基准,也是经
tech-report 发现法浮现的语音基准之一(它出现在 Qwen3-Omni 等 omni 报告的音频基准里)。它由 **6,783
条合成与真实口语指令**构成,横跨 **8 个任务**,评估三个能力维度——**general knowledge、
instruction-following、safety compliance**——并刻意注入真实口语变异:**说话人特征(口音)、环境条件
(混响)、内容复杂度**。这把评测从单纯的 ASR 转写推向"它是不是一个好的口语助手"。

局限:部分语音是合成的(TTS),可能不完全反映真实用户音频,且面向通用。适合作为 MoA 中的口语交互维度
(以及一个口语 safety 检查)。

<!-- 仅事实;来源为所引 arXiv/TACL 论文与 VoiceBench 仓库。 -->

## Expert verdict

<!-- 人工署名(chenhao)。值得回答:对一个语音 MoA,VoiceBench 的口语 safety 维度是否比它的知识分更
     重要?"部分合成语音"相对真实音频基准该打多少折? -->
