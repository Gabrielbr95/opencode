---
name: review-plan
description: >-
  Pre-implementation design review. Use when the antagonist is reviewing planning
  artifacts (plan/spec.md, plan/architecture.md, plan/tasks.md) before code is
  written. Finds structural weaknesses, unnecessary complexity, and hidden
  assumptions. Load tier-calibration alongside this skill.
---

# Review Plan

Adversarial design critique. Find weaknesses before code is written. No implementation, no plan file edits without explicit approval.

## Process

1. **Read everything**: `plan/tasks.md` (required), `plan/spec.md`, `plan/architecture.md`, and `plan/decisions.md` if present.
2. **Calibrate to tier**: Read the `tier:` field. Load **tier-calibration** and follow its plan-review table.
3. **Audit**: Work through all audit parameters below.
4. **Present findings**: Use the output format. Wait for approval before editing any file.

## Audit Parameters

### Assumptions
- Highlight unverified assumptions that break the code if false.
- Every assumption in spec.md is a potential failure point — verify or flag.

### Scope Creep
- Identify unnecessary abstractions, extra layers, or features out of scope.
- Challenge any custom class, framework, or dependency where stdlib suffices.

### Gaps
- Omitted edge-case boundaries, missing hardware/device protections, safety concerns.
- Missing error handling, config management, or dependency risks.

### Unnecessary Complexity
Look for these specific patterns:
- Interfaces with one implementation.
- Abstract base classes used for a single concrete type.
- Generic solutions to non-generic problems.
- Data that passes through more layers than needed.
- Functions whose only job is to call another function.
- Config systems where hardcoded defaults would work.
- Async where sync would be fine.
- Distributed where monolithic would be fine.
- Pluggable where fixed would be fine.
- More than 3 layers of indirection for a single operation.

Every layer of abstraction has a maintenance cost. An abstraction that saves 10 lines but requires reading 3 files to understand one operation is not a win.

### Simplicity Checklist
- [ ] Can this be a function instead of a class?
- [ ] Can this be a module instead of a package?
- [ ] Can a stdlib solution replace this dependency?
- [ ] Is this abstraction used in more than one place?
- [ ] Does this config option solve a real problem or a hypothetical one?
- [ ] Would a new reader know why this exists without being told?

### Tech Alternatives
- Recommend simpler, robust alternatives with clear tradeoffs for every major choice.

### Task Plan Risks
- Wrong sequence, missing dependencies, bloated tasks.

### Undocumented Decisions
- Architectural choices not recorded in `decisions.md`.

## Output Format

```
Verdict: PROCEED / AMEND / BLOCKED

Critical Blockers
- <breaks feasibility, reliability, or timeline — or "None">

YAGNI Violations
- <simpler path exists>

Complexity Findings
- <pattern found, evidence, why it's a problem, simpler alternative>

Task Plan Risks
- <wrong order, missing dep, bloated task>

Undocumented Decisions
- <architectural choice not recorded in plan/decisions.md>

Open Questions
- <targeted, brief>
```

Report only. Do not rewrite the plan unprompted. Amend only after explicit instruction.
