#!/usr/bin/env python3
"""Publish gate — the other half of staged sign-off.

`validate_entry.py` lets unsigned drafts through (so the agent can scaffold).
This gate is stricter: an entry is *publishable* only when the human has signed
it. Run before rendering the GitHub page / in CI.

Per entry it checks, on top of schema validity:
  1. `expert_verdict` frontmatter exists and is signed (signed_by + signed_date).
  2. The `## Expert verdict` body actually contains prose (not just comments).
  3. Citations look resolvable (http/doi shape; not a deep network fetch).

It also prints a non-blocking WARN when an entry's `as_of` is older than
STALE_AS_OF_DAYS — a nudge that the verdict may have rotted, never a gate.

Usage:
  python3 bin/check_publish.py                 # all entries/*.md
  python3 bin/check_publish.py entries/x.md ... # specific files
Exit 0 = all publishable; exit 1 = at least one blocked (reasons printed).
"""
import datetime
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Verdicts rot — leaderboards update. Flag entries whose `as_of` is older than
# this many days so a stale verdict gets re-checked. A WARNING only: it never
# blocks publish (an aging verdict is still the expert's signed call), it just
# nudges a refresh. Mirrors the freshness-audit pattern in CLAUDE.md §5.
STALE_AS_OF_DAYS = 365


def load_deps():
    try:
        import yaml
        from jsonschema import Draft202012Validator
        return yaml, Draft202012Validator
    except ImportError as e:
        print(f"FATAL: missing dependency ({e}); pip install pyyaml jsonschema", file=sys.stderr)
        sys.exit(2)


def verdict_body(text):
    m = re.search(r"^## Expert verdict\s*\n(.*?)(?=^## |\Z)", text, re.S | re.M)
    if not m:
        return ""
    body = re.sub(r"<!--.*?-->", "", m.group(1), flags=re.S)
    return re.sub(r"\s+", " ", body).strip()


def load_frontmatter(text, yaml):
    """Parse the YAML frontmatter. Returns (data, error). data is None on error."""
    fm = re.match(r"^---\n(.*?)\n---", text, re.S)
    if not fm:
        return None, "no YAML frontmatter"
    try:
        return yaml.safe_load(fm.group(1)), None
    except Exception as e:
        return None, f"frontmatter not valid YAML: {e}"


def staleness_warning(data, today=None):
    """Return a WARN string if `as_of` is older than STALE_AS_OF_DAYS, else None.

    Non-blocking: a signed verdict stays publishable even when aging — this only
    flags that the underlying leaderboard may have moved since the expert looked.
    """
    raw = data.get("as_of")
    if not raw:
        return None
    try:
        as_of = datetime.date.fromisoformat(str(raw).strip())
    except ValueError:
        return None  # schema check already flags malformed dates
    today = today or datetime.date.today()
    age = (today - as_of).days
    if age > STALE_AS_OF_DAYS:
        return f"as_of {as_of.isoformat()} is {age} days old (> {STALE_AS_OF_DAYS}); re-check the leaderboard and refresh the verdict"
    return None


def check_entry(path, schema, yaml, Validator, schema_only=False):
    """Return list of problems ([] = publishable).

    schema_only=True keeps only schema/parse problems (ignores signature, verdict
    body, citation checks) — the hard CI gate. A draft that is schema-valid but
    unsigned passes schema_only and is simply not rendered by render_site.py.
    """
    problems = []
    text = open(path, encoding="utf-8").read()
    data, err_msg = load_frontmatter(text, yaml)
    if data is None:
        return [err_msg]

    for err in sorted(Validator(schema).iter_errors(data), key=lambda x: list(x.path)):
        where = ".".join(str(p) for p in err.path) or "(root)"
        problems.append(f"schema: {where}: {err.message}")

    if schema_only:
        return problems

    ev = data.get("expert_verdict")
    if not isinstance(ev, dict):
        problems.append("not signed: expert_verdict frontmatter block is missing")
    else:
        for field in ("signed_by", "signed_date", "confidence"):
            if not ev.get(field):
                problems.append(f"not signed: expert_verdict.{field} is empty")

    if not verdict_body(text):
        problems.append("'## Expert verdict' body has no prose (only comments/blank)")

    for i, c in enumerate(data.get("citations", []) or []):
        url = (c or {}).get("url", "")
        if not re.match(r"^https?://", url) and not (c or {}).get("doi"):
            problems.append(f"citations[{i}]: no resolvable url/doi")
    return problems


def main(argv):
    schema_only = "--schema-only" in argv
    argv = [a for a in argv if not a.startswith("--")]
    yaml, Validator = load_deps()
    schema = json.load(open(os.path.join(ROOT, "schema", "entry.schema.json")))
    targets = argv or sorted(glob.glob(os.path.join(ROOT, "entries", "*.md")))
    targets = [t for t in targets if not os.path.basename(t).startswith("_")]
    if not targets:
        print("no entries to check")
        return 0

    bad_label = "INVALID" if schema_only else "BLOCKED"
    ok_word = "schema-valid" if schema_only else "publishable"
    blocked = 0
    warned = 0
    for path in targets:
        rel = os.path.relpath(path, ROOT)
        problems = check_entry(path, schema, yaml, Validator, schema_only=schema_only)
        if problems:
            blocked += 1
            print(f"{bad_label}  {rel}")
            for p in problems:
                print(f"    - {p}")
        else:
            print(f"OK       {rel}")
        # Non-blocking staleness nudge (skipped in schema-only/CI hard-gate runs).
        if not schema_only:
            data, _ = load_frontmatter(open(path, encoding="utf-8").read(), yaml)
            warn = staleness_warning(data) if isinstance(data, dict) else None
            if warn:
                warned += 1
                print(f"    ! WARN: {warn}")
    summary = f"\n{len(targets) - blocked}/{len(targets)} {ok_word}."
    if warned:
        summary += f" ({warned} stale as_of warning(s) — non-blocking.)"
    print(summary)
    return 1 if blocked else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
