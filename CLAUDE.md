# CLAUDE.md

Project ground rules for this repository. Every contributor — human or AI agent —
reads this file first.

This is a **teaching template**. Copy it into your own project and edit the parts
that are project-specific (Sections 4, 5, and 8).

---

## 1. Start-Of-Day Rule (Required)

- Before doing any task, read this file first.
- Then check:
  - `WORKLOG.md`
  - `TODO.md`
- If something conflicts, follow this order:
  1. This file (`CLAUDE.md`)
  2. `WORKLOG.md` and `TODO.md`
  3. Ad-hoc notes in chat

---

## 2. Worklog Rules

File: `WORKLOG.md`

- One entry per contributor per day.
- Do not split the same contributor/day into multiple sections.
- If new progress happens on the same day, append to the existing entry.
- Use English.
- Use latest-first order (reverse chronological).
- Include contributor name and date in every entry.
- If tasks remain, keep status as `IN PROGRESS` and list next actions.

Header format:

`## YYYY-MM-DD | Contributor: Name`

---

## 3. Todo Rules

File: `TODO.md`

- One entry per contributor per day.
- Simple list style only. No priority sections.
- Keep tasks as short bullet points.
- Status markers: `[ ]` not started, `[~]` in progress, `[x]` done, `[-]` dropped.
- Append updates to the same contributor/day entry.
- Use latest-first order.

Header format:

`## YYYY-MM-DD | Assignee: Name`

---

## 4. Code Organization Rules

- Never place scripts directly in `code/`. Always use a task-specific subfolder,
  e.g. `code/descriptive/`, `code/estimation/`.
- Mirror that subfolder structure in `output/` and `intermediate/`.
- Never hardcode absolute paths. Define a root variable at the top of each script
  and build every other path from it.
- One script should do one job. If a file grows past a few hundred lines, split it.

---

## 5. Python Environment Rules

- Use one virtual environment per repository, named `.venv`.
- Do not create parallel environments (`.venv-1`, `venv2`, ...).
- VS Code interpreter target: `.venv\Scripts\python.exe` (Windows) or `.venv/bin/python` (Mac/Linux).
- Install packages and run scripts inside `.venv`.
- Record dependencies in `requirements.txt` when you add one.

---

## 6. Secret Handling Rules

- Secrets live in the local `.env` only. `.env` is gitignored.
- Never commit `.env` or any key, token, or password to Git.
- Keep `.env.example` as a placeholder template with empty values.
- If a key is exposed, rotate it immediately — removing the commit is not enough.

---

## 7. Documentation Update Rules

- When work status changes, update both `WORKLOG.md` and `TODO.md`.
- Keep records concise and consistent.
- Contributor attribution must match the person who actually did the work.

---

## 8. Data Folder Junction Rules

Data, output, and intermediate folders are **not** stored in Git. Create local
junctions in the repository root after cloning. They are gitignored and never pushed.

| Junction name | Target |
|---|---|
| `data` | `<Dropbox>\sample_project\data` |
| `output` | `<Dropbox>\sample_project\output` |
| `intermediate` | `<Dropbox>\sample_project\intermediate` |

Create with PowerShell:

```powershell
New-Item -ItemType Junction -Path "data" -Target "<Dropbox>\sample_project\data"
```

Never save data, drafts, or large files directly in the Git repository.

---

## 9. Commit Rules

- Commit at logical stopping points, not once a week.
- One commit = one idea. Do not mix unrelated changes.
- Write a short imperative subject line: `Add main regression script`.
- When a commit touches several files, add file-specific notes in the commit body
  so each change can be reviewed independently.
- Never commit generated output, data, or secrets.

---

## 10. Operational Principle

Goal: any contributor can start from the same rules and continue the work consistently.

Minimum daily cycle:

1. Read `CLAUDE.md`
2. Check `WORKLOG.md` and `TODO.md`
3. Pull, then do the work
4. Commit and push
5. Update worklog and todo before ending the session
