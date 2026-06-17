#!/usr/bin/env python3
"""Coverage / de-bias census — the "routine checkup" half of the census principle.

CLAUDE.md §working-principle-2 ("coverage is a census across genres, not a
name-search") and docs/SOURCING.md ask for whole-category gaps to be *visible*.
A keyword sweep silently misses shared-task / paper-bound / regional benchmarks;
this report makes the shape of the collection legible so a human can spot what's
thin BEFORE it becomes a blind spot.

It reports, across all entries/*.md (drafts included — coverage is about what
exists, not what's signed):
  1. `genre` distribution, flagging genres below MIN_PER_GENRE as thin.
  2. Domain skew: medical vs non-medical share (the repo's running "去医疗偏斜"
     metric) — flags if medical share exceeds MAX_MEDICAL_SHARE.
  3. `year` spread (is the survey stuck in one vintage?).
  4. Signed vs draft counts (publish backlog, informational).

By default it is INFORMATIONAL and exits 0 — a checkup, never a gate. Pass
--strict to exit 1 when a thin genre or medical over-skew is detected, so it can
double as an optional CI nag without ever blocking the schema-only publish gate.

Usage:
  python3 bin/coverage_report.py            # census of all entries
  python3 bin/coverage_report.py --strict   # exit 1 if thin genre / over-skew
"""
import glob
import os
import re
import sys
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# A genre with fewer than this many entries is "thin" — a whole category we can
# name but have barely covered (the exact failure mode the census guards against).
MIN_PER_GENRE = 2
# This survey deliberately fights medical skew (it began medical-heavy). Flag if
# medical entries exceed this share of the collection.
MAX_MEDICAL_SHARE = 0.5
# All known genres from schema/entry.schema.json — listed so a genre with ZERO
# entries still shows up as a gap (a Counter alone can't report what's absent).
KNOWN_GENRES = ["online-leaderboard", "shared-task", "paper-bound", "aggregator", "dataset"]


def load_yaml():
    try:
        import yaml
        return yaml
    except ImportError as e:
        print(f"FATAL: missing dependency ({e}); pip install pyyaml", file=sys.stderr)
        sys.exit(2)


def load_frontmatter(text, yaml):
    fm = re.match(r"^---\n(.*?)\n---", text, re.S)
    if not fm:
        return None
    try:
        data = yaml.safe_load(fm.group(1))
        return data if isinstance(data, dict) else None
    except Exception:
        return None


def is_medical(domain):
    """Medical iff 'medical' appears in the domain list (case-insensitive)."""
    return any(str(d).strip().lower() == "medical" for d in (domain or []))


def collect(paths, yaml):
    """Return list of per-entry dicts: {id, genre, medical, year, signed}."""
    rows = []
    for path in paths:
        data = load_frontmatter(open(path, encoding="utf-8").read(), yaml)
        if data is None:
            continue
        ev = data.get("expert_verdict")
        rows.append({
            "id": data.get("id") or os.path.basename(path),
            "genre": data.get("genre") or "(missing)",
            "medical": is_medical(data.get("domain")),
            "year": data.get("year"),
            "signed": isinstance(ev, dict) and bool(ev.get("signed_by")),
        })
    return rows


def bar(n, total, width=24):
    filled = int(round(width * n / total)) if total else 0
    return "█" * filled + "·" * (width - filled)


def report(rows):
    """Print the census. Return list of warning strings ([] = healthy)."""
    warnings = []
    total = len(rows)
    if not total:
        print("no entries to report")
        return warnings

    print(f"AgentBench coverage census — {total} entries\n")

    # 1. Genre distribution (including known genres with zero entries).
    print("Genre distribution")
    counts = Counter(r["genre"] for r in rows)
    genres = list(dict.fromkeys(KNOWN_GENRES + sorted(counts)))
    for g in genres:
        n = counts.get(g, 0)
        flag = "  ⚠ THIN" if n < MIN_PER_GENRE else ""
        print(f"  {g:<20} {n:>3}  {bar(n, total)}{flag}")
        if n < MIN_PER_GENRE:
            warnings.append(f"thin genre '{g}': {n} entr{'y' if n == 1 else 'ies'} (< {MIN_PER_GENRE})")

    # 2. Medical vs non-medical skew.
    med = sum(1 for r in rows if r["medical"])
    non = total - med
    share = med / total
    print("\nDomain skew (de-medical-skew metric)")
    print(f"  medical              {med:>3}  {bar(med, total)}")
    print(f"  non-medical          {non:>3}  {bar(non, total)}")
    print(f"  medical share = {share:.0%} (target ≤ {MAX_MEDICAL_SHARE:.0%}); non-medical {non}/{total}")
    if share > MAX_MEDICAL_SHARE:
        warnings.append(f"medical skew: {share:.0%} medical (> {MAX_MEDICAL_SHARE:.0%})")

    # 3. Year spread.
    print("\nYear spread")
    years = Counter(str(r["year"]) for r in rows if r["year"])
    for y in sorted(years):
        print(f"  {y:<20} {years[y]:>3}  {bar(years[y], total)}")

    # 4. Signed vs draft (informational publish backlog).
    signed = sum(1 for r in rows if r["signed"])
    print("\nSign-off status")
    print(f"  signed (published)   {signed:>3}  {bar(signed, total)}")
    print(f"  draft (awaiting)     {total - signed:>3}  {bar(total - signed, total)}")

    return warnings


def main(argv):
    strict = "--strict" in argv
    yaml = load_yaml()
    paths = sorted(glob.glob(os.path.join(ROOT, "entries", "*.md")))
    paths = [p for p in paths if not os.path.basename(p).startswith("_")]
    rows = collect(paths, yaml)
    warnings = report(rows)
    if warnings:
        print("\nCoverage warnings (census gaps to consider — not a publish gate):")
        for w in warnings:
            print(f"  ⚠ {w}")
    else:
        print("\nNo coverage warnings.")
    return 1 if (strict and warnings) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
