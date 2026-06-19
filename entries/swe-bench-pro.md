---
id: swe-bench-pro
name: SWE-Bench Pro
aliases: [SWE-Bench Pro Public, SWE-Bench Pro Private, SWEAP]
homepage: https://labs.scale.com/leaderboard/swe_bench_pro_public
year: 2025
domain: [general, code, software-engineering, agentic]
genre: online-leaderboard

authority:
  maintainers: [Scale AI (Xiang Deng, Jeff Da 等 22 名作者)]
  institution_count: 0
  update_cadence: live           # Scale Labs 公榜持续接收提交;另有 private/held-out 不公开
  online: true

methodology:
  evaluation: [automated]
  contamination_controls: "刻意的抗污染设计:① 公开集与 held-out 集只选**强 copyleft(GPL)** 许可的仓库(法律上限制被随意纳入训练集);② 另购 18 个真实创业公司的**商用代码库**做 commercial 集(受限访问)。public(731 题)公开,held-out(858 题,12 仓)与 commercial(276 题,18 仓)**不公开**,专门用于监测过拟合。"
  notes: "SWE-bench 的'加难加抗污染'续作。任务=真实 GitHub issue + 仓库快照 → 生成补丁(patch),用仓库自带测试判 % resolved——与 SWE-bench 同范式但**长程(long-horizon)**:常跨多文件、大改动,人类工程师需数小时到数天,全部经人工校验并补足上下文以保证可解。共 1,865 题、41 个仓库(public 11 / held-out 12 / commercial 18)。"

models_ranked:
  - { model: Claude Sonnet 4.5, rank: 1, axis: software-engineering, license: closed, note: "public 集 43.6%(论文 v2,2025-11 口径);Claude Sonnet 4 42.7%、GPT-5(high)41.8% 紧随。注意整体仍低——比 SWE-bench Verified 的 ~80% 饱和区低一半多" }

citations:
  - { title: "SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks? (Deng, Da et al., Scale AI, arXiv 2509.16941v2, 2025-11-14)", url: "https://arxiv.org/abs/2509.16941", accessed: "2026-06-19" }
  - { title: "SWE-Bench Pro 公榜(Public Dataset)— Scale Labs Leaderboard", url: "https://labs.scale.com/leaderboard/swe_bench_pro_public", accessed: "2026-06-19" }
  - { title: "SWE-Bench Pro 私榜(Private/Held-out Dataset)— Scale Labs Leaderboard", url: "https://labs.scale.com/leaderboard/swe_bench_pro_private", accessed: "2026-06-19" }
  - { title: "SWE-Bench Pro: Raising the Bar for Agentic Coding(Scale AI 官方博客)", url: "https://scale.com/blog/swe-bench-pro", accessed: "2026-06-19" }

as_of: "2026-06-19"
freshness:
  status: fresh
  last_checked: "2026-06-19"
  note: "2025-09 首发、2025-11 修订;很新。作为 SWE-bench 在'前沿已 ~80% 饱和'后的**抗污染 + 长程**接棒榜收入,与既有 swe-bench 条目互为对照(刻意收的近族,增量在难度与污染控制)。"

agent_summary:
  author: agent
  generated: "2026-06-19"

moa:
  capability_axes: [software-engineering, code-generation, agentic, long-horizon, repo-level-reasoning, tool-use]
  modalities: [text]
  access: [api, open-weights]
  recommended_for:
    - "当 SWE-bench Verified 已 ~80% 饱和、区分不开顶尖编码模型时,用它做**更难、抗污染**的横比(public 集 40% 上下,区分度回来了)"
    - "关心**长程**工程能力(跨多文件、数小时级任务)而非单点修 bug 的 agent 选型"
    - "需要'未进训练集'信号时,看其 held-out/commercial 私榜的相对位次(public 分可能仍有泄漏)"
  caveats:
    - "刻意收的 **swe-bench 近族**——若已有 SWE-bench(Verified)信号,增量主要在难度/抗污染,不是新能力轴"
    - "vendor 自评循环性:Scale AI 同时是基准作者、榜主与商业评测方;private/commercial 集不公开,外部无法独立复核"
    - "仍是 issue→patch 一种工作流;长程≠覆盖多语言/架构/调试全谱"
    - "public 集分数随榜滚动更新,本条记的是 2025-11 论文口径,用前请核对实时榜"

tags: [code, agentic, swe, executable-eval, long-horizon, contamination-resistant, census-near-duplicate]
---

## Agent summary

SWE-Bench Pro(Scale AI,arXiv 2509.16941,2025-09 首发 / 2025-11 修订)是 **SWE-bench 的"加难 + 抗污染"续作**,
正面回应原 SWE-bench 在前沿已 **~80% 饱和**、且 gold patch 早进训练集的两大问题。

**任务范式**与 SWE-bench 一致:给真实 GitHub issue + 仓库快照,模型/agent 生成**补丁**,用仓库**自带测试**判定是否 resolved——
端到端可执行,不是选择题。区别在**长程(long-horizon)**:任务常跨**多文件、大改动**,一个专业工程师要**数小时到数天**才能完成,
全部经人工校验并补足上下文以保证"可解"。共 **1,865 题、41 个仓库**,分三层:**public**(731 题 / 11 仓,公开)、
**held-out**(858 题 / 12 仓,不公开)、**commercial**(276 题 / 18 个真实创业公司私有代码库,不公开)。

**抗污染怎么做。** 两手:① public 与 held-out 只选**强 copyleft(GPL)许可**的仓库,用许可证从法律上抬高"被随意吸进训练集"的门槛;
② commercial 集直接买**真实创业公司的私有代码**,靠受限访问杜绝泄漏。held-out 与 commercial 不公开,专门用来**监测过拟合**。

**结果(论文 v2,2025-11 口径)。** public 集最好成绩 **Claude Sonnet 4.5 = 43.6%**,Claude Sonnet 4 = 42.7%,GPT-5(high)= 41.8%;
更难的 commercial 集进一步掉到 ~16–18%。对照 SWE-bench Verified 的 ~80% 饱和区,**Pro 把区分度重新拉开了**——这正是它的价值。

**三信号分离提醒。** 它有真实工程难度(capability),但**权威性需打折**:Scale AI 同时是基准作者、榜主与商业评测方,存在
vendor 自评循环;private/commercial 集不公开,外部无法独立复核。引用数本条**未核实具体数值**(很新),不臆造。

<!-- 仅事实;来源:arXiv 2509.16941v2、Scale Labs public/private 榜、Scale 官方博客。分数为 2025-11 论文口径,实时榜可能已变,已在 caveats 标注。 -->

## Expert verdict

<!-- 人工署名(chenhao)。在本注释之外用中文作答:
     1) 你已有 SWE-bench(Verified)条目。SWE-bench Pro 作为"更难+抗污染"近族,值不值得在 MoA 选码模型时单独看?还是 Verified 饱和后直接换它当主信号?
     2) Scale AI 既是作者又是榜主、private 集不公开:这种 vendor 自评 + 不可复核,你给它的权威性打几折?会要求配独立私域复核吗?
     3) public 集 ~40% 的分,你读成"agent 还远不能做长程工程"的证据,还是"在长程任务上已有可用下限"?对你的 agent 选型阈值意味着什么? -->
