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

HealthBench 是 OpenAI 的健康-AI 评测(arXiv 2505.08775,2025 年 5 月),由 **262 位来自约
60 个国家的医生**共建。它是模型与用户或临床医生之间的 **5,000 段多轮对话**;每段对话都附带
一份**医生编写、对话专属的评分量规**(合计 48,562 条加权标准)。一个基于模型的评分器
(GPT-4.1)按量规给每个回答打分;OpenAI 报告该评分器与医生的一致性为 **macro-F1 0.71**,约
等于医生间一致性。变体包括 **HealthBench Hard**(更难子集)与 **HealthBench Consensus**。与
选择题式医疗-QA 榜不同,它针对*行为*——完整性、沟通、留有余地,以及何时该追问上下文或升级转诊。
它以开放 eval set 形式分发,而非实时、可提交的在线 leaderboard。一篇独立 PMC 评述提醒它"推进
了医疗 AI 评测,但[仍]尚未达到临床应用标准"。

**社交热度(sentiment,不是 authority):** 在所调研的医疗榜中,HealthBench 的英文社交存在感
最高——被 @EricTopol 等独立人物讨论,并在前沿模型发布公告中被当作*那个*参考指标(如 Opus 4.8
的 system card 报告 HealthBench Professional)。注意其循环性:OpenAI 既是作者,各实验室又在营销
中引用它,所以这里的关注度部分是厂商驱动的。Reddit 上几乎没有讨论。permalink 见
`popularity.social`(2026-06-16 采集)。

**独立采用(authority,不是 sentiment):** 一篇 *Nature Medicine* 研究(s41591-026-04431-5,
2026 年 6 月 12 日)把 **500 道 HealthBench 题目**用作三个评测阶段之一——与 MedQA 和新的
Real-Clinical-Queries(RCQ)基准并列——证明前沿 LLM(GPT-5.2、Gemini 3.1 Pro、Claude Opus
4.6)胜过专用临床工具(OpenEvidence 62.6、UpToDate 61.3)。这是对 HealthBench 的同行评议第三方
使用,区别于上面的厂商热度。

<!-- 仅事实;来源为所引 arXiv/OpenAI/PMC 页面 + 登录浏览 X/Reddit。 -->

## Expert verdict

人工署名（chenhao）。值得探讨的是：一个由供应商编写、由LLM（大语言模型）评分的行为基准测试，如果和人类专家一致性0.85以上，就达到了评审 “决策级” 的可靠，从而可以用来为面向患者的模型进行路由选择（routing）。 “尚未达到临床应用标准（not yet clinically ready）” 这一警告/免责声明会降低可信度，除非此benchmark很有名
