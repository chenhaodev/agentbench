---
id: pulse-ecg
name: PULSE / ECGBench
aliases: [PULSE, ECGBench, ECGInstruct]
homepage: https://aimedlab.github.io/PULSE/
year: 2024
domain: [medical, ecg, cardiology, multimodal, clinical]
genre: dataset

authority:
  maintainers: [Ruoqi Liu, Yuelin Bai, Xiang Yue, Ping Zhang (AIMedLab / Ohio State 等)]
  institution_count: 0
  update_cadence: frozen          # 论文随附的固定 benchmark(ECGBench)
  online: false

methodology:
  evaluation: [automated, llm-judge]
  contamination_controls: "ECGBench 含真实世界与合成 ECG 图像,跨 9 个数据集做 held-out 评测;但多模态 LLM 预训练语料是否见过同源公开 ECG 图/题面无法完全排除。属随论文发布的固定评测集,无滚动新题。"
  notes: "评测**多模态 LLM 读 ECG 图像(printed/digital image,不是原始波形信号)**的能力——这点与 signalmc-med(评信号编码器)正交。配套:① ECGInstruct,百万级 ECG 图像指令微调数据集;② PULSE,在其上训练的开源多模态 LLM;③ ECGBench,评测基准,覆盖 4 类 ECG 图像解读任务、跨 9 个数据集(真实 + 合成图)。主要结果:PULSE 平均准确率较通用多模态 LLM 提升 15%–30%,设新 SOTA。npj Digital Medicine 已收(2026),ICLR 评审见 OpenReview。"

models_ranked:
  - { model: PULSE, rank: 1, axis: ecg-image-interpretation, license: open-source, note: "在 ECGBench 上较通用多模态 LLM(如 GPT-4V 等)平均 +15%~30%,设新 SOTA——但这是**作者自训模型在自家基准上**领先,存在自评循环,需独立复核" }

citations:
  - { title: "Teach Multimodal LLMs to Comprehend Electrocardiographic Images (Liu, Bai, Yue, Zhang, arXiv 2410.19008, 2024-10)", url: "https://arxiv.org/abs/2410.19008", accessed: "2026-06-19" }
  - { title: "Teaching multimodal LLMs to comprehend 12-lead electrocardiographic images (npj Digital Medicine, 2026)", url: "https://www.nature.com/articles/s41746-026-02551-3", accessed: "2026-06-19" }
  - { title: "PULSE 项目页(代码 / 数据 / 模型)", url: "https://aimedlab.github.io/PULSE/", accessed: "2026-06-19" }
  - { title: "PULSE-ECG/ECGBench — 评测数据集(Hugging Face)", url: "https://huggingface.co/datasets/PULSE-ECG/ECGBench", accessed: "2026-06-19" }
  - { title: "Teach Multimodal LLMs to Comprehend Electrocardiographic Images — OpenReview", url: "https://openreview.net/forum?id=NOfmlsnCsS", accessed: "2026-06-19" }

as_of: "2026-06-19"
freshness:
  status: fresh
  last_checked: "2026-06-19"
  note: "2024-10 arXiv,2026 已上 npj Digital Medicine(同行评审),比纯预印本更可信。作为'多模态 LLM 读 ECG 图像'这一稀缺体裁的 census 锚点收入,与 signalmc-med(信号编码器)互补。"

agent_summary:
  author: agent
  generated: "2026-06-19"

moa:
  capability_axes: [ecg-image-interpretation, multimodal-medical, clinical-reasoning, image-comprehension]
  modalities: [image, text]
  access: [open-weights, local, api]
  recommended_for:
    - "为'读 ECG **图像**(打印/数字图,而非原始波形)'的临床任务选多模态 LLM——填本 census 里 ECG-图像 这条空白"
    - "资源受限/只拿得到 ECG 图片(非信号)的场景:这正是该基准刻意针对的设定"
    - "需要开源可自托管的医学多模态 LLM 时,PULSE 本体可直接评估纳入"
  caveats:
    - "测的是 **LLM 读图**,与 signalmc-med 的 **信号编码器** 正交;两者别混为'ECG 能力'一个轴"
    - "vendor/作者自评循环:PULSE 是作者自训模型,在自家 ECGBench 上领先,SOTA 声明需独立复核"
    - "固定评测集、无滚动新题;合成图占一部分,与真实临床分布的差距待评"

tags: [medical, ecg, cardiology, multimodal, llm-reads-image, census-anchor]
---

## Agent summary

PULSE / ECGBench(Liu、Bai、Yue、Ping Zhang 等,AIMedLab,arXiv 2410.19008,2024-10;2026 已上 **npj Digital Medicine**)
评测的是 **多模态 LLM 读 ECG 图像** 的能力。这里要和 repo 里已有的 signalmc-med 划清界限:signalmc-med 评的是**信号编码器**
(把原始 ECG/PPG 波形编码成表示),而 PULSE 评的是**多模态 LLM 看 ECG 图片**(打印或数字图像)——两者**正交**,
合起来才覆盖"机器读心电"的两种现实路径。PULSE 刻意针对**资源受限场景**:很多地方只拿得到 ECG 的**图片**,拿不到原始信号。

**三件套。**(1)**ECGInstruct**:百万级 ECG 图像指令微调数据集;(2)**PULSE**:在其上训练的**开源**多模态 LLM;
(3)**ECGBench**:评测基准,覆盖 **4 类** ECG 图像解读任务、跨 **9 个**数据集(含真实世界图与合成图)。

**结果。** PULSE 在 ECGBench 上较通用多模态 LLM(如 GPT-4V 等)**平均准确率提升 15%–30%**,设新 SOTA。
评分混用 automated 与 LLM-judge(开放式解读题)。

**三信号分离提醒。** 权威性比纯预印本强一档——已上 **npj Digital Medicine**(同行评审);但能力声明要警惕**自评循环**:
PULSE 是作者自训模型、在作者自建的 ECGBench 上领先,SOTA 需第三方独立复核。引用数本条**未核实具体数值**,不臆造。

<!-- 仅事实;来源:arXiv 2410.19008、npj Digital Medicine(2026)、PULSE 项目页、HF ECGBench、OpenReview。与 signalmc-med 的正交关系为事实陈述。 -->

## Expert verdict

<!-- 人工署名(chenhao)。在本注释之外用中文作答:
     1) PULSE 读 ECG 图像、signalmc-med 读 ECG 信号:在你的医学 MoA 里这两条是各占一个模块,还是按"能拿到信号就用编码器、只有图就用 LLM"来路由?
     2) 自评循环(作者自训 PULSE 在自家 ECGBench 领先)+ 部分合成图:SOTA 的 +15~30% 你信几成?要不要等第三方在真实临床图上复现?
     3) 已上 npj Digital Medicine(同行评审)这一点,对你给医学基准的权威性评级加多少分?够不够让它从"census 锚点"升为"可据此选型"? -->
