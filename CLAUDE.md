# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Current state: schema-first, no app code yet

This repo currently contains `TASK.md` (the brief, Chinese), this file, and the **data layer** (`schema/`, `entries/`). There is **no build system, no custom CLI, no tests, no `README.md` yet**. Do not assume commands exist. The deliverable is being built **data-first**: the entry schema is the contract; rendering and any tooling come later and stay thin.

When you add a static-site renderer or CI, update this file with the real commands at that point.

## Decided architecture (reviewed 2026-06-16)

**CLI/docs-as-data over TUI, packaged as a Skill.** A Skill's interface is the agent conversation, so a TUI the agent can't drive is the wrong primary layer. Recommendation survived an adversarial review with these binding amendments:

- **(a) No custom CLI in v1.** This repo only renders curated text (unlike `med-agent-verifier`, which runs evals and *needs* scripts). Lead with an off-the-shelf static-site generator (MkDocs Material / Astro) + JSON-Schema validation in CI. Add a CLI only when a concrete need appears.
- **(b) The schema is the real deliverable.** See `schema/entry.schema.json`. It enforces the integrity-critical boundaries below.
- **(c) TUI is a deferred *view* over the schema**, not a discarded option. If high-volume comparative review of entries becomes the primary human workflow, a lightweight Textual/Bubble Tea view over the same data files is reasonable — design nothing that blocks it.

### Enforcement hooks (`hooks/`, wired in `.claude/settings.json`)
The integrity rules are mechanically enforced — they don't depend on the agent behaving:
- **`guard_verdict.py`** (PreToolUse, Write/Edit) — **blocks the agent** from authoring or altering the `## Expert verdict` prose of any `entries/*.md`. It compares the verdict section before/after the proposed change; only real prose changes are blocked (empty/comment-only scaffolding is fine). Because hooks fire only on tool calls, **the expert editing a verdict in their own editor is never blocked** — that is the intended path for chenhao to sign off.
- **`validate_entry.py`** (PostToolUse, Write/Edit) — validates any written `entries/*.md` against `schema/entry.schema.json` and feeds violations back to the agent. **Unsigned drafts pass** (staged sign-off): `expert_verdict` is optional in the schema, so the agent can scaffold a draft; a later publish/render step is what should require the signature.
- Both **fail open** on internal errors (warn, don't wedge the workflow) and ignore non-entry files and `_`-prefixed scaffolding. Deps: `pyyaml`, `jsonschema` (validator degrades gracefully if absent).
- **`bin/check_publish.py`** (run in CI / before rendering, not a hook) — the **publish gate**. Stricter than the draft validator: an entry is publishable only when the expert has signed it (`expert_verdict` block with `signed_by`/`signed_date`/`confidence`, real prose under `## Expert verdict`, resolvable citations). Exit 1 if any entry is unsigned. This is the "block publish, not commit" half: drafts commit freely; only signed entries reach the GitHub page. Run: `python3 bin/check_publish.py [entries/x.md ...]`.

### Integrity rules the schema enforces (do not relax)
- **Human vs agent authorship is separated.** `expert_verdict` is **human-signed** (the repo owner, chenhao, is "the expert / people in the loop") with `signed_by` + `signed_date`. `agent_summary` is agent-authored, factual, and must never be presented as the expert opinion. Never write into `expert_verdict` on the user's behalf without explicit sign-off.
- **Citations must resolve.** No bare/hallucinated DOIs or URLs; citation entries carry an `accessed` date. Use the available `WebFetch` / PubMed tools to verify before adding.
- **Verdicts carry freshness.** Leaderboards update and verdicts rot. Every entry has `as_of` + a `freshness` block (mirrors the verifier's freshness-audit pattern, which *does* transfer here).
- **Entries must be MoA-actionable.** The brief's payoff is "help someone draft an MoA." Each entry carries selection-relevant fields (capability axes, modalities, access, license) — not just a reading-list blurb.

## Working principles (distilled from the expert's session feedback)

These are durable corrections chenhao (the expert / human-in-the-loop) has given. They are **guidance, not mechanically enforceable** — see "What a hook can vs cannot enforce" below for the split. Honor them like the integrity rules above.

1. **Verify before you write; never fabricate.** No benchmark, score, citation, or institution from memory. Every factual claim traces to a resolvable source; citations carry `accessed` dates. If you can't verify it, say so and ask — don't invent. (Origin: the "ACL-Bench" episode — it didn't exist under that name; the real item was MEDIQA-Chat.)
2. **Coverage is a census across genres, not a name-search.** A keyword sweep only finds things you can name that rank well on web search — it silently misses shared tasks, paper-bound, and regional benchmarks. Enumerate by `genre` × source per `docs/SOURCING.md`. "Not found by my query" ≠ "doesn't exist."
3. **Keep three signals separate, always:** `popularity` (adoption/buzz — can be faked or vendor-manufactured) ≠ `authority` (citations, institutions, physicians) ≠ capability (`models_ranked`). Likes are never quality. Watch for circularity (a vendor authoring a benchmark *and* citing it).
4. **Social platforms stratify by signal type** — use accordingly, all as *leads/sentiment* only: **X** = launch metrics + buzz (clean permalinks); **LinkedIn** = clinician/institution signal that points to *real papers* (no clean permalinks); **Reddit** = practitioner reality-check (self-built evals). None is `authority`.
5. **In medicine specifically, popularity is a weak signal.** Authority = physician/clinician involvement + backing institution + citations + clinical realism (real text/dialogue > saturated MCQ recall).
6. **Outward-facing safety:** never store the user's cookies/credentials; keep third-party-site automation light and read-only; stop at any login/security wall rather than working around it.

## What a hook can vs cannot enforce (answer to "can my feedback live in a HOOK?")

A hook only fires on the agent's tool calls and can only check *mechanical invariants*:
- **Enforceable today** (and wired): schema validity (`validate_entry.py`), the human-vs-agent verdict boundary (`guard_verdict.py`), the publish-signature gate (`bin/check_publish.py`), resolvable-URL *shape*, presence of `as_of`/`freshness`.
- **Enforceable if we extend it**: stale-`as_of` warnings, `genre`-coverage report, live citation-resolves check (slow/flaky — kept as URL-shape only on purpose).
- **NOT hook-able — lives here as guidance**: principles 1–5 above (verify-don't-fabricate, census-not-sample, popularity≠authority, platform stratification, medical-authority metric). These require judgment; a hook can't tell a true citation from a plausible fake or buzz from authority. So: **mechanical rules → hooks; judgment → CLAUDE.md (agent) / README (readers) / global memory (cross-project).**

## What we're building (from `TASK.md`)

A **flexible, human-in-the-loop, *subjective* benchmark** — not an automated scorer. The deliverable is a curated, opinionated survey of existing AI benchmarks/leaderboards that ends in an **expert subjective evaluation** of each.

Each entry follows a recurring shape (paraphrasing the brief's examples):
- **MedBench** — a 2024 leaderboard backed by 18 authoritative institutions; model X ranks at the frontier on capabilities Y/Z; therefore the subjective verdict on X is: …
- **EQBench** — published by …; the only frequently-updated, highly-cited, multi-model online EQ leaderboard; model X is open-source and ranks high under double-blind testing; therefore the verdict is: …

The output is a **GitHub page** aimed at two audiences:
1. **Non-AI people** — to browse and learn (科普 / popular-science framing).
2. **AI people outside this domain** — to quickly sketch a **MoA (Mixture-of-Agents) architecture draft**, using the leaderboard/citation evidence as selection input.

Evidence is **subjective but grounded**: cite literature, citation counts, and expert evaluation. The point is *judgment for experts to iterate on repeatedly*, not a code pipeline that runs.

### Two open decisions to resolve early
- **TUI vs CLI** — the brief explicitly asks which. Since this is "thinking/ideas for experts to iterate," favor whichever best supports human-in-the-loop review and editing of entries. Confirm with the user before committing to one.
- **This repo must ship as a SKILL.** Before designing, search for good open-source skill tooling/inspiration (e.g. github / skill.sh). The end product should be invocable as a skill, consistent with the other skills in this `~/.claude` setup.

## Reference template: `../med-agent-verifier`

The brief says to model the README and framework template on the sibling repo `../med-agent-verifier` (i.e. `/Users/chenhao/ClaudeCode/focus/med-agent-verifier`). It is a different domain (an *objective* model-capability verifier) but its **conventions** are the pattern to reuse. Read its `CLAUDE.md`, `README.md`, and `Makefile` before designing this repo. Key conventions worth carrying over:

- **`Makefile` as the discoverable task entry point** — collapse scattered commands into self-documenting `make` targets (`make help` lists them via a `## comment` convention). Use this instead of leaving commands only in prose.
- **README written for a non-expert first** — note its top sections: "一分钟看懂（无需医学或算法背景）" then "核心概念（先读这 7 个词）". The layered, jargon-light, audience-first structure matches this repo's "科普 for non-AI people" goal.
- **`CLAUDE.md` ingests task briefs verbatim, then the standalone `TASK.md` is removed.** When `TASK.md`'s intent has been fully captured here, fold it in and delete `TASK.md` (the verifier did exactly this — see its "Original task briefs … ingested verbatim then removed" section).
- **Orientation toward MoA routing** — the verifier's pipeline ends in a `routing_manifest.yaml` that drives offline MoA model selection. This repo's subjective leaderboard serves the same downstream purpose (helping someone draft an MoA), so keep entries structured enough to feed that decision.
- **Bilingual content is expected** — briefs and user-facing docs are Chinese; code/identifiers are English.

### Entry language convention (per the expert's request)
Entry **prose is Chinese** (keep technical terms in English: HealthBench, Elo, MoA, ROUGE…); **structured/enum fields stay English** because the schema validates them.
- **中文 (free text):** `## Agent summary` body, `## Expert verdict` body, and the free-text frontmatter fields `notes`, `caveats`, `recommended_for`, `one_liner`, `freshness.note`, `contamination_controls`.
- **English (machine keys — do NOT translate, validation depends on it):** all field *names*; enum *values* (`genre`, `confidence`, `methodology.evaluation`, `moa.access`, `freshness.status`, `license`, `modalities`); identifiers (`id`, `capability_axes` tokens, `platform`).
The expert writes the verdict in Chinese; the agent should write `agent_summary` in Chinese too for the 科普 audience.

## Sibling repos for context

Many `med-agent-*` sibling repos exist under `/Users/chenhao/ClaudeCode/focus/` (e.g. `med-agent-verifier`, `med-agent-internists`, `med-agent-os-core`). They share conventions and are useful precedent when shaping this repo, but this benchmark is a survey/evaluation artifact, not another agent.
