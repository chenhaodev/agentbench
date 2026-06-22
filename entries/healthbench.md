---
id: healthbench
name: HealthBench
aliases: [HealthBench Hard, HealthBench Consensus]
homepage: https://openai.com/index/healthbench/
year: 2025
domain: [medical, clinical-safety, health-QA]
genre: paper-bound

authority:
  maintainers: [OpenAI]
  institution_count: 0          # not institution-counted; authority is physician-graded (262 physicians, 60 countries)
  update_cadence: irregular     # static release + Hard / Consensus variants
  online: false                 # released as an open eval set (simple-evals), not a live community leaderboard

popularity:
  trending: false               # not a HuggingFace-hosted leaderboard
  as_of: "2026-06-16"
  social:
    - { platform: x, handle: "@EricTopol", url: "https://x.com/EricTopol/status/2047126414554701836", note: "权威的独立医疗-AI 声音,在讨论 HealthBench Professional", as_of: "2026-06-16" }
    - { platform: x, handle: "@btibor91", url: "https://x.com/btibor91/status/2047227802790064322", note: "前沿发布把 HealthBench Professional 当作 THE 参考指标(如 Opus 4.8 的 55.8%)", as_of: "2026-06-16" }
    - { platform: x, handle: "@Thom_Wolf", url: "https://x.com/Thom_Wolf/status/2046560319196070016", note: "HuggingFace 联合创始人", as_of: "2026-06-16" }
    - { platform: reddit, url: "https://www.reddit.com/r/LocalLLaMA/search/?q=medical+benchmark", note: "Reddit 上几乎没有讨论;r/LocalLLaMA 更偏好自建的实用 eval(医疗 STT/WER、分诊)", as_of: "2026-06-16" }

methodology:
  evaluation: [human, llm-judge]
  contamination_controls: "开源 eval set;采用真实多轮对话,而非复用的考试题。"
  notes: "5,000 段多轮对话;262 位医生编写对话专属评分量规(共 48,562 条加权标准);由 GPT-4.1 模型评分器按量规打分。评分器与医生的 macro-F1 0.71,约等于医生间一致性。"

citations:
  - { title: "HealthBench: Evaluating Large Language Models Towards Improved Human Health", url: "https://arxiv.org/abs/2505.08775", accessed: "2026-06-16" }
  - { title: "Introducing HealthBench (OpenAI)", url: "https://openai.com/index/healthbench/", accessed: "2026-06-16" }
  - { title: "HealthBench: Advancing AI evaluation in healthcare, but not yet clinically ready (PMC review)", url: "https://pmc.ncbi.nlm.nih.gov/articles/PMC12547120/", accessed: "2026-06-16" }
  - { title: "General-purpose large language models outperform specialized clinical AI tools on medical benchmarks (Nature Medicine, 12 Jun 2026) — uses 500 HealthBench items as one of three eval stages", url: "https://www.nature.com/articles/s41591-026-04431-5", accessed: "2026-06-16" }

as_of: "2026-06-16"
freshness:
  status: fresh
  last_checked: "2026-06-16"
  note: "2025 年 5 月发布;静态 eval set,故事实稳定;模型成绩随新模型跑分而变化。"

agent_summary:
  author: agent
  generated: "2026-06-16"

expert_verdict:
  signed_by: chenhao
  signed_date: "2026-06-16"
  confidence: high          # low / medium / high 三选一

moa:
  capability_axes: [clinical-safety, health-communication, emergency-referrals, hedging-under-uncertainty]
  modalities: [text]
  access: [api, open-weights]
  recommended_for:
    - "衡量在真实多轮健康对话中的安全性与行为,而非 QA 背诵"
    - "压力测试模型如何 hedge(留有余地)、升级转诊、以及在回答前主动追问上下文"
  caveats:
    - "医生编写量规 + LLM(GPT-4.1)评分器——不是实时社区 leaderboard"
    - "由模型厂商(OpenAI)发布;需权衡利益冲突的框架效应"
    - "一篇独立 PMC 评述判定它作为部署门槛'尚未达到临床应用标准'"
---

## Agent summary

HealthBench 是 OpenAI(一家做大模型的公司)推出的一套健康类 AI 测验(arXiv 编号 2505.08775,2025 年 5 月发布),由 262 位来自约 60 个国家的医生一起编写。它的题目不是选择题,而是 5,000 段模型与用户或临床医生之间的多轮对话(一来一回、能接着往下聊的完整对话)。每段对话都配一份医生事先写好的评分细则(rubric),只针对这段对话,合起来共 48,562 条加权标准。打分的不是人,而是另一个 AI 当“阅卷老师”(让另一个大模型按细则给回答打分,叫 LLM 评判),这里用的是 GPT-4.1。OpenAI 说这个 AI 阅卷员和医生打分的吻合程度是 macro-F1 0.71(一个 0 到 1 之间的一致性指标,越高越接近),差不多等于医生彼此之间的一致程度。它还有两个变体:HealthBench Hard 是更难的一小部分题,HealthBench Consensus 则是另一个子集。和那种考选择题(MCQ)、比谁背得准的医疗问答榜不同,HealthBench 考的是 AI 的“行为”:回答全不全、会不会好好沟通、懂不懂在没把握时留有余地(hedge),以及该不该先追问情况、该不该建议转诊。它是以一份公开的测验题集发布的,不是那种能随时提交成绩、实时刷新排名的在线榜(benchmark,即给 AI 出的标准考卷)。有一篇独立的 PMC 评述提醒:它“推进了医疗 AI 评测,但[仍]尚未达到临床应用标准”。

社交热度(只代表风声和情绪,不代表权威):在我们调研过的医疗榜里,HealthBench 在英文社交平台上被提及得最多。独立人士比如 @EricTopol 在讨论它,前沿模型发布公告也把它当成“那个”要看的参考指标(例如 Opus 4.8 的 system card 就报了 HealthBench Professional 的成绩)。但要留意一个绕圈子的问题:OpenAI 自己是出题方,各家实验室又在自家宣传里引用它,所以这份关注度有一部分是厂商自己带起来的。Reddit 上几乎没人聊。具体的帖子链接见 `popularity.social`(2026-06-16 采集)。

独立采用(这才算权威,不是风声):一篇《Nature Medicine》的研究(编号 s41591-026-04431-5,2026 年 6 月 12 日)把 500 道 HealthBench 题目当作三个评测环节之一,和 MedQA、以及新的 Real-Clinical-Queries(RCQ)基准并列使用。研究显示,前沿的通用大模型(GPT-5.2、Gemini 3.1 Pro、Claude Opus 4.6)胜过了专门给临床用的工具(OpenEvidence 得 62.6,UpToDate 得 61.3)。这是经过同行评议的第三方在用它,和上面那种厂商自己带的热度是两码事。

<!-- 仅事实;来源为所引 arXiv/OpenAI/PMC 页面 + 登录浏览 X/Reddit。 -->

## Expert verdict

人工署名（chenhao）。值得探讨的是：一个由供应商编写、由LLM（大语言模型）评分的行为基准测试，如果和人类专家一致性0.85以上，就达到了评审 “决策级” 的可靠，从而可以用来为面向患者的模型进行路由选择（routing）。 “尚未达到临床应用标准（not yet clinically ready）” 这一警告/免责声明会降低可信度，除非此benchmark很有名
