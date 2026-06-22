---
id: lmarena
name: LMArena (Chatbot Arena)
aliases: [Chatbot Arena, LMSYS Chatbot Arena]
homepage: https://lmarena.ai
year: 2023
domain: [general, chatbot, human-preference]
genre: online-leaderboard

authority:
  maintainers: [LMArena (formerly LMSYS), UC Berkeley SkyLab — Wei-Lin Chiang et al.]
  institution_count: 0
  update_cadence: live           # refreshed frequently, often daily
  online: true

popularity:
  hf_space: https://huggingface.co/spaces/lmarena-ai/arena-leaderboard
  trending: false
  as_of: "2026-06-16"

methodology:
  evaluation: [human, pairwise, elo]
  contamination_controls: "实时、众包的新鲜 prompt + 人类投票——抗静态 benchmark 污染（但易受刷票与 prompt 分布偏差影响）。"
  notes: "匿名并排对战:用户把一条 prompt 同时发给两个隐藏模型并投票更好的回答;投票后揭示身份。用 Bradley-Terry 模型把成对投票转成带置信区间的 Elo 式评分。奠基论文（arXiv 2403.04132,2024 年 3 月）分析了 24 万票;实时榜此后累计了数百万票,并增加了分类和风格控制的子榜（以及视觉/多模态 arena)。"

citations:
  - { title: "Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference (Chiang et al., 2024)", url: "https://arxiv.org/abs/2403.04132", accessed: "2026-06-16" }
  - { title: "LMArena (live leaderboard)", url: "https://lmarena.ai", accessed: "2026-06-16" }
  - { title: "lmarena-ai — human-preference datasets & Space (HuggingFace)", url: "https://huggingface.co/lmarena-ai", accessed: "2026-06-16" }

as_of: "2026-06-16"
freshness:
  status: fresh
  last_checked: "2026-06-16"
  note: "实时 leaderboard ~每日更新;任何具体排名都是快照。票数持续增长。"

agent_summary:
  author: agent
  generated: "2026-06-16"

expert_verdict:
  signed_by: chenhao
  signed_date: "2026-06-16"
  confidence: medium          # low / medium / high

moa:
  capability_axes: [general-chat-quality, instruction-following, human-preference]
  modalities: [text, image]
  access: [api, open-weights]
  recommended_for:
    - "用真实人类偏好（而非静态测试）衡量通用对话质量"
    - "来自新鲜众包 prompt 的抗饱和/抗污染信号"
  caveats:
    - "衡量的是人类 PREFERENCE——奖励风格、排版与长度,未必是正确性或安全"
    - "易受刷票与 prompt 分布偏差影响;通用,不针对具体领域"
    - "Elo 每日变动——任何引用的排名都是某一时点的快照,不是稳定事实"
---

## Agent summary

LMArena（原名 LMSYS Chatbot Arena,由 UC Berkeley SkyLab 团队 Chiang 等人发起）是目前关注度最高的
通用大模型排行榜,比的是“哪个 AI 的回答更讨人喜欢”（human preference,人类偏好）。它也是本集合里第一个
跟医疗无关的参照标杆。玩法很简单:真实用户输入一个问题（prompt）,系统把它同时发给两个隐藏身份的模型,
用户投票觉得哪个回答更好,投完票才揭晓刚才是哪两个模型。然后用一个统计模型（Bradley-Terry,由两两胜负
反推各模型实力分）把这些两两投票换算成一个带误差范围的分数,形式上类似棋类等级分（Elo,按两两对战胜负
算出的分）。这个榜 2023 年上线;奠基论文（arXiv 2403.04132,2024 年 3 月）分析了 24 万票,实时榜此后
累计了数百万票,大约每天更新一次,还分出了按题型分类、控制行文风格的子榜,以及看图读文的多模态（multimodal,
能同时处理图和文字）arena。

它最大的优点是不容易作弊取巧:题目是网友现场产生、由真人当场评判的新鲜内容,这是固定题库的基准测试
（benchmark,给 AI 出的标准考卷）做不到的——固定题库容易被模型提前见过、靠背答案虚高（数据污染,
contamination）。但它有个根子上的局限:它量的是“讨喜程度”,不是“对不对”。语气、排版、回答长度都会
影响投票,刷票和提问分布的偏差也会干扰结果,而且它是通用榜,几乎不涉及临床这类领域的安全把关。所以在
组队用模型（MoA,把多个模型组队、各管一块）的选型里,它适合当一个宽泛参考——看“人类愿不愿意跟它聊天”,
而不能当成判断对错或安全的门槛。

<!-- 仅事实;来源为所引 arXiv 论文与 LMArena/HF 页面。 -->

## Expert verdict

人工署名(chenhao)。值得回答: 偏好-Elo 在 MoA 选型里该占多少权重 vs 任务-准确率榜? 我认为，情感居多的场景Elo高，其他场景准确率好些。 
每日变动的排名不能作为证据? 我认为，每周/每月均值比较好。
