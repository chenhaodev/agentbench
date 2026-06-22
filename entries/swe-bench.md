---
id: swe-bench
name: SWE-bench
aliases: [SWE-bench Verified, SWE-bench Lite, SWE-bench Multimodal, SWE-bench Multilingual]
homepage: https://www.swebench.com/
year: 2024
domain: [general, code, software-engineering, agentic]
genre: online-leaderboard

authority:
  maintainers: [Carlos Jimenez & John Yang et al. (Princeton NLP / Stanford); SWE-bench Verified 子集由 OpenAI 与原作者合作发布]
  institution_count: 0
  update_cadence: live           # 官方榜持续接收 agent/模型提交
  citation_count:
    value: 2000
    source: Google Scholar (约数,持续增长)
    as_of: "2026-06-17"
  online: true

popularity:
  trending: true
  as_of: "2026-06-17"

methodology:
  evaluation: [automated]
  contamination_controls: "原始 500/2294 任务的 GitHub issue 与 gold patch 早于发布即可能进入训练集;OpenAI 自身审计发现前沿模型能逐字复现部分 gold patch。社区以 SWE-bench Live(滚动新 issue)等变体对抗污染。"
  notes: "任务=给定真实 GitHub issue + 仓库快照,模型/agent 生成补丁(patch),用仓库自带测试套件判定是否真正修复(% resolved)。这是可执行、端到端的评测,不是 MCQ。原始集 2294 题、12 个 Python 仓库;Verified=人工校验过的 500 题干净子集;另有 Lite(300)、Multimodal、Multilingual 等变体。ICLR 2024 oral。"

models_ranked:
  - { model: 前沿模型(多家并列), rank: 1, axis: software-engineering, license: closed, note: "2026 年中 Verified 上 Claude Opus 4.x / Gemini 3.x Pro 等多家在 ~80% 统计并列——榜在前沿已趋饱和、区分度下降" }

citations:
  - { title: "SWE-bench: Can Language Models Resolve Real-World GitHub Issues? (Jimenez et al., ICLR 2024 oral)", url: "https://arxiv.org/abs/2310.06770", accessed: "2026-06-17" }
  - { title: "SWE-bench 官方榜与文档(原始 / Verified / Lite / Multimodal / Multilingual)", url: "https://www.swebench.com/", accessed: "2026-06-17" }
  - { title: "SWE-bench — 代码与数据(SWE-bench/SWE-bench, GitHub)", url: "https://github.com/swe-bench/SWE-bench", accessed: "2026-06-17" }
  - { title: "Introducing SWE-bench Verified(OpenAI 与原作者合作的 500 题人工校验子集)", url: "https://openai.com/index/introducing-swe-bench-verified/", accessed: "2026-06-17" }

as_of: "2026-06-17"
freshness:
  status: fresh
  last_checked: "2026-06-17"
  note: "live,持续收提交;但前沿分已聚到 ~80% 并列,作为'谁更强'的区分器在饱和,价值更多在'能不能真修代码'这条门槛。"

agent_summary:
  author: agent
  generated: "2026-06-17"

expert_verdict:
  signed_by: chenhao
  signed_date: "2026-06-22"
  confidence: medium          # low / medium / high

moa:
  capability_axes: [software-engineering, code-generation, agentic, tool-use, repo-level-reasoning]
  modalities: [text]
  access: [api, open-weights]
  recommended_for:
    - "为'修真实代码库 / 编码 agent'选模型——这是该能力事实上的标准榜,且端到端可执行(测试通过才算修好)"
    - "用 Verified 子集而非原始集做横比(原始集含噪声/不可解任务)"
    - "需要抗污染的当下能力快照时,优先看 SWE-bench Live 等滚动变体"
  caveats:
    - "数据污染明确存在:gold patch 早于发布即可能进训练集,高分可能含记忆成分"
    - "前沿已 ~80% 并列饱和,Verified 分很难再区分顶尖模型;真实工程能力差距未必反映在这一个数上"
    - "纯 Python、issue→patch 这一种工作流;不代表多语言、架构设计、调试等更广的工程能力"

tags: [code, agentic, swe, executable-eval]
---

## Agent summary

SWE-bench 是给 AI 出的一份"修代码"考卷(benchmark,基准测试),由 Princeton NLP 的 Jimenez、Yang 等人做出来,论文入选 ICLR 2024 oral。现在它基本被当成衡量 AI 能不能修真实代码的标准榜。这里的"修代码"对象,既可以是普通模型,也可以是 agent(能自己分步骤、调用工具干活的 AI,也叫智能体)。

考题本身很实在:先给 AI 一个真实的 GitHub issue(代码仓库里登记的待修 bug 或需求),再配上对应仓库当时的代码快照,要求 AI 生成一个 patch(提交的代码修改)。改完之后,用这个仓库自带的 unit test(自动跑的测试用例,用来判定改对没有)来跑一遍,只有测试通过,这道题才算 resolved(问题被解决)。换句话说,它是从头到尾真跑一遍、看结果的评测,不是做选择题。最早这套题有 2294 道,覆盖 12 个 Python 仓库。

后来又分出几个子集和变体。Verified 是 OpenAI 和原作者一起做的人工核验过的子集(SWE-bench Verified),从原始题里挑出 500 道干净题,把那些描述不清、根本没法做、测试时灵时不灵的题剔掉了,现在各家发布会报成绩基本都用它。Lite 是 300 道的轻量版,此外还有 Multimodal、Multilingual 等。配套的 agent 工具叫 SWE-agent,出自同一个团队。

挑模型时有两点要特别留意。第一,数据污染(模型提前见过考题、靠背答案虚高)是公开存在的问题:issue 和标准答案补丁(gold patch)在 SWE-bench 发布前就可能被模型在训练时见过,OpenAI 自己查过,发现前沿模型能一字不差地复现部分标准答案,所以高分里可能掺了"背出来"的成分。为对抗这一点,社区做了 SWE-bench Live 等变体,不断把新出现的 issue 加进来。第二,这份榜在顶尖模型这一段已经快考满了:到 2026 年中,Claude Opus 4.x、Gemini 3.x Pro 等多家前沿模型在 Verified 上的成绩都在 80% 左右、统计上分不出高下,所以它当"谁更强"的尺子越来越不好使了。不过当作一道"能不能真修代码"的及格门槛,它仍然有用。

<!-- 仅事实;来源:ICLR 论文 (arXiv 2310.06770)、官方站 swebench.com、GitHub 仓库、OpenAI 的 Verified 说明。具体并列分数为多家聚合榜口径,标 as_of 2026-06-17。 -->

## Expert verdict

Verified 已多家并列 ~80% 饱和,叠加已知 gold-patch 污染,原始/Verified 分对我已基本没有区分力。在 MoA 里选编码冠军模型不再据它定主信号——改看 SWE-bench Live 这类滚动、抗污染的榜才算数;原始分只当历史参照与及格门槛。
