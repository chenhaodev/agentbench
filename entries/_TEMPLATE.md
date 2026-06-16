---
# Validated against ../schema/entry.schema.json. Copy this file to <id>.md and fill in.
id: example-bench
name: Example Bench
aliases: []
homepage: https://example.org/leaderboard
year: 2024
domain: [domain-area]

authority:
  maintainers: [Org A, Org B]
  institution_count: 18
  update_cadence: monthly        # live|monthly|quarterly|yearly|irregular|frozen|unknown
  citation_count:
    value: 0
    source: Google Scholar
    as_of: "2026-06-16"
  online: true

methodology:
  evaluation: [human, double-blind]   # automated|human|blind|double-blind|llm-judge|elo|pairwise
  contamination_controls: "How it resists train-set leakage, or omit."
  notes: ""

models_ranked:
  - { model: Model-X, rank: 1, axis: reasoning, license: open-weights, note: "frontier on axis Y/Z" }

citations:
  - { title: "Paper / leaderboard ref", url: "https://example.org/paper", accessed: "2026-06-16" }

as_of: "2026-06-16"
freshness:
  status: fresh                   # fresh|aging|stale
  last_checked: "2026-06-16"
  note: ""

agent_summary:
  author: agent                   # always 'agent'
  generated: "2026-06-16"

expert_verdict:
  signed_by: chenhao              # the human in the loop
  signed_date: "2026-06-16"
  confidence: medium              # low|medium|high
  one_liner: "Tweet-length verdict for listing views."

moa:
  capability_axes: [axis-1, axis-2]
  modalities: [text]
  access: [api, open-weights]
  recommended_for: ["use case where this board's signal is decision-grade"]
  caveats: ["what this board does NOT tell you"]

tags: []
---

## Agent summary

<!-- 用中文写(术语保留英文:HealthBench/Elo/MoA…)。Agent-authored, FACTUAL only.
     这个榜是什么、谁在做、怎么评分、现在谁领先。只写事实,不写观点;绝不冒充专家判语。 -->

## Expert verdict

<!-- 用中文写,且必须在 <!-- --> 之外(注释会被发布门禁当成"未写")。Human-signed (chenhao).
     主观判断:这个榜的信号可信吗?高分到底买到了什么?会不会据此在 MoA 里选它的冠军模型,为什么?
     这是全仓的核心,只有签字人能写。 -->

