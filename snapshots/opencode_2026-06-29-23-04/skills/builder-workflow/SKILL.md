---
name: builder-workflow
description: >-
  Shared workflow procedure for all coding/builder tasks. Use when implementing
  any task from plan/tasks.md regardless of tier. Defines state continuity
  protocol, in-progress marking, definition of done, and task report format.
  Always load this alongside the tier-specific skill.
---

# Builder Workflow

Standard procedure for every builder task.

## 1. State Continuity (do this first, every time)

1. Read `plan/tasks.md`. Identify the `tier:` on the first line and the next unchecked `- [ ]` task. If a `- [-]` task exists, it was interrupted — resume it first.
2. If `plan/spec.md`, `plan/architecture.md`, or `plan/decisions.md` exist, read them for context.
3. Work ONLY on the active task. Do not skip ahead or combine tasks.

## 2. Mark In-Progress

Before writing any code or making any file changes, edit `plan/tasks.md` to change `- [ ]` to `- [-]` on the assigned task line. This marks the task as started so an interrupted session leaves a visible dirty state.

## 3. Definition of Done (self-verify before reporting)

- Code runs without ImportError or SyntaxError.
- No hardcoded paths that won't exist on the user's machine (unless tier is jerryrig/poc).
- Changes match the task's acceptance criteria.
- Implementation does not contradict any active decision in `plan/decisions.md`.
- `plan/tasks.md` updated: active task marked `[x]`, any new blockers noted.

## 4. Task Report

After completing a task, update `plan/tasks.md` (`- [-]` to `- [x]`) and output:

```
## Completed: Task N — Short Name

**What changed**
- path/to/file.py: what was added or modified (function names, class names, config keys)

**How to run**
<exact command — include flags, example input, expected output format>

**How to verify**
<concrete pass/fail signal — test output, printed value, file existence, log line>

**Blockers / follow-ups**
- <issues, deferred edge cases, open questions — or "None">
```

### Report rules

- One bullet per file in "What changed".
- No preamble ("I have successfully...").
- No code reproduction unless explicitly asked.
- No suggestions beyond task scope unless they are blockers.
- "How to verify" must be concrete — a human must be able to run it and know immediately if it passed.
