# Architecture — [Project Name]

## Overview

<!--
2-4 sentences. What does this system do, how is it structured, and what are the key technical choices?
A new maintainer should be able to understand the shape of the system from this paragraph alone.
-->

## Folder Structure

<!--
Show the directory tree with a one-line comment per significant file or folder.
Example:

project/
├── main.py           # entry point — CLI arg parsing and orchestration
├── extractor.py      # PDF text extraction logic
├── writer.py         # CSV output and append logic
├── config.py         # constants and configurable defaults
├── tests/
│   └── test_extractor.py
├── requirements.txt
└── README.md
-->

## Components

<!--
One section per significant module or component.
For each:
  - What it does (responsibility)
  - What it depends on
  - What depends on it
  - Key functions or classes (name + 1-line description)
-->

### [Component Name]

**Responsibility**: 

**Depends on**: 

**Depended on by**: 

**Key interfaces**:
- `function_name(args) -> return_type` — description

---

## Data Flow

<!--
Describe how data moves through the system for the primary use case.
A simple numbered list is fine. A diagram (ASCII) if the flow is non-trivial.

Example:
1. User drops PDF into ./watch-dir
2. Watcher detects new file, calls extractor.extract_fields(path)
3. Extractor returns dict {order_number, equipment_tag}
4. Writer appends row to output.csv
5. Log entry written to script.log
-->

## Technology Choices

<!--
One row per significant choice. State what was chosen, why, and what was rejected.

| Choice | Decision | Why | Rejected alternative |
|---|---|---|---|
| PDF parsing | pdfplumber | Handles both text and table extraction; good Windows support | PyPDF2 — text-only, poor table handling |
| Filesystem watch | watchdog | Cross-platform, stable, stdlib-compatible | Polling loop — less efficient, misses rapid sequences |
-->

| Choice | Decision | Why | Rejected alternative |
|---|---|---|---|
| | | | |

## Configuration

<!--
List all configurable values: what they control, where they live, and their defaults.

| Parameter | Default | Where | Notes |
|---|---|---|---|
| --watch-dir | ./input | CLI arg | Directory to monitor for new files |
| --output-csv | ./output.csv | CLI arg | Append destination |
-->

| Parameter | Default | Where | Notes |
|---|---|---|---|
| | | | |

## Error Handling Strategy

<!--
Describe the overall approach to failures:
- What gets logged vs raised vs silently skipped
- How the user is notified of failures
- Recovery behavior (retry, skip and continue, halt)
-->

## Limitations and Known Constraints

<!--
Honest list of what this design does not handle well.
Better to document it now than discover it in production.
-->
