# Sample Project — GitHub Setup Guide for Research Students

Author: Kensuke Suzuki
Last updated: 2026-08-24

This repository is a **teaching template**. It shows how to set up Git and GitHub for an
empirical research project, and how to keep track of code changes over time.
Clone it, read it, and copy the structure into your own project.

## Repository

```
https://github.com/kensukesuzuki04/sample_project.git
```

---

## Quick Start

Use this order the first time you set up a repository.

1. Install Git and VS Code (Section 1).
2. Configure your Git name and email once per machine (Section 2).
3. Clone the repository to a **local** folder only. Do not clone it inside Dropbox or OneDrive.
4. Read [CLAUDE.md](CLAUDE.md) — the project ground rules — before editing anything.
5. Create the local junctions to your cloud-synced data folders (Section 6).
6. Copy `.env.example` to `.env` and fill in any API keys. Never commit `.env`.
7. Keep new code in a task-specific subfolder under `code/`, such as `code/descriptive/`.
8. Run a script and verify that outputs are written outside the repository.

---

## What Is Git / GitHub?

- **Git** is a version control tool that tracks changes to files over time. You can always go back to an earlier version.
- **GitHub** is a website that hosts Git repositories online, making it easy to share code with collaborators.
- Think of it like "Track Changes" in Word, but for your entire project folder — and shared with the team.

---

## 1. Install Git and VS Code

### Git

1. Download from [https://git-scm.com/download/win](https://git-scm.com/download/win) (Windows) — the default installer options are fine
2. On Mac: open Terminal, run `git --version`, and follow the prompt if Git is not installed

### VS Code

Download from [https://code.visualstudio.com](https://code.visualstudio.com). VS Code has Git support built in — no extensions needed for basic workflows.

---

## 2. Configure Git (One-Time Setup)

Open the VS Code terminal (**Terminal → New Terminal**) and run:

```bash
git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"
```

Use the same email address as your GitHub account. This only needs to be done once per machine.

---

## 3. Get Access to a Private Repository

This sample repository is public — anyone can clone it. For a real project repository,
ask the owner to add you as a collaborator on GitHub. You will receive an email
invitation; accept it before proceeding.

---

## 4. Clone the Repository

"Cloning" downloads the repository to your computer.

> **Important**: Clone to a **local folder only** — do NOT clone inside Dropbox, OneDrive, or any other cloud-synced folder. Git and cloud sync services conflict and can corrupt your repository.

**In VS Code:**

1. Open the Command Palette: `Ctrl+Shift+P` (Windows) / `Cmd+Shift+P` (Mac)
2. Type `Git: Clone` and select it
3. Paste the repository URL: `https://github.com/kensukesuzuki04/sample_project.git`
4. Choose a **local** destination folder (e.g., `C:\Users\<username>\GitHub\`)
5. Click **Open** when VS Code asks to open the cloned repository

**From the terminal:**

```bash
cd C:/Users/<username>/GitHub
git clone https://github.com/kensukesuzuki04/sample_project.git
cd sample_project
```

---

## 5. Repository Structure and Ground Rules

### Directory Structure

```
sample_project/
  code/
    descriptive/      <- Descriptive analysis scripts
    estimation/       <- Estimation scripts
  note/               <- Notes and documentation
  data/               <- Junction to Dropbox (see Section 6) - NOT tracked in Git
  output/             <- Junction to Dropbox (see Section 6) - NOT tracked in Git
  intermediate/       <- Junction to Dropbox (see Section 6) - NOT tracked in Git
  CLAUDE.md           <- Project ground rules
  WORKLOG.md          <- Daily progress log
  TODO.md             <- Task list
  .gitignore
  .env.example
```

### Ground Rules

1. **Do not save data in this repository.** All data, output, and intermediate files are stored in Dropbox (not Git). Only code is tracked here.

2. **Do not mix code and data/output files in the same folder.**
   - `code/` contains only scripts (`.do`, `.py`, `.qmd`, `.m`, `.R`)
   - Data, outputs, and intermediate files live outside `code/`, in their own top-level folders

3. **Always create a subfolder under `code/` — never place scripts directly in `code/` itself.**
   Group scripts by task (e.g., `code/descriptive/`, `code/estimation/`).

   **Commit rule:** When committing, include file-specific comments in the commit message
   so that each file can be reviewed and versioned independently.

4. **Mirror the folder structure across `code/`, `output/`, and `intermediate/`.**
   A script at `code/estimation/regMain.do` writes outputs to `output/estimation/` and intermediates to `intermediate/estimation/`.

5. **Folder and file naming conventions:**
   - Use lowercase for folder names. camelCase (e.g., `regMain`) is acceptable when it aids readability.
   - Keep file names concise — avoid overly long names.

6. **Never hardcode absolute paths in scripts.** Set a root variable at the top of each script:

   ```stata
   global root "C:\Users\<username>\GitHub\sample_project"
   ```

   ```python
   from pathlib import Path
   ROOT = Path(__file__).resolve().parents[2]
   ```

   See [code/descriptive/summaryStats.py](code/descriptive/summaryStats.py) and
   [code/estimation/regMain.do](code/estimation/regMain.do) for worked examples.

---

## 6. Set Up Junctions to Dropbox

Data, output, and intermediate files are stored in Dropbox (not Git). After cloning, create
junctions (Windows) or symlinks (Mac/Linux) so your scripts can reference them using local paths.

> **Note**: Junctions are local only — they are listed in `.gitignore` and are never pushed to GitHub. Each member must create them on their own machine after cloning.

### Option A: Manual (Command Prompt, Windows)

Open **Command Prompt** (cmd.exe) — not PowerShell — and run:

```cmd
cd C:\Users\<username>\GitHub\sample_project

mklink /J data         "<path to your Dropbox>\sample_project\data"
mklink /J output       "<path to your Dropbox>\sample_project\output"
mklink /J intermediate "<path to your Dropbox>\sample_project\intermediate"
```

Replace `<path to your Dropbox>` with the actual Dropbox path on your machine (e.g., `D:\Dropbox\Research`).

On Mac/Linux, use `ln -s` instead:

```bash
ln -s ~/Dropbox/Research/sample_project/data data
```

### Option B: Ask an Agentic AI (Claude Code, etc.)

If you have Claude Code or a similar agentic AI tool available, paste the following prompt:

```
I have cloned the GitHub repository sample_project to my local machine.
Please create junction symlinks for the following folders inside the cloned repo,
pointing to the corresponding Dropbox folders:

- data         -> <path to your Dropbox>\sample_project\data
- output       -> <path to your Dropbox>\sample_project\output
- intermediate -> <path to your Dropbox>\sample_project\intermediate

The repo is located at: <path to your local repo>\sample_project
Use PowerShell's New-Item -ItemType Junction to create them.
```

Replace the placeholders with your actual paths before sending.

### Verify

Open the cloned folder in Explorer and confirm that `data`, `output`, and `intermediate` appear as shortcut/junction folders pointing to Dropbox.

### Dropbox Shared Folder Structure

```
sample_project/          (D:\Dropbox\Research\sample_project\)
  data/                  <- Raw data files (never pushed to GitHub)
  intermediate/          <- Intermediate files generated by scripts
  output/                <- Final output files generated by scripts
  paper/                 <- Drafts and writing files (never pushed to GitHub)
```

| Folder | Contents |
|---|---|
| `data/` | Raw data files — do not edit manually |
| `intermediate/` | Auto-generated by scripts — do not edit manually |
| `output/` | Auto-generated by scripts — do not edit manually |

---

## 7. Daily Workflow in VS Code

Open the **Source Control panel** with `Ctrl+Shift+G`.

### Before starting — pull the latest changes

Click the **Sync Changes** button (circular arrows) in the Source Control panel, or go to `... → Pull`.
Always do this before editing anything.

### After making changes — commit and push

1. **See what changed**: modified files appear automatically in the Source Control panel
2. **Stage files**: click the `+` icon next to each file you want to include, or stage all with `+` at the top
3. **Write a commit message**: type a short description in the message box at the top
4. **Commit**: click the **Commit** checkmark (or `Ctrl+Enter`)
5. **Push**: click **Sync Changes** (or `... → Push`) to upload to GitHub

### The same workflow from the terminal

```bash
git pull                       # get the latest version
git status                     # see what changed
git diff                       # see the actual line-by-line changes
git add code/estimation/regMain.do
git commit -m "Add main regression script"
git push
```

### Commit frequently

Commit whenever you reach a logical stopping point — after fixing a bug, finishing a step, or completing a block of analysis. Small, focused commits are much easier to review and revert.

Write a brief but descriptive message. Examples:
- `"Add main regression script"`
- `"Fix output path in estimation"`
- `"Clean up descriptive analysis"`

---

## 8. Tracking Code Changes

This is the point of using Git. Useful commands:

| Command | What it shows |
|---|---|
| `git log --oneline` | Compact list of all commits |
| `git log -p <file>` | Full change history of one file |
| `git diff` | Unstaged changes in your working folder |
| `git diff --staged` | Changes you have staged but not committed |
| `git blame <file>` | Who last changed each line, and in which commit |
| `git show <commit>` | Everything that changed in one commit |

In VS Code: right-click a file and choose **Open Timeline** to browse its version history, or
install the **GitLens** extension for inline authorship annotations.

### Undoing things

```bash
git restore <file>             # discard uncommitted changes to a file
git restore --staged <file>    # unstage a file, keep the edits
git revert <commit>            # create a new commit that undoes an old one (safe)
```

Avoid `git reset --hard` — it deletes work permanently. When in doubt, ask first.

---

## 9. Working on a Branch

For anything larger than a quick fix, work on a branch and merge it back when it is done.

```bash
git switch -c yourname-feature   # create and move to a new branch
# ... edit, commit as usual ...
git push -u origin yourname-feature
```

Then open a **Pull Request** on GitHub so the change can be reviewed before it enters `main`.

---

## 10. Git in MATLAB

MATLAB has built-in Git support and can handle most common operations without leaving the app.

### Setup

1. Open MATLAB and navigate to the cloned repository folder in the **Current Folder** panel
2. Go to **Home → Source Control → Manage Files**
3. MATLAB will detect the existing Git repository automatically

### Daily Use

- **View changes**: right-click a file in the Current Folder panel → **Source Control → View Modified Files**
- **Commit**: right-click → **Source Control → Commit**
- **Push / Pull**: **Home → Source Control → Push** or **Pull**
- **View history**: right-click a file → **Source Control → View File History**

MATLAB's Source Control UI covers the same pull → edit → commit → push workflow as VS Code.

---

## 11. What Is (and Is Not) Tracked

| Tracked in Git | Not Tracked (gitignored) |
|---|---|
| `.do`, `.py`, `.qmd`, `.m`, `.R` scripts | Data files (`.dta`, `.csv`, `.xlsx`) |
| Notes and documentation (`.md`) | Output and intermediate files |
| `.gitignore`, `.env.example` | Figures and images |
| | GIS/spatial files (`.shp`, `.geojson`) |
| | Stata logs (`.log`, `.smcl`) |
| | Secrets (`.env`) |

See [.gitignore](.gitignore) for the full list.

---

## 12. Secrets and API Keys

- Store keys in a local `.env` file only. `.env` is gitignored.
- Commit `.env.example` as a placeholder template so collaborators know which keys are needed.
- If a key is ever committed by accident, **rotate it immediately** — deleting the commit is not enough, since the key stays in the repository history.

---

## 13. If Something Goes Wrong

- **Accidentally staged a wrong file?** In Source Control panel, click the `−` icon next to the file to unstage it
- **Want to discard changes to a file?** Right-click the file in Source Control → **Discard Changes**
- **Conflict when pulling?** VS Code will highlight the conflicting lines — ask a collaborator before resolving if unsure

When in doubt, do not delete or reset anything. Ask first.

---

## 14. Worklog and Todo Usage

### Worklog (`WORKLOG.md`)

A chronological record of daily progress, problems, and solutions.

1. **Daily updates**: at the end of each work session, add an entry with the date and a summary.
2. **Challenges and solutions**: document issues encountered and how they were resolved.
3. **Future plans**: note the next steps.

```
## 2026-08-24 | Contributor: Your Name
- Cloned the repository and created the Dropbox junctions.
- Ran summaryStats.py and confirmed output in output/descriptive/.
- Next: add the first estimation script.
```

### Todo (`TODO.md`)

A simple running task list.

```
## 2026-08-24 | Assignee: Your Name
- [x] Set up Git and clone the repository
- [ ] Draft the descriptive statistics script
- [ ] Review folder naming conventions
```

---

## 15. Exercise for Students

Work through these steps once to confirm your setup:

1. Clone this repository to a local folder.
2. Create a branch: `git switch -c yourname-practice`
3. Add a new file `code/descriptive/practice.py` that prints your name.
4. Commit it with a descriptive message and push the branch.
5. Run `git log --oneline` and `git diff main` to see what you changed.
6. Add an entry to `WORKLOG.md` describing what you did, then commit again.
7. Open a Pull Request on GitHub and look at the diff view.

---

## License

Released under the MIT License — see [LICENSE](LICENSE). Reuse and adapt freely for teaching.
