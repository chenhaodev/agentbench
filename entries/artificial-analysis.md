---
id: artificial-analysis
name: Artificial Analysis
aliases: [AA, Artificial Analysis Intelligence Index, AA-II]
homepage: https://artificialanalysis.ai/
year: 2024                         # 私下 2023 起步,2024-01 公开上线
domain: [meta, model-selection, ai-benchmarks]
genre: aggregator

authority:
  maintainers: [Artificial Analysis]   # 独立公司,非学术机构;创始人 Micah Hill-Smith / George Cameron
  institution_count: 0
  update_cadence: live
  online: true

popularity:
  trending: true                  # 被各家 lab、媒体广泛引用作"中立第三方"口径
  as_of: "2026-06-22"

methodology:
  evaluation: [automated]
  contamination_controls: "自己跑标准化评测、不取 lab 自报数,以抵御'同一题不同 prompt/few-shot 刷分';但其组成 benchmark(GPQA Diamond、HLE 等)本身的污染问题不在其控制范围。"
  notes: "聚合器中的'对比/指数'型(区别于本仓已有的'发现'型 leaderboard-of-leaderboards)。它把多个 eval 压成一个 0–100 的 Artificial Analysis Intelligence Index(v4.1 含 9 项:GDPval-AA v2、τ³-Banking、Terminal-Bench v2.1、SciCode、Humanity's Last Exam、GPQA Diamond、CritPt、AA-Omniscience、AA-LCR,按成本加权合成),并在同一视图里横比各 provider 的 速度(输出 tokens/s、TTFT)与 价格(按 cache/input/output 加权的 blended 价)。另有 Omniscience Index 及图像/视频/音乐/语音/编码 agent 等独立榜。重点:它会自己跑评测,不是纯粹索引别家榜。"

citations:
  - { title: "Artificial Analysis — Models leaderboard (homepage)", url: "https://artificialanalysis.ai/", accessed: "2026-06-22" }
  - { title: "Artificial Analysis — Methodology", url: "https://artificialanalysis.ai/methodology", accessed: "2026-06-22" }
  - { title: "Latent Space — Independent LLM Evals as a Service (founders George Cameron & Micah Hill-Smith)", url: "https://www.latent.space/p/artificialanalysis", accessed: "2026-06-22" }

as_of: "2026-06-22"
freshness:
  status: fresh
  last_checked: "2026-06-22"
  note: "实时站点;Intelligence Index 会换版本(当前 v4.1,9 项),组成与权重随版本变,横比时要锁定同一 index 版本。"

agent_summary:
  author: agent
  generated: "2026-06-22"

expert_verdict:
  signed_by: chenhao
  signed_date: "2026-06-22"
  confidence: medium          # low / medium / high
  one_liner: "透明的独立第三方:质量当粗筛、速度×价格最有用;综合分必下钻,别当能力定论。"

moa:
  capability_axes: [model-selection, composite-intelligence, cost-performance-tradeoff, inference-speed, price-comparison]
  modalities: [text, image, audio, video, tool-use]
  access: [api, open-weights, closed]
  recommended_for:
    - "起草 MoA 时做'质量×速度×价格'三轴横比、按 provider/endpoint 选型与路由(本仓唯一覆盖速度/价格轴的条目)"
    - "想要一个中立第三方、自己跑评测(不取 lab 自报数)的综合质量快照时"
  caveats:
    - "Intelligence Index 是成本加权的合成分,会换版本(v4.1=9 项);跨时间/跨模型比必须锁同一 index 版本,否则不可比"
    - "组成 benchmark 的污染/饱和会传导进合成分;指数高≠每个子能力都强,选型仍要下钻看分项"
    - "是独立商业公司而非学术机构(institution_count=0);权威来自方法透明 + 媒体/lab 采信(popularity),不是引用或机构背书"
    - "速度/价格随 provider、负载、量价合同实时变;站点快照仅供参考,不等于你自己端到端的实测"

tags: [aggregator, model-selection, price, speed, intelligence-index, meta]
---

## Agent summary

本条目覆盖 **aggregator** 体裁里的**"对比/指数"型**(与本仓已有的"发现"型
[leaderboard-of-leaderboards] 互补:那个索引别人的榜,这个把多项评测压成可横比的选型指数)。
**Artificial Analysis(AA)**由 **Micah Hill-Smith(Co-founder & CEO)与 George Cameron
(Co-founder & CPO)于 2023 年发起、2024 年 1 月公开上线**,定位是**独立第三方**的 AI 模型/推理服务
横评平台,覆盖 **proprietary 与 open-weights** 两类模型、跨 OpenAI、Bedrock、Together.ai 等多家 provider。

它的核心产物是 **Artificial Analysis Intelligence Index(AA-II)**——一个 **0–100 的综合质量分**。
当前 **v4.1 由 9 项评测按成本加权合成**:GDPval-AA v2、τ³-Banking、Terminal-Bench v2.1、SciCode、
Humanity's Last Exam、GPQA Diamond、CritPt、AA-Omniscience、AA-LCR(覆盖 agentic 真实工作任务、编码、
科学/物理推理、知识、长上下文)。除质量外,它在**同一视图**给出**速度**(输出 tokens/s、Time-to-First-Token)
与**价格**(按 cache/input/output 加权的 blended 价),另有 Omniscience Index 及图像/视频/音乐/语音/编码 agent
等独立榜。

一个关键事实区分:**AA 会自己跑标准化评测、而非采用各 lab 自报数**——其公开动机是 lab 之间
"prompt 方式不同、挑 chain-of-thought 例子刷分"(如早期 Gemini 1.0 Ultra 用 32-shot 在 MMLU 上压 GPT-4)。
因此它**不是纯索引别家榜的聚合器**,而是"自评 + 合成指数 + 跨 provider 横比"的混合体。对起草 MoA 的人,
它的独特价值在于**唯一把质量、速度、价格摆在一起做选型/路由**;但要记住:合成指数会换版本、组成 benchmark 的
污染会传导进总分,且它的权威来自**方法透明与被广泛采信(popularity 信号)**,而非学术引用或机构背书。

<!-- 仅事实;来源:AA 首页、AA Methodology 页、Latent Space 创始人访谈(均见 citations,accessed 2026-06-22)。9 项组成为 Intelligence Index v4.1 的站点口径。 -->

## Expert verdict

AA 的质量指数我当**独立的粗筛信号**——起草 MoA 时先用它快速圈定候选,但不据它定稿。它"自己跑评测、不取 lab 自报数"值得**加权威分**,可它是商业公司、Intelligence Index 还换版本,所以这个综合分**必须下钻看分项**才能进选型。至于"人气≠权威":AA 这种方法透明的独立第三方**介于二者之间,看用途**——拿来粗筛/路由时算一种可采信的轻权威,但要当某个子能力的能力定论,就仍只是 sentiment,得回到专项权威榜。它真正不可替代的价值在速度×价格轴,那是本仓其他条目都没覆盖的选型输入。
