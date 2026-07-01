---
name: plan-project
description: Model-invoked. The procedure for generating a project plan before coding begins. Loads when the user asks to start a new project or feature.
---

# Plan Project
**Triggered by:** The user requesting a new project, feature, or script, and after the requirements are clarified.

## Procedure
1. **Identify Tier:** Confirm the project Tier with the user (Jerryrig, POC, Script, or Application).
2. **Load Tier Rules:** Load the matching tier skill before planning or execution (`tier-jerryrig`, `tier-poc`, `tier-script`, or `tier-application`).
3. **Jerryrig Tier:** Stop. Do not write any planning artifacts. Proceed directly to execution.
4. **Draft the Plan:** 
   - Load the relevant formatters (`format-spec`, `format-tasks`, etc.).
   - Write the required artifacts for the tier.
     - **POC**: `plan/spec.md`, `plan/tasks.md`
     - **Script**: `plan/spec.md`, `plan/tasks.md`, `plan/decisions.md`
     - **Application**: `plan/spec.md`, `plan/architecture.md`, `plan/tasks.md`, `plan/decisions.md`
5. **Task Structure Check:** Ensure `plan/tasks.md` is organized into outcome-level slices, with sequential micro-tasks under each slice.
6. **Task Granularity Check:** Ensure every task represents 2-5 minutes of work and includes a verification step.
7. **Approval:** Present the plan to the user and wait for explicit approval before writing any code.
