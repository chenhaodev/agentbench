#!/usr/bin/env python3
"""PreToolUse guard: the agent may not author or alter the human-signed
'## Expert verdict' section of an entry.

Fires on Write/Edit. Computes the entry text *after* the proposed change and
compares the normalized '## Expert verdict' section before vs after. If the
agent would introduce or change real prose there, the call is blocked (exit 2)
with guidance. Edits the agent makes elsewhere in the file are untouched.

Rationale: only tool calls trigger hooks, so the human editing a verdict in
their own editor never trips this. The agent stays factual ('## Agent summary');
the expert (chenhao) owns the verdict. See CLAUDE.md 'Integrity rules'.
"""
import json
import os
import re
import sys

ENTRIES_DIR = "entries"
SECTION = "## Expert verdict"


def fail_open(msg):
    # Productivity guard, not an adversarial boundary: never wedge the workflow
    # on an internal error — warn and allow.
    print(f"[guard_verdict] non-fatal: {msg}", file=sys.stderr)
    sys.exit(0)


def extract_section(text):
    """Return the body of the '## Expert verdict' section (until the next
    '## ' heading or EOF), or '' if absent."""
    m = re.search(rf"^{re.escape(SECTION)}\s*\n(.*?)(?=^## |\Z)", text, re.S | re.M)
    return m.group(1) if m else ""


def normalize(section):
    """Strip HTML comments and whitespace — what's left is real authored prose."""
    section = re.sub(r"<!--.*?-->", "", section, flags=re.S)
    return re.sub(r"\s+", " ", section).strip()


def is_entry(path):
    if not path:
        return False
    norm = os.path.normpath(path).replace("\\", "/")
    base = os.path.basename(norm)
    return (
        f"/{ENTRIES_DIR}/" in f"/{norm}"
        and base.endswith(".md")
        and not base.startswith("_")  # _TEMPLATE.md etc. are scaffolding
    )


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception as e:
        fail_open(f"unreadable stdin: {e}")

    tool = payload.get("tool_name", "")
    ti = payload.get("tool_input", {}) or {}
    path = ti.get("file_path", "")
    if tool not in ("Write", "Edit") or not is_entry(path):
        sys.exit(0)

    before = ""
    if os.path.exists(path):
        try:
            before = open(path, encoding="utf-8").read()
        except Exception as e:
            fail_open(f"cannot read existing file: {e}")

    if tool == "Write":
        after = ti.get("content", "")
    else:  # Edit
        old, new = ti.get("old_string", ""), ti.get("new_string", "")
        if ti.get("replace_all"):
            after = before.replace(old, new)
        else:
            after = before.replace(old, new, 1)

    before_v = normalize(extract_section(before))
    after_v = normalize(extract_section(after))

    if after_v and after_v != before_v:
        print(
            "BLOCKED: the '## Expert verdict' section is human-signed and only "
            "the expert (chenhao) may write it. The agent must leave it empty "
            "(HTML-comment guidance only) and fill '## Agent summary' instead.\n"
            "If you ARE the expert, edit the file directly in your own editor "
            "(that is not a tool call and will not be blocked), then sign the "
            "expert_verdict frontmatter.",
            file=sys.stderr,
        )
        sys.exit(2)
    sys.exit(0)


if __name__ == "__main__":
    main()
