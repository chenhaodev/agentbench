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
  contamination_controls: "实时、众包的新鲜 prompt + 人类投票——抗静态 benchmark 污染(但易受刷票与 prompt 分布偏差影响)。"
  notes: "匿名并排对战:用户把一条 prompt 同时发给两个隐藏模型并投票更好的回答;投票后揭示身份。用 Bradley-Terry 模型把成对投票转成带置信区间的 Elo 式评分。奠基论文(arXiv 2403.04132,2024 年 3 月)分析了 24 万票;实时榜此后累计了数百万票,并增加了分类和风格控制的子榜(以及视觉/多模态 arena)。"

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
    - "用真实人类偏好(而非静态测试)衡量通用对话质量"
    - "来自新鲜众包 prompt 的抗饱和/抗污染信号"
  caveats:
    - "衡量的是人类 PREFERENCE——奖励风格、排版与长度,未必是正确性或安全"
    - "易受刷票与 prompt 分布偏差影响;通用,不针对具体领域"
    - "Elo 每日变动——任何引用的排名都是某一时点的快照,不是稳定事实"
---

## Agent summary

LMArena(原 LMSYS Chatbot Arena;UC Berkeley SkyLab,Chiang et al.)是关注度最高的通用 LLM
**人类偏好** leaderboard——也是本集合的第一个**非医疗**锚点。真实用户把一条 prompt 发给两个**匿名**
模型,投票哪个回答更好,投票后揭示身份;一个 **Bradley-Terry** 模型把这些成对投票转成带置信区间的
**Elo 式评分**。2023 年上线;奠基论文(arXiv 2403.04132,2024 年 3 月)分析了 **24 万票**,实时榜
此后累计了**数百万票**,约每日更新,并带有分类和风格控制的子榜以及视觉/多模态 arena。

它的强项是**抗污染**:新鲜、众包、由人类评判的 prompt,这是静态 benchmark 无法复制的。它的结构性弱点
是衡量**偏好,而非正确性**——它奖励语气、排版和长度,易受刷票与 prompt 分布偏差影响,且是通用的
(因此对临床等领域安全说明很少)。适合作为 MoA 中"人类是否爱跟它说话"的宽泛维度,而不是正确性或
安全门槛。

<!-- 仅事实;来源为所引 arXiv 论文与 LMArena/HF 页面。 -->

## Expert verdict

人工署名(chenhao)。值得回答: 偏好-Elo 在 MoA 选型里该占多少权重 vs 任务-准确率榜? 我认为，情感居多的场景Elo高，其他场景准确率好些。 
每日变动的排名不能作为证据? 我认为，每周/每月均值比较好。
