---
name: gen-task_report
description: Load after finishing a task implementation. Defines how to close out a task and what to include in the completion summary.
---

# gen-task_report

## When to load

Load when implementation of an assigned task is complete and it is time to update `tasks.md` and report back.

## Step 0 — Mark task in-progress

Before writing any code or making any file changes, edit `tasks.md` to change `- [ ]` to `- [-]` on the assigned task line. This marks the task as started so an interrupted session leaves a visible dirty state.

## Step 1 — Update tasks.md

1. Change `- [-]` to `- [x]` on the completed task line only.
2. Add any blockers, questions, or follow-ups discovered during implementation to the **Blockers / Open Questions** section.
3. Do not touch other task entries.

## Step 2 — Completion Summary

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

## Rules

- One bullet per file in "What changed".
- No preamble ("I have successfully...").
- No code reproduction unless explicitly asked.
- No suggestions beyond task scope unless they are blockers.
- "How to verify" must be concrete — a human must be able to run it and know immediately if it passed.

## Example

```
## Completed: Task 2 — Implement PDF extraction

**What changed**
- watch_workorders.py: added `extract_fields(path: str) -> dict` using pdfplumber; returns `order_number` and `equipment_tag` from first page; raises `ExtractionError` with filename if fields not found.

**How to run**
python watch_workorders.py --watch-dir ./samples --output-csv ./log.csv

**How to verify**
Drop any sample PDF into ./samples. Within 2 seconds, ./log.csv gains a new row with order_number and equipment_tag populated.

**Blockers / follow-ups**
- PDFs from the legacy system use a different field label ("WO#" vs "Order No.") — extraction will fail on those until Task 3 adds label normalization.
```
