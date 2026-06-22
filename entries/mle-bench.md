---
id: mle-bench
name: MLE-bench
aliases: [MLE bench, OpenAI MLE-bench]
homepage: https://openai.com/index/mle-bench/
year: 2024
domain: [general, machine-learning, ml-engineering, agentic]
genre: paper-bound

authority:
  maintainers: [OpenAI(Jun Shern Chan, Neil Chowdhury 等）]
  institution_count: 0
  update_cadence: irregular      # 论文基准 + 开源 harness,非持续更新的在线榜
  online: false

popularity:
  trending: true
  as_of: "2026-06-17"

methodology:
  evaluation: [automated]
  contamination_controls: "题源是历史 Kaggle 赛,网上已有大量公开方案 → 泄漏风险明确;评测需防 agent 抄现成解。打分锚定 Kaggle 真实人类排行榜的奖牌线,而非主观判定。"
  notes: "agentic 基准:把 75 个 Kaggle ML 工程竞赛打包,让 agent 端到端完成——预处理数据、训练模型、跑实验、产出提交,再用各赛**真实的人类 Kaggle 排行榜奖牌线**（铜/银/金）评级。最佳配置 o1-preview + AIDE 脚手架仅在 **16.9%** 的赛中达到至少铜牌。ICLR 2025,代码开源（openai/mle-bench)。"

models_ranked:
  - { model: o1-preview + AIDE（脚手架）, rank: 1, axis: ml-engineering, license: closed, note: "16.9% 的竞赛达到≥铜牌;距 Kaggle 人类高手仍远" }

citations:
  - { title: "MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering(OpenAI)", url: "https://openai.com/index/mle-bench/", accessed: "2026-06-17" }
  - { title: "MLE-bench(arXiv 2410.07095,ICLR 2025 oral)", url: "https://arxiv.org/abs/2410.07095", accessed: "2026-06-17" }
  - { title: "openai/mle-bench — 代码与数据（GitHub)", url: "https://github.com/openai/mle-bench", accessed: "2026-06-17" }

as_of: "2026-06-17"
freshness:
  status: fresh
  last_checked: "2026-06-17"
  note: "ML-engineering agent 的事实标准基准;题集固定（非滚动）,但仍是该轴的主要参照。"

agent_summary:
  author: agent
  generated: "2026-06-17"

expert_verdict:
  signed_by: chenhao
  signed_date: "2026-06-17"
  confidence: low          # low / medium / high

moa:
  capability_axes: [ml-engineering, model-training, data-preparation, experimentation, agentic]
  modalities: [text]
  access: [api, open-weights]
  recommended_for:
    - "评估‘把模型/agent 当 ML 工程师用’的可行性——端到端训模型/跑实验,而非只改代码（补 [swe-bench] 之上的上游能力）"
    - "用真实 Kaggle 奖牌线做参照,横比 agent 的 ML 工程水平"
  caveats:
    - "题源是公开 Kaggle 赛 → 方案泄漏/抄解风险;高分需排除记忆成分"
    - "成绩高度依赖**脚手架**(AIDE 等）,不只是底座模型——分数是‘模型×scaffold’的合成"
    - "16.9% 铜牌≈仍远未达人类高手;别据此高估 agent 的自动 ML 能力"

tags: [machine-learning, ml-engineering, agentic, kaggle]
---

## Agent summary

MLE-bench 由 OpenAI 出品（收录于 ICLR 2025 oral）,是给“AI 智能体（agent,能自己分步骤、调用工具干活的 AI）做机器学习工程”打分的一份标准考卷,目前业内基本都拿它当参照。机器学习工程（ML engineering）说白了就是自己写代码训练模型。这套考卷把 75 个 Kaggle（知名数据科学竞赛平台）上的竞赛打包成一道道完整任务:智能体得从头到尾自己来,先处理数据,再训练模型、跑实验,最后交出参赛结果。评级方式很关键:它直接套用每场竞赛里真实的人类排行榜奖牌线（铜、银、金,medal 即 Kaggle 竞赛里的奖牌名次）,也就是说,成绩好不好是跟真人高手比出来的,不是靠人主观打分。

结论说得很实在:就算用目前表现最好的组合（o1-preview 模型,加上一个叫 AIDE 的“脚手架”——也就是帮模型把活儿安排好流程的外挂工具）,也只在 16.9% 的竞赛里拿到了铜牌以上,离 Kaggle 的人类高手还差得远。有两点要留意。第一,题目都来自公开的 Kaggle 竞赛,网上早有大量现成解法,所以存在明确的数据污染风险（模型可能提前见过题、靠背答案虚高）,看到高分得先排除掉这种“背出来”的成分。第二,成绩很大程度上靠脚手架撑着,分数其实是“模型本身 × 脚手架”两者合在一起的结果,不能全算到模型头上。它考的能力比 [swe-bench]（那个主要看改代码）更上游一层:能不能从头到尾自动做完一整套机器学习。

<!-- 仅事实;来源:OpenAI 官方页、arXiv 2410.07095、openai/mle-bench 仓库。 -->

## Expert verdict
人工署名(chenhao)。值得回答:
1) 分数是"模型×脚手架"的合成——给 MoA 选 ML 工程冠军时,你怎么把脚手架红利和底座能力分开? 信号/特征工程时，我还是信任它的。
2) 16.9% 铜牌:你把它读成"agent 还不能自动做 ML"的证据,还是"在窄任务上已可用"的下限? 我认为是"在窄任务上已可用"的下限
3) Kaggle 方案公开 → 污染;你信 MLE-bench 分到什么程度,要不要配一道私域、无公开解的 ML 任务复核? 不用
