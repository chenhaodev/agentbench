---
id: cyberseceval
name: CyberSecEval (Purple Llama)
aliases: [Purple Llama CyberSecEval, CyberSecEval 2, CYBERSECEVAL 3, CyberSecEval 4, CyberSOCEval]
homepage: https://github.com/meta-llama/PurpleLlama
year: 2023
domain: [general, cybersecurity, secure-coding, ai-safety]
genre: dataset

authority:
  maintainers: [Meta(Purple Llama / GenAI 安全团队）;CyberSOCEval 子集与 CrowdStrike 合作]
  institution_count: 0
  update_cadence: irregular        # v1(2023-12)→v2→v3(2024-08)→v4,随 Llama 发布节奏迭代
  online: false                    # 没有官方在线排行榜——是自跑的开源评测套件,不是 live leaderboard

methodology:
  evaluation: [automated, llm-judge]
  contamination_controls: "不安全代码（Instruct/Autocomplete）测试集与生成模板公开,存在被训练集吸收的风险;漏洞利用（CTF）与 AutoPatch 用程序化编译/打分,offensive 套件部分用例程序化生成,污染面相对小。无统一的滚动新题机制。"
  notes: "不是单一数据集,而是一组覆盖多风险面的测试套件,跑在自家开源 harness(meta-llama/PurpleLlama 的 CybersecurityBenchmarks）上。两大类:①对模型自身/下游用户的风险——Instruct & Autocomplete（诱导生成不安全代码）、Code Interpreter abuse、Textual/Visual Prompt Injection;②被武器化的攻击能力（dual-use)——MITRE（按 ATT&CK 框架评估配合网络攻击的顺从度）、MITRE FRR（误拒率）、Vulnerability Exploitation(CTF 式）、Spear-Phishing 说服力、Autonomous Offensive Cyber Operations、AutoPatch（自动打安全补丁）。Textual/Visual Prompt Injection 与 Code Interpreter abuse 是 v2(arXiv 2404.13161）才引入的。v4 并入 CyberSOCEval（与 CrowdStrike 合作,另有独立论文 arXiv 2509.20166):Threat-Intel Reasoning 为多选题（可多正确项）、Malware Analysis 是对真实沙箱产物（如 CrowdStrike Falcon Sandbox 的进程树/网络流量）提问。评分:安全编码用静态分析（ICD）自动判;MITRE/注入/钓鱼/恶意软件/情报推理用 LLM-judge;CTF/AutoPatch 靠编译与测试自动打分。注意‘高分’语义随套件翻转:拒绝协助攻击/写安全代码=越高越好;offensive uplift=越低越安全。"

models_ranked: []
# 刻意留空:CyberSecEval 产出的是多维风险/能力测量,不是单一名次榜。
# v1 论文的标志性发现:能力越强的模型反而越倾向给出不安全代码（secure-coding 维度）。
# v3 把整套基准应用于 Llama 3 及同期前沿模型,带/不带缓解（如 Llama Guard / Prompt Guard）对比。

citations:
  - { title: "Purple Llama CyberSecEval: A Secure Coding Benchmark for Language Models (Bhatt, Saxe et al., 2023-12-07) — v1;Semantic Scholar 引用数 154", url: "https://arxiv.org/abs/2312.04724", accessed: "2026-06-17" }
  - { title: "CyberSecEval 2: A Wide-Ranging Cybersecurity Evaluation Suite for Large Language Models (Bhatt et al., 2024-04) — v2,新增 prompt injection 与 code interpreter abuse", url: "https://arxiv.org/abs/2404.13161", accessed: "2026-06-17" }
  - { title: "CYBERSECEVAL 3: Advancing the Evaluation of Cybersecurity Risks and Capabilities in Large Language Models (Wan et al., 2024-08)", url: "https://arxiv.org/abs/2408.01605", accessed: "2026-06-17" }
  - { title: "CyberSOCEval: Benchmarking LLMs Capabilities for Malware Analysis and Threat Intelligence Reasoning (Meta × CrowdStrike, 2025-09) — v4 并入的 SOC 防御子集独立论文", url: "https://arxiv.org/abs/2509.20166", accessed: "2026-06-17" }
  - { title: "CybersecurityBenchmarks — 官方实现与套件清单（CyberSecEval 4 当前版,含 CyberSOCEval)", url: "https://github.com/meta-llama/PurpleLlama/blob/main/CybersecurityBenchmarks/README.md", accessed: "2026-06-17" }
  - { title: "CyberSOCEval_data — CrowdStrike 侧公开数据仓库（Meta & CrowdStrike 合作）", url: "https://github.com/CrowdStrike/CyberSOCEval_data", accessed: "2026-06-17" }
  - { title: "Purple Llama CyberSecEval — Meta AI 研究发布页", url: "https://ai.meta.com/research/publications/purple-llama-cyberseceval-a-benchmark-for-evaluating-the-cybersecurity-risks-of-large-language-models/", accessed: "2026-06-17" }

as_of: "2026-06-17"
freshness:
  status: fresh
  last_checked: "2026-06-17"
  note: "以仓库当前 CyberSecEval 4 为准;Meta 随 Llama 迭代,版本会继续往上走。"

agent_summary:
  author: agent
  generated: "2026-06-17"

moa:
  capability_axes: [secure-code-generation, cyberattack-refusal, prompt-injection-resistance, offensive-cyber-capability]
  modalities: [text, image]
  access: [api, open-weights, local]
  recommended_for:
    - "给‘会写代码的 agent’做安全门禁:量化它生成不安全代码的倾向、对注入的抵抗力"
    - "部署 LLM 编码助手前的 red-team 体检（secure-coding + prompt-injection 两套）"
    - "评估某模型的 dual-use offensive 风险（钓鱼/CTF/自主攻击）以决定是否加缓解层"
  caveats:
    - "不是能力排行榜——没有官方在线名次;别拿它当‘选冠军模型’的榜用"
    - "‘高分’语义会翻转:安全编码/拒绝攻击是越高越好,offensive uplift 是越低越安全;混着看会误判"
    - "secure-coding 测试集公开,存在被训练吸收/刷分风险;无滚动新题机制"
    - "主要英文;静态分析（ICD）与 LLM-judge 各有误差,judge 本身用 LLM 会引入噪声"
    - "vendor 自评要警惕循环:Meta 既出基准又用它给自家 Llama 背书（虽与 CrowdStrike 合作部分缓解）"

tags: [cybersecurity, secure-coding, ai-safety, red-team, dual-use, meta, purple-llama]
---

## Agent summary

CyberSecEval（又名 Purple Llama CyberSecEval）是 Meta（开发 Llama 系列大模型的公司）开源的一套基准测试,也就是给 AI 出的标准考卷,专门考察大语言模型（LLM,即能读写文字的通用 AI）在网络安全上的风险和能力。它 2023 年 12 月 7 日首发（arXiv 2312.04724,arXiv 是论文预印本网站,编号可查到原文）,之后一路更新:v2（2024-04,arXiv 2404.13161,新增 prompt injection 和 code interpreter abuse 两项）、v3（2024 年 8 月,arXiv 2408.01605）,到现在的 v4（把和 CrowdStrike 合作的 CyberSOCEval 并了进来,另有独立论文 arXiv 2509.20166）。代码和全部测试套件都放在 `meta-llama/PurpleLlama` 仓库的 `CybersecurityBenchmarks` 目录下。要注意它不是一个在线排行榜,而是一组你得自己跑起来的测试套件。它对本库的价值正在这里:网络安全这条线之前在本库完全空白,而且它“不排名次、只按风险维度逐项测量”的形态,也和库里大多数条目不一样。

它考什么?分两大类风险。

1. 对模型自己和使用者的风险:`Instruct` / `Autocomplete`（在写指令和自动补全这两种场景下,试着诱导模型写出不安全的代码）、`Code Interpreter` 滥用、`Textual` 和 `Visual Prompt Injection`。这里的 prompt injection 指往输入里塞恶意指令骗 AI 照做,后者是多模态（能同时看图读文）的版本,把恶意指令藏在图片里。
2. 被当成武器的攻击能力,即所谓 dual-use（同一项能力既能防守也能攻击）:`MITRE`（按 ATT&CK 这套攻击手法框架,测模型有多愿意配合网络攻击）、`MITRE FRR`（误拒率,看模型会不会“安全过头”,把正常请求也拒了）、`Vulnerability Exploitation`（类似 CTF 夺旗赛,找漏洞拿“旗子”）、`Spear-Phishing` 说服力（写钓鱼邮件骗人的能耐）、`Autonomous Offensive Cyber Operations`（能自己分步骤干活的攻击型 agent,即智能体）、`AutoPatch`（自动生成安全补丁）。v4 又加上和 CrowdStrike 合作的 CyberSOCEval,里头有 `Malware Analysis`（恶意软件分析）和 `Threat-Intel Reasoning`（威胁情报推理）,都是选择题形式,面向 SOC（企业安全运营中心）的防守场景。

怎么打分?各部分用法不一样。安全编码那部分用一个叫 Insecure Code Detector 的静态分析器自动判;MITRE、注入、钓鱼、恶意软件、情报推理这些用 LLM-judge,也就是让另一个 AI 当“阅卷老师”打分;CTF 找漏洞和 AutoPatch 则靠编译和跑测试来自动打分。所以同一套基准里,机器自动判和 AI 阅卷两种评法是混着用的。

它最出名的一个发现,挺反直觉:能力越强的模型,反而越容易写出不安全的代码（v1 论文摘要原话是 “the tendency of more advanced models to suggest insecure code”）。换句话说,“会写代码”不等于“会写安全的代码”。v2 把风险量化得更细:所测模型在 prompt injection 上的攻击成功率有 26% 到 41%,说明“靠训练把攻击风险消掉”至今没解决,而且模型一旦拒绝过头（把正常请求也拒了）,反过来又会拖累可用性。v3 把整套基准系统地跑在 Llama 3 和同期的前沿模型上,还对比了加防护层（如 Llama Guard、Prompt Guard）前后的差别。

最后提醒,看这类基准要把三种信号分开。权威性这块,主要来自 Meta GenAI 安全团队的工程投入、多篇论文,加上 CyberSOCEval 和 CrowdStrike 的合作。人气和被引用情况这块,只有 v1 核实到 = 154 次（Semantic Scholar 数据,2026-06-17 取的）,v2、v3、CyberSOCEval 当时因为接口限流没取到,这里不瞎编。能力这块,它本就不产出名次,所以 `models_ranked` 留空。还要当心 vendor 自评的循环问题:出基准的和被基准背书的 Llama 是同一家公司。

## Expert verdict

<!-- 人工署名(chenhao)。值得回答:
     1) 形态错配——它没有 online 名次榜,是"按风险维度测量"的自跑 harness。对一个本质是"主观 leaderboard 评测"的库,这种 dataset/harness 该判它"作为选型信号有多大用",还是更该当作"安全门禁工具"来评?confidence 给 low 还是 medium?
     2) dual-use 的方向性——offensive 套件"越低越安全",secure-coding/refusal"越高越好"。在 MoA 选型语境里,你会建议把它当"淘汰高风险模型的负向门禁",还是"正向能力信号"?
     3) vendor 循环——Meta 既造基准又用它背书 Llama;CyberSOCEval 拉了 CrowdStrike。这点把它的权威性打几折?够不够进 MoA 安全选型的证据链? -->
