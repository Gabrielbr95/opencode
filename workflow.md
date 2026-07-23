# Workflow (v5 Harness)

This file is the conceptual source of truth for the tool-agnostic coding harness.

It describes **how I want to work** at a high level:
- the philosophy behind the harness
- the operating model
- the tier system
- the boundary between durable project truth, agent behavior, and reusable procedures

This document is meant to be read **on demand**, not loaded automatically into every session.
Use it when:
- designing or refactoring the harness
- checking whether agents or skills still match the intended workflow
- resolving policy or boundary confusion
- making major changes to planning, execution, review, or memory behavior

Do **not** treat this file as the day-to-day runtime prompt. That job belongs to the distilled agent-facing files.

## 1. Conceptual Model

The harness is organized into four layers. OpenCode is only the runtime. The harness itself should remain understandable and portable if the runtime changes.

| Layer | Purpose | Scope | Primary Artifacts |
| :--- | :--- | :--- | :--- |
| **Why** | Workflow philosophy, operating principles, and governance intent. | Universal | `workflow.md` |
| **What** | Objective, decisions, durable context, and current project state. | Per project | `plan/*` (durable), `activeContext.md` (resume baton) |
| **Who** | Identities, responsibilities, and decision boundaries of agents. | Universal | `AGENTS.md`, `agents/*` |
| **How** | Reusable procedures, checklists, formatting rules, and execution methods. | Universal | `skills/*`, `rules/*` |

Keep these responsibilities separate.

- `workflow.md` should explain the intended way of working.
- `AGENTS.md` and `agents/*` should encode who owns decisions and how responsibilities are divided.
- `skills/*` should encode reusable procedures.
- `plan/*` should hold durable project truth.
- `activeContext.md` should remain only a short resume baton.

If a concept belongs more naturally in another layer, move it there instead of duplicating it.

## 2. Core Principles

### Human-Directed Leverage
Use AI to increase leverage, not to remove human direction. Agents should automate routine execution and routine reasoning, but meaningful decisions, risky actions, and scope-changing choices should remain visible to the user.

### Learning vs Solving
Before choosing an approach, clarify whether the goal is primarily:
- **solving** a problem,
- **learning** how something works,
- or some mix of both.

If the goal is solving, prefer the simplest reliable path, including existing tools. If the goal is learning, deeper explanation or a custom build can be justified.

### Prevent Reinvention
Before designing custom workflow machinery or code, check whether a mature, cost-effective, local-first tool already solves the problem well enough. Do not build custom systems by default when an existing boring solution is sufficient. Extra complexity must earn its keep through better outcomes, lower risk, or lower total maintenance burden.

### Workflow vs Agentic Control
Prefer predefined workflow when the path is stable, inspectable, and known in advance. Use model-directed control only when dynamic judgment materially improves the result enough to justify the extra complexity, cost, testing difficulty, and control burden.

### A Gradient of Operation Modes
Working modes are a spectrum, not rigid boxes. It should be normal to move between them inside the same project:
1. **Direct Edit:** user asks for a small low-risk change and the primary agent handles it directly.
2. **Human-in-the-loop:** discuss, clarify, plan as needed, execute, and let the user check or approve at the right points.
3. **Autonomous:** after the work is understood and bounded, the system may execute more independently.

The workflow should start with the lightest mode that fits the task and move upward only when the extra autonomy is worth the added complexity.

### Clarify Before Planning, Plan Before Implementation
Do not jump into code before the problem is understood. Clarify first when ambiguity matters. Plan before implementation when the task is large enough or risky enough to need it. Do not confuse planning with execution.

### Value and Efficiency Over Maximum Formality
Optimize for **value and efficiency**, not for maximum ceremony, nor for raw speed. Prefer the simplest approach that reliably accomplishes the task. Use more process only when it materially reduces risk or confusion.

### Solo-Maintainable by Default
The system should be understandable, debuggable, and maintainable by one person working intermittently. Reject complexity that only pays off at larger team scale or under continuous daily development.

### Session-Sized Progress
Work should usually be broken into slices that can produce useful, resumable progress within a short session. Prefer steps that fit real life: limited time, interruptions, and frequent pauses.

### Tool-Agnostic Resilience
The harness should live in plain files under version control. Runtime-specific tools may read the harness, but the core design should survive tool migration with minimal rewriting.

### Tier-Calibrated Effort
The level of planning, verification, documentation, and ceremony should match the actual risk. Always choose the lowest tier that satisfies the need.

### Offline Survivability
Long interruptions are normal. Durable truth should live in project artifacts that survive 14-day offshore gaps. The system should not rely on chat memory or on the human remembering prior reasoning.

### Corporate Safety
Default to local-first behavior. No silent data exfiltration, no hidden network dependencies, no destructive actions without explicit awareness, and no workflow design that assumes admin privileges or relaxed corporate controls.

### Protect Durable Writes
Transient drafting can stay lightweight. Changes that become durable truth, long-lived behavior, repository rules, prompts, skills, config, or future defaults should cross stronger review, provenance, and sometimes approval boundaries.

### Evidence-Driven Improvement
Improve the harness based on observed behavior, real failure modes, and lightweight evaluation rather than taste, verbosity, or theoretical elegance alone. Observability records what happened; evaluation judges whether that behavior was good enough.

## 3. Tier System and Artifacts

The tier defines how much rigor is appropriate. The point of the tier system is to keep effort proportional to risk.

The tier should be stated by the user or inferred and confirmed early. If uncertain, prefer the lower tier unless the risks clearly justify more structure.

| Tier | Purpose | Default Mode | Required Artifacts |
| :--- | :--- | :--- | :--- |
| **Jerryrig** | Run once today, discarded tomorrow. | Direct Edit | *None* |
| **POC** | Answer "can this be done?" | Human-in-the-loop (Light) | `plan/spec.md`, `plan/tasks.md` |
| **Script** | Recurring automation. Needs reliability and logging. | Human-in-the-loop | `plan/spec.md`, `plan/tasks.md`, `plan/decisions.md` |
| **Application** | Long-lived software or small-team tooling. Needs stronger maintainability. | Human-in-the-loop (Strict) | `plan/spec.md`, `plan/architecture.md`, `plan/tasks.md`, `plan/decisions.md` |

Notes:
- `activeContext.md` is **not** a durable design log. It is only the short resume baton.
- Durable decisions, architecture, and project truth belong in `plan/*`.
- Higher tier does **not** mean every task gets maximum ceremony. Work intensity should still be proportional to the actual task.

### Task Status Symbols (`plan/tasks.md`)
- `[ ]` — Pending
- `[>]` — In Progress
- `[x]` — Completed
- `[!]` — Failed / Blocked

## 4. Durable Truth and Memory Boundaries

The system should preserve continuity without turning every conversation into permanent memory.

### Durable Project Truth
`plan/*` is the durable project truth for the current project. If a future session must be able to rely on something, it should usually live there.

### Resume Baton
`activeContext.md` is a short handoff note for restarting after interruption. It should point the next session back to the durable truth, not duplicate it.

### Working Model vs Re-reading
Durable files are authoritative, but they do not need to be reread in full at every step. The intended behavior is:
- rely on the current working model when it is sufficient
- start rereads from the touched files and immediately relevant artifacts
- expand to broader rereads only when uncertainty, contradiction, drift, or session restart justifies it

The goal is honest durable state without wasting effort on repeated full context reacquisition.

### Memory Is Not Context
Memory and context are different layers.

- **Memory** is information intentionally retained for later reuse.
- **Context** is the information actually loaded for the current step.

Do not treat everything visible in a session as something that should persist. Prefer selective durable memory, deliberate retrieval, and compact resume support over replaying large histories.

## 5. Responsibility Model

The harness should center on **one primary session owner**.

That primary agent should:
- talk directly to the user
- infer or confirm tier and mode
- decide when clarification is needed
- decide when planning is needed
- decide when direct execution is appropriate
- decide when a specialized helper is justified

Specialized helper agents may exist, but they should remain narrow and optional. The default shape should be a strong primary agent with a small number of focused specialists, not a large autonomous pipeline.

Examples of useful specialist roles:
- an execution-focused helper for isolated implementation work
- a local exploration helper for reading and summarizing the repository
- an external research helper for docs and outside information
- an independent reviewer for critique in a fresh context window

These are support roles, not co-owners of the session.

### When Delegation Is Justified
Delegation should happen only when it clearly helps with one of these:
1. **Context isolation** — for example, unbiased review or isolated execution.
2. **Token window management** — for example, large codebase exploration.
3. **Token or time efficiency** — for example, offloading repetitive work that does not need to stay in the main thread.

Avoid delegation when it adds more coordination overhead than value.

Delegation is not the same as handoff. The primary session owner should normally retain responsibility for the overall result unless ownership is explicitly transferred.

## 6. Planning and Execution Boundaries

Planning and execution are different kinds of work and should be treated differently.

### Planning
Planning should:
- clarify goals and constraints
- choose the tier and working mode
- define the next meaningful slice
- capture durable requirements, decisions, or architecture only when needed by the tier

Planning should stop when the work is clear enough to proceed safely at the chosen tier. It should not keep expanding just because more detail could be added.

### Execution
Execution should:
- implement the agreed slice
- verify results proportionally to risk
- surface blockers honestly
- update durable artifacts when the changes materially affect project truth

### Work-Type Sensitivity
The workflow should distinguish between:
- **implementation work**
- **planning/documentation work**
- **mixed work**

Tier alone is not enough. High-tier documentation work does not automatically deserve high-tier coding ceremony.

### Reconciliation Boundaries
Honest reconciliation matters, but it should happen at meaningful boundaries such as:
- completion of a task or slice that materially changed code or durable truth
- feature completion
- session wrap
- moments where untouched artifacts would otherwise become misleading

The system should avoid treating every micro-step as a full-project convergence event.

## 7. Control Boundaries

The workflow should distinguish clearly between different kinds of control instead of treating all safety or governance as one thing.

### Policy
Policy guides what the model should try to do:
- when to clarify
- when to use tools
- when to avoid acting
- when to prefer drafting over execution

Policy shapes behavior, but it is not hard enforcement.

### Permissions
Permissions define what the runtime will actually allow. A policy-compliant action can still be forbidden by permissions.

### Guardrails
Guardrails are automatic checks on inputs, outputs, tool calls, or intermediate states. They help catch malformed, unsafe, or suspicious actions, but they do not replace human judgment where consequence is high.

### Approvals
Approvals gate a specific run or action before it continues. Approval is not the same as authorization: authorization asks whether an actor may ever do something; approval asks whether this specific action may proceed now.

### Human-in-the-Loop
HITL is broader than approval. It includes review, edit, override, reject, clarify, or stop. Human involvement is most valuable at consequential boundaries, not as friction on every small step.

### Side Effects Should Drive Friction
Control intensity should rise with consequence.

- low-risk reasoning and drafting should stay smooth
- read-only retrieval should usually stay low-friction
- temporary and reversible internal changes may need light or guarded control
- durable internal mutations should face stronger review
- destructive, privileged, or external side effects should face the strongest control

This keeps low-risk work fluid without under-protecting consequential actions.

## 8. Recommended Operating Flow

This is the intended high-level flow, not a rigid script.

1. **Initiate:** state the objective and establish the tier.
2. **Orient:** determine whether the goal is learning, solving, or both.
3. **Size the work:** decide whether the task should start in direct edit, human-in-the-loop, or autonomous mode.
4. **Clarify:** resolve meaningful ambiguity before planning or implementation.
5. **Explore if needed:** gather only the facts needed for the next decision.
6. **Plan when warranted:** create or refine the required project artifacts for the chosen tier.
7. **Approve major choices:** the user should approve meaningful decisions before risky or broad execution begins.
8. **Execute:** implement the next slice with effort proportional to the task.
9. **Reconcile:** keep touched durable artifacts honest when the boundary crossed justifies it.
10. **Wrap explicitly:** when the user wants to pause, write a short resume baton to `activeContext.md`.

This flow should stay adaptable. It is a guide for how the harness should behave, not a mandate to add ceremony where it is unnecessary.

## 9. Reference Documents

### Human-Facing Source Documents
These may be longer and more expressive because they are not meant to be auto-loaded into every session.

- `my-context.md` — who I am, my constraints, my working style, and the practical realities that should shape recommendations
- `workflow.md` — this file; the conceptual source of truth for how the harness is supposed to work
- `ai-workflow-improvement.md` — design brief and long-term improvement charter for evolving the workflow

### Distilled Agent-Facing Documents
These should encode the operational version of the workflow.

- `AGENTS.md` — universal distilled operating context
- `agents/*` — role definitions and decision boundaries
- `skills/*` — reusable procedures and execution methods

The ideal state is:
- `workflow.md` explains the intended way of working
- `my-context.md` explains the human realities behind it
- the agents and skills encode that intent in a lighter, more operational form

## 10. Design Standard for the Harness Itself

When evolving the harness, prefer changes that make it:
- easier to understand
- easier to resume after interruption
- easier to maintain alone
- less repetitive
- less context-hungry
- more explicit where it matters
- more local-first and portable
- more proportional in its use of rigor
- easier to observe and evaluate at meaningful boundaries

Reject changes that mainly add sophistication, ceremony, or architectural complexity without delivering clear practical value.
