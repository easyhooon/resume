#!/usr/bin/env python3
"""Flag wording that AGENTS.md bans, in lines added since the last commit.

Only added lines are checked (git diff against HEAD), so wording the user
already committed is never flagged. Every rule mirrors a rule in AGENTS.md;
change both together.

Usage:
  lint_resume.py [FILE ...]   check files (default: the three resume Markdown files)
  lint_resume.py --hook       read a Claude Code PostToolUse payload from stdin

Exit codes: 0 clean, 1 violations (CLI), 2 violations (hook: stderr goes back to Claude).
"""
import json
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]
TARGETS = ("RESUME.md", "PORTFOLIO.md", "RESUME_PRODUCT_ENGINEER.md")

# (name, pattern, what to do instead)
RULES = [
    ("속도 강조",
     re.compile(r"\d+\s*(일|주|개월)\s*(만에|간|동안)|열흘|단기간|하루 만에"),
     "기간·속도 대신 검증 과정과 결과 수치로 쓴다"),
    ("연속 소개 프레이밍",
     re.compile(r"\d+\s*주\s*연속"),
     "서로 다른 결과물을 하나의 연속 성과처럼 묶지 않는다. '각각 #747·#748'처럼 쓴다"),
    ("원문자 번호",
     re.compile(r"[①-⑳]"),
     "①②③ 대신 평범한 라벨(예: 'A-A 검증')을 쓴다"),
    ("추상적 결과 서술",
     re.compile(r"쉬워짐|쉬워졌|용이해|수월해|가능해짐|할 수 있게 됨|있게 됐|향상됨"),
     "무엇을 실제로 하게 됐는지 행동이나 수치로 쓴다"),
    ("따옴표 개념어",
     re.compile(r"[\"“][^\"”]{2,40}[\"”]\s*(이라는|라는)"),
     "따옴표로 만든 개념어 대신 구체적인 사실을 쓴다"),
    ("긴 대시",
     re.compile(r"[—―]"),
     "긴 대시 대신 쉼표·마침표·괄호로 문장을 잇는다"),
    ("메타 설명",
     re.compile(r"감으로 판단하지|검증 가능한 형태"),
     "글쓴이의 의도 설명을 빼고 사실만 남긴다"),
]
MAX_BOLD_PER_LINE = 2


def added_lines(path: Path):
    """(line number, text) for each line added relative to HEAD."""
    rel = path.relative_to(REPO)
    tracked = subprocess.run(["git", "-C", str(REPO), "ls-files", "--error-unmatch", str(rel)],
                             capture_output=True).returncode == 0
    if not tracked:
        return list(enumerate(path.read_text(encoding="utf-8").splitlines(), 1))
    diff = subprocess.run(["git", "-C", str(REPO), "diff", "-U0", "HEAD", "--", str(rel)],
                          capture_output=True, text=True).stdout
    out, lineno = [], 0
    for line in diff.splitlines():
        m = re.match(r"@@ -\d+(?:,\d+)? \+(\d+)(?:,\d+)? @@", line)
        if m:
            lineno = int(m.group(1))
        elif line.startswith("+") and not line.startswith("+++"):
            out.append((lineno, line[1:]))
            lineno += 1
    return out


def check(path: Path):
    problems = []
    for lineno, text in added_lines(path):
        for name, pattern, fix in RULES:
            m = pattern.search(text)
            if m:
                problems.append(f"{path.name}:{lineno} [{name}] '{m.group(0)}' → {fix}")
        # The portfolio opens bullets with a bold label ("- **결과**:"); that is layout, not emphasis.
        body = re.sub(r"^\s*[-*]\s+\*\*[^*]{1,20}\*\*\s*:", "", text)
        bold = body.count("**") // 2 + body.count("<strong>")
        if bold > MAX_BOLD_PER_LINE and not text.lstrip().startswith("|"):
            problems.append(f"{path.name}:{lineno} [굵게 과다] 한 줄에 {bold}개 → 핵심 수치에만, 줄당 {MAX_BOLD_PER_LINE}개 이하")
    return problems


def main():
    if "--hook" in sys.argv:
        try:
            payload = json.load(sys.stdin)
        except json.JSONDecodeError:
            return 0
        fp = (payload.get("tool_input") or {}).get("file_path") or ""
        if Path(fp).name not in TARGETS:
            return 0
        problems = check(Path(fp).resolve())
        if problems:
            print("AGENTS.md 작성 규칙 위반 (새로 추가한 줄):\n" + "\n".join(problems), file=sys.stderr)
            return 2
        return 0

    files = [Path(a).resolve() for a in sys.argv[1:]] or [REPO / t for t in TARGETS]
    problems = [p for f in files if f.exists() for p in check(f)]
    for p in problems:
        print(p)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
