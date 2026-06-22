---
id: mediqa-chat
name: MEDIQA-Chat 2023
aliases: [MEDIQA-Chat, ClinicalNLP MEDIQA-Chat]
homepage: https://aclanthology.org/2023.clinicalnlp-1.52/
year: 2023
domain: [medical, clinical-nlp, dialogue-summarization]
genre: shared-task

authority:
  maintainers: [Asma Ben Abacha et al. (Microsoft / Nuance), ACL ClinicalNLP Workshop]
  institution_count: 0
  update_cadence: frozen        # 2023 edition; the MEDIQA series runs in different years
  online: false                 # shared task + GitHub eval, not a live submission leaderboard

popularity:
  trending: false
  as_of: "2026-06-16"           # 在临床-NLP 圈内有名,不在通用 LLM-leaderboard 话语里

methodology:
  evaluation: [automated, human]
  contamination_controls: "测试集仅在挑战赛时释出;取自真实/策展的医患对话。"
  notes: "三个任务:A——句段级 Dialogue2Note 摘要 + 章节标题分类(MTS-Dialog,1.7k 对话);B——整篇临床病历摘要(ACI-Bench);C——Note2Dialogue 生成(ACI-Bench)。17 支队伍。由 ROUGE、BERTScore、BLEURT 的集成打分,并用 Pearson 相关校验对齐人工评分。"

citations:
  - { title: "Overview of the MEDIQA-Chat 2023 Shared Tasks on the Summarization & Generation of Doctor-Patient Conversations (ACL ClinicalNLP 2023)", url: "https://aclanthology.org/2023.clinicalnlp-1.52/", accessed: "2026-06-16" }
  - { title: "MEDIQA-Chat-2023 (organizer GitHub: data, baselines, eval)", url: "https://github.com/abachaa/MEDIQA-Chat-2023", accessed: "2026-06-16" }
  - { title: "Aci-bench: a Novel Ambient Clinical Intelligence Dataset for Benchmarking Automatic Visit Note Generation (Nature Scientific Data, 2023)", url: "https://www.nature.com/articles/s41597-023-02487-3", accessed: "2026-06-16" }

as_of: "2026-06-16"
freshness:
  status: aging
  last_checked: "2026-06-16"
  note: "2023 shared task,基线属前-前沿-LLM 时代;任务(环境式病历生成)依然当下,但 leaderboard 快照已过时。"

agent_summary:
  author: agent
  generated: "2026-06-16"

expert_verdict:
  signed_by: chenhao
  signed_date: "2026-06-16"
  confidence: low          # low / medium / high

moa:
  capability_axes: [clinical-note-generation, dialogue-summarization, ambient-scribe]
  modalities: [text]
  access: [api, open-weights]
  recommended_for:
    - "评测医患对话 → 临床病历摘要(环境式 scribe 用例)"
    - "一个具体的生成/摘要任务,补充 QA 背诵榜与行为榜"
  caveats:
    - "体裁是一次性 shared task,不是持续维护的 leaderboard——结果是 2023 年快照"
    - "ROUGE/BERTScore/BLEURT 更能反映表层重叠,而非临床事实性"
    - "在临床-NLP 圈内有名;不是 HealthBench 那种面向大众的 leaderboard"
---

## Agent summary

MEDIQA-Chat 2023 是一场公开评测竞赛(shared task),2023 年在 ACL 会议下属的 ClinicalNLP Workshop 上举办,由 Asma Ben Abacha 等人组织(来自 Microsoft / Nuance),主题是给医患对话做摘要和生成。它分三个任务。Task A 是把对话里的一段段内容压成就诊记录的对应片段(Dialogue2Note),再给片段标上章节标题,用的是 MTS-Dialog 数据集(约 1.7k 段短对话配好摘要,其中 1,201 条用于训练、100 条用于验证)。Task B 是把整段对话写成一份完整的临床病历(clinical note,即就诊记录),用的是 ACI-Bench 数据集。Task C 反过来,根据病历自动生成对话(Note2Dialogue),用来扩充训练数据。一共 17 支队伍参赛。打分用的是三种自动指标的组合:ROUGE、BERTScore、BLEURT——它们都是按机器输出和参考答案的重合程度自动算分;组织方还用 Pearson 相关系数检验这些自动分和人工打分是否一致。

它瞄准的是"环境式记录助手"(ambient scribe)这类用法,也就是医生看诊时,系统在旁边把对话直接转成结构化的就诊记录。这是一个生成类任务,正好补上本集合里其它几份偏选择题背诵或行为测试的榜单。它也有几个短板:这是一次性的 2023 年比赛,当时的基线模型还在顶级大模型出现之前;而且按重合度算分的指标,对病历是否在临床上写对了事实,反映得并不够。

<!-- 仅事实;来源为 ACL Anthology 概述、组织者 GitHub 与 ACI-Bench 论文。 -->

## Expert verdict

人工署名(chenhao)。值得回答:一个 2023 shared-task 快照如今该算几分? 我认为很低
MTS-Dialog/ACI-Bench 是否仍是环境式 scribe 的参考,还是已被超越? 如果只是评测结构化病历能力，我认为还是可以参考的；就看榜单是否还更新了。
