---
name: format-tasks-md
description: >-
  Canonical format for tasks.md — the project task checklist. Use when creating,
  reading, or updating tasks.md. Loaded by the planner (to write it), the
  builder (to read and mark tasks), the antagonist (to read it), and during
  orchestration (to sequence work).
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
  - **Files**: `path/to/expected_file.py`, `path/to/other.py`
  - **Depends on**: Task X, Task Y (or "none")
  - **Acceptance**: Concrete, verifiable criteria.
  - **Outcome**: What artifact or state exists when done and how to verify it.
```

## Task Checkbox States

- `[ ]` — not started
- `[-]` — in progress (started but not complete; marks interrupted sessions)
- `[x]` — done

## Rules

1. The first line is always `tier: <name>` — the project-level default tier.
2. Tasks are numbered sequentially. Numbers are stable — do not renumber after deletion.
3. Each task has all fields: number+title, description, files, depends on, acceptance, outcome.
4. Acceptance criteria must be **falsifiable** — it should be possible to check pass/fail mechanically or by inspection. Avoid "works correctly" or "is clean."
5. Mark completed tasks with `[x]`. Do not delete them.
6. Tasks should be modular, sequential, and bite-sized. If a task touches more than 3-4 files, consider splitting it.
7. Blockers go in the dedicated section, not inline with tasks.
8. `depends_on` is the only reordering mechanism. Tasks are sequentially executable top-to-bottom by default.
9. Verb-first names: Create, Implement, Add, Configure, Write, Refactor.
10. Aim for 4-10 tasks. Split into phases if more.

## Scaling Rules

| Tier | Artifacts |
|---|---|
| `jerryrig` | `tasks.md` only — 2-3 line inline plan + checklist |
| `poc` | `spec.md` + `tasks.md` |
| `script` | `spec.md` + `tasks.md` |
| `application` | `spec.md` + `architecture.md` + `tasks.md` |

## Example

```markdown
tier: script

## High-Level Plan
Watch a shared folder for new PDF work orders, extract the order number and equipment tag from the first page, and append a row to a local CSV log. Single Python file using watchdog for filesystem events and pdfplumber for extraction.

## Blockers / Open Questions
- PDF layout varies by originating system — needs sample files to confirm extraction logic.

## Tasks
- [ ] **1. Scaffold script and CLI args**
  - **Description**: Set up the script entry point with argparse for --watch-dir and --output-csv.
  - **Files**: `watch_workorders.py`
  - **Depends on**: none
  - **Acceptance**: Running with --help prints usage. No logic yet.
  - **Outcome**: Script accepts CLI args and exits cleanly.

- [ ] **2. Implement PDF extraction**
  - **Description**: Add extract_fields function using pdfplumber to pull order_number and equipment_tag from first page.
  - **Files**: `watch_workorders.py`
  - **Depends on**: Task 1
  - **Acceptance**: Function returns correct dict for two sample PDFs.
  - **Outcome**: `extract_fields(path)` returns dict with `order_number` and `equipment_tag`. Tested manually against sample PDFs.

- [ ] **3. Implement folder watcher and CSV append**
  - **Description**: Add watchdog observer that calls extract_fields on new .pdf files and appends rows to the output CSV.
  - **Files**: `watch_workorders.py`
  - **Depends on**: Task 2
  - **Acceptance**: Dropping a PDF into the folder produces a new CSV row within 2 seconds.
  - **Outcome**: End-to-end pipeline works: drop PDF → extract → CSV row.
```
