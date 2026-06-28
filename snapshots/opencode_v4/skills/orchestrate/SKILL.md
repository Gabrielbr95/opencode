---
name: orchestrate
description: >-
  Autonomous task execution across multiple tasks. Use when the user wants to
  run through a batch of tasks from tasks.md without manually switching agents.
  Loaded by planner or antagonist. Reads planning files, delegates to the
  builder, and monitors progress.
---

# Orchestrate

Coordinate autonomous execution of tasks from the project plan. Read planning files, delegate coding to the builder agent, and track progress. Do not write code.

## Before You Start

Read in order — stop if any required file is missing or malformed:

1. `tasks.md` — required. Must have `tier:` on line 1 and a `## Tasks` section.
2. `spec.md` — read if present.
3. `architecture.md` — read if present.
4. `decisions.md` — read if present.

Stop and report if `tasks.md` is missing, lacks `tier:`, or has no task checklist.

## Confirm Scope

Present the task list to the user. Ask which tasks to execute (e.g., "all", "tasks 1-3", or "just task 2"). Wait for explicit confirmation before proceeding.

## Execution

**Parse**: Extract each task's number, name, `files:`, `depends_on:`, `outcome:`. Skip `[x]` tasks. Treat `[-]` tasks as interrupted — re-delegate them before processing any `[ ]` tasks (preserve original order). Identify eligible tasks (all `depends_on` satisfied).

**Handoff per task** — pass only this, trimmed to task scope:

```
Tier: <tier>
Goal (2-3 sentences): <from spec.md, or omit if absent>
Architecture constraints (relevant to this task's files): <from architecture.md, or "none">
Active decisions: <relevant entries from decisions.md, or "none">
Task N: <name>
Files: <files>
Outcome: <outcome>
Follow the builder-workflow skill for task reporting.
```

Never pass full plan documents to the builder.

**On success**: Verify task is `[x]` in `tasks.md`, proceed to next eligible task.

**On failure**: Do not retry. Skip task and all tasks that depend on it. Note reason. Continue with unblocked tasks.

## Final Report

```
## Orchestration Complete

Completed (N): Task 1 — outcome. Task 3 — outcome.
Skipped (N): Task 2 — reason. Task 4 — blocked by Task 2.
Files changed: path/to/file.py
Next steps: <what unblocks skipped tasks, or "None">
```

## Rules

- If a task requires a design decision not in the plan, skip it and note it. Never invent an answer.
- If Task B depends on failed Task A, skip Task B.
- Only modify `tasks.md` to add blocker notes. The builder checks off tasks.
- Never retry a failed task without user approval.
- Never skip a task or reorder the checklist without user approval.
- Stop if the builder reports a blocker that requires plan changes.
