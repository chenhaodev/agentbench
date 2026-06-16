# Sourcing & coverage method

> Written after a real miss: the user recalled an "ACL-Bench"; it turned out to be
> **MEDIQA-Chat 2023** (a ClinicalNLP-workshop *shared task*). It was missed because
> earlier sweeps were **targeted samples of one genre** (online leaderboards), not a
> **census across genres and sources**. This file makes coverage a checklist so whole
> categories stop slipping through. Each entry now carries a `genre` field.

## The lesson (generalized)

A keyword search for a benchmark name only works if you have the *right name* and the
benchmark *ranks well on general web search*. Neither holds for workshop shared tasks,
paper-bound benchmarks, or regional boards. So: **enumerate by genre × source, don't
fish by name.** Absence from a name-search means "not found by that query," never
"doesn't exist."

## Benchmark genres (the `genre` field)

| genre | what it is | examples in repo | where it hides |
|---|---|---|---|
| `online-leaderboard` | live submissions, updates over time | MedBench, BRIDGE, Open Medical-LLM | HF Spaces, dedicated sites |
| `shared-task` | one-off challenge + overview paper | **MEDIQA-Chat** | ACL/EMNLP/NAACL Anthology workshops, codalab |
| `paper-bound` | introduced inside a paper, no live board | RCQ, HealthBench | arXiv, journals (Nature Med), PMC |
| `aggregator` | leaderboard-of-leaderboards | Leaderboard of Leaderboards | HF (OpenEvals, MAYA-AI) |
| `dataset` | eval set, scored offline, no ranking | MedQA | HF Datasets, GitHub |

If a genre column is empty in our entry set, that is a **visible coverage gap**, not a
sign the genre is unimportant.

## Sources to sweep per genre (the census, not the sample)

- **ACL Anthology** (`aclanthology.org`) — main + **workshops** (ClinicalNLP, BioNLP, MEDIQA series). Workshop shared tasks live here and rank LOW on general web search. Search the Anthology directly.
- **arXiv / PMC / journals** — paper-bound benchmarks (RCQ ← Nature Medicine). Follow citations from survey papers.
- **HuggingFace** — Spaces (leaderboards), Datasets, and the aggregators (OpenEvals/every-leaderboards, MAYA-AI/all-leaderboard).
- **Papers with Code** (now on HF) — SOTA leaderboards by benchmark.
- **Regional / vendor ecosystems** — OpenCompass (CN), ModelScope (CN), national pilot bases. Often only surfaced via social (see below).
- **Model tech reports** — frontier-model reports (Qwen3-Omni `arXiv:2509.17765`, plus GPT/Gemini/Llama/Claude cards) list the benchmarks a lab chose to report on. High-signal *discovery* source, especially for modalities we under-sample (vision/audio/video/agent). **Caveat — selection bias:** labs report benchmarks they *win* on, so presence is partly marketing (same vendor-circularity as HealthBench). Use to *find* benchmarks; verify each independently; never copy the report's framing or scores. Derives a real signal: **cross-report citation frequency** (how many frontier reports benchmark against X) — more rigorous than HF likes or social buzz. Record it as `popularity`, not `authority`.
- **Social, as leads only** — X (launch metrics), LinkedIn (clinician posts → real papers), Reddit (self-built practical evals). Sentiment, never authority — see `CLAUDE.md` integrity rules.

## Known gaps to backfill (living list)
- ~~`aggregator` genre has no entry~~ — done (Leaderboard of Leaderboards).
- ~~`dataset` genre has no entry~~ — done (MedQA).
- ~~Backfill `genre` on pre-`genre` entries~~ — done (all entries tagged).
- MEDIQA **series beyond 2023** (other years / sibling shared tasks) not surveyed.
- Non-medical anchors deferred: EQ-Bench, LMArena, MTEB, Open LLM Leaderboard.
- All 5 genres now have ≥1 entry, but coverage is still **thin** (medical-skewed); breadth per domain is the next push.

> Rule of thumb before claiming "that's everything": can you name at least one entry in
> **each** `genre` for the domain? If not, you sampled — keep sweeping.
