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

expert_verdict:
  signed_by: chenhao
  signed_date: "2026-06-16"
  confidence: low          # low / medium / high

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

VoiceBench(Chen、Yue et al.,NUS,2024;TACL)是给语音助手(voice assistant,你用嘴说话、它用语音回应的 AI)出的一套标准考卷(benchmark,给 AI 出的标准考卷),据称是第一套从多个角度考查这类助手的。它的来路有点特别:我们是在别人的技术报告里发现它的,比如 Qwen3-Omni 这类全模态模型的报告,会拿它来测音频能力。

这份考卷有 6,783 条口语指令(spoken instruction,用说话的方式下达的命令),一部分是机器合成的语音,一部分是真人录的,一共覆盖 8 类任务。它考三方面:通用知识(general knowledge)、听懂并照做指令(instruction-following)、安全合规(safety compliance,会不会照着危险要求乱答)。它还故意往里掺真实说话场景里的干扰,比如说话人口音、混响等环境噪声、内容本身的复杂度。这样一来,考的就不只是"能不能把话听写成文字"(也就是 ASR,语音转文字),而是"它当个语音助手到底好不好用"。

要注意的地方:有一部分语音是机器合成的(TTS,文字转语音),不一定能反映真实用户讲话的样子;而且它面向的是通用场景。拿来用的话,它适合充当 MoA(把多个模型组队、各管一块来用)里的口语交互这一块,顺带也能做个口语安全检查。

<!-- 仅事实;来源为所引 arXiv/TACL 论文与 VoiceBench 仓库。 -->

## Expert verdict

人工署名(chenhao)。值得回答:
对一个语音 MoA, VoiceBench 的口语 safety 维度是否比它的知识分更重要? 我认为是伪命题 - 这里很多合成语音、根本不是真实口语环境。
"部分合成语音"相对真实音频基准该打多少折? 我认为影响很大，打1折吧，或者直接不用了。
