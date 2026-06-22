---
id: swe-bench-pro
name: SWE-Bench Pro
aliases: [SWE-Bench Pro Public, SWE-Bench Pro Private, SWEAP]
homepage: https://labs.scale.com/leaderboard/swe_bench_pro_public
year: 2025
domain: [general, code, software-engineering, agentic]
genre: online-leaderboard

authority:
  maintainers: [Scale AI (Xiang Deng, Jeff Da 等 22 名作者）]
  institution_count: 0
  update_cadence: live           # Scale Labs 公榜持续接收提交;另有 private/held-out 不公开
  online: true

methodology:
  evaluation: [automated]
  contamination_controls: "刻意的抗污染设计:① 公开集与 held-out 集只选**强 copyleft(GPL)** 许可的仓库（法律上限制被随意纳入训练集）;② 另购 18 个真实创业公司的**商用代码库**做 commercial 集（受限访问）。public(731 题）公开,held-out(858 题,12 仓）与 commercial(276 题,18 仓）**不公开**,专门用于监测过拟合。"
  notes: "SWE-bench 的‘加难加抗污染’续作。任务=真实 GitHub issue + 仓库快照 → 生成补丁（patch),用仓库自带测试判 % resolved——与 SWE-bench 同范式但**长程（long-horizon)**:常跨多文件、大改动,人类工程师需数小时到数天,全部经人工校验并补足上下文以保证可解。共 1,865 题、41 个仓库（public 11 / held-out 12 / commercial 18)。"

models_ranked:
  - { model: Claude Sonnet 4.5, rank: 1, axis: software-engineering, license: closed, note: "public 集 43.6%（论文 v2,2025-11 口径）;Claude Sonnet 4 42.7%、GPT-5(high)41.8% 紧随。注意整体仍低——比 SWE-bench Verified 的 ~80% 饱和区低一半多" }

citations:
  - { title: "SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks? (Deng, Da et al., Scale AI, arXiv 2509.16941v2, 2025-11-14)", url: "https://arxiv.org/abs/2509.16941", accessed: "2026-06-19" }
  - { title: "SWE-Bench Pro 公榜（Public Dataset)— Scale Labs Leaderboard", url: "https://labs.scale.com/leaderboard/swe_bench_pro_public", accessed: "2026-06-19" }
  - { title: "SWE-Bench Pro 私榜（Private/Held-out Dataset)— Scale Labs Leaderboard", url: "https://labs.scale.com/leaderboard/swe_bench_pro_private", accessed: "2026-06-19" }
  - { title: "SWE-Bench Pro: Raising the Bar for Agentic Coding(Scale AI 官方博客）", url: "https://scale.com/blog/swe-bench-pro", accessed: "2026-06-19" }

as_of: "2026-06-19"
freshness:
  status: fresh
  last_checked: "2026-06-19"
  note: "2025-09 首发、2025-11 修订;很新。作为 SWE-bench 在‘前沿已 ~80% 饱和’后的**抗污染 + 长程**接棒榜收入,与既有 swe-bench 条目互为对照（刻意收的近族,增量在难度与污染控制）。"

agent_summary:
  author: agent
  generated: "2026-06-19"

expert_verdict:
  signed_by: chenhao
  signed_date: "2026-06-17"
  confidence: medium          # low / medium / high

moa:
  capability_axes: [software-engineering, code-generation, agentic, long-horizon, repo-level-reasoning, tool-use]
  modalities: [text]
  access: [api, open-weights]
  recommended_for:
    - "当 SWE-bench Verified 已 ~80% 饱和、区分不开顶尖编码模型时,用它做**更难、抗污染**的横比（public 集 40% 上下,区分度回来了）"
    - "关心**长程**工程能力（跨多文件、数小时级任务）而非单点修 bug 的 agent 选型"
    - "需要‘未进训练集’信号时,看其 held-out/commercial 私榜的相对位次（public 分可能仍有泄漏）"
  caveats:
    - "刻意收的 **swe-bench 近族**——若已有 SWE-bench(Verified）信号,增量主要在难度/抗污染,不是新能力轴"
    - "vendor 自评循环性:Scale AI 同时是基准作者、榜主与商业评测方;private/commercial 集不公开,外部无法独立复核"
    - "仍是 issue→patch 一种工作流;长程≠覆盖多语言/架构/调试全谱"
    - "public 集分数随榜滚动更新,本条记的是 2025-11 论文口径,用前请核对实时榜"

tags: [code, agentic, swe, executable-eval, long-horizon, contamination-resistant, census-near-duplicate]
---

## Agent summary

SWE-Bench Pro（由数据标注公司 Scale AI 制作,arXiv 2509.16941,2025-09 首发 / 2025-11 修订）是 SWE-bench 的续作,目标是“更难、更抗背答案”。它要解决老 SWE-bench 的两个毛病:一是顶尖模型在上面已经能做到约 80% 的题,大家挤在高分区,分不出高下（术语叫“饱和”）;二是它的标准答案补丁很早就进了各家模型的训练数据,模型可能是“见过答案”而不是真会做。

出题方式和 SWE-bench 一样。它给模型一个真实的 GitHub issue（代码仓库里登记的待修 bug 或需求）,再加上当时的代码快照,让能自己分步骤、调用工具干活的 AI（agent,智能体）写出一段代码修改（patch,补丁）;改完后用这个仓库自带的、自动跑的测试用例（unit test）来判定改对没有,通过了就算解决。整个过程是真把代码跑起来,不是做选择题。和老版的区别在于“长程”（long-horizon）:一道题往往要改好几个文件、动很多地方,一个专业工程师都得花几小时到几天才能搞定;所有题目都经过人工核对、补齐了上下文,确保确实有解。全套共 1,865 题、41 个仓库,分三层:public（公开集,731 题 / 11 仓）、held-out（留存集,858 题 / 12 仓,不公开）、commercial（商用集,276 题 / 18 个真实创业公司的私有代码库,不公开）。

抗“背答案”（contamination-resistant）用了两招。第一,public 和 held-out 只选用“强 copyleft（GPL）”许可证的仓库,这类许可证在法律上限制别人随便把代码塞进训练集,等于抬高了泄题门槛。第二,commercial 集干脆花钱买真实创业公司的私有代码,外人根本拿不到,自然没法泄漏。held-out 和 commercial 都不公开,专门用来检查模型是不是只是“背熟了公开题”（过拟合）。

成绩看 2025-11 的论文口径。public 集上最好的是 Claude Sonnet 4.5,43.6%;Claude Sonnet 4 紧随,42.7%;GPT-5（high）41.8%。到了更难的 commercial 集,分数进一步掉到 16% 到 18% 左右。对比 SWE-bench Verified 已经约 80% 的饱和成绩,Pro 重新把好坏拉开了距离,这正是它的价值所在。

最后提醒读者分清三种信号。这套题确实有真实的工程难度（能力是实打实的）,但它的权威性要打折:Scale AI 既是出题人、又是榜单管理方、还是商业评测方,自己出题自己评,存在“自评”的循环嫌疑;private 和 commercial 集不公开,外部无法独立复核成绩。这一条的引用数没有核实到具体数值（基准很新）,不臆造。

<!-- 仅事实;来源:arXiv 2509.16941v2、Scale Labs public/private 榜、Scale 官方博客。分数为 2025-11 论文口径,实时榜可能已变,已在 caveats 标注。 -->

## Expert verdict

1) 你已有 SWE-bench(Verified)条目。SWE-bench Pro 作为"更难+抗污染"近族,值不值得在 MoA 选码模型时单独看? 我认为它是 Verified 饱和后直接换它当主信号
2) Scale AI 既是作者又是榜主、private 集不公开: 这种 vendor 自评 + 不可复核, 你给它的权威性打几折? 8折, 因为符合我&人们对ClaudeCode/Codex的编程体验排序。
3) public 集 ~40% 的分,你读成"agent 还远不能做长程工程"的证据,还是"在长程任务上已有可用下限"? 对你的 agent 选型阈值意味着什么? 我认为是长程任务上已有可用下限；agent 选型阈值：根据经验公式，至少40%分才可以进行长程工程。
