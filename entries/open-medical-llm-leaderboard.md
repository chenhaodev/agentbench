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

Open Medical-LLM Leaderboard(Open Life Science AI × Hugging Face,2024)是一个 HuggingFace
Space,在一套**医疗问答数据集**上给模型排名——MedQA(USMLE 式)、PubMedQA、MedMCQA,以及 MMLU 的
医疗子集等——按准确率打分,开放社区提交,并可按模型类型、精度、规模筛选。它是筛查**开源**医疗模型
最便捷的入口。它的局限是结构性的:底层任务多为**选择题知识背诵**(MultiMedQA 家族),前沿模型
**已大体掌握**,因此该榜正在**饱和**,对真实临床行为、安全或沟通几乎不说明问题。最好把它当作一个
快速的知识下限,而非部署信号。

<!-- 仅事实;来源为 HF 博客与 Space。 -->

## Expert verdict

<!-- 人工署名(chenhao)。值得回答:既然已饱和,这个榜还值得引用吗——作为下限、作为负向过滤,还是
     干脆不用?开源覆盖在哪些方面仍提供闭源榜没有的信号? -->
