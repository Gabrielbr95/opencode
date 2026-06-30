# Workflow

This file is the source of truth for the opencode workflow.
Read it on request when iterating on the opencode setup. Do **not** auto-load it during normal opencode use.
Use it together with `my-context.md` for my constraints and preferences.

### Conceptual model

The workflow is organized into four layers:

| Layer    | Purpose                                                      | Scope       | Primary artifacts |
| -------- | ------------------------------------------------------------ | ----------- | ----------------- |
| **Why**  | Defines the workflow philosophy, principles, and governance. | Universal   | `workflow.md`     |
| **What** | Defines the current objective, decisions, and progress.      | Per project | `plan/*`          |
| **Who**  | Defines responsibilities and reasoning focus.                | Universal   | Agents            |
| **How**  | Defines reusable techniques and procedures.                  | Universal   | Skills            |

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

## Roles

* **planner**: clarifies the problem and owns the structure of the implementation plan.
* **antagonist**: reviews planning artifacts or completed work from a critical perspective. Has the same editing authority as the planner, but optimizes for correctness, simplicity, maintainability, risk reduction, and identifying overlooked alternatives.
* **builder**: executes one assigned task at a time according to the current planning artifacts. Stops and reports back when the plan is incomplete, inconsistent, or blocked.

## Communication

* Planning artifacts are authoritative for the current project.
* Persistent decisions belong in planning artifacts, not in transient conversations.
* Agents may call other agents when appropriate, passing only the context required for the current task.

## Supporting files

* `my-context.md`: the source of truth for personal constraints and preferences.
* `plan/*`: the source of truth for the current project's implementation plans, decisions, open questions, and progress.
* Skills: reusable implementation knowledge and procedures.
