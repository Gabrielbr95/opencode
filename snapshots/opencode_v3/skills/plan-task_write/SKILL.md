---
name: plan-task_write
description: Load before writing or significantly amending tasks.md. Defines the required schema, field rules, and formatting.
---

# plan-task_write

## When to load

Load when about to write a new `tasks.md` or make structural changes to an existing one. Do not load just to check off a task.

## Schema

```markdown
tier: <jerryrig|poc|script|application>

## High-Level Plan
2-3 sentences: approach, key decisions, why.

## Blockers / Open Questions
- Item 1
- [or "None"]

## Tasks Checklist

- [ ] Task N: Short Name
      agent: builder
      files: path/to/file.py, path/to/other.py
      depends_on: Task X, Task Y  (or "none")
      outcome: What exists when done and how to verify it.
```

Task checkbox states: `[ ]` not started · `[-]` in progress (started but not complete) · `[x]` done.

## Field Definitions

**tier** — First line, no heading. Drives rigor for every downstream agent.
- `jerryrig` — run today, speed over everything
- `poc` — answers "can this be done?" throwaway code
- `script` — recurring automation, YAGNI, stdlib focus
- `application` — long-lived, structure and quality matter

**Task N: Short Name** — Sequential integer. Name is 3-6 words, verb-first. E.g. `Parse equipment CSV`.

**agent** — Always `builder`. The tier field drives how the builder behaves.

**files** — Comma-separated relative paths expected to change. Write `unknown` if unsure.

**depends_on** — Comma-separated task names that must finish first. `none` if independent.

**outcome** — 1-2 sentences: what artifact or state exists and the exact verify command or check.

## Scaling Rules

| Tier | Artifacts |
|---|---|
| `jerryrig` | `tasks.md` only — 2-3 line inline plan + checklist |
| `poc` | `spec.md` + `tasks.md` |
| `script` | `spec.md` + `tasks.md` |
| `application` | `spec.md` + `architecture.md` + `tasks.md` |

## Task Authoring Rules

- One clear outcome per task.
- Sequentially executable top-to-bottom; `depends_on` is the only reordering mechanism.
- Each task independently verifiable — the outcome must state how.
- Aim for 4-10 tasks. Split into phases if more.
- Verb-first names: `Create`, `Implement`, `Add`, `Configure`, `Write`, `Refactor`.

## Example

```markdown
tier: script

## High-Level Plan
Watch a shared folder for new PDF work orders, extract the order number and equipment tag from the first page, and append a row to a local CSV log. Single Python file using watchdog for filesystem events and pdfplumber for extraction.

## Blockers / Open Questions
- PDF layout varies by originating system — needs sample files to confirm extraction logic.

## Tasks Checklist

- [ ] Task 1: Scaffold script and CLI args
      agent: builder
      files: watch_workorders.py
      depends_on: none
      outcome: Script accepts --watch-dir and --output-csv via argparse. Running with --help prints usage. No logic yet.

- [ ] Task 2: Implement PDF extraction
      agent: builder
      files: watch_workorders.py
      depends_on: Task 1
      outcome: `extract_fields(path)` returns dict with `order_number` and `equipment_tag` from first page. Tested manually against two sample PDFs.

- [ ] Task 3: Implement folder watcher and CSV append
      agent: builder
      files: watch_workorders.py
      depends_on: Task 2
      outcome: Script watches --watch-dir, calls extract_fields on each new .pdf, appends row to --output-csv. Dropping a PDF into the folder produces a new CSV row within 2 seconds.
```
