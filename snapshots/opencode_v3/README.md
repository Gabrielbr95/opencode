# OpenCode Agent Framework

This is my personal OpenCode configuration — agents, skills, and templates for software development workflows. It is tuned for solo engineering work in a corporate environment: Windows laptop, no admin, data must stay local, no budget for external services.

---

## Why this exists

I build automation tools for maintenance engineering workflows — scripts that parse PDFs, fill in forms, extract data from systems that don't expose APIs, and produce reports for compliance review. I am not a professional developer. I use AI coding assistants to go faster, but the outputs need to be reliable, maintainable, and auditable.

The problem with vanilla AI coding sessions is that they lose context, jump to implementation before the problem is well-defined, ignore the constraints of my environment, and produce over-engineered solutions to simple problems. This framework exists to fix that by enforcing a deliberate planning and implementation workflow.

---

## Design Decisions

### Why a tiered execution model

Not all problems warrant the same rigor. A one-off CSV conversion and a team-facing work order tracker are fundamentally different things. Treating them the same wastes time on small things and under-engineers important ones.

The four tiers (jerryrig, poc, script, application) force an explicit classification before any work starts. The tier drives everything downstream: which artifacts get written, how much error handling is expected, whether tests are required. This decision is made once per project and documented in line 1 of `tasks.md`.

### Why separate planning and building agents

Planning agents (planner, architect) cannot write source code. Building agents cannot redesign the architecture. This is a hard constraint, not a suggestion. The reason is that mixing planning and building in a single agent produces a common failure mode: the agent starts coding before the problem is fully understood, makes implicit design decisions that are never documented, and produces something that is hard to course-correct.

The separation means the plan is always explicitly approved before code is written.

### Why `tasks.md` as the source of truth

Chat history is not durable. If I switch models, start a new session, or come back after three months, I need to restore context without relying on memory. `tasks.md` is a machine-readable project state: tier, approach, what's done, what's blocked. Every agent reads it first. The orchestrator drives from it entirely.

### Why no ORM, no heavy frameworks in examples

My tools run on a locked-down corporate laptop with no admin. Complex dependency chains are a liability. The application example uses Flask + sqlite3 + plain SQL. This is intentional — it installs cleanly via pip, runs without a database server, and can be understood by anyone who knows Python. SQLAlchemy is fine for a professional team with a DBA; it's overkill for a 5-person maintenance team running a local web app.

### Why the builder is a single agent (not four)

The v1 setup had four separate coding agents (jerryrig, poc, script, application). In practice, I was selecting the agent manually for each task anyway, and the tier was already encoded in `tasks.md`. One builder that reads the tier and calibrates behavior accordingly is simpler. Fewer agents to manage, fewer permission configurations, same outcome.

### Why skills are separate from agents

Skills are reusable behaviors that modify what an agent does for a specific task. An agent owns a role permanently. A skill is loaded on demand for a specific context. This distinction matters because it keeps agent system prompts short and focused, and it lets skills be composed or updated without touching every agent that uses them. The `plan-task_write` skill only loads when the planner is about to write `tasks.md` — not on every message.

---

## Workflow

### Normal (I'm at the keyboard)

```
@planner   → clarifies requirements, classifies tier, writes spec + tasks (+ architecture if application tier)
@architect → optional, on demand, for complex or risky plans — adversarial review before code starts
@builder   → I call this per task, one at a time, with the task number
@reviewer  → optional, on demand, after implementation is complete
```

### Autonomous (unattended)

```
@planner      → produces tasks.md with full task metadata
@architect    → optional review
@orchestrator → runs the full task sequence, skips blockers, reports on return
```

The orchestrator is for "start this and come back in an hour." When I'm watching, I drive directly.

---

## File Structure

```
~/.config/opencode/
├── AGENTS.md                          # Who I am and how I work — loaded by every session
├── agents/
│   ├── planner.md                     # Planning + artifact writing, no code
│   ├── architect.md                   # Adversarial design review, no code
│   ├── builder.md                     # Implementation, tier-calibrated
│   ├── reviewer.md                    # Post-implementation review, no edits
│   └── orchestrator.md                # Autonomous task runner
├── skills/
│   ├── plan-task_write/               # Schema for writing tasks.md
│   ├── plan-task_report/              # Schema for task completion reports
│   ├── plan-create_skill/             # How to create a new skill
│   ├── gen-tier_classifier/           # Classify execution tier
│   ├── gen-jerryrig/                  # Jerryrig tier behavior rules
│   ├── gen-poc/                       # POC tier behavior rules
│   ├── gen-script/                    # Script tier behavior rules
│   ├── gen-application/               # Application tier behavior rules
│   ├── gen-pragmatic_engineer/        # Baseline: busy maintainer, changing requirements
│   ├── gen-simplicity_enforcement/    # Challenge every abstraction
│   ├── gen-dependency_police/         # Challenge every dependency
│   ├── gen-architecture_critique/     # Find unnecessary complexity in design
│   ├── gen-documentation_sync/        # Keep planning docs in sync with code
│   ├── gen-enterprise_auditability/   # Audit trail for regulated workflows
│   ├── gen-debug_mode/                # Root cause analysis protocol
│   ├── gen-playwright_mode/           # Browser automation best practices
│   ├── gen-refactoring_mode/          # Safe complexity reduction
│   └── gen-senior_maintainer_review/  # Review as if the author is gone
├── templates/
│   ├── spec.md                        # Fill-in-the-blank spec template
│   ├── architecture.md                # Fill-in-the-blank architecture template
│   ├── tasks.md                       # Fill-in-the-blank tasks template
│   └── decisions.md                   # Fill-in-the-blank decision log template
└── examples/
    ├── script-example/                # spec.md + tasks.md for a PDF watcher script
    └── application-example/           # spec.md + architecture.md + tasks.md for a web app
```

---

## Skill Naming Convention

```
{auto-}{category}-{name}

category:  plan  — planning knowledge (task writing, reporting)
           gen   — general/cross-cutting (applies across roles and languages)
           exec  — language/framework standards (loaded by builder)

auto-      prefix for agent-generated skills (vs manually authored)
```

Multi-word names use `_` within the name segment.

---

## Constraints This Framework Is Designed For

- Windows, no admin — all tools must install via pip without elevated privileges
- Data locality — nothing leaves the machine except through the approved Claude API
- No budget — free and open source tooling only
- Solo or small team — no dedicated ops, QA, or security review
- Corporate environment — audit trails matter, compliance is a real concern
- Varying project complexity — from one-off scripts to team-facing applications

---

## What This Is Not

- A general-purpose agent framework for any engineer
- A replacement for proper software engineering on production systems
- A security or access control system
- Optimized for large teams or complex deployment pipelines
