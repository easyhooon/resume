#!/usr/bin/env python3
"""Print every change in the resume Markdown as numbered AS IS / TO BE pairs, grouped by section.

The model only adds the judgment part (which feedback item each change answers).
Pairs come from difflib on the base version vs the working tree, so the list is
complete: a change that is not here was not made, and every change here must be
accounted for in the report.

Usage:
  diff_pairs.py [--base REV] [FILE ...]   default base HEAD, default files RESUME.md PORTFOLIO.md
"""
import argparse
import difflib
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]
DEFAULT_FILES = ("RESUME.md", "PORTFOLIO.md")
HEADING = re.compile(r"^(#{2,4})\s+(.*)")
SPAN = re.compile(r"<span[^>]*>.*?</span>")


def heading_text(line):
    m = HEADING.match(line)
    return SPAN.sub("", m.group(2)).strip() if m else None


def section_at(lines, idx):
    """Nearest '##' and '###' headings at or above line idx, joined as 'H2 > H3'."""
    h2 = h3 = None
    for line in lines[: idx + 1]:
        m = HEADING.match(line)
        if not m:
            continue
        if len(m.group(1)) == 2:
            h2, h3 = heading_text(line), None
        elif len(m.group(1)) == 3:
            h3 = heading_text(line)
    return " > ".join(x for x in (h2, h3) if x) or "(문서 머리)"


def old_text(rel, base):
    r = subprocess.run(["git", "-C", str(REPO), "show", f"{base}:{rel}"],
                       capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else ""


def pairs(rel, base):
    old = old_text(rel, base).splitlines()
    new = (REPO / rel).read_text(encoding="utf-8").splitlines()
    sm = difflib.SequenceMatcher(a=old, b=new, autojunk=False)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            continue
        a = [l for l in old[i1:i2] if l.strip()]
        b = [l for l in new[j1:j2] if l.strip()]
        if not a and not b:
            continue  # blank-line-only change
        sec = section_at(new, j1) if j1 < len(new) else section_at(old, i1)
        yield sec, a, b


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", default="HEAD")
    ap.add_argument("files", nargs="*")
    args = ap.parse_args()
    n = 0
    for rel in args.files or DEFAULT_FILES:
        if not (REPO / rel).exists():
            continue
        print(f"# {rel}\n")
        last = None
        for sec, a, b in pairs(rel, args.base):
            n += 1
            if sec != last:
                print(f"## {sec}\n")
                last = sec
            print(f"### C{n}")
            print("AS IS:")
            print("\n".join(a) if a else "(없음)")
            print("TO BE:")
            print("\n".join(b) if b else "(삭제)")
            print()
    print(f"총 변경 {n}건", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
