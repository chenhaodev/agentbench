---
name: agentbench
description: >-
  Survey and subjectively evaluate AI benchmarks/leaderboards into a
  human-in-the-loop knowledge base. Research a benchmark from primary sources,
  draft a FACTUAL summary, and prepare it for the expert's signed verdict — the
  agent never writes the verdict. Use when the user wants to add/review a
  benchmark or leaderboard entry, judge whether a benchmark is trustworthy for
  MoA (Mixture-of-Agents) model selection, compare leaderboards, or render/deploy
  the AgentBench site. Triggers: "add a benchmark", "evaluate this leaderboard",
  "is <benchmark> trustworthy", "agentbench".
---

# AgentBench — subjective leaderboard review

This skill turns a benchmark/leaderboard into a curated entry that ends in a
**human expert's verdict**. Objective aggregators answer *"who's on the board"*;
AgentBench answers *"should you trust this board, and what does a high score buy."*

## THE GOLDEN RULE (never violate)

**The agent writes facts; only the human expert writes the verdict.**
- `## Agent summary` (+ `notes`/`caveats`/`recommended_for`): agent-authored, factual, sourced.
- `## Expert verdict` + the `expert_verdict` frontmatter: **human-signed only**. Never write, draft, or sign it on the user's behalf. A `PreToolUse` hook (`hooks/guard_verdict.py`) will block you if you try.

Keep the three signals separate, always: **popularity** (buzz — can be faked/vendor-driven) ≠ **authority** (citations, institutions, physicians) ≠ **capability** (`models_ranked`). Likes are never quality.

## Workflow

### 1. Discover (census, not name-search)
A keyword search only finds what you can name and what ranks well — it misses workshop shared tasks, paper-bound and regional benchmarks. Enumerate by **genre × source** per `docs/SOURCING.md`. "Not found by my query" ≠ "doesn't exist". Good sources: ACL Anthology (workshops!), arXiv/PMC/journals, HuggingFace Spaces/Datasets + aggregators, model **tech reports** (high-signal but vendor-biased — treat as discovery, verify each).

### 2. Draft an entry — `entries/<id>.md`
- Copy `entries/_TEMPLATE.md`. Fill the frontmatter against `schema/entry.schema.json`.
- **Verify before you write.** No benchmark, score, citation, or institution from memory. Every `citations[].url` must resolve (use WebFetch/web search to confirm); add `accessed` dates. If you can't verify it, say so and ask.
- Write `## Agent summary` in **Chinese** (keep technical terms English: HealthBench, Elo, MoA, ROUGE…). Leave `## Expert verdict` as an HTML comment with 2–3 sharp questions for the expert.
- Tag `genre` (online-leaderboard | shared-task | paper-bound | aggregator | dataset). Fill `moa` (capability_axes, modalities, access, recommended_for, caveats) so the entry is MoA-actionable.
- **Language:** prose Chinese; field names, enum values (`genre`/`confidence`/`evaluation`/`access`/`status`/`license`/`modalities`), and identifiers (`id`, `capability_axes`) stay English (the schema validates them).

### 3. Validate
`python3 bin/check_publish.py --schema-only entries/<id>.md` → must be schema-valid. (The `PostToolUse` hook `hooks/validate_entry.py` also validates on every write.)

### 4. Hand to the expert
Tell the user to edit the file in their own editor (not a tool call — the guard hook won't block them) and:
- add the `expert_verdict` block (`signed_by`, `signed_date` quoted, `confidence` ∈ {low,medium,high}, optional `one_liner`);
- replace the `## Expert verdict` comment with their prose, **outside** the `<!-- -->`.
Then `python3 bin/check_publish.py entries/<id>.md` should flip to `OK`.

### 5. Render / deploy
- `python3 bin/render_site.py` → builds `site/` from **publishable (signed)** entries only.
- Push to GitHub; `.github/workflows/pages.yml` runs the schema gate → render → deploys to Pages. Unsigned drafts never reach the page.

## Scripts & resources (in this repo)
- `schema/entry.schema.json` — the entry contract. `entries/_TEMPLATE.md` — copy to start.
- `bin/check_publish.py` — publish gate (`--schema-only` for the CI/hard gate). `bin/render_site.py` — static site.
- `bin/coverage_report.py` — coverage/de-bias census (genre distribution, medical-skew, year spread; `--strict` to gate). `make coverage`.
- `Makefile` — discoverable task entry (`make help`): `check` / `check-schema` / `coverage` / `render` / `serve`.
- `hooks/guard_verdict.py` (protect the verdict) + `hooks/validate_entry.py` (schema on write), wired in `.claude/settings.json`.
- `docs/SOURCING.md` — discovery method & coverage map. `CLAUDE.md` — full conventions, integrity rules, decisions.

## Install
This repo *is* the skill. To make it invocable: symlink it into your skills dir —
`ln -s "$PWD" ~/.claude/skills/agentbench` — or publish it (SKILL.md format is the
open standard used by skill.sh / agentskill.sh). The `description` above is what an
agent matches on, so keep it specific.
