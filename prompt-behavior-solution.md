# Prompt Behavior Solution Map

## Purpose
This note maps the previously discussed behavior fixes to the current prompt files in this opencode config.

It is **not** an implementation diff.
It is a file-by-file change plan for a later editing session.

It addresses the problems captured in:
- `prompt-behavior-problems.md`

---

## Design Intent
Keep the strengths of the harness:
- durable project truth in `plan/*`
- explicit task state
- good safety for real implementation work
- resume reliability after long gaps

Reduce the costs that showed up in planning-heavy sessions:
- repeated full rereads of durable files
- code-grade verification loops on documentation/planning work
- state synchronization on every micro-step
- planning refinement that keeps expanding before coding begins

---

## Core Policy Changes To Encode
These are the cross-cutting behavior changes that should appear across multiple files.

### 1. Classify work type before choosing workflow intensity
The agent should distinguish between:
- **implementation**
- **planning/docs**
- **mixed**

Tier alone is not enough.
An Application-tier documentation refinement task should not automatically receive Application-tier coding ceremony.

### 2. Prefer the lightest sufficient loop
The operating prompt layer should explicitly say:
- use the lightest procedure that preserves reliability
- do not apply code-grade verification to planning/docs work by default
- optimize for session-level efficiency, not only local explicitness

### 3. Use delta-based rereads by default
The agent should:
- rely on its current working model when sufficient
- reread only the touched or relevant durable artifacts first
- expand to broader rereads only when uncertainty, contradiction, or broad drift justifies it

### 4. Move full convergence/sync to meaningful boundaries
Heavy reconciliation should be the default at:
- slice completion
- feature completion
- wrap-session
- broad design-impacting changes

It should **not** be the default after every small planning or wording edit.

### 5. Add a planning sufficiency stop condition
The planning workflow should explicitly stop refining when the next execution slice is clear enough to start safely.

---

## Recommended Structural Direction

### Recommended
Keep the same general skills, but make them branch internally based on:
- work type
- scope of delta
- boundary crossed

### Not recommended
Do **not** create many near-duplicate skills that perform lighter or heavier versions of the same job.
That would increase maintenance burden and prompt surface area.

### Merge candidate
`converge-work` and `sync-artifacts` are strong candidates for consolidation into a single reconciliation skill.
Reason:
- they operate on almost the same inputs
- they often trigger back-to-back
- they both compare reality against durable truth
- keeping both encourages duplicate rereads and duplicate reasoning

If merged later, the merged skill should still support two modes:
- **inspect-only**
- **inspect-and-update**

Suggested replacement name:
- `reconcile-work`

If not merged, both existing skills still need lighter triggers and delta-first behavior.

---

# File-by-File Change Map

## 1. `AGENTS.md`

### Role in the problem
This file sets the universal operating bias.
Right now it strongly reinforces:
- durable truth in `plan/*`
- strict task state discipline
- anti-drift behavior
- safety-first explicitness

Those are good principles, but there is no equally strong counterweight for:
- session efficiency
- selective rereads
- lighter treatment of planning/docs work

### Intended changes
Add explicit top-level rules such as:
- classify the current work as implementation, planning/docs, or mixed before selecting workflow intensity
- prefer the lightest workflow that preserves reliability
- do not repeatedly reread durable artifacts when a sufficient working model already exists
- prefer delta-based rereads over full durable-context reacquisition
- batch bookkeeping when immediate propagation is not necessary to avoid misleading future work
- optimize for session-level efficiency, not just local explicitness

### Why here
If this counterweight is not in `AGENTS.md`, the heavier skills will keep winning by default.

---

## 2. `agents/generalist.md`

### Role in the problem
This file is light, but it governs the primary agent's behavior.
It currently says the Generalist owns planning, execution, and delegation, but it does not explicitly require work-type classification before choosing a heavy or light process.

### Intended changes
Add guidance that the Generalist should:
- classify work type first
- choose the lightest sufficient workflow for that work type
- avoid unnecessary subagent loops for planning/docs work
- treat reviewer dispatch as conditional, not default, outside risky implementation work

### Why here
This makes the branching behavior a first-class responsibility of the session owner.

---

## 3. `agents/reviewer.md`

### Role in the problem
This file forces the Reviewer to:
- load `review-code`
- take an adversarial stance

That is appropriate for risky code review.
It is too aggressive as a default stance for planning/docs work.

### Intended changes
Keep the reviewer adversarial for real code review, but update the prompt so the reviewer can:
- respect review mode selected by the Generalist
- apply strict adversarial review for implementation work
- apply lighter consistency-oriented review for planning/docs work
- avoid broad rereads unless the review target suggests broader drift

### Why here
Without this change, any reviewer dispatch tends to become expensive by default.

---

## 4. `agents/coder.md`

### Role in the problem
Minimal. The Coder is not the main source of the planning-session overhead.

### Intended changes
Probably none, or only a minor clarification that the Coder is primarily for implementation tasks, not for routine documentation reshaping.

### Why here
The main problem is upstream workflow selection, not the Coder prompt itself.

---

## 5. `skills/plan-project/SKILL.md`

### Role in the problem
This skill is one of the strongest drivers of planning-depth runaway.
Current pressure points:
- required artifact generation by tier
- task structure check
- universal 2-5 minute task granularity
- verification on every task
- approval before coding

This drives the system toward increasingly detailed contract-writing before execution begins.

### Intended changes
Update this skill so that it:
- explicitly classifies whether the current planning effort is for implementation-heavy work or planning/docs work
- allows task granularity to vary by work type
- does not require universal 2-5 minute micro-tasks for planning/docs work
- states a clear stopping rule for planning sufficiency
- says planning is sufficient when the next execution slice is actionable, constraints are captured, and remaining uncertainty is small enough to resolve during execution
- encourages moving to implementation once that threshold is met

### Why here
This is the main place to stop planning from expanding indefinitely while still feeling "safe."

---

## 6. `skills/format-tasks/SKILL.md`

### Role in the problem
This skill amplifies verification fan-out and state-management inflation by enforcing:
- strict micro-tasking
- sequentiality
- verification on every task

That is useful for execution-heavy work.
It is too expensive for planning/docs sessions.

### Intended changes
Change this skill so that:
- task granularity depends on work type
- implementation tasks can stay relatively fine-grained
- planning/docs tasks may be coarser and outcome-oriented
- verification language for planning/docs tasks can be lightweight, such as internal consistency or stale-reference checks
- the file can still remain sequential, but without forcing unnecessary micro-fragmentation

### Why here
This reduces the number of ceremony boundaries that trigger claim/verify/review/sync overhead.

---

## 7. `skills/workflow-execute/SKILL.md`

### Role in the problem
This skill applies a strict code-grade task loop:
- claim task
- implement
- verify
- troubleshoot
- mark complete or blocked

That loop is good for implementation.
It is too heavy for planning/docs edits.

### Intended changes
Keep a single skill, but make it branch internally.

#### Branch A: implementation work
Keep the current strict loop largely intact.

#### Branch B: planning/docs work
Use a lighter loop:
- claim the task only if task tracking is warranted for the session
- edit the targeted artifacts directly
- perform a consistency check rather than code-style verification
- escalate to heavier verification only if the change materially affects implementation, creates ambiguity, or changes core contract meaning
- avoid diagnose-bug style troubleshooting patterns for ordinary documentation adjustments

### Why here
This is the main place to stop applying code-grade execution ritual to low-risk planning/doc maintenance.

---

## 8. `skills/review-code/SKILL.md`

### Role in the problem
This skill is a major driver of verification fan-out.
It currently behaves like a universal post-work strict review process and points to `converge-work` afterward.

### Intended changes
Keep one review skill, but add an initial classification step.

#### Stage 0: classify review target
- implementation
- planning/docs
- mixed

#### If implementation
Keep the current stricter review structure.

#### If planning/docs
Review for:
- internal contradiction
- stale references
- misleading wording
- scope drift
- mismatch with touched tasks or decisions
- terminology inconsistency in touched artifacts

For planning/docs review, do **not** default to:
- adversarial PASS/FAIL loops
- full rereads of all durable artifacts
- repair cycles unless the inconsistency is material

### Why here
This keeps one review skill while preventing code-grade review from leaking into every documentation task.

---

## 9. `skills/converge-work/SKILL.md`

### Role in the problem
This is probably the strongest single inducer of context reacquisition bias.
It explicitly instructs the agent to reread the durable truth and reconcile everything before declaring work complete.

### Intended changes if kept separate
Change it from a universal full-reread checkpoint into a boundary-based, delta-first reconciliation process.

It should:
- start from the claimed scope and touched artifacts
- read only the relevant durable files first
- expand to broader rereads only if contradiction, ambiguity, or likely broad drift appears
- run full convergence mainly at slice/feature/session boundaries
- avoid treating every small planning edit as a full convergence event

### Intended changes if merged with `sync-artifacts`
This skill would likely disappear and be replaced by a merged reconciliation skill.
In that case, the merged skill should handle:
- drift detection
- backlog updates
- touched durable-file updates
- honest completion decisions

### Why here
This is the central fix for repeated expensive reacquisition of durable context.

---

## 10. `skills/sync-artifacts/SKILL.md`

### Role in the problem
This skill turns anti-drift correctness into a standing synchronization obligation.
Its current wording strongly encourages immediate durable-file alignment.

### Intended changes if kept separate
Change it so that:
- sync starts with touched artifacts only
- broader sync happens only when untouched durable files would become misleading
- sync is expected at meaningful boundaries, not every micro-step
- batching durable updates is acceptable when immediate full propagation is unnecessary

### Intended changes if merged with `converge-work`
This skill would likely be removed and its update logic folded into a merged reconciliation skill.

### Why here
This is the main fix for state-management inflation.

---

## 11. `skills/wrap-session/SKILL.md`

### Role in the problem
This skill currently forces:
- `converge-work`
- `sync-artifacts`
- rereading of current project state and relevant durable files
before writing the resume baton.

That is safe, but expensive.

### Intended changes
Make wrap behavior conditional.
It should say:
- if the session materially changed code or durable docs in a way that could mislead the next session, reconcile first
- otherwise write the baton from the current known state without forcing a heavy full reconciliation pass
- keep `activeContext.md` short and avoid duplicating durable truth

### Why here
This prevents wrap-up from always becoming another full project-state reacquisition cycle.

---

## 12. `skills/tier-application/SKILL.md`

### Role in the problem
This skill is not the root problem, but it reinforces high rigor.
That rigor is valid for implementation work and can spill into planning/docs work when the system lacks branching rules.

### Intended changes
Probably minimal.
At most, clarify that these rules apply primarily to implementation work, not to all planning or documentation tasks under Application tier.

### Why here
The issue is not that Application tier is too strict.
The issue is that its strictness is leaking into the wrong work types.

---

## 13. `skills/diagnose-bug/SKILL.md`

### Role in the problem
Low. This is not a core cause of the planning-session overhead.

### Intended changes
Probably none.
At most, ensure it is not pulled into planning/docs tasks that are merely inconsistent or underspecified rather than truly bugged.

---

## 14. `skills/orchestrate-batch/SKILL.md`

### Role in the problem
Secondary.
This skill hardcodes a coder-reviewer loop for batched execution.
That is acceptable for autonomous implementation batches.
It is not a good template for planning/docs restructuring.

### Intended changes
Probably minimal.
Maybe clarify that this workflow is intended for implementation execution, not default documentation maintenance.

---

## 15. `skills/grill-me/SKILL.md`

### Role in the problem
Secondary, but it can amplify planning-depth runaway.
It currently says to continue until there is absolutely zero ambiguity.

### Intended changes
Relax the stopping rule slightly.
Prefer something like:
- continue until ambiguity is reduced enough to plan or execute safely at the current tier
- do not force exhaustive interrogation when remaining uncertainty can be handled cheaply during execution

### Why here
This helps prevent infinite clarification before doing real work.

---

# Combined Recommendation Summary

## Highest-priority files to change
If editing later, start here:
1. `AGENTS.md`
2. `skills/plan-project/SKILL.md`
3. `skills/format-tasks/SKILL.md`
4. `skills/workflow-execute/SKILL.md`
5. `skills/review-code/SKILL.md`
6. `skills/converge-work/SKILL.md`
7. `skills/sync-artifacts/SKILL.md`
8. `skills/wrap-session/SKILL.md`

## Recommended merge
Strongly consider merging:
- `skills/converge-work/SKILL.md`
- `skills/sync-artifacts/SKILL.md`

into one reconciliation skill.

## Keep mostly unchanged
- `agents/coder.md`
- `agents/explorer.md`
- `agents/researcher.md`
- `skills/diagnose-bug/SKILL.md`
- `skills/tier-jerryrig/SKILL.md`
- `skills/tier-poc/SKILL.md`
- `skills/tier-script/SKILL.md`

---

# Practical Editing Order For A Future Session

## Pass 1: Add missing top-level counterweights
Edit:
- `AGENTS.md`
- `agents/generalist.md`

Goal:
- classify work type first
- prefer lightest sufficient loop
- prefer delta-based rereads

## Pass 2: Stop planning runaway
Edit:
- `skills/plan-project/SKILL.md`
- `skills/format-tasks/SKILL.md`
- optionally `skills/grill-me/SKILL.md`

Goal:
- variable task granularity
- explicit planning sufficiency stop condition

## Pass 3: Stop code-grade treatment of doc work
Edit:
- `skills/workflow-execute/SKILL.md`
- `skills/review-code/SKILL.md`
- `agents/reviewer.md`

Goal:
- branch by work type
- lighter planning/docs review path

## Pass 4: Reduce reconciliation overhead
Edit or merge:
- `skills/converge-work/SKILL.md`
- `skills/sync-artifacts/SKILL.md`
- `skills/wrap-session/SKILL.md`

Goal:
- delta-first behavior
- boundary-based full reconciliation
- fewer repeated full durable-context rereads

---

# Final Position
The main fix is **not** to weaken the harness into informality.
The main fix is to make the operational layer distinguish:
- risky implementation work
from
- lower-risk planning/docs maintenance

and to make rereads, review intensity, and state propagation depend on:
- work type
- delta scope
- boundary crossed

That preserves discipline while reducing the context hunger that appeared in the planning-heavy session.
