---
id: medqa
name: MedQA (USMLE)
aliases: [MedQA-USMLE]
homepage: https://github.com/jind11/MedQA
year: 2020
domain: [medical, medical-QA, multilingual]
genre: dataset

authority:
  maintainers: [Di Jin / Eileen Pan et al. (MIT, Szolovits group)]
  institution_count: 0
  update_cadence: frozen         # static dataset
  online: false                  # a dataset, not a leaderboard — no official ranking of its own

methodology:
  evaluation: [automated]
  contamination_controls: "无——自 2020 年起公开,且在预训练语料中无处不在,记忆/污染风险高;前沿模型分数已贴近天花板。"
  notes: "首个取自专业医师执照考试的自由式多项选择 OpenQA 数据集(4 或 5 个选项)。英文约 12,723 题(常用切分 10,178 训练 / 1,273 测试);简体中文 34,251;繁体中文 14,123。前 LLM 时代最佳方法在英文仅约 36.7%。它是众多医疗榜的构件——例如 Open Medical-LLM Leaderboard,RCQ 研究里也用了 500 道 MedQA 题。"

citations:
  - { title: "What Disease does this Patient Have? A Large-scale Open Domain Question Answering Dataset from Medical Exams (Jin et al., 2020)", url: "https://arxiv.org/abs/2009.13081", accessed: "2026-06-16" }
  - { title: "MedQA — code and data (jind11/MedQA)", url: "https://github.com/jind11/MedQA", accessed: "2026-06-16" }

as_of: "2026-06-16"
freshness:
  status: stale
  last_checked: "2026-06-16"
  note: "已饱和、且几乎肯定在训练数据里;前沿模型贴近天花板,故区分力很弱——但仍是别人据以构建的标准参考数据集。"

agent_summary:
  author: agent
  generated: "2026-06-16"

expert_verdict:
  signed_by: chenhao
  signed_date: "2026-06-16"
  confidence: low          # low / medium / high
  one_liner: "太旧、很多模型在此过拟合"

moa:
  capability_axes: [medical-knowledge-QA, multilingual-medical]
  modalities: [text]
  access: [api, open-weights]
  recommended_for:
    - "理解 QA 背诵榜到底由什么构成——MedQA 是它们共同的底料"
    - "一个多语种(EN / zh-Hans / zh-Hant)的医疗知识下限"
  caveats:
    - "它是 DATASET,不是 leaderboard——没有官方排名;任何分数都取决于谁、怎么跑的"
    - "已饱和 + 很可能被记忆 → 贴近天花板,难以区分顶部模型"
    - "选择题背诵 ≠ 临床行为、安全或沟通"
---

## Agent summary

MedQA 是一份给 AI 出的医学题库(Jin et al., 2020;MIT / Szolovits 组),很多医疗类基准测试(benchmark,给 AI 出的标准考卷)都拿它当原料。要分清楚:它本身只是一套题目(数据集),不是排行榜,所以它自己不给模型排名。题目取自专业的医师执照考试,也就是美国执业医师资格考试(USMLE)那种风格,每道都是选择题(MCQ),4 个或 5 个选项,在当时它是第一个这么做的开放域问答数据集。它有三种语言版本:英文约 12,723 题(常见的划分是 10,178 题用于训练、1,273 题用于测试)、简体中文 34,251 题、繁体中文 14,123 题。刚发布那会儿,用传统的"先检索资料再读题作答"方法,英文准确率只有约 36.7%。后来的前沿大模型已经把成绩追到接近满分。

正因为它公开得早、用得多、年头久,MedQA 有两个老毛病。一是数据污染(模型在训练时可能提前见过这些题,靠背答案虚高);二是分数饱和,顶尖模型几乎都做满了。所以它还能当一条医学知识的"及格线",也能当别人搭榜单时的共同配料,比如 Open Medical-LLM Leaderboard,它的 500 道题还被用在 RCQ 研究的一个环节里。但它已经很难区分最顶尖的几个模型,对模型在真实临床里怎么表现、安不安全,它什么也说不了。

<!-- 仅事实;来源为所引 arXiv 论文与 jind11/MedQA 仓库。 -->

## Expert verdict

人工署名(chenhao)。值得回答:一个已饱和、很可能被记忆的数据集,还该不该锚定一个医疗 leaderboard? 我认为不应该；但若在此榜单分数都太低，就要被直接排除。
MedQA 现在是不是最好当作负向过滤 (不过它的模型直接淘汰) 而非排名? 我认为是的。
