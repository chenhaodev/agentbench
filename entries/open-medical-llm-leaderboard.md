---
id: open-medical-llm-leaderboard
name: Open Medical-LLM Leaderboard
aliases: [openlifescienceai medical leaderboard]
homepage: https://huggingface.co/spaces/openlifescienceai/open_medical_llm_leaderboard
year: 2024
domain: [medical, medical-QA]
genre: online-leaderboard

authority:
  maintainers: [Open Life Science AI, Hugging Face]
  institution_count: 0
  update_cadence: irregular      # community submissions
  online: true

popularity:
  hf_space: https://huggingface.co/spaces/openlifescienceai/open_medical_llm_leaderboard
  as_of: "2026-06-16"

methodology:
  evaluation: [automated]
  contamination_controls: "在公开医疗-QA 数据集上的标准化评测框架;继承这些数据集的污染风险。"
  notes: "聚合医疗问答数据集(如 MedQA/USMLE、PubMedQA、MedMCQA、MMLU 的医疗子集);按准确率打分;开放社区模型提交。可按类型、精度、规模筛选。"

citations:
  - { title: "The Open Medical-LLM Leaderboard: Benchmarking Large Language Models in Healthcare (HF blog)", url: "https://huggingface.co/blog/leaderboard-medicalllm", accessed: "2026-06-16" }
  - { title: "Open Medical-LLM Leaderboard (HuggingFace Space)", url: "https://huggingface.co/spaces/openlifescienceai/open_medical_llm_leaderboard", accessed: "2026-06-16" }

as_of: "2026-06-16"
freshness:
  status: aging
  last_checked: "2026-06-16"
  note: "QA 背诵类任务(MultiMedQA 式)已被前沿模型大幅饱和;区分力正在消退。"

agent_summary:
  author: agent
  generated: "2026-06-16"

expert_verdict:
  signed_by: chenhao
  signed_date: "2026-06-16"
  confidence: low          # low / medium / high

moa:
  capability_axes: [medical-knowledge-QA]
  modalities: [text]
  access: [open-weights]
  recommended_for:
    - "在深入评测前,对开源模型做一次快速的医疗知识筛查"
    - "对比小型/量化的开源模型——此时考试-QA 仍有区分度"
  caveats:
    - "以选择题知识背诵为主——对真实临床行为或安全信号很弱"
    - "MultiMedQA 式任务正在饱和;顶部得分扎堆贴近天花板"
---

## Agent summary

Open Medical-LLM Leaderboard 是一个排行榜,由 Open Life Science AI 和 Hugging Face(一个公开托管 AI 模型的平台)在 2024 年做出来,挂在 HuggingFace Space 上(就是 Hugging Face 上的一个在线小应用页面)。它的做法是拿几套医学考卷来考各家模型,再按答对率排名:这些考卷包括 MedQA(题目仿照美国执业医师资格考试 USMLE)、PubMedQA、MedMCQA,以及 MMLU 里的医学子集。任何人都可以把自己的模型提交上来,页面还能按模型类型、精度、规模来筛选。想给那些权重公开、可以自己部署的(open-weights)医学模型做一次初筛,这是最方便的入口。

它的短板是结构性的。这些考卷大多是选择题(MCQ),考的是知识背诵,属于所谓的 MultiMedQA 这一类。如今顶尖模型基本都答得上来,所以这个榜已经饱和(saturated),也就是高分模型扎堆挤在天花板附近、分不出高下,对模型在真实临床里怎么表现、安不安全、会不会好好沟通,几乎说明不了什么。建议把它当成一个快速判断知识下限的工具,而不是决定要不要部署某个模型的依据。

<!-- 仅事实;来源为 HF 博客与 Space。 -->

## Expert verdict

人工署名(chenhao)。值得回答: 
既然已饱和,这个榜还值得引用吗——作为下限、作为负向过滤, 还是干脆不用? 我认为可以作为下限、若后续更新太慢则可不用。
