---
id: rcq
name: RCQ (Real Clinical Queries)
aliases: [Real Clinical Queries benchmark]
homepage: https://www.nature.com/articles/s41591-026-04431-5
year: 2026
domain: [medical, clinical-deployment, real-world-queries]
genre: paper-bound

authority:
  maintainers: [NYU Langone Health, University of Texas at Austin]
  institution_count: 2          # small, single-study benchmark — not a multi-institution consortium
  update_cadence: frozen        # static; bound to one Nature Medicine paper
  online: false                 # introduced inside a paper, not a live submission leaderboard

popularity:
  trending: false
  as_of: "2026-06-16"           # 全新（论文 2026-06-12 发表）;经 LinkedIn 临床医生讨论发现

methodology:
  evaluation: [human, blind]
  contamination_controls: "查询是真实的医生-向-LLM 提问,采自真实临床环境——不是可复用的考试题,难以训练或刷分。"
  notes: "100 条真实临床查询,采自医生自己的 LLM 提问;12 位美国临床医生做随机、盲法评审,产生 1,800 条模型-问题标注。是该研究三个阶段之一（另两个为 500 道 MedQA + 500 道 HealthBench)。"

models_ranked:
  - { model: GPT-5.2, axis: real-clinical-queries, license: closed, note: "前沿梯队——胜过专用临床工具" }
  - { model: Gemini 3.1 Pro, axis: real-clinical-queries, license: closed, note: "前沿梯队" }
  - { model: Claude Opus 4.6, axis: real-clinical-queries, license: closed, note: "前沿梯队" }
  - { model: OpenEvidence, axis: real-clinical-queries, license: closed, note: "专用临床工具——在 RCQ 上与 Google Search AI Overview 相当" }
  - { model: UpToDate Expert AI, axis: real-clinical-queries, license: closed, note: "专用临床工具——较低梯队" }

citations:
  - { title: "General-purpose large language models outperform specialized clinical AI tools on medical benchmarks (Nature Medicine, 12 Jun 2026)", url: "https://www.nature.com/articles/s41591-026-04431-5", accessed: "2026-06-16" }
  - { title: "General-purpose AI beats out specialized clinical AI in some assessments (TechTarget coverage)", url: "https://www.techtarget.com/healthtechanalytics/news/366644497/General-purpose-AI-beats-out-specialized-clinical-AI-in-some-assessments", accessed: "2026-06-16" }

as_of: "2026-06-16"
freshness:
  status: fresh
  last_checked: "2026-06-16"
  note: "2026-06-12 发表。静态基准,冻结于一篇论文与一组早-2026 模型快照;随模型进步会过时。"

agent_summary:
  author: agent
  generated: "2026-06-16"

expert_verdict:
  signed_by: chenhao
  signed_date: "2026-06-16"
  confidence: high          # low / medium / high

moa:
  capability_axes: [real-clinical-query-handling, clinician-preference, deployment-realism]
  modalities: [text]
  access: [api]
  recommended_for:
    - "核查 benchmark/考试上的优势,是否迁移到处理真实医生查询"
    - "抗饱和证据:小、真实、人工评判——与 MCQ 背诵榜相反"
  caveats:
    - "只有 100 条查询——统计功效低;是研究结果,不是持续维护的 leaderboard"
    - "单一研究,尚未被独立复现"
    - "冻结于早-2026 模型;作者自己也指出结果已被超越"
---

## Agent summary

RCQ（Real Clinical Queries,意思是“真实临床查询”）是一份小而看重真实场景的 benchmark（给 AI 出的标准考卷）。它出自一篇 Nature Medicine 研究（编号 s41591-026-04431-5,2026 年 6 月 12 日发表）,作者来自 NYU Langone Health 和 University of Texas at Austin 这两家美国机构。它的题目是 100 条真实临床查询,也就是医生在日常看病时自己拿去问 AI（这里的 LLM 指大语言模型,就是 ChatGPT 那类会聊天答题的 AI）的问题。收集好之后,12 位美国临床医生在不知道答案出自哪个模型的情况下打分（也就是盲法评审）,一共产生了 1,800 条“模型答某道题”的评价记录。RCQ 只是这篇论文三个测试环节中的一个,另外两个是 500 道 MedQA 题和 500 道 HealthBench 题。

最主要的结论是:几款最强的通用模型（GPT-5.2、Gemini 3.1 Pro、Claude Opus 4.6）赢过了专门给临床场景做的 AI 工具。在 RCQ 上,OpenEvidence 和 UpToDate Expert AI 的表现只跟 Google Search AI Overview（谷歌搜索结果上方那段 AI 总结）差不多,而临床医生更喜欢通用模型给的答案。RCQ 的好处是贴近真实使用、不容易被刷分:题目是真问题,又由人盲评打分。它的短板也很明显:只有 100 道题,样本太少,结论说服力有限;而且只是一项还没被别人重复验证过的研究,用的还是 2026 年初那一批模型,等于停在了那个时间点的快照上。

<!-- 仅事实;来源为所引 Nature Medicine 文章与 TechTarget 报道。 -->

## Expert verdict

人工署名(chenhao)。值得回答:
像 RCQ 这样小、真实、人工评判的基准, 在 MoA 选型里是否该比一个已饱和的 70 万题大榜权重更高? 我认为是的。
"n=100、单一研究、冻结" 该打多少折? 我认为, 在权威机构背书且榜单分数未饱和前, 权重依然会很高。 
"临床工具 ≈ Google Search AI Overview" 对 "自建 vs 用前沿" 意味着什么? 我不清楚，可能意味着RAG/SKILL+强推理模型就是未来方向。
