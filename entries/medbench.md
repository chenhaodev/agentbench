---
id: medbench
name: MedBench
aliases: [OpenCompass MedBench]
homepage: https://medbench.opencompass.org.cn
year: 2024
domain: [medical, clinical-QA, chinese-medical]
genre: online-leaderboard

authority:
  maintainers: [OpenCompass / Shanghai AI Laboratory, China national medical-AI pilot base]
  institution_count: 500
  update_cadence: irregular        # versioned releases; v1 (2023) → v4 (Nov 2025)
  online: true

popularity:
  trending: false
  as_of: "2026-06-16"
  social:
    - { platform: x, handle: "@ELYZA_inc", url: "https://x.com/ELYZA_inc/status/1867388977130746286", note: "日文讲解(2024 年 12 月)——区域(日本)关注", as_of: "2026-06-16" }
    - { platform: x, handle: "@Marktechpost", url: "https://x.com/Marktechpost/status/2054313064397447281", note: "通常作为 SECONDARY 指标,在模型宣传里排在 HealthBench 之后被提及", as_of: "2026-06-16" }
    - { platform: x, handle: "@ModelScope2022", url: "https://x.com/ModelScope2022/status/2054200239959982090", note: "中文生态(ModelScope)", as_of: "2026-06-16" }
    - { platform: reddit, url: "https://www.reddit.com/search/?q=MedBench", note: "几乎没有讨论;最接近的 Reddit 命中是无关的 Stanford MedAgentBench", as_of: "2026-06-16" }

methodology:
  evaluation: [automated, llm-judge]
  contamination_controls: "题目与标准答案物理隔离;动态评测以防走捷径学习/背答案。"
  notes: "v4 的开放式回答由一个对齐人类评分的 LLM-as-judge 打分;题目经多轮临床医生审核策展。"

models_ranked:
  - { model: Claude Sonnet 4.5, rank: 1, axis: base-LLM, license: closed, note: "62.5/100 (base-LLM mean 54.1)" }
  - { model: GPT-5, rank: 1, axis: multimodal, license: closed, note: "54.9/100 (multimodal mean 47.5)" }
  - { model: Claude Sonnet 4.5 (agent), rank: 1, axis: agent, license: closed, note: "85.3/100 overall, 88.9/100 safety" }

citations:
  - { title: "MedBench v4: A Robust and Scalable Benchmark for Evaluating Chinese Medical Language Models, Multimodal Models, and Intelligent Agents", url: "https://arxiv.org/abs/2511.14439", accessed: "2026-06-16" }
  - { title: "MedBench: A Comprehensive, Standardized, and Reliable Benchmarking System for Evaluating Chinese Medical Large Language Models", url: "https://arxiv.org/abs/2407.10990", accessed: "2026-06-16" }

as_of: "2026-06-16"
freshness:
  status: fresh
  last_checked: "2026-06-16"
  note: "v4 于 2025 年 11 月发布;在线 leaderboard 随新模型提交而更新。"

agent_summary:
  author: agent
  generated: "2026-06-16"

expert_verdict:
  signed_by: chenhao
  signed_date: "2026-06-16"
  confidence: high          # low / medium / high

moa:
  capability_axes: [clinical-reasoning, medical-knowledge, multimodal-medical, agentic-medical, safety-ethics]
  modalities: [text, image]
  access: [api, open-weights]
  recommended_for:
    - "跨 LLM、多模态模型与 agent 的中文临床能力对比"
    - "在把模型路由到面向患者环节前,先发现 safety/ethics 短板"
  caveats:
    - "围绕中国临床指南与监管优先级构建——未必迁移到其他地区"
    - "榜首是闭源 API 模型;base LLM 的 safety/ethics 普遍偏低(~18.4/100)"
    - "开放式评分用 LLM-as-judge,带有评判偏差"

tags: [medical, chinese, multimodal, agents, leaderboard]
---

## Agent summary

MedBench 是给中文医疗 AI 出的一套标准考卷(benchmark,即基准测试),放在网上、由系统自动评分,托管在 OpenCompass 平台(`medbench.opencompass.org.cn`)。最初的 2024 版攒出了它自称当时最大的医疗题库:300,901 道题,覆盖 43 个临床专科。它跑在全自动的云端系统上,把题目和标准答案分开存放(物理隔离),还采用会变的"动态评测",防止模型靠提前背过的答案虚高(也就是走捷径学习)。

到了 MedBench v4(arXiv 2511.14439,2025 年 11 月),题库扩到超过 700,000 个由专家挑选的任务,覆盖 24 个一级、91 个二级专科,由 500 多家机构的临床医生审核,一共测了 15 个前沿模型,分成三类:普通语言模型、能同时看图读文的多模态模型(multimodal),以及能自己分步骤、调用工具干活的智能体(agent)。其中开放式的回答,由另一个 AI 来当"阅卷老师"打分(LLM-as-judge),它的打分已经过校准、向人类评分看齐。报告里的领先者是这样的:在没做专门改造的通用大模型(base-LLM)这一档,Claude Sonnet 4.5 居首,得 62.5/100(这一档的平均分是 54.1);在多模态这一档,GPT-5 居首,得 54.9/100(平均 47.5);在智能体这一档,一个基于 Claude Sonnet 4.5 搭的 agent 居首,总分 85.3/100,其中回答的安全与合规(safety)拿了 88.9。有一个值得注意的现象:就算临床知识答得很好,通用大模型(base-LLM)在回答的安全性与伦理合规(safety 与 ethics)上仍然很弱,大约只有 18.4/100。

社交热度(这里说的是网上的讨论声量 sentiment,不等于权威性 authority):MedBench 在社交平台确实有人提,但偏区域性,在中文和日文圈子里更热(比如 @ModelScope2022,以及一条 @ELYZA_inc 的日文讲解),而且在各家发布模型的宣传里,它通常只是个次要指标,排在 HealthBench 后面,不当头条。Reddit 上几乎没人讨论它(搜到最接近的也只是一个不相干的 Stanford MedAgentBench)。在 LinkedIn 上,中国厂商把它当成可信度的背书,例如科大讯飞(iFlytek)的星火医疗大模型 V3.5,就把"MedBench Agent Evaluation 榜首"写进了它的第三方验证里。这些都说明 MedBench 更像是中国本地的一个权威信号。X 的原始链接见 `popularity.social`(2026-06-16 采集;LinkedIn 帖子的 URL 没法干净抓取)。

<!-- 仅事实;数字来源为两篇所引 arXiv 摘要 + 登录浏览 X/Reddit。不含观点。 -->

## Expert verdict

人工署名(chenhao)。值得回答:
MedBench 的信号对 MoA 选型是决策级, 还是只是知识代理? 62.5/100 的天花板说明了什么? 我认为是决策级，因为就要当下最好的、最合适的。
~18.4/100 的 safety/ethics 下限,应该多大程度上改变你的设计? 我会让高safe的模型在后面再审核一次
中国指南的框架, 对你的用例是帮助还是妨碍? 我认为是帮助。
