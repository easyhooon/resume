---
name: resume-feedback
description: Applies feedback from another person (recruiter, referrer, senior, reviewer) to this repo's RESUME.md, PORTFOLIO.md or RESUME_PRODUCT_ENGINEER.md. Every time, it reports each change as AS IS → TO BE, tagged with the feedback item it answers, and lists feedback it did not follow and wording it dropped. Use when the user pastes or describes feedback and asks to reflect it ("피드백 반영", "이 피드백대로 고쳐줘", "리뷰 받은 거 적용"), or asks what changed and why after such an edit. Do NOT use for edits the user dictates themselves with no outside feedback, for PDF regeneration alone (use resume-pdf), or for documents outside this repo.
---

# resume-feedback

Owner: easyhooon (mraz3068@gmail.com) · Last review: 2026-10-19

The user forwards the revised resume back to the reviewer and has to explain each change, so the report matters as much as the edit. `scripts/diff_pairs.py` lists every change mechanically. You do the judgment part: which feedback item each change answers, and what to do when feedback conflicts with `AGENTS.md`.

## Procedure

1. **Split the feedback into items.** Number them F1, F2, … and quote each one in a few words. Mark items the reviewer gave as "참고만" (reference only). Done when every sentence of the feedback belongs to one item.
2. **Fix the baseline.** Run `git fetch` and `git status -sb`. The target files must be clean and not behind `origin/main`; fast-forward if behind. If they have uncommitted edits, ask before touching them.
   - Why: `diff_pairs.py` diffs against `HEAD`. If `HEAD` is not the version the reviewer read, the AS IS column is wrong.
3. **Check each item against `AGENTS.md` before editing.** Where they conflict, `AGENTS.md` wins and the item goes to "그대로 따르지 않은 피드백" in the report. Common conflicts:
   - A number the reviewer rounded differently (reviewer "6.5만" vs source 64,484 → write 6.4만). Why: interviewers ask where numbers come from.
   - Dropping "완료 예정" from unfinished work. Why: the claim must be true on the submission date.
   - Merging two techniques into one phrase ("A-A 검증 뮤테이션 테스트"). Keep them separate; they are different methods.
4. **Edit only what some item requires.** Reorder, split, or re-bold the user's own wording; don't add facts or new numbers. When an item means deleting content (for example cutting bullets 5 → 3), choose a cut, but list every deleted line in the report for the user's approval.
   - Why: the resume has to stay in the user's words, and only the user can judge which result matters more to them.
5. **Run the diff script.**
   ```bash
   python3 -I .claude/skills/resume-feedback/scripts/diff_pairs.py [--base REV] [FILE ...]
   ```
   It prints numbered changes C1, C2, … with section, AS IS and TO BE. Defaults: base `HEAD`, files `RESUME.md PORTFOLIO.md`. Pass `RESUME_PRODUCT_ENGINEER.md` too if it was edited.
6. **Map both directions.** Every C needs at least one F, or a reason under "피드백 외 변경". Every F needs at least one C, or a reason under "그대로 따르지 않은 피드백". Then compare AS IS and TO BE word by word for dropped content (a qualifier, a number, a label like "Libraries & Code") and list it under "재작성 중 빠진 표현".
7. **Report in chat in the format below**, then ask whether to restore anything and whether to commit and push. Build PDFs with `resume-pdf` only after the user approves. Commit and push only when asked.
   - Why push matters: the resume's Portfolio link points at GitHub `main`, so the reviewer sees the old portfolio until it is pushed.

## Report format

```
### 피드백 항목
F1 두괄식 … / F2 불릿 5→3 … / F3 (참고) …

### AS IS → TO BE
#### C7 · 세컨드 윈드/닥터 · 반영: F1, F2, F5
AS IS
> (원문 그대로)
TO BE
> (수정문 그대로)
빠진 내용: (없으면 생략)

(Group same-kind small changes, e.g. "C4·C6·C8 다운로드 수치 굵게 해제 · F3", in one row instead of repeating them.)

### 그대로 따르지 않은 피드백
- F? 내용 → 이유

### 피드백 외 변경
- C? 내용 → 이유

### 재작성 중 빠진 표현
- 위치: "빠진 표현" (되살릴지 결정 필요)
```

Quote AS IS and TO BE verbatim. A summary like "문장 정리" hides exactly the dropped words the user needs to check.

### Excuses for skipping the report, and why they fail

- *"The changes are obvious, so a one-line summary will do."* In the first run, a summary missed three dropped phrases ("클래스 사진", "Libraries & Code", "걸음 수·심박수·소모 칼로리를 직접 동기화"). The full script output caught them.
- *"Heading renames don't need a feedback tag."* The user still has to tell the reviewer why the section names changed. Group them into one row; don't omit them.
- *"I'll map the changes from memory instead of running the script."* Memory misses changes made by Bash or sed. The script reads the actual files.

## Change history

- 2026-10-19: Created after applying a Toss referrer's feedback (두괄식, bullets 5 → 3, bold keywords over numbers, shorter Introduce, separate company and side projects). The user asked for an AS IS → TO BE report with feedback mapping on every future feedback round. Verified `diff_pairs.py` on that edit: it produced 20 changes across RESUME.md and PORTFOLIO.md, including dropped phrases the first summary had missed. Not yet re-tested on a second feedback round.
