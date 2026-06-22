---
id: re-bench
name: RE-Bench
aliases: [RE Bench, Research Engineering Benchmark, METR RE-Bench]
homepage: https://metr.org/blog/2024-11-22-evaluating-r-d-capabilities-of-llms/
year: 2024
domain: [general, ai-research, ml-research-engineering, agentic]
genre: paper-bound

authority:
  maintainers: [METR(Hjalmar Wijk 等）]
  institution_count: 0
  update_cadence: irregular
  online: false

methodology:
  evaluation: [automated, human]
  contamination_controls: "7 个为评测新设计的开放式研究工程环境（如拟合 scaling law、优化 GPU kernel),非现成题库,泄漏风险低;关键是用 **61 位人类专家、71 次 8 小时尝试**做对照基线。"
  notes: "衡量前沿 **AI 研发（R&D)** 能力:7 个开放式 ML 研究工程环境,直接与人类专家对打。结论很有信息量——**2 小时预算**下最佳 AI 得分约为人类 **4 倍**(AI 生成/试解快 10 倍、成本低得多）;但**8 小时**人类略反超,**32 小时**人类约为 AI 的 **2 倍**。即:AI 在短时迭代上强,长时程深度研究仍输人类。ICML 2025。"

models_ranked:
  - { model: 前沿 agent（短预算）, rank: 1, axis: ml-research-engineering, license: closed, note: "2h 预算下 ≈4× 人类;但时间拉长（8h/32h）后被人类反超 → 长时程是短板" }

citations:
  - { title: "Evaluating frontier AI R&D capabilities of language model agents against human experts(METR 博客）", url: "https://metr.org/blog/2024-11-22-evaluating-r-d-capabilities-of-llms/", accessed: "2026-06-17" }
  - { title: "RE-Bench(arXiv 2411.15114)", url: "https://arxiv.org/abs/2411.15114", accessed: "2026-06-17" }
  - { title: "RE-Bench(ICML 2025,PMLR v267 wijk25a)", url: "https://proceedings.mlr.press/v267/wijk25a.html", accessed: "2026-06-17" }

as_of: "2026-06-17"
freshness:
  status: fresh
  last_checked: "2026-06-17"
  note: "AI R&D 自动化能力的标杆评测;题集固定但带稀缺的人类专家对照,适合读‘高分=多接近人类研究员’。"

agent_summary:
  author: agent
  generated: "2026-06-17"

moa:
  capability_axes: [ml-research-engineering, ai-r-and-d, agentic, long-horizon-reasoning]
  modalities: [text]
  access: [api, open-weights]
  recommended_for:
    - "判断 agent 离‘自动做 AI 研发/研究工程’还有多远——带真人专家对照,信号比纯刷分榜硬"
    - "区分**短时迭代**(AI 强）与**长时程深度研究**（人类仍强）两种很不同的能力诉求"
  caveats:
    - "只有 7 个环境,覆盖窄;测的是‘研究工程’（实现/优化）,不是完整的科研创意"
    - "结论强依赖**时间预算**——'AI 4× 人类‘只在 2h 成立,长时被反超,引用单一数字会误导"
    - "成绩同样含脚手架/采样预算因素,需与底座能力分开看"

tags: [ai-research, ml-research-engineering, agentic, human-baseline]
---

## Agent summary

RE-Bench 是 METR（一家专门评估 AI 能力的机构）出的一套考题,用来看最前沿的大模型（frontier model）能不能干机器学习研究工程（ML research engineering,就是自己设计实验、写代码调模型）。它出了 7 道开放式的研究工程题,比如拟合 scaling law（预测模型规模和效果之间的规律）、优化 GPU kernel（让显卡上的计算跑得更快）,让能自己分步骤、调用工具干活的 AI（agent）和人类专家做同样的题。它最值钱的一点是配了一份很难得的人类对照成绩（human baseline）:61 位人类专家,做了 71 次、每次 8 小时的尝试。

它的结论高度取决于给多少完成时限（time budget）,所以不能只看一个数字。给 2 小时,最好的 AI 拿到的分数大约是人类专家的 4 倍（AI 生成并测试方案比人类快 10 倍以上,花的钱也少得多）;但把时间放到 8 小时,人类就略微反超;放到 32 小时,人类大约是 AI 的 2 倍。换句话说:论短时间里快速试错、反复迭代,AI 已经很强了;可一旦是要花很久的深度研究,人类还是赢。

几点要留心。它只有 7 道题,覆盖面窄;考的是研究里的「工程」那一半（把想法实现出来、再优化）,不是从头想出科研创意。成绩里还掺了脚手架（给模型搭的外围程序）和采样预算的因素。所以「AI 是人类的 4 倍」这种说法,一旦不提是几小时的预算,就会严重误导人。它和 [mle-bench]（Kaggle 式的 ML 工程）同属「让 AI 做机器学习」这一类,但更偏向前沿研究那一头。

<!-- 仅事实;来源:METR 博客、arXiv 2411.15114、ICML 2025（PMLR v267）。 -->

## Expert verdict

<!-- 人工署名(chenhao)。值得回答:
     1) "2h 4× 人类 / 32h 人类 2× AI"——在你的信任标尺里,这种随时间反转的结论怎么用?你更看哪个预算下的数?
     2) 它带真人专家对照(很稀缺)——这会不会让你给它的权重高于没有人类基线的刷分榜?
     3) 只 7 个研究工程环境:对你关心的"agent 能否自动推进 AI 研发"这个判断,外推性够不够? -->
