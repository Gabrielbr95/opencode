---
name: format-tasks-md
description: >-
  Canonical format for tasks.md — the project task checklist. Use when creating,
  reading, or updating tasks.md. Loaded by the planner (to write it), the
  builder (to read and mark tasks), the reviewer and architect (to read it),
  and the orchestrator (to sequence work).
---

# tasks.md Format

Every project has a `tasks.md`. It is the single source of truth for what needs to be done, in what order, and to what standard.

## Structure

```markdown
tier: <tier_name>

## High-Level Plan
[2-3 sentence overview of the chosen approach]

## Blockers / Open Questions
- [List any questions or blockers, or state "None"]

## Tasks
- [ ] **1. Short Title**
  - **Description**: What this task accomplishes, in 1-3 sentences.
  - **Tier**: jerryrig | poc | script | application
  - **Files**: `path/to/expected_file.py`, `path/to/other.py`
  - **Acceptance**: Concrete, verifiable criteria (e.g., "runs without error", "test suite passes", "output matches expected.csv").

- [ ] **2. Short Title**
  - **Description**: ...
  - **Tier**: ...
  - **Files**: ...
  - **Acceptance**: ...
```

## Rules

1. The first line is always `tier: <name>` — the project-level default tier. Individual tasks can override it.
2. Tasks are numbered sequentially. Numbers are stable — do not renumber after deletion.
3. Each task has all five fields: number+title, description, tier, files, acceptance.
4. Acceptance criteria must be **falsifiable** — it should be possible to check pass/fail mechanically or by inspection. Avoid "works correctly" or "is clean."
5. Mark completed tasks with `[x]`. Do not delete them.
6. Tasks should be modular, sequential, and bite-sized. If a task touches more than 3-4 files, consider splitting it.
7. Blockers go in the dedicated section, not inline with tasks.
