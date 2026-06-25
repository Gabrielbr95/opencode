---
name: builder-workflow
description: >-
  Shared workflow procedure for all coding/builder tasks. Use when implementing
  any task from tasks.md regardless of tier. Defines state continuity protocol,
  definition of done, and conclusion/handoff format. Always load this alongside
  the tier-specific skill.
---

# Builder Workflow

Standard procedure for every builder task.

## 1. State Continuity (do this first, every time)

1. Read `tasks.md`. Identify the `tier:` on the first line and the next unchecked `- [ ]` task. The **format-tasks-md** skill defines the canonical format.
2. If `spec.md` or `architecture.md` exist, read them for context.
3. Work ONLY on the active task. Do not skip ahead or combine tasks.

## 2. Definition of Done (self-verify before reporting)

- Code runs without ImportError or SyntaxError.
- No hardcoded paths that won't exist on the user's machine (unless tier is jerryrig/poc).
- Changes match the task's acceptance criteria.
- `tasks.md` updated: active task marked `[x]`, any new blockers noted.

## 3. Conclusion Format

After completing a task, always output:

1. **What changed**: Files created/modified, one line each.
2. **How to run**: Exact command(s) to execute or test.
3. **Next step**: Recommend the logical next action for the human orchestrator (e.g., *"Now you can invoke the Reviewer to verify, or proceed to Task N..."*).
