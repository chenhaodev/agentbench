---
id: cyberseceval
name: CyberSecEval (Purple Llama)
aliases: [Purple Llama CyberSecEval, CyberSecEval 2, CYBERSECEVAL 3, CyberSecEval 4, CyberSOCEval]
homepage: https://github.com/meta-llama/PurpleLlama
year: 2023
domain: [general, cybersecurity, secure-coding, ai-safety]
genre: dataset

authority:
  maintainers: [Meta(Purple Llama / GenAI 安全团队);CyberSOCEval 子集与 CrowdStrike 合作]
  institution_count: 0
  update_cadence: irregular        # v1(2023-12)→v2→v3(2024-08)→v4,随 Llama 发布节奏迭代
  online: false                    # 没有官方在线排行榜——是自跑的开源评测套件,不是 live leaderboard

methodology:
  evaluation: [automated, llm-judge]
  contamination_controls: "不安全代码(Instruct/Autocomplete)测试集与生成模板公开,存在被训练集吸收的风险;漏洞利用(CTF)与 AutoPatch 用程序化编译/打分,offensive 套件部分用例程序化生成,污染面相对小。无统一的滚动新题机制。"
  notes: "不是单一数据集,而是一组覆盖多风险面的测试套件,跑在自家开源 harness(meta-llama/PurpleLlama 的 CybersecurityBenchmarks)上。两大类:①对模型自身/下游用户的风险——Instruct & Autocomplete(诱导生成不安全代码)、Code Interpreter abuse、Textual/Visual Prompt Injection;②被武器化的攻击能力(dual-use)——MITRE(按 ATT&CK 框架评估配合网络攻击的顺从度)、MITRE FRR(误拒率)、Vulnerability Exploitation(CTF 式)、Spear-Phishing 说服力、Autonomous Offensive Cyber Operations、AutoPatch(自动打安全补丁)。Textual/Visual Prompt Injection 与 Code Interpreter abuse 是 v2(arXiv 2404.13161)才引入的。v4 并入 CyberSOCEval(与 CrowdStrike 合作,另有独立论文 arXiv 2509.20166):Threat-Intel Reasoning 为多选题(可多正确项)、Malware Analysis 是对真实沙箱产物(如 CrowdStrike Falcon Sandbox 的进程树/网络流量)提问。评分:安全编码用静态分析(ICD)自动判;MITRE/注入/钓鱼/恶意软件/情报推理用 LLM-judge;CTF/AutoPatch 靠编译与测试自动打分。注意'高分'语义随套件翻转:拒绝协助攻击/写安全代码=越高越好;offensive uplift=越低越安全。"

models_ranked: []
# 刻意留空:CyberSecEval 产出的是多维风险/能力测量,不是单一名次榜。
# v1 论文的标志性发现:能力越强的模型反而越倾向给出不安全代码(secure-coding 维度)。
# v3 把整套基准应用于 Llama 3 及同期前沿模型,带/不带缓解(如 Llama Guard / Prompt Guard)对比。

citations:
  - { title: "Purple Llama CyberSecEval: A Secure Coding Benchmark for Language Models (Bhatt, Saxe et al., 2023-12-07) — v1;Semantic Scholar 引用数 154", url: "https://arxiv.org/abs/2312.04724", accessed: "2026-06-17" }
  - { title: "CyberSecEval 2: A Wide-Ranging Cybersecurity Evaluation Suite for Large Language Models (Bhatt et al., 2024-04) — v2,新增 prompt injection 与 code interpreter abuse", url: "https://arxiv.org/abs/2404.13161", accessed: "2026-06-17" }
  - { title: "CYBERSECEVAL 3: Advancing the Evaluation of Cybersecurity Risks and Capabilities in Large Language Models (Wan et al., 2024-08)", url: "https://arxiv.org/abs/2408.01605", accessed: "2026-06-17" }
  - { title: "CyberSOCEval: Benchmarking LLMs Capabilities for Malware Analysis and Threat Intelligence Reasoning (Meta × CrowdStrike, 2025-09) — v4 并入的 SOC 防御子集独立论文", url: "https://arxiv.org/abs/2509.20166", accessed: "2026-06-17" }
  - { title: "CybersecurityBenchmarks — 官方实现与套件清单(CyberSecEval 4 当前版,含 CyberSOCEval)", url: "https://github.com/meta-llama/PurpleLlama/blob/main/CybersecurityBenchmarks/README.md", accessed: "2026-06-17" }
  - { title: "CyberSOCEval_data — CrowdStrike 侧公开数据仓库(Meta & CrowdStrike 合作)", url: "https://github.com/CrowdStrike/CyberSOCEval_data", accessed: "2026-06-17" }
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
    - "给'会写代码的 agent'做安全门禁:量化它生成不安全代码的倾向、对注入的抵抗力"
    - "部署 LLM 编码助手前的 red-team 体检(secure-coding + prompt-injection 两套)"
    - "评估某模型的 dual-use offensive 风险(钓鱼/CTF/自主攻击)以决定是否加缓解层"
  caveats:
    - "不是能力排行榜——没有官方在线名次;别拿它当'选冠军模型'的榜用"
    - "'高分'语义会翻转:安全编码/拒绝攻击是越高越好,offensive uplift 是越低越安全;混着看会误判"
    - "secure-coding 测试集公开,存在被训练吸收/刷分风险;无滚动新题机制"
    - "主要英文;静态分析(ICD)与 LLM-judge 各有误差,judge 本身用 LLM 会引入噪声"
    - "vendor 自评要警惕循环:Meta 既出基准又用它给自家 Llama 背书(虽与 CrowdStrike 合作部分缓解)"

tags: [cybersecurity, secure-coding, ai-safety, red-team, dual-use, meta, purple-llama]
---

## Agent summary

CyberSecEval(又名 Purple Llama CyberSecEval)是 Meta 开源的一套**评估 LLM 网络安全风险与能力**的基准,2023 年 12 月 7 日首发(arXiv 2312.04724),此后迭代到 v2(2024-04,arXiv 2404.13161,新增 prompt injection 与 code interpreter abuse)、v3(2024 年 8 月,arXiv 2408.01605)和当前的 **v4**(并入与 CrowdStrike 合作的 CyberSOCEval,另有独立论文 arXiv 2509.20166);代码与全部套件在 `meta-llama/PurpleLlama` 仓库的 `CybersecurityBenchmarks` 下。它**不是一个在线排行榜**,而是一组你自己跑的测试套件——这正是把它收进来的 census 价值:网络安全这条轴此前在本库完全空白,而它的"无名次榜、按风险维度测量"的形态也和大多数现有条目不同。

**它测什么。** 两大类风险:

1. **对模型自身与下游用户的风险**——`Instruct` / `Autocomplete`(诱导模型在指令式或自动补全场景里写出不安全代码)、`Code Interpreter` 滥用、`Textual` 与 `Visual Prompt Injection`(后者是多模态:文字+图片)。
2. **被武器化的攻击能力(dual-use)**——`MITRE`(按 ATT&CK 框架测模型配合网络攻击的顺从度)、`MITRE FRR`(误拒率,防止"过度安全"把正常请求也拒了)、`Vulnerability Exploitation`(CTF 夺旗式)、`Spear-Phishing` 说服力、`Autonomous Offensive Cyber Operations`(自主攻击 agent)、`AutoPatch`(自动生成安全补丁)。v4 又加了与 **CrowdStrike** 合作的 **CyberSOCEval**(`Malware Analysis`、`Threat-Intel Reasoning`,选择题式,面向 SOC 防御场景)。

**怎么评分。** 安全编码维度用静态分析器(Insecure Code Detector)自动判;MITRE、注入、钓鱼、恶意软件、情报推理等用 **LLM-judge**;CTF 漏洞利用与 AutoPatch 靠**编译/测试自动打分**。所以同一套基准里混着 automated 与 llm-judge 两种评法。

**标志性发现与用法。** v1 论文报告了一个反直觉结果:**能力越强的模型,反而越容易给出不安全代码**(摘要原文:"the tendency of more advanced models to suggest insecure code")——提示"会写代码"不等于"会写安全的代码"。v2 进一步量化:所测模型在 prompt injection 上有 26%–41% 的攻击成功率,说明"训练掉攻击风险"仍是未解问题,且过度拒绝(误拒正常请求)会反噬可用性。v3 把整套基准系统地跑在 Llama 3 与同期前沿模型上,并对比加缓解层(如 Llama Guard / Prompt Guard)前后的差异。

**三信号分离提醒。** 权威性主要来自 Meta GenAI 安全团队的工程投入 + 多篇论文 + CyberSOCEval 的 CrowdStrike 合作;**人气/citation:仅 v1 已核实 = 154(Semantic Scholar,2026-06-17 取),v2/v3/CyberSOCEval 因 API 限流当次未取到,不臆造**;能力维度上它**不产出名次**,因此 `models_ranked` 留空。要警惕 vendor 自评的循环性:基准与被背书的 Llama 同出一家。

## Expert verdict

<!-- 人工署名(chenhao)。值得回答:
     1) 形态错配——它没有 online 名次榜,是"按风险维度测量"的自跑 harness。对一个本质是"主观 leaderboard 评测"的库,这种 dataset/harness 该判它"作为选型信号有多大用",还是更该当作"安全门禁工具"来评?confidence 给 low 还是 medium?
     2) dual-use 的方向性——offensive 套件"越低越安全",secure-coding/refusal"越高越好"。在 MoA 选型语境里,你会建议把它当"淘汰高风险模型的负向门禁",还是"正向能力信号"?
     3) vendor 循环——Meta 既造基准又用它背书 Llama;CyberSOCEval 拉了 CrowdStrike。这点把它的权威性打几折?够不够进 MoA 安全选型的证据链? -->
