---
id: eq-bench
name: EQ-Bench
aliases: [EQ-Bench 3, EQBench]
homepage: https://eqbench.com/
year: 2023
domain: [general, emotional-intelligence]
genre: online-leaderboard

authority:
  maintainers: [Samuel J. Paech (独立研究者)]
  institution_count: 0
  update_cadence: live           # eqbench.com 常更新,新模型持续加入
  online: true

popularity:
  hf_space: https://huggingface.co/spaces/sam-paech/EQ-Bench-Leaderboard
  trending: false
  as_of: "2026-06-17"

methodology:
  evaluation: [llm-judge, elo]
  contamination_controls: "原始 60 题为固定集(易污染);EQ-Bench 3 改用多轮角色扮演 + 文稿分析,由 LLM 评判,降低死记风险。"
  notes: "原始版(2023)让模型预测对话中角色情绪状态的强度(约 60 道英文题,与 MMLU 相关 r≈0.97)。EQ-Bench 3 = 多轮角色扮演 + 文稿分析,由 LLM judge 评分(默认 Claude——先 Sonnet 3.7、headline 跑用 Opus 4.6;任意 OpenAI-兼容端点可替换),按 Elo 排名(归一化 o3=1500、llama-3.2-1b=200)。eqbench.com 同站还有创意写作、长篇创意写作、judge 校准(Judgemark)等姊妹榜。"

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
    - "一个常更新、多模型在线的情商榜(原始 brief 点名的例子)"
  caveats:
    - "EQ-Bench 3 用 LLM-judge(默认 Claude)——评判可能带模型家族自偏好,给 Claude 系打分时尤需注意"
    - "原始版与 MMLU 相关 r≈0.97,可能更多在测通用智能而非纯情商"
    - "由独立研究者维护,无机构背书——权威靠透明方法与高引用,而非机构"
---

## Agent summary

EQ-Bench 是独立研究者 **Samuel J. Paech** 提出的**情商(EQ)基准**(arXiv 2312.06281,2023 年 12
月),也是原始项目 brief 点名的"常更新、引用率高、多模型在线的情商榜"。**原始版**让模型预测对话中
角色情绪状态的*强度*(约 60 道英文题),高度可复现;有意思的是它与 MMLU 的相关系数高达 **r≈0.97**,
提示它捕捉的很大程度是广义智能。**EQ-Bench 3**(当前主榜,托管在 `eqbench.com`)改为**多轮角色扮演
+ 文稿分析**,由一个 **LLM judge** 按评分量规打分(默认 Claude——先 Sonnet 3.7、headline 跑用
Opus 4.6,也可换任意 OpenAI-兼容端点),并以 **Elo** 排名(归一化:o3=1500、llama-3.2-1b=200)。
同站还挂着创意写作、长篇创意写作、judge 校准(Judgemark)等姊妹榜。

它的价值是一个**少见且持续更新的情感/社交维度**,补充以正确性为主的榜。要警惕两点:一是 LLM-judge
(默认 Claude)存在**模型家族自偏好**风险;二是与 MMLU 的高相关意味着高分可能更多反映通用能力而非
"纯情商"。

<!-- 仅事实;来源为所引 arXiv 论文、eqbench.com 与 EQ-bench/eqbench3 仓库。 -->

## Expert verdict

人工署名(chenhao)。值得回答:
情商/共情是否值得在 MoA 里作为一个独立选型维度, 还是被通用对话质量涵盖(r≈0.97 与 MMLU)? 若场景分前台、后台，则可以成为独立选型。
默认 Claude 当 judge 的自偏好风险, 会不会让你在给 Claude 系模型选型时打折看待它的排名? 不会，只要该榜单有名、更新率高、模型全、自动评判者与专家一致性好。
独立研究者维护 (无机构背书) 对"可信度"是加分还是减分? 
