# TASKS.md — How to Create, Find & Maintain Tasks

> For all agents: Jade (personal) · Sisi MaxClaw (Excel Plumbing) · and any future agents
> Owner: Ken Tam · Version 1.0 · April 2026

---

## The Core Problem This Solves

Agents forget. Files get lost in daily notes. Tasks are stored by date, not by name — so when Ken says "run the daily weather task," the agent spends 20 minutes searching through old daily logs trying to find it.

**This system fixes that forever.**

---

## Rule 1 — Where Tasks Live

Every recurring task lives in exactly ONE place:

```
/workspace/tasks/
```

Not in daily notes. Not in MEMORY.md. Not in chat history.
**In `/workspace/tasks/` — and nowhere else.**

If Ken gives you a recurring task, you create a file here immediately.
If you need to update a task, you update the file in `/workspace/tasks/`.
Every session, if you need the task, you read it from the file.

---

## Rule 2 — File Naming

Files are named by **what they do**, not when they were created.

**Good:**
- `daily-weather-report.md`
- `china-trip-updates.md`
- `excel-bookkeeping-weekly.md`
- `family-legacy-reviews.md`

**Bad:**
- `march-2026-notes.md`  ← you will never find this again
- `task-v2-final.md`  ← which v2? which final?
- `reminder.md`  ← what reminder? for who?

Inside every task file, include a header:

```markdown
# [Task Name]
Version: 1.0
Created: 2026-04-02
Last Updated: 2026-04-02
Owner: Ken Tam
Run Trigger: [e.g. "Every Sunday 9AM" / "When requested" / "Daily at 8AM"]
Backs up to: jades-memory (GitHub)
```

---

## Rule 3 — How to Create a New Task

When Ken gives you a recurring task:

1. **Create the file** in `/workspace/tasks/[descriptive-name].md`
2. **Write the full instructions** — what to do, when, how, what tools to use
3. **Note the GitHub repo** where this task's output gets backed up
4. **Update MEMORY.md** — add one line: `Recurring task: [name] → /workspace/tasks/[file].md`
5. **Done.** Next time Ken says "run the [task name]", you read the file and run it.

---

## Rule 4 — How to Update a Task

When Ken gives you new information that changes how a task works:

1. **Open the existing file** in `/workspace/tasks/`
2. **Update the instructions** — overwrite the old version entirely
3. **Update the "Last Updated" date** in the header
4. **Update MEMORY.md** if the change is significant

Never create a new file for an update. **Edit the existing one.**
The file is always the current, authoritative version.

---

## Rule 5 — How to Find a Task (Memory Search)

If Ken asks you to do something and you're not sure if there's a file for it:

1. Run `memory_search` with the task name or keywords
2. If it finds something in MEMORY.md pointing to `/workspace/tasks/`, use that file
3. If there's no file but this is a recurring task, **create one now** in `/workspace/tasks/`
4. Never dig through daily notes (`memory/YYYY-MM-DD.md`) for task instructions — that's too slow and unreliable

---

## Rule 6 — The Startup Rule

At the start of every session, before doing anything else:

1. Read `SOUL.md`, `USER.md`, `memory/YYYY-MM-DD.md` (today + yesterday) — as always
2. Run `memory_search` for any recurring tasks you know are active
3. Check `/workspace/tasks/` — if a file exists for something Ken might ask you to do, **read it before you need it**, not after

---

## Rule 7 — GitHub Backup (Critical)

Every task file MUST be backed up to GitHub so it survives server restarts.

**What to back up:**
```
/workspace/tasks/
/workspace/MEMORY.md
/workspace/memory/  (daily notes)
```

**Setup — one time only:**

```bash
#!/bin/bash
cd /workspace
git add tasks/ MEMORY.md memory/
if ! git diff --cached --quiet; then
  git commit -m "🌸 Auto-backup $(date '+%Y-%m-%d %H:%M')"
  git push origin main
fi
```

**Schedule:** Run this automatically every night via cron at 3 AM PT.

**This is non-negotiable.** If you lose a task file, you set it up again. GitHub is the source of truth.

---

## Rule 8 — Backup for MaxClaw Desktop Agents

If you're running on Ken's local machine (MaxClaw desktop):

- Your workspace lives at: `~/clawd-workspace/`
- Create the same `/workspace/tasks/` structure inside your workspace
- Set up GitHub backup the same way (cron + git push)
- If you don't have exec access: use the **cron tool** instead of bash scripts — cron runs in an isolated session that may have exec permissions even if your main session doesn't

---

## Rule 9 — What to Do If You Can't Find a Task File

1. Run `memory_search` for the task keywords
2. Check MEMORY.md for any references
3. If you still can't find it: **ask Ken for clarification**
4. Do NOT spend more than 2 minutes searching before asking

---

## Rule 10 — When Ken Says "Pin It"

When Ken says "Pin it" or "Save this for later":

1. Save a snapshot to `/workspace/memory/pins/YYYY-MM-DD-HH-[topic].md`
2. Include: Topic, Status, Key decisions, Files involved, Next steps, Restore prompt
3. Update MEMORY.md with a reference to the pin
4. The pin is a bookmark, not the live file — keep working from the live file

When Ken says "bring back [topic]":
1. List pins in `/workspace/memory/pins/`
2. Read the relevant pin
3. Say: "Here's where we were on [topic]..." and wait for direction

---

## Quick Reference — Command Cheat Sheet

| What | How |
|---|---|
| Create a new task | Write to `/workspace/tasks/[name].md` |
| Update a task | Edit the existing file in `/workspace/tasks/` |
| Find a task | `memory_search` → MEMORY.md → then `/workspace/tasks/` |
| Back up now | `cd /workspace && git add tasks/ MEMORY.md memory/ && git commit -m "backup" && git push` |
| Schedule auto-backup | Use `cron` tool — daily at 3 AM PT |
| Pin a checkpoint | Save to `/workspace/memory/pins/YYYY-MM-DD-HH-[topic].md` |
| Restore a pin | Read the pin file, then resume from it |

---

## Template — New Task File

```markdown
# [Task Name]
Version: 1.0
Created: YYYY-MM-DD
Last Updated: YYYY-MM-DD
Owner: Ken Tam / [Agent Name]
Run Trigger: [e.g. "Every Sunday", "Daily", "When requested"]
Backs up to: [GitHub repo name]

## What This Task Does
[One paragraph description]

## Step-by-Step Instructions
1. [Step 1]
2. [Step 2]
3. [Step 3]

## Tools to Use
- [Tool name]: [what it's for]

## Notes
[Any special considerations, Ken's preferences, edge cases]

## Change Log
- YYYY-MM-DD: Initial version created
```

---

*This file lives in `/workspace/TASKS.md` and in every agent's workspace.*
*Updated by: Jade on behalf of Ken Tam · April 2026*
