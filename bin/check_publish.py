#!/usr/bin/env python3
"""Publish gate — the other half of staged sign-off.

`validate_entry.py` lets unsigned drafts through (so the agent can scaffold).
This gate is stricter: an entry is *publishable* only when the human has signed
it. Run before rendering the GitHub page / in CI.

Per entry it checks, on top of schema validity:
  1. `expert_verdict` frontmatter exists and is signed (signed_by + signed_date).
  2. The `## Expert verdict` body actually contains prose (not just comments).
  3. Citations look resolvable (http/doi shape; not a deep network fetch).

Usage:
  python3 bin/check_publish.py                 # all entries/*.md
  python3 bin/check_publish.py entries/x.md ... # specific files
Exit 0 = all publishable; exit 1 = at least one blocked (reasons printed).
"""
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


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


def check_entry(path, schema, yaml, Validator, schema_only=False):
    """Return list of problems ([] = publishable).

    schema_only=True keeps only schema/parse problems (ignores signature, verdict
    body, citation checks) — the hard CI gate. A draft that is schema-valid but
    unsigned passes schema_only and is simply not rendered by render_site.py.
    """
    problems = []
    text = open(path, encoding="utf-8").read()
    fm = re.match(r"^---\n(.*?)\n---", text, re.S)
    if not fm:
        return ["no YAML frontmatter"]
    try:
        data = yaml.safe_load(fm.group(1))
    except Exception as e:
        return [f"frontmatter not valid YAML: {e}"]

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
    print(f"\n{len(targets) - blocked}/{len(targets)} {ok_word}.")
    return 1 if blocked else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
