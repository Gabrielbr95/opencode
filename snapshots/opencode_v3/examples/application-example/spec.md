# Spec — Equipment Work Order Tracker

## Problem

The maintenance team tracks open work orders in a shared Excel file that multiple people edit manually. The file gets corrupted occasionally, version conflicts are common, and there is no audit trail of who changed what. When work orders are closed late, nobody is sure who last touched the record. Compliance audits require showing the history of status changes for safety-critical equipment.

## Goal

Replace the shared Excel tracker with a local web application that multiple team members can use simultaneously, that enforces required fields, and that keeps a complete audit log of every status change.

## Scope

### In Scope
- Create, view, update, and close work orders
- Required fields: WO number, equipment tag, description, assigned to, due date, status
- Status transitions: OPEN → IN PROGRESS → PENDING APPROVAL → CLOSED
- Full audit log: every status change logged with user, timestamp, previous and new value
- Simple user identification — no passwords, just name selection at login (internal tool, not security-critical)
- Export current open work orders to CSV
- Local deployment — runs on one machine, team accesses via browser on the local network

### Out of Scope
- Integration with SAP or any external system
- Email notifications
- File attachment handling
- Mobile-optimised UI
- User authentication / access control beyond name selection
- Reporting or dashboards beyond the basic work order list

## Users

4-6 maintenance engineers and one supervisor. All on the same local network. Comfortable using a browser but not technical users. The tool will be explained in a 10-minute walkthrough.

## Inputs

- Manual data entry via web form
- Optional: bulk import from CSV for initial data migration from the Excel file

## Outputs

- Work order list view (filterable by status, assignee, equipment tag)
- Audit trail view per work order
- CSV export of open work orders

## Constraints

- Must run locally — no cloud hosting, no external network access
- Windows server (or the engineer's laptop as a temporary host)
- No admin on client machines — access via browser only
- SQLite database — no separate database server installation
- Must support at least 5 concurrent users without noticeable lag
- Audit log must be tamper-evident — append-only, not editable through the UI

## Acceptance Criteria

- A work order can be created, progressed through all status stages, and closed
- Every status change appears in the audit log with user, timestamp, old status, new status
- Two users can update different work orders simultaneously without conflict
- Exporting open work orders produces a valid CSV with correct data
- If the server restarts, all data is preserved and the application starts correctly

## Open Questions

- What is the initial data migration path from Excel? → Needs sample Excel file to design import logic. Deferred to a later phase if not critical for launch.
- Who hosts the server? → Engineer's laptop initially; move to a shared machine later if adopted.
