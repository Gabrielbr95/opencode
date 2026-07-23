---
name: plan-project
description: Model-invoked. The procedure for planning a new project, feature, or other bounded work when planning is warranted.
---

# Plan Project
**Triggered by:** The user requesting a new project, feature, script, or other bounded work that needs planning, and after the requirements are clarified.

This skill governs planning only. Use it when planning is actually warranted by the tier, scope, or risk. Once the plan is approved, execution passes to the relevant execution workflow.

## Procedure
1. **Identify Tier:** Confirm the project Tier with the user (Jerryrig, POC, Script, or Application).
2. **Load Tier Rules:** Load the matching tier skill before planning or execution (`tier-jerryrig`, `tier-poc`, `tier-script`, or `tier-application`).
3. **Check Whether Planning Is Needed:** If the work is already clear, low-risk, and small enough not to justify planning overhead, do not force this skill. If planning is warranted, continue.
4. **Jerryrig Tier:** Stop. Do not write planning artifacts unless the user explicitly asks for them. Proceed with the lightest workable execution path.
5. **Draft the Plan with Progressive Disclosure:**
   - Load the relevant formatters as needed by tier and scope: `format-spec`, `format-tasks`, `format-decisions`, `format-architecture`.
   - Write the required artifacts for the tier.
     - **POC**: `plan/spec.md`, `plan/tasks.md`
     - **Script**: `plan/spec.md`, `plan/tasks.md`, `plan/decisions.md`
     - **Application**: `plan/spec.md`, `plan/architecture.md`, `plan/tasks.md`, `plan/decisions.md`
6. **Outline First, Refine Selectively:** Draft the outline of the full plan up front, then refine only the next execution slice or the user-requested slices in more detail. Keep the overall shape visible without forcing every later step to be fully detailed immediately, unless the user explicitly asks for a fully detailed plan up front.
7. **Task Structure Check:** Ensure `plan/tasks.md` is organized into outcome-level slices, with sequential tasks under each slice.
8. **Task Granularity Check:** Size tasks relative to the work:
   - implementation-heavy work may use finer-grained tasks
   - planning/docs work may use coarser outcome-oriented tasks
   - avoid universal 2-5 minute micro-tasking when it adds ceremony without reducing risk
9. **Verification Check:** Ensure tasks include a clear way to tell whether they are done, but keep verification proportional to the work. Planning/docs tasks may use lightweight consistency checks instead of code-grade verification.
10. **Decision Discipline Check:** Surface major decisions for user approval. Handle minor, low-risk, or easily reversible decisions autonomously when that keeps work moving. Log only decisions that materially affect architecture, dependencies, user workflow, or later resume clarity.
11. **Planning Sufficiency Check:** The plan is sufficient when the full path is outlined, the next execution slice is actionable, and the remaining uncertainty outside that slice can be handled later without avoidable confusion or risk.
12. **Approval:** Present the plan to the user and wait for explicit approval before broad or risky execution begins. Do not keep expanding minor details just to make the plan more complete if the outline is clear and the next step is ready.
