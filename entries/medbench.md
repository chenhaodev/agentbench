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

MedBench 是面向**中文医疗 AI**的标准化、云端基准系统,托管在 OpenCompass
(`medbench.opencompass.org.cn`)。最初的 2024 版汇集了它所称的当时最大医疗评测数据集——
**300,901 道题、覆盖 43 个临床专科**——构建在全自动云端基础设施上,将题目与标准答案物理隔离,并用
*动态评测*抵抗走捷径学习与背答案。

**MedBench v4**(arXiv 2511.14439,2025 年 11 月)将其扩展到 **超过 700,000 个专家策展任务,
覆盖 24 个一级 / 91 个二级专科**,由 **500 多家机构**的临床医生审核,并评测三类模型——语言模型、
多模态系统与自主 agent(15 个前沿模型)。开放式回答由一个对齐人类评分的 LLM-as-judge 打分。报告
中的领先者:**Claude Sonnet 4.5** 在 base LLM 居首,**62.5/100**(类均值 54.1);**GPT-5** 在
多模态居首,**54.9/100**(均值 47.5);一个 **基于 Claude Sonnet 4.5 的 agent** 在 agent 赛道
居首,总分 **85.3/100**(safety 88.9)。一个醒目发现是:即便临床知识得分很高,base LLM 的
**safety 与 ethics 仍然薄弱**(~18.4/100)。

**社交热度(sentiment,不是 authority):** MedBench 的社交存在感真实但更**区域化**——在中文和
日文生态更强(如 @ModelScope2022、一则 @ELYZA_inc 讲解),且在模型发布宣传里通常作为*次要*指标、
排在 HealthBench 之后,而非头条。Reddit 上几乎没有讨论(最接近的命中是无关的 Stanford
MedAgentBench)。在 LinkedIn 上,中国厂商把它当作可信度背书——例如 iFlytek 的星火医疗大模型
V3.5 将"MedBench Agent Evaluation 榜首"列入其第三方验证——强化了 MedBench 作为**区域(中国)
权威信号**的定位。X permalink 见 `popularity.social`(2026-06-16 采集;LinkedIn 帖子 URL 无法
干净抓取)。

<!-- 仅事实;数字来源为两篇所引 arXiv 摘要 + 登录浏览 X/Reddit。不含观点。 -->

## Expert verdict

<!-- 人工署名(chenhao)。仅签字人可在此处书写,然后填写 expert_verdict frontmatter
     (signed_by / signed_date / confidence / one_liner)。guard_verdict hook 会阻止 agent
     在此写入。值得回答:
       - MedBench 的信号对 MoA 选型是决策级,还是只是知识代理?62.5/100 的天花板说明了什么?
       - ~18.4/100 的 safety/ethics 下限,应该多大程度上改变你的设计?
       - 中国指南的框架,对你的用例是帮助还是妨碍? -->
