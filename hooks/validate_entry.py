#!/usr/bin/env python3
"""PostToolUse validator: any entries/*.md the agent writes must satisfy
schema/entry.schema.json.

Fires after Write/Edit. On a schema violation it exits 2 so the error text is
fed back to the agent to self-correct. Unsigned drafts (no expert_verdict) pass
— that block is optional by design (staged sign-off); a separate publish/render
gate is what should require it.

Degrades gracefully if pyyaml / jsonschema are absent (warn, do not block).
"""
import json
import os
import re
import sys

ENTRIES_DIR = "entries"


def note(msg):
    print(f"[validate_entry] {msg}", file=sys.stderr)


def is_entry(path):
    if not path:
        return False
    norm = os.path.normpath(path).replace("\\", "/")
    base = os.path.basename(norm)
    return (
        f"/{ENTRIES_DIR}/" in f"/{norm}"
        and base.endswith(".md")
        and not base.startswith("_")
    )


def schema_path(entry_path):
    # schema/ sits next to entries/ at the project root.
    root = os.path.dirname(os.path.dirname(os.path.abspath(entry_path)))
    return os.path.join(root, "schema", "entry.schema.json")


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception as e:
        note(f"unreadable stdin: {e}")
        sys.exit(0)

    ti = payload.get("tool_input", {}) or {}
    path = ti.get("file_path", "")
    if not is_entry(path) or not os.path.exists(path):
        sys.exit(0)

    try:
        import yaml
        from jsonschema import Draft202012Validator
    except ImportError as e:
        note(f"skipping validation (missing dep: {e}); install pyyaml jsonschema")
        sys.exit(0)

    text = open(path, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    if not m:
        note(f"{os.path.basename(path)}: no YAML frontmatter found")
        sys.exit(2)

    try:
        data = yaml.safe_load(m.group(1))
    except Exception as e:
        note(f"{os.path.basename(path)}: frontmatter is not valid YAML: {e}")
        sys.exit(2)

    try:
        schema = json.load(open(schema_path(path), encoding="utf-8"))
    except Exception as e:
        note(f"cannot load schema: {e}")
        sys.exit(0)

    errs = sorted(Draft202012Validator(schema).iter_errors(data), key=lambda x: list(x.path))
    if errs:
        loc = os.path.basename(path)
        lines = [f"{loc}: {len(errs)} schema violation(s):"]
        for e in errs:
            where = ".".join(str(p) for p in e.path) or "(root)"
            lines.append(f"  - {where}: {e.message}")
        note("\n".join(lines))
        sys.exit(2)

    signed = isinstance(data.get("expert_verdict"), dict)
    note(f"{os.path.basename(path)}: valid ({'signed' if signed else 'draft, unsigned'})")
    sys.exit(0)


if __name__ == "__main__":
    main()
