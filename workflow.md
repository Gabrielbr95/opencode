# Workflow (v5 Harness)

This file is the conceptual source of truth for the tool-agnostic coding harness.
Read it to understand the philosophy, tier definitions, and working modes.
Do **not** auto-load it during normal agent sessions.

## 1. Conceptual Model

The harness is organized into four layers. OpenCode is merely the runtime; the harness itself is tool-agnostic and designed to survive tool migrations.

| Layer | Purpose | Scope | Primary Artifacts |
| :--- | :--- | :--- | :--- |
| **Why** | Workflow philosophy, principles, and governance. | Universal | `workflow.md` |
| **What** | Objective, decisions, durable context, and current state. | Per Project | `plan/*` (durable), `activeContext.md` (resume baton) |
| **Who** | Identity, constraints, and responsibilities. | Universal | `AGENTS.md`, Subagents |
| **How** | Reusable techniques, procedures, and rules. | Universal | `skills/*`, `rules/*` |

Keep these responsibilities separate. Persistent decisions belong in planning artifacts, not in transient conversations.

## 2. Core Principles

*   **Human-Directed Leverage:** Increase leverage through selective automation while keeping the workflow human-directed. Agents automate execution and routine reasoning; important decisions remain with the user.
*   **A Gradient of Operation Modes:** Working modes are a fluid spectrum, not strict categories. It is expected to switch between them dynamically within a project:
    1. *Direct Edit:* User request → Generalist edits immediately.
    2. *Human-in-the-loop:* User prompt → User/Generalist discussion & planning → Generalist executes → User checks.
    3. *Autonomous:* User prompt → Discussion & planning → Autonomous orchestration and execution.
*   **Task Sizing & Clarification:** Clarify before planning, and plan before implementation. The Generalist must gauge the size and scope of the task upfront. If uncertain or if a choice materially affects the solution, it must ask before acting.
*   **Value & Efficiency:** Optimize for **value and efficiency**, not for maximum quality, nor speed. Prefer the simplest solution that reliably accomplishes the task. Favor local-first, maintainable, and portable designs.
*   **Tool-Agnostic Resilience:** The harness lives in git. Agent platforms (OpenCode, Cursor, etc.) read from it. If the tool changes, 80% of the harness survives.
*   **Tier-Calibrated Effort:** Scope work to match actual risk. Always choose the lowest tier that satisfies the stated requirements.
*   **Offline Survivability:** Keep plans small enough to resume after interruptions. 14-day offshore gaps destroy mental context, so durable truth belongs in `plan/*` while `activeContext.md` stays a short, human-triggered resume baton.
*   **Corporate Safety:** Local-first by default. No silent data exfiltration, no destructive `rm -rf` without explicit approval, and strict logging for audit trails.

## 3. Tier System & Artifacts

The tier dictates the working mode, required planning artifacts, and definition of done. The tier is stated by the user at the start; if unstated, the agent infers and confirms. Planning artifacts are the source of truth for the current project.

| Tier | Purpose | Default Mode | Required Artifacts |
| :--- | :--- | :--- | :--- |
| **Jerryrig** | Run once today, discarded tomorrow. | Direct Edit | *None* |
| **POC** | Answer "can this be done?" | Human-in-loop (Light) | `plan/spec.md`, `plan/tasks.md` |
| **Script** | Recurring automation. Needs logging. | Human-in-loop | `plan/spec.md`, `plan/tasks.md`, `plan/decisions.md` |
| **Application** | Long-lived software. Needs tests/docs. | Human-in-loop (Strict) | `plan/spec.md`, `plan/architecture.md`, `plan/tasks.md`, `plan/decisions.md` |

*(Note: `activeContext.md` is a short resume baton, not a durable design log. Durable decisions, vocabulary, and architecture belong in `plan/*`.)*

### Task Status Symbols (`plan/tasks.md`)
*   `[ ]` — Pending
*   `[>]` — In Progress (Agent marks this *before* touching code to prevent silent failures)
*   `[x]` — Completed
*   `[!]` — Failed / Blocked

## 4. Roles (Single Generalist + Specialist Subagents)

The multi-agent pipeline is dead. A single primary agent handles the session, orchestrating stateless subagents only for very specific reasons.

*   **The Generalist (Default):** Your primary pair programmer. Its main activity is coding, but it also handles coding-adjacent inquiries (explaining concepts, technical research, discussing ideas). It manages discussion, inferring tiers, planning, and core implementation.
*   **Coder (Subagent):** Execution worker. Dispatched by the Generalist for parallelization or when context isolation makes sense for a specific implementation block.
*   **Explorer (Subagent):** Inward-looking scout. Dispatched via task to grep, read, and summarize local codebases.
*   **Researcher (Subagent):** Outward-looking scout. Dispatched to fetch docs, scrape the web, and return summarized technical answers with source links.
*   **Reviewer (Subagent):** Adversarial critic. Dispatched manually, or by the Generalist, to review code or plans in a fresh, unbiased context window.

### Subagent Dispatch Rules
When agents call subagents, they pass *only the context required for the current task*. The Generalist calls subagents strictly for one of three reasons:
1. **Context isolation:** Preventing bias or cross-contamination (e.g., code review, isolated coding).
2. **Token window management:** Keeping the main session from becoming bloated (e.g., deep codebase scans).
3. **Token saving:** Offloading heavy repetitive tasks to save costs.

### Orchestration Execution
The `orchestrate-batch` skill is **never** called autonomously by the agent. It is strictly triggered by the user to coordinate autonomous work and optional parallelization across multiple tasks.

## 5. Reference Documents

*   **Human-Facing Only (DO NOT LOAD INTO AGENTS):**
    *   `my-context.md` — Personal constraints, preferences, and working style.
    *   `workflow.md` — This file.
    *   *Note:* These files are too verbose for the agent's context window. They serve as the source of truth for the human to design and refine the system.
*   **Agent-Facing Context:**
    *   `AGENTS.md` — Always-loaded universal context for every session. This is the highly distilled, strictly operational version of `my-context.md`.

## 6. Standard Operating Procedure

1.  **Initiation:** State the objective and the Tier.
2.  **Sizing & Mode Selection:** Generalist gauges the task. Determines where on the gradient (Direct Edit, Human-in-the-loop, or Autonomous) the flow should begin.
3.  **Exploration:** Generalist dispatches Explorer/Researcher subagents to gather facts without polluting main context (if token window management is needed).
4.  **Planning:** Generalist writes the required artifacts in `plan/` based on the Tier and structures `plan/tasks.md` as outcome-level slices containing sequential micro-tasks.
5.  **Approval:** You review and approve the `plan/` files.
6.  **Execution:** Depending on the current mode, Generalist implements directly, loops you in for checks, or you invoke the `orchestrate-batch` skill for autonomous execution. Modes can shift fluidly during this step. Tasks are marked sequentially (`[>]` → `[x]` or `[!]`). After 3 failed troubleshooting loops, the task is marked `[!]` and escalated instead of being brute-forced indefinitely.
7.  **Converge:** Before declaring a slice or feature done, Generalist reconciles code, tasks, and durable artifacts. Missing work becomes new tasks instead of being silently ignored.
8.  **Wrap Session:** You trigger the `/wrap-session` skill. The Generalist writes only the resume baton—current state, blockers, and next steps—to `activeContext.md`.
