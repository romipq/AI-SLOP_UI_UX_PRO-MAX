#!/usr/bin/env python3
"""gen_rubric.py — refresh the signal tables in references/07-slop-score.md.

Reads weights, ids and hints straight from slop_lint.py so the documentation can
never drift from the code. Edits only the "All 90 signals" section; the prose,
grades and advice around it are left alone.

Usage:
    python3 tools/gen_rubric.py
    python3 tools/gen_rubric.py --check   # exit 1 if the doc is stale (CI)

MIT © 2026 romipq
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

import slop_lint as L  # noqa: E402

DOC = ROOT / "references" / "07-slop-score.md"
START = "## All 90 signals"
END = "\n---\n\n## How to reach 100"


def render_signals() -> str:
    chunks = []
    for key, label, cap in L.CATEGORIES:
        chunks.append(f"\n### {label.title()} — budget {cap}\n")
        chunks.append("| W | Signal | How to add it |")
        chunks.append("|---|--------|---------------|")
        for s in L.SIGNALS:
            if s["cat"] == key:
                chunks.append(f"| {s['w']} | `{s['id']}` · {s['label']} | {s['hint']} |")
    return "\n".join(chunks) + "\n"


def rebuild(text: str) -> str:
    start = text.find(START)
    end = text.find(END)
    if start == -1 or end == -1:
        raise SystemExit("error: markers not found in 07-slop-score.md")
    head = text[: start + len(START)]
    tail = text[end:]
    return head + "\n" + render_signals() + tail


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="only verify, don't write")
    args = ap.parse_args(argv)

    if not DOC.is_file():
        print(f"error: {DOC} not found", file=sys.stderr)
        return 2

    current = DOC.read_text(encoding="utf-8")
    updated = rebuild(current)

    if args.check:
        if current != updated:
            print("rubric is stale — run: python3 tools/gen_rubric.py")
            return 1
        print("rubric is up to date")
        return 0

    DOC.write_text(updated, encoding="utf-8")
    print(f"updated {DOC.relative_to(ROOT)} · {len(L.SIGNALS)} signals")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
