# Active Context

## Resume Here
- **Tier:** POC
- **Current Slice:** Transition from research to iteration / implementation
- **Current Task:** N/A
- **Next Action:** Start an implementation-focused session, not another broad research session. First read `plan/tasks.md`, `research/index.md`, `my-context.md`, `workflow.md`, and `ai-workflow-improvement.md`. Then inspect the current harness/setup and propose the smallest high-leverage improvement slice using the completed research base. Default stance: iterate with what already exists; only do targeted research if a real implementation decision is blocked.

## Completed This Session
- Built a substantial local research base under `research/` covering agent architectures, skill systems, context engineering, planning systems, evaluation/prompt testing, memory systems, HITL control points, tool-use policy/permissions, prompt modularity/repository architecture, and observability/traceability.
- Added synthesis docs that are meant to guide implementation decisions rather than continue broad theory gathering:
  - `research/vocabulary.md`
  - `research/control-boundaries.md`
  - `research/principles-only.md`
  - `research/memory-policy.md`
  - `research/observability-schema.md`
  - `research/workflow-pattern-comparison.md`
  - `research/evaluation-method-comparison.md`
- Completed `plan/tasks.md` through Slice 11. Slice 12 is still open only as a placeholder for future targeted research if implementation exposes a real gap.
- Reached the conclusion that there is **no major missing core concept** blocking application of the research. The likely next broad topic would be policy-as-code for local-first governance, but it is **not a prerequisite** for starting iteration.
- Reached the stronger conclusion that the project should now shift from broad research to **practical iteration** on the workflow/setup.

## Blockers / Open Questions
- No hard blocker.
- The next session should decide the **first concrete improvement slice** for the current setup rather than continue open-ended research.
- Important framing for the next agent session:
  - the user is an **engineer, not a programmer**; coding is a means to an end
  - be **pragmatic, not purist**
  - the user is a **solo developer** and must be able to understand and maintain the system alone
  - much online advice comes from programmers/researchers operating at much larger scale, so recommendations must be aggressively filtered for small-scale local-first practicality
- Practical implication: prefer the smallest boring improvement that increases leverage, clarity, or safety. Avoid enterprise-style governance, premature multi-agent complexity, or design work that the user cannot realistically maintain.

## Read These First
- `plan/tasks.md`: Shows the completed research slices and that the next phase should be iteration, not more broad topic expansion.
- `research/index.md`: Entry point to the full research base and the synthesis docs most relevant for implementation choices.
- `research/principles-only.md`: The distilled decision rules; best high-level guide before changing the setup.
- `research/control-boundaries.md`: Use this to decide where approvals, permissions, and durable-write controls should actually exist.
- `research/memory-policy.md`: Use this before changing anything related to durable context, task memory, or promotion of state into long-lived artifacts.
- `research/observability-schema.md`: Use this if the next iteration touches traceability, auditability, or debugging visibility.
- `research/workflow-pattern-comparison.md`: Use this to avoid overbuilding the workflow architecture.
- `research/evaluation-method-comparison.md`: Use this to choose lightweight evidence for future workflow changes.
- `my-context.md`: Human-facing source of truth about the user’s constraints, working style, time limits, and cost/maintenance preferences.
- `workflow.md`: Human-facing conceptual source of truth for the harness model, tiers, and operating philosophy.
- `ai-workflow-improvement.md`: Human-facing mission and design brief for improving the AI workflow; reinforces simplicity, composability, maintainability, portability, observability, testability, and incremental change.
