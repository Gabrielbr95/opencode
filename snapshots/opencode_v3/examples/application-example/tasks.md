tier: application

## High-Level Plan
Flask + SQLite web app replacing a shared Excel work order tracker. Server-side rendered with Jinja2 templates. No ORM — plain SQL via sqlite3. Deployed locally; team accesses via browser on the LAN. Audit log is append-only and written in the same transaction as every status change.

## Blockers / Open Questions
- Initial data migration from Excel is deferred to a later phase — not required for launch.
- Hosting machine not confirmed (engineer's laptop for now, move later if adopted).

## Tasks Checklist

- [ ] Task 1: Initialise project structure and database schema
      agent: builder
      files: app.py, database.py, config.py, requirements.txt
      depends_on: none
      outcome: Running `python app.py` starts Flask on port 5000 with no errors. `work_orders` and `audit_log` tables created in workorders.db on first run. `python -m pytest tests/` passes (empty test suite is fine at this stage).

- [ ] Task 2: Implement data access layer
      agent: builder
      files: models.py, tests/test_models.py
      depends_on: Task 1
      outcome: create_workorder, get_workorder, list_workorders, update_status, get_audit_trail, and export_open_workorders functions implemented with plain SQL. update_status writes to both tables atomically. `pytest tests/test_models.py` passes covering: create and retrieve a WO, status update produces audit entry, list filters by status.

- [ ] Task 3: Implement work order list and detail routes
      agent: builder
      files: app.py, templates/base.html, templates/index.html, templates/detail.html
      depends_on: Task 2
      outcome: `GET /` renders list of work orders with status filter. `GET /workorders/<id>` renders detail view with full audit trail. Visiting an invalid ID returns 404 with a readable message. Manual check in browser confirms both pages render correctly against a seeded test record.

- [ ] Task 4: Implement create and status update routes
      agent: builder
      files: app.py, templates/create.html, tests/test_routes.py
      depends_on: Task 3
      outcome: `GET/POST /workorders/new` renders form and creates record on valid submit, re-renders with inline error on missing required fields. `POST /workorders/<id>/status` updates status and redirects to detail. `pytest tests/test_routes.py` passes covering: successful create, missing field rejected, valid status transition recorded in audit log.

- [ ] Task 5: Implement CSV export
      agent: builder
      files: app.py
      depends_on: Task 4
      outcome: `GET /export/open` returns a CSV file download containing all OPEN and IN PROGRESS work orders. File has correct headers and one row per matching record. Manual test confirms download works in browser and CSV opens correctly in Excel.

- [ ] Task 6: Write README
      agent: builder
      files: README.md
      depends_on: Task 5
      outcome: README covers: purpose, requirements, setup (pip install + first run command), how to access from another machine on the LAN, how to back up the database. A new user with no prior context can set up and run the tool by following it.
