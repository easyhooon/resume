---
name: resume-pdf
description: Regenerates the A4 PDFs of this repo's RESUME.md, PORTFOLIO.md and RESUME_PRODUCT_ENGINEER.md (and the masked 제출용_개인정보마스킹 copies) with headless Chrome, then checks page count, links and every page visually. Use after editing any of those Markdown files, or when asked to "PDF 갱신/재생성/변환", "제출용 PDF 만들어줘", or to send the resume/portfolio to someone. Do NOT use for writing or rewording resume content itself, for converting other documents (docx, slides, notes), or for Word/HWP output.
---

# resume-pdf

Owner: easyhooon (mraz3068@gmail.com) · Last review: 2026-10-16

Turns the Markdown in the repo root into the PDFs under `output/pdf/`. The script does the deterministic part (render, print, measure); you do the judgment part (does each page look right, does it fit the page budget).

## Targets

| key | source | output | page budget |
|---|---|---|---|
| `resume` | `RESUME.md` | `output/pdf/이지훈_이력서.pdf` | 3 pages (A4) |
| `portfolio` | `PORTFOLIO.md` | `output/pdf/이지훈_포트폴리오.pdf` | no fixed budget, currently about 10 |
| `pe` | `RESUME_PRODUCT_ENGINEER.md` | `output/pdf/product-engineer/이지훈_Product_Engineer_이력서.pdf` | 2–3 pages |

`--masked` also writes `<name>_제출용_개인정보마스킹.pdf` next to each output. It shows the phone as `010-****-3068` and the email as `mraz****@gmail.com`.

## Procedure

1. **Pick targets.** Build only the Markdown files that changed: `git status --short -- '*.md'`. If the user asked for a submission copy, add `--masked`.
2. **Build into a QA folder:**
   ```bash
   python3 -I .claude/skills/resume-pdf/scripts/build_pdf.py <resume|portfolio|pe|all> [--masked] --qa <scratchpad>/qa
   ```
   Each output prints one line: `pages=… links=… bytes=…`. A `MASK-LEAK=[…]` marker or a non-zero exit means the masked PDF still contains the real phone or email. Never send that file. Stop and fix `MASKS` in the script.
3. **Check the page budget.** If the resume is over 3 pages, don't shrink fonts or margins in `PRINT_CSS`. Tell the user how much spills over (for example "Education 1줄이 4쪽으로 넘어감") and propose specific lines to cut. The user decides what to cut. The 3-page budget is the user's default, not a hard rule. If the user decides the content justifies 4 pages, accept that, but still avoid a last page with only a line or two on it.
4. **Look at every page image** in `<qa>/<pdf-stem>/page-*.jpg`. Check for:
   - literal `**` or `<span` text (the renderer missed some formatting)
   - a heading left alone at the bottom of a page
   - an image cut off at a page break
   - a gray date missing next to a project heading
   - a nearly empty last page
   To find leftover bold markers fast, run `pdftotext <pdf> - | grep -n '\*\*'`. Masked PDFs show `010-****-3068`, so filter `****` out there first, or every masked file will look broken.
5. **Report.** For each file, give the path, page count and link count, and list whatever the page check found. Commit only when the user asks. Never commit the masked PDFs: they are untracked on purpose, because the repo is public and the masked copy exists only for submission.

### Steps that get skipped, and why they still matter

- *"The script exited 0, so the PDF is fine."* The script can't see layout. In the first real run, `**27.6% 단축)**로` printed literal asterisks while the exit code was 0. Only the page images showed it.
- *"Only one line changed, so I'll skip the visual check."* One added line pushed the resume from 3 to 4 pages. The page budget is the thing most likely to break.
- *"I'll just regenerate all three."* Rebuilding untouched PDFs creates binary diffs nobody asked for. Build only what changed (step 1).

## Rules

- **Never** hand-edit the PDFs or swap in another renderer. GitHub's `gh api markdown` strips inline `style`, so the gray dates disappear. Pandoc and others don't match the GitHub look these PDFs have always had.
- **Keep** `assets/marked.min.js` (v15.0.12) and `assets/github-markdown-light.css` (github-markdown-css 5.8.1) vendored. The build then works offline and gives the same output every time. Upgrade them only on purpose, and then re-check all three targets visually.
- **Keep** `cjk_bold()` in place. CommonMark won't close `**` between punctuation and a Korean particle, and that pattern appears in almost every metric line.
- Change only what was asked. Don't reword resume text while regenerating PDFs. If you spot a typo or a stale fact, point it out instead.

## Requirements

- macOS with Google Chrome at `/Applications/Google Chrome.app`
- `pdfinfo`, `pdftotext` and `pdftoppm` (poppler: `brew install poppler`)
- Python 3.10+ (stdlib only)

## Change history

- 2026-10-16: Created. The earlier PDFs were made with headless Chrome, but no script had been kept. The first version used `gh api markdown` and was replaced by vendored marked.js because GitHub strips inline styles. Added `cjk_bold()` after Korean-adjacent bold failed to render, then made it handle bold that wraps a code span (`**TTL이 있는 \`localStorage\`**`). Added a per-target zoom (portfolio 0.8): at 1.0 the portfolio grew from 10 pages to 13, but the old PDF was 10. Added retries because back-to-back headless Chrome runs sometimes exit with code 2. There are now up to 5 attempts with a growing pause between them: in a later run, 3 immediate retries all failed. Even 5 attempts failed once, because Chrome had already written the PDF and only its teardown failed. Success is now judged by whether the file is a complete PDF (`%%EOF` and readable by `pdfinfo`), not by the exit code. Chrome prints to a draft path first, so a half-written file never replaces the previous output. Verified by regenerating RESUME (3 pages), PORTFOLIO (10 pages) and the masked resume, and by checking every page image.
