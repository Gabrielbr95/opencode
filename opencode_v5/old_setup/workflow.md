# Workflow

This file is the source of truth for the opencode workflow.
Read it on request when iterating on the opencode setup. Do **not** auto-load it during normal opencode use.
Use it together with `my-context.md` for my constraints and preferences.

### Conceptual model

The workflow is organized into four layers:

| Layer    | Purpose                                                      | Scope       | Primary artifacts     |
| -------- | ------------------------------------------------------------ | ----------- | ----------------------|
| **Why**  | Defines the workflow philosophy, principles, and governance. | Universal   | `workflow.md`         |
| **What** | Defines the current objective, decisions, and progress.      | Per project | `plan/*`              |
| **Who**  | Defines responsibilities and reasoning focus.                | Universal   | `Agents/*`, AGENTS.md |
| **How**  | Defines reusable techniques and procedures.                  | Universal   | `Skills/*`            |

Universal artifacts define how work is performed across all projects.

Project artifacts define the state and decisions of a single project.

Keep these responsibilities separate.

## Default flow

planner -> antagonist (optional) -> builder -> antagonist (optional)

Both reviews are user-invoked by default. Automatic orchestration is an optional workflow.

## Principles

* Increase leverage through selective automation while keeping the workflow human-directed. Agents should automate execution and routine reasoning while leaving important decisions to the user.
* Planning artifacts are the source of truth for the current project. If a design choice matters later, record it explicitly.
* Clarify before planning, and plan before implementation. If something is unclear and materially affects the solution, ask.
* Keep plans small enough to resume after interruptions.
* Prefer the simplest solution that reliably accomplishes the task. Favor local-first, simple, maintainable, and portable designs.
* Optimize for value, not maximum capability. Use the lowest-cost model or workflow that can reliably complete the task, and escalate capability only when necessary.
* Keep the system simple. Reuse existing agents instead of creating new ones unless a new role provides clear value.
* Scope work to match its actual risk. Every project is classified into a tier that calibrates rigor, required artifacts, and acceptable tradeoffs. Always choose the lowest tier that satisfies the stated requirements.

## Tiers

| Tier | Purpose | Optimize for |
|---|---|---|
| `jerryrig` | Run once today, probably discarded tomorrow | Speed |
| `poc` | Answer "can this be done?" — throwaway code | Learning |
| `script` | Recurring personal automation | Simplicity |
| `application` | Small-team software, long-lived | Maintainability |

Tier determines which planning artifacts to produce, how strictly to review, and what coding standards apply. Details in the planner agent and tier-* skills.

## Roles

* **planner**: clarifies the problem and owns the structure of the implementation plan.
* **antagonist**: reviews planning artifacts or completed work from a critical perspective. Has the same editing authority as the planner, but optimizes for correctness, simplicity, maintainability, risk reduction, and identifying overlooked alternatives.
* **builder**: executes one assigned task at a time according to the current planning artifacts. Stops and reports back when the plan is incomplete, inconsistent, or blocked.

## Communication

* Planning artifacts are authoritative for the current project.
* Persistent decisions belong in planning artifacts, not in transient conversations.
* Agents may call other agents during user-invoked orchestration, passing only the context required for the current task.

## Reference documents

Not part of any project. Inform all projects. Not covered by the Conceptual model above.

* `my-context.md` — personal constraints, preferences, and working style. User-edited; agents treat as read-only.
* `AGENTS.md` — always-loaded universal context for every session; distills `my-context.md` into agent instructions. Editable as system configuration, not during normal agent use.
