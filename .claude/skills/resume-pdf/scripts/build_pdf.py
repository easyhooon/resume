#!/usr/bin/env python3
"""Render resume/portfolio Markdown to A4 PDF the way GitHub shows it.

Pipeline: Markdown is embedded in an HTML page, rendered in the browser by the
vendored marked.js (GFM, raw HTML kept), styled with github-markdown-css + print
CSS, then printed by headless Chrome --print-to-pdf. Fully offline.

Why not `gh api markdown`: GitHub's renderer strips inline `style` attributes,
so the gray date spans next to headings lose their color.

Usage:
  build_pdf.py [resume|portfolio|pe|all] [--masked] [--qa DIR]

--masked  also writes the *_제출용_개인정보마스킹.pdf variant (phone/email hidden)
--qa DIR  render every page as JPEG into DIR for visual review
"""
import argparse
import html
import json
import os
import re
import subprocess
import sys
import tempfile
import time
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
REPO = SKILL_DIR.parent.parent.parent  # <repo>/.claude/skills/resume-pdf
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# key: (source, output, zoom). The portfolio has always been printed denser
# than the resume; zoom keeps that look instead of changing font sizes.
TARGETS = {
    "resume": ("RESUME.md", "output/pdf/이지훈_이력서.pdf", 1.0),
    "portfolio": ("PORTFOLIO.md", "output/pdf/이지훈_포트폴리오.pdf", 0.8),
    "pe": ("RESUME_PRODUCT_ENGINEER.md",
           "output/pdf/product-engineer/이지훈_Product_Engineer_이력서.pdf", 1.0),
}
MASKED_SUFFIX = "_제출용_개인정보마스킹"

# Only the visible text is masked; the contact table stays the same shape.
MASKS = [
    (re.compile(r"010-(\d{4})-(\d{4})"), r"010-****-\2"),
    (re.compile(r"\bmraz3068@gmail\.com\b"), "mraz****@gmail.com"),
]

PRINT_CSS = """
@page { size: A4; margin: 14mm 13mm 14mm 13mm; }
html, body { background: #fff; }
.markdown-body {
  font-family: -apple-system, BlinkMacSystemFont, "Apple SD Gothic Neo", "Segoe UI", sans-serif;
  font-size: 13px; line-height: 1.55; max-width: none; margin: 0; padding: 0;
}
.markdown-body h1 { font-size: 26px; }
.markdown-body h2 { font-size: 20px; margin-top: 20px; }
.markdown-body h3 { font-size: 16px; margin-top: 16px; }
.markdown-body h4 { font-size: 14px; }
.markdown-body h1, .markdown-body h2, .markdown-body h3, .markdown-body h4 {
  break-after: avoid; page-break-after: avoid;
}
.markdown-body li, .markdown-body tr, .markdown-body blockquote,
.markdown-body img, .markdown-body p[align] { break-inside: avoid; page-break-inside: avoid; }
.markdown-body img { max-height: 340px; object-fit: contain; }
.markdown-body a { text-decoration: none; }
/* GitHub adds anchor icons next to headings; they are noise on paper. */
.markdown-body .anchor, .markdown-body .octicon-link { display: none !important; }
"""


def run(cmd, **kw):
    return subprocess.run(cmd, check=True, capture_output=True, text=True, **kw)


BOLD = re.compile(r"\*\*(?=\S)(.+?)(?<=\S)\*\*")
CODE_SPAN = re.compile(r"(`[^`]*`)")


def cjk_bold(md_text: str) -> str:
    """Turn **x** into <strong>x</strong> before marked sees it.

    CommonMark does not close `**` when it follows punctuation and is followed
    by a letter, so `**27.6% 단축)**로` stays literal. Korean particles hit this
    constantly. Code blocks and code spans are left untouched.
    """
    out, fenced = [], False
    for line in md_text.split("\n"):
        if line.lstrip().startswith("```"):
            fenced = not fenced
        if not fenced:
            # Park code spans so `**` inside them is untouched, but bold may still wrap them.
            spans = []
            line = CODE_SPAN.sub(lambda m: spans.append(m.group(1)) or f"\x00{len(spans) - 1}\x00", line)
            line = BOLD.sub(r"<strong>\1</strong>", line)
            line = re.sub(r"\x00(\d+)\x00", lambda m: spans[int(m.group(1))], line)
        out.append(line)
    return "\n".join(out)


def build_html(md_text: str, title: str, zoom: float = 1.0) -> str:
    assets = SKILL_DIR / "assets"
    css = (assets / "github-markdown-light.css").read_text(encoding="utf-8")
    marked = (assets / "marked.min.js").read_text(encoding="utf-8")
    base = REPO.as_uri() + "/"
    # json.dumps + "</" escape keeps the Markdown safe inside <script>
    md_js = json.dumps(cjk_bold(md_text)).replace("</", "<\\/")
    return f"""<!doctype html>
<html lang="ko"><head><meta charset="utf-8">
<base href="{base}">
<title>{html.escape(title)}</title>
<style>{css}</style><style>{PRINT_CSS}</style>
<style>.markdown-body {{ zoom: {zoom}; }}</style>
<script>{marked}</script>
</head><body><article class="markdown-body" id="c"></article>
<script>document.getElementById("c").innerHTML = marked.parse({md_js}, {{gfm: true}});</script>
</body></html>"""


def pdf_complete(path: Path) -> bool:
    """True when the file is a whole PDF (poppler can read it and it ends with %%EOF)."""
    if not path.exists() or path.stat().st_size == 0:
        return False
    if b"%%EOF" not in path.read_bytes()[-1024:]:
        return False
    return subprocess.run(["pdfinfo", str(path)], capture_output=True).returncode == 0


def print_pdf(html_text: str, out_pdf: Path):
    out_pdf.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        src = Path(tmp) / "page.html"
        src.write_text(html_text, encoding="utf-8")
        draft = Path(tmp) / "out.pdf"
        cmd = [CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
               "--no-first-run", "--no-default-browser-check", "--disable-extensions",
               "--disable-sync", "--disable-component-update",
               "--allow-file-access-from-files", "--virtual-time-budget=5000",
               f"--user-data-dir={tmp}/profile", f"--print-to-pdf={draft}", src.as_uri()]
        # Headless Chrome sometimes exits 2 during teardown (crashpad watchdog) after the
        # PDF is already written, so judge success by the file, not the exit code. Printing
        # to a draft path keeps a half-written file from replacing the previous output.
        for attempt in range(5):
            draft.unlink(missing_ok=True)
            r = subprocess.run(cmd, capture_output=True, text=True)
            if pdf_complete(draft):
                draft.replace(out_pdf)
                return
            print(f"  chrome exit {r.returncode}, no complete PDF (attempt {attempt + 1}): "
                  f"{r.stderr.strip()[-300:]}", file=sys.stderr)
            time.sleep(2 * (attempt + 1))
        raise SystemExit(f"Chrome failed to print {out_pdf}")


def report(pdf: Path, qa_dir: Path | None, masked: bool):
    info = run(["pdfinfo", str(pdf)]).stdout
    pages = re.search(r"Pages:\s+(\d+)", info).group(1)
    text = run(["pdftotext", "-layout", str(pdf), "-"]).stdout
    links = len(re.findall(r"/URI", pdf.read_bytes().decode("latin-1")))
    leaked = [p for p in ("010-2010", "mraz3068@") if p in text] if masked else []
    print(f"{pdf.relative_to(REPO)}  pages={pages}  links={links}  bytes={pdf.stat().st_size}"
          + (f"  MASK-LEAK={leaked}" if leaked else ""))
    if qa_dir:
        d = qa_dir / pdf.stem
        d.mkdir(parents=True, exist_ok=True)
        run(["pdftoppm", "-r", "70", "-jpeg", str(pdf), str(d / "page")])
        print(f"  qa images: {d}")
    return not leaked


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("target", nargs="?", default="all", choices=[*TARGETS, "all"])
    ap.add_argument("--masked", action="store_true")
    ap.add_argument("--qa", type=Path)
    ap.add_argument("--skip-lint", action="store_true",
                    help="build despite AGENTS.md wording violations (only when the user asked)")
    a = ap.parse_args()

    keys = list(TARGETS) if a.target == "all" else [a.target]
    # Same check as the PostToolUse hook; this also catches edits made through Bash.
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import lint_resume
    problems = [p for k in keys for p in lint_resume.check(REPO / TARGETS[k][0])]
    if problems and not a.skip_lint:
        print("AGENTS.md 작성 규칙 위반으로 PDF를 만들지 않습니다 (새로 추가한 줄):", file=sys.stderr)
        print("\n".join(problems), file=sys.stderr)
        sys.exit(1)

    ok = True
    for key in keys:
        md_name, out_rel, zoom = TARGETS[key]
        md = (REPO / md_name).read_text(encoding="utf-8")
        title = md.splitlines()[0].lstrip("# ").strip()
        variants = [(md, REPO / out_rel, False)]
        if a.masked:
            mmd = md
            for pat, rep in MASKS:
                mmd = pat.sub(rep, mmd)
            out = REPO / out_rel
            variants.append((mmd, out.with_name(out.stem + MASKED_SUFFIX + out.suffix), True))
        for b, out, masked in variants:
            print_pdf(build_html(b, title, zoom), out)
            ok &= report(out, a.qa, masked)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
