tier: jerryrig

## High-Level Plan
Convert exported session JSON into a markdown transcript with a single small Python script, keeping the full transcript format and timestamps.

## Blockers / Open Questions
- None

## Tasks
- [x] **1. Implement JSON-to-Markdown converter**
  - **Description**: Add a one-file Python script that reads an OpenCode session export JSON file and writes a markdown transcript in the requested format.
  - **Files**: `json_convertet.py`, `plan/session7_export.md`
  - **Depends on**: none
  - **Acceptance**: Running `python json_convertet.py plan/session7_export.json` produces a markdown file with `## USER` / `## ASSISTANT` sections, timestamps, and preserved tool call blocks.
  - **Outcome**: `plan/session7_export.md` exists and is readable as a transcript export.

- [x] **2. Remove tool call outputs**
  - **Description**: Adjust the converter so tool call blocks keep only the input payload and omit tool outputs.
  - **Files**: `json_convertet.py`
  - **Depends on**: Task 1
  - **Acceptance**: Tool blocks in the markdown contain `Input:` and no `Output:` lines.
  - **Outcome**: Regenerated transcript is shorter and only records tool call inputs.
