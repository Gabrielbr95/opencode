tier: script

## High-Level Plan
Watch a shared inbox folder for new PDF work orders. For each new file, extract the work order number, equipment tag, and due date from the first page using pdfplumber, and append a row to a local CSV log. Single Python file. Runs as a long-lived process or on a schedule.

## Blockers / Open Questions
- PDF layout varies between originating systems (SAP export vs scanned form) — needs 2-3 sample files from each source to confirm field extraction logic before Task 2.

## Tasks Checklist

- [ ] Task 1: Scaffold script and CLI arguments
      agent: builder
      files: watch_workorders.py
      depends_on: none
      outcome: Script accepts --watch-dir and --output-csv via argparse. Logging initialised (file + console). Running with --help prints correct usage. No extraction logic yet.

- [ ] Task 2: Implement PDF field extraction
      agent: builder
      files: watch_workorders.py
      depends_on: Task 1
      outcome: extract_fields(path) returns dict with order_number, equipment_tag, and due_date from the first page using pdfplumber. Returns None for any field not found — does not raise. Manual test against two sample PDFs confirms correct extraction.

- [ ] Task 3: Implement folder watcher and CSV append
      agent: builder
      files: watch_workorders.py
      depends_on: Task 2
      outcome: Script watches --watch-dir with watchdog, calls extract_fields on each new .pdf, appends a row to --output-csv with timestamp, filename, and extracted fields. Dropping a PDF into the watched folder produces a new CSV row and a log entry within 3 seconds. Missing fields logged as WARNING, not crash.
