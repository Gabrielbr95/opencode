# Workflow Improvement Cycle

This document defines the **recurring operating cycle** for improving the AI workflow over time.

It is intentionally narrower and more procedural than `ai-workflow-improvement.md`.

- `ai-workflow-improvement.md` is the **charter**: mission, principles, research scope, and success criteria.
- `workflow-improvement-cycle.md` is the **playbook**: how to run a bounded improvement pass in practice.

This document should stay operational, session-sized, and reusable.

---

## 1. Purpose

Use this cycle when you want to improve the harness deliberately rather than opportunistically.

The goal is to make progress through **small, evidence-driven passes** instead of broad rewrites, trend chasing, or endless theoretical research.

The cycle may include:
- research
- evaluation
- implementation
- documentation
- permission/control review
- prompt/skill review

But it should not try to do all of them every time.

---

## 2. Core Rule

Run the **smallest useful cycle** that answers the current improvement question.

Do not force every pass to include:
- new research
- full prompt review
- code changes
- evaluations
- architectural redesign

Choose the lightest cycle that can still produce a meaningful durable improvement.

---

## 3. When to Run the Cycle

Run a workflow improvement cycle when at least one of these is true:

- a repeated failure mode appeared
- a prompt/skill boundary feels blurry
- a permission/control problem created friction or risk
- the harness became harder to resume or reason about
- a repeated manual pattern looks stable enough to standardize
- targeted research is needed to answer a real design question
- an existing workflow artifact is now misleading or stale

Do **not** run the cycle just to keep the harness in motion.

No real problem -> no cycle.

---

## 4. Cycle Types

Not every run needs the same shape.

### A. Research-only cycle
Use when the problem is not understood well enough yet.

Typical outputs:
- research notes
- comparison notes
- clarified vocabulary
- backlog or open questions

### B. Evaluation/review-only cycle
Use when the main question is whether the current harness is good enough, coherent, or drifting.

Typical outputs:
- drift notes
- defect list
- keep-as-is decision
- bounded change proposal

### C. Implementation-only cycle
Use when the needed change is already understood and no further research is required.

Typical outputs:
- prompt/config/skill edits
- tasks updates
- small policy refinements

### D. Mixed cycle
Use when one bounded pass needs a small amount of research, followed by review, followed by implementation.

This is often the most practical shape, but it must stay scoped.

---

## 5. Standard Loop

### Step 1: Name the trigger
State why this cycle exists now.

Examples:
- “Generalist git approvals are too chatty.”
- “Permission boundaries are too broad for Coder.”
- “Need to understand whether a dedicated maintenance skill is justified.”

If the trigger is vague, clarify it before planning.

### Step 2: Choose the cycle type
Pick one of:
- research-only
- evaluation/review-only
- implementation-only
- mixed

The type determines how much process is needed.

### Step 3: Bound the scope
Keep the cycle narrow enough to finish honestly.

Good scope boundaries:
- one layer (`AGENTS.md`, agents, skills, config, research)
- one problem family (permissions, delegation, resume behavior, review boundaries)
- one slice of work that can be verified proportionally

Bad scope boundaries:
- “improve the whole workflow”
- “modernize all prompts”
- “research everything related to agents”

### Step 4: Re-anchor only what is relevant
Read only the durable artifacts needed for this cycle:
- touched files
- relevant `plan/*`
- relevant research notes
- current prompt/config targets

Do not reload broad context unless the narrow read reveals drift or contradiction.

### Step 5: Produce the right intermediate output
Depending on the cycle type, create one or more of:
- research note
- decision note
- bounded proposal
- task slice
- small implementation patch

Do not skip durable planning when the work is large enough to need it.

### Step 6: Approve meaningful durable changes
Before changing long-lived behavior, get user approval for meaningful decisions.

Examples:
- permission model changes
- new skill creation
- agent role changes
- workflow policy changes
- major restructuring

### Step 7: Implement narrowly
When implementation is approved:
- make the smallest boring change that solves the scoped problem
- verify proportionally
- avoid opportunistic side quests

### Step 8: Evaluate outcome
At the end of the cycle, answer:
- what problem was actually improved?
- what stayed unresolved?
- what new risk or follow-up was discovered?
- is the current state good enough for now?

### Step 9: Reconcile durable truth
Update only the durable artifacts that changed materially:
- `plan/tasks.md`
- `plan/spec.md`
- `plan/decisions.md`
- policy/playbook docs
- prompt/config/skill files

Do not turn every micro-step into full-project convergence theater.

---

## 6. Preferred Outputs by Situation

### If the problem is unclear
Prefer:
- research note
- comparison note
- backlog item

### If the problem is understood but the fix is uncertain
Prefer:
- bounded proposal
- explicit options and tradeoffs

### If the fix is obvious and low-risk
Prefer:
- direct small implementation slice

### If the current system is already good enough
Prefer:
- no change
- maybe a short note explaining why the current state is retained

“No change needed” is a valid outcome.

---

## 7. Anti-Patterns

Do **not** use this cycle as an excuse for:

- broad rewrites with unclear benefit
- prompt sprawl
- giant “maintenance” skills with mixed responsibilities
- research that is disconnected from a real design question
- inventing improvements just to show activity
- turning every improvement pass into multi-agent orchestration
- replacing durable docs with chat history

---

## 8. Relationship to Skills, Commands, and Automation

This cycle is currently a **document-driven operating playbook**, not a single omnibus skill.

Why:
- the cycle can take multiple shapes
- not every run needs the same procedure
- the repeated pattern is real, but still broader than one narrow reusable capability

The actual subprocedures should continue to come from existing skills where appropriate.

Examples:
- planning -> `plan-project`
- implementation -> `workflow-execute`
- review -> `review-code` / `review-plan`
- reconciliation -> `reconcile-work`
- wrap -> `wrap-session`

---

## 9. When to Keep It Manual

Keep this cycle document-driven and manually steered when:

- the improvement question is still open-ended
- the steps vary significantly between runs
- the work spans several layers in different combinations
- user judgment is still needed to choose the right branch each time
- the repeated pattern is visible but not yet stable enough to compress safely

This is the default for now.

---

## 10. When a Command May Be Justified Later

A **user-invoked command** may be justified when:

- the entry ritual is repetitive
- the command can safely bootstrap the cycle without hiding major decisions
- its job is mainly to start the process, not to replace judgment

Good future command role:
- load the charter and cycle playbook
- inspect the current backlog
- ask what kind of cycle this is
- help create the next bounded slice

That is an entrypoint, not a full autonomous maintenance system.

---

## 11. When a Dedicated Skill May Be Justified Later

A dedicated skill is justified only if repeated real usage shows that the procedure is now stable enough to define clearly.

Minimum graduation criteria:
- stable trigger conditions
- stable inputs
- stable outputs
- stable stop conditions
- clear out-of-scope boundaries
- low risk of becoming a junk drawer

If those conditions are not met, keep using this playbook plus existing narrower skills.

---

## 12. Current Decision

For now:

- `ai-workflow-improvement.md` remains the **charter**
- `workflow-improvement-cycle.md` is the **operational playbook**
- a dedicated harness-maintenance skill remains **deferred**
- a user-invoked command may be considered later if the entry pattern becomes repetitive enough to justify it

This keeps the improvement process explicit without prematurely compressing it into the wrong abstraction.
