# Architecture — Equipment Work Order Tracker

## Overview

Flask web application with a SQLite database. Single-process, single-machine deployment. Team accesses via browser on the local network. SQLite chosen to avoid any database server installation. Flask chosen for minimal footprint and straightforward routing. All state persists in a single `.db` file — easy to back up and move.

## Folder Structure

```
workorder_tracker/
├── app.py                  # Flask application factory and route registration
├── database.py             # SQLite connection, schema init, migration helper
├── models.py               # Data access functions — no ORM, plain SQL
├── config.py               # Configurable defaults (DB path, host, port)
├── templates/
│   ├── base.html           # Shared layout, nav
│   ├── index.html          # Work order list with filters
│   ├── detail.html         # Single work order view + audit trail
│   └── create.html         # New work order form
├── static/
│   └── style.css           # Minimal styling — no framework
├── tests/
│   ├── test_models.py      # Data access logic tests
│   └── test_routes.py      # Route behaviour tests (Flask test client)
├── requirements.txt
└── README.md
```

## Components

### app.py

**Responsibility**: Flask application setup, route definitions, request handling, template rendering.

**Depends on**: models.py, config.py

**Depended on by**: nothing (entry point)

**Key interfaces**:
- `create_app(config=None) -> Flask` — application factory, used for testing
- Routes: `GET /`, `GET/POST /workorders/new`, `GET /workorders/<id>`, `POST /workorders/<id>/status`

---

### database.py

**Responsibility**: SQLite connection management, schema initialisation, schema migration on startup.

**Depends on**: config.py (for DB path), stdlib sqlite3

**Depended on by**: models.py, app.py (init call on startup)

**Key interfaces**:
- `get_db() -> sqlite3.Connection` — returns connection for current request context
- `init_db()` — creates tables if they don't exist; safe to call on every startup

---

### models.py

**Responsibility**: All database reads and writes. No business logic. Plain SQL functions.

**Depends on**: database.py

**Depended on by**: app.py

**Key interfaces**:
- `create_workorder(data: dict) -> int` — inserts record, returns new ID
- `get_workorder(id: int) -> dict | None`
- `list_workorders(filters: dict) -> list[dict]`
- `update_status(id: int, new_status: str, user: str)` — updates status and appends audit log entry atomically
- `get_audit_trail(id: int) -> list[dict]`
- `export_open_workorders() -> list[dict]`

---

### config.py

**Responsibility**: Centralised configuration defaults. All environment-specific values live here.

**Key values**:
- `DB_PATH` — default `./workorders.db`
- `HOST` — default `0.0.0.0`
- `PORT` — default `5000`

## Data Flow

**Creating a work order**
1. User fills form at `GET /workorders/new`
2. `POST /workorders/new` validates required fields
3. `models.create_workorder(data)` inserts row into `work_orders` table
4. Redirect to `GET /workorders/<id>` (detail view)

**Updating status**
1. User selects next status on detail page, submits
2. `POST /workorders/<id>/status` receives new_status and current user
3. `models.update_status(id, new_status, user)` — single transaction: updates `work_orders.status`, inserts row into `audit_log`
4. Redirect to detail view

## Technology Choices

| Choice | Decision | Why | Rejected alternative |
|---|---|---|---|
| Web framework | Flask | Minimal, well-documented, no magic, easy to deploy | Django — too heavy for this scale; FastAPI — adds async complexity without benefit |
| Database | SQLite | Zero installation, single file, sufficient for <10 concurrent users | PostgreSQL — requires server install, no admin on machine |
| ORM | None — plain SQL | Fewer abstractions, queries are readable, easier to debug | SQLAlchemy — justified at larger scale, overkill here |
| Frontend | Server-side Jinja2 templates | No build step, no JS framework to maintain | React/Vue — adds significant complexity for a form-based internal tool |
| CSS framework | None — minimal custom CSS | No npm, no build toolchain | Bootstrap — fine but adds an external dependency for modest styling needs |

## Configuration

| Parameter | Default | Where | Notes |
|---|---|---|---|
| DB_PATH | ./workorders.db | config.py | Override via environment variable TRACKER_DB_PATH |
| HOST | 0.0.0.0 | config.py | 0.0.0.0 to accept LAN connections |
| PORT | 5000 | config.py | Override via environment variable TRACKER_PORT |

## Error Handling Strategy

- **Validation errors**: caught in route handlers, re-render form with inline error messages. No raw exceptions shown to users.
- **Database errors**: logged at ERROR level with the operation that failed. User sees a plain "Something went wrong" page with a reference to check the log.
- **Missing work order** (invalid ID): 404 response with a clear message.
- **Startup failures** (DB not writable, port in use): log clearly and exit with non-zero code — do not start silently broken.

## Limitations and Known Constraints

- SQLite has write concurrency limits — a single write lock means rapid simultaneous writes may queue briefly. Acceptable for 5-6 users; would need PostgreSQL for higher concurrency.
- No authentication — user identity is name selection only. Not suitable if the tool is ever accessible outside the team's local network.
- No automatic backups — the `.db` file should be included in whatever backup routine the team already uses.
- CSV import from the legacy Excel file is not in scope for v1. Migration is manual for the initial data set.
