---
id: eq-bench
name: EQ-Bench
aliases: [EQ-Bench 3, EQBench]
homepage: https://eqbench.com/
year: 2023
domain: [general, emotional-intelligence]
genre: online-leaderboard

authority:
  maintainers: [Samuel J. Paech （独立研究者）]
  institution_count: 0
  update_cadence: live           # eqbench.com 常更新,新模型持续加入
  online: true

popularity:
  hf_space: https://huggingface.co/spaces/sam-paech/EQ-Bench-Leaderboard
  trending: false
  as_of: "2026-06-17"

methodology:
  evaluation: [llm-judge, elo]
  contamination_controls: "原始 60 题为固定集（易污染）;EQ-Bench 3 改用多轮角色扮演 + 文稿分析,由 LLM 评判,降低死记风险。"
  notes: "原始版（2023）让模型预测对话中角色情绪状态的强度（约 60 道英文题,与 MMLU 相关 r≈0.97)。EQ-Bench 3 = 多轮角色扮演 + 文稿分析,由 LLM judge 评分（默认 Claude——先 Sonnet 3.7、headline 跑用 Opus 4.6;任意 OpenAI-兼容端点可替换）,按 Elo 排名（归一化 o3=1500、llama-3.2-1b=200)。eqbench.com 同站还有创意写作、长篇创意写作、judge 校准（Judgemark）等姊妹榜。"

citations:
  - { title: "EQ-Bench: An Emotional Intelligence Benchmark for Large Language Models (Paech, 2023)", url: "https://arxiv.org/abs/2312.06281", accessed: "2026-06-17" }
  - { title: "EQ-Bench Leaderboard (eqbench.com)", url: "https://eqbench.com/", accessed: "2026-06-17" }
  - { title: "EQ-Bench 3 — code (EQ-bench/eqbench3)", url: "https://github.com/EQ-bench/eqbench3", accessed: "2026-06-17" }

as_of: "2026-06-17"
freshness:
  status: fresh
  last_checked: "2026-06-17"
  note: "live leaderboard;EQ-Bench 3 当前主榜,LLM-judge + Elo,持续加入新模型。"

agent_summary:
  author: agent
  generated: "2026-06-17"

expert_verdict:
  signed_by: chenhao
  signed_date: "2026-06-17"
  confidence: medium          # low / medium / high

moa:
  capability_axes: [emotional-intelligence, empathy-social-reasoning, roleplay]
  modalities: [text]
  access: [api, open-weights]
  recommended_for:
    - "为对共情/情感/角色扮演要求高的对话场景挑模型"
    - "一个常更新、多模型在线的情商榜（原始 brief 点名的例子）"
  caveats:
    - "EQ-Bench 3 用 LLM-judge（默认 Claude)——评判可能带模型家族自偏好,给 Claude 系打分时尤需注意"
    - "原始版与 MMLU 相关 r≈0.97,可能更多在测通用智能而非纯情商"
    - "由独立研究者维护,无机构背书——权威靠透明方法与高引用,而非机构"
---

## Agent summary

EQ-Bench 是一份专门测 AI 情商（EQ）的基准测试,也就是给 AI 出的一套标准考卷（benchmark）,看它在理解人的情绪上表现如何。它由独立研究者 Samuel J. Paech 提出（arXiv 2312.06281,2023 年 12 月）,也是本项目最初的任务说明里点名的例子:一个常更新、引用率高、多个模型同台在线比拼的情商榜。

最早的版本让模型读一段对话,然后预测里面角色的情绪有多强烈（约 60 道英文题）,结果稳定、容易复现。有意思的是,它的分数跟另一份通用知识考卷 MMLU 的分数几乎同涨同跌（相关系数 r≈0.97,意思是两个分数高度同步,很可能在测同一种能力）,这说明它测到的很大程度上是 AI 的总体聪明程度,而不只是情商。

现在的主榜是 EQ-Bench 3（挂在 eqbench.com 上）,改成了两种新题:多轮角色扮演（roleplay,让模型扮演角色对话）和文稿分析。打分的不是人,而是另一个 AI 充当“阅卷老师”（LLM judge,即 LLM 评判）,按一份评分标准给分。默认用的阅卷 AI 是 Claude（先用 Sonnet 3.7,正式跑榜的成绩用 Opus 4.6,也可以换成任意 OpenAI 兼容的接口）。最后用 Elo 来排名,Elo 是借用棋类等级分的算法,按两两对战的胜负折算出分数（归一化后 o3=1500、llama-3.2-1b=200）。同一个网站上还挂着创意写作、长篇创意写作、阅卷 AI 校准（Judgemark）等几个姊妹榜。

它的价值在于补上了一个少见、又一直更新的维度:情感和社交能力,而大多数榜单只看答得对不对。但用它时要留意两点。第一,负责打分的是 AI（默认是 Claude）,可能存在模型家族自偏好,也就是评判 AI 倾向给自家同门的模型打高分。第二,它跟 MMLU 高度相关,意味着高分可能更多反映的是 AI 的通用能力,而不是单纯的情商。

<!-- 仅事实;来源为所引 arXiv 论文、eqbench.com 与 EQ-bench/eqbench3 仓库。 -->

## Expert verdict

人工署名(chenhao)。值得回答:
情商/共情是否值得在 MoA 里作为一个独立选型维度, 还是被通用对话质量涵盖(r≈0.97 与 MMLU)? 若场景分前台、后台，则可以成为独立选型。
默认 Claude 当 judge 的自偏好风险, 会不会让你在给 Claude 系模型选型时打折看待它的排名? 不会，只要该榜单有名、更新率高、模型全、自动评判者与专家一致性好。
独立研究者维护 (无机构背书) 对"可信度"是加分还是减分? 
