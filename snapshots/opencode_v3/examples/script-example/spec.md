# Spec — PDF Work Order Inbox Watcher

## Problem

New work orders arrive as PDF files dropped into a shared folder on the network drive. Engineers manually open each file, copy the work order number, equipment tag, and due date into a spreadsheet. This takes 5-10 minutes per batch and is done inconsistently — some fields get missed, dates get transcribed wrong.

## Goal

Automatically extract key fields from incoming PDF work orders and append them to a CSV log, eliminating manual transcription for routine work order intake.

## Scope

### In Scope
- Monitor a specified folder for new .pdf files
- Extract work order number, equipment tag, and due date from each PDF
- Append one row per PDF to a CSV log file
- Log all activity (processed, extracted values, failures) to a log file

### Out of Scope
- UI or dashboard — CSV output only
- Handling non-PDF files
- Uploading data to any system
- Parsing PDFs older than those already in the watch folder at start time
- Email or notification alerts

## Users

Single user: the engineer who runs the script. Runs on a corporate Windows laptop. No admin privileges. Technically capable of running Python scripts from the command line.

## Inputs

- PDF files dropped into a watch folder (network drive or local)
- Two source formats in practice:
  - SAP-generated PDF exports (machine-readable text)
  - Scanned maintenance forms (some may be image-only — extraction may fail)

## Outputs

- `output.csv` — one row per processed PDF: timestamp, filename, order_number, equipment_tag, due_date
- `watch_workorders.log` — all activity, warnings for missing fields, errors for unreadable files

## Constraints

- Windows, no admin — all dependencies must install via pip without elevated privileges
- No network calls — processes files locally, writes locally
- Must not delete or modify input PDFs
- Must not crash on a bad PDF — log the error and continue

## Acceptance Criteria

- Dropping a valid PDF into the watch folder produces a new CSV row within 3 seconds
- All three fields extracted correctly from the two known PDF formats
- A PDF with no extractable text logs a WARNING and continues — does not halt the watcher
- Running with --help shows usage
- Log file records: filename, extracted values, timestamp for every processed file

## Open Questions

- Are there more than two PDF layout variants in use? → Engineer to collect 5 sample files before Task 2 starts.
- Should PDFs from the folder on startup be processed, or only new arrivals? → Decided: new arrivals only (simpler, avoids reprocessing).
