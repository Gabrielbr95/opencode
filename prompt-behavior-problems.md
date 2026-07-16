# Prompt Behavior Problems Observed In This Session

## Purpose
This note records the **general behavioral problems** that showed up during the long planning/refactor session, especially the ones that drove token usage up very quickly.

This file is **not** a solution proposal.
It is a problem statement for a future session focused on improving the system prompts and agent behavior.

## Context
The session was dominated by planning and contract-writing work rather than application code.
The agent still behaved with a very heavy implementation-and-verification style.
That mismatch exposed behavioral problems that are larger than any one file or task.

---

## Problem 1: The agent re-acquires durable truth too aggressively

### What the problem is
The agent repeatedly reloads large "source of truth" files even after it already has the relevant working understanding.
This is not just a file-size issue. It is a behavioral tendency to **re-prove context from the durable artifacts over and over**, instead of carrying forward a sufficient internal working model.

### Why this matters
When the durable files are large, every review loop, every verification step, and every handoff causes another expensive context reacquisition pass.
As the project documents become more detailed, this behavior scales badly.
The more carefully documented the project becomes, the more the agent tends to reread it.

### Why I acted this way
I was strongly shaped by instructions that make the durable artifacts the authoritative truth and emphasize not letting those artifacts drift from reality.
That pushed me toward repeatedly rereading:
- `plan/tasks.md`
- `plan/spec.md`
- `plan/decisions.md`
- `plan/architecture.md`
- later, the split contract docs

The behavior was also reinforced by wrap-up, converge, sync, and review patterns that all point back to the durable docs as the canonical source.
So the agent kept treating repeated rereading as the safest way to avoid contradiction.

### General form of the problem
This is a **context reacquisition bias**:
- the agent treats repeated re-reading as safer than relying on already-built understanding,
- even when the task is only validating a narrow delta,
- and even when the cost of doing so is very high.

---

## Problem 2: The agent over-applies a code-grade execution loop to documentation work

### What the problem is
The agent used a heavy coder/reviewer/repair pattern on documentation-heavy tasks that did not always need that much ceremony.
This created multiple rounds of duplicated reasoning for small contract edits.

### Why this matters
The more granular the task list becomes, the more each small change triggers:
- a task claim,
- a coder pass,
- a reviewer pass,
- sometimes a repair pass,
- then another reviewer pass,
- then status synchronization.

That style is appropriate for risky implementation work, but it becomes very expensive when applied to documentation restructuring and planning refinement.

### Why I acted this way
I was operating under a workflow that strongly favors explicit execution and explicit verification:
- Application-tier caution
- strict task-state transitions
- orchestration guidance using coder + reviewer loops
- strong anti-drift expectations
- preference for loud, explicit correctness over informal progress

Once the session was framed as autonomous execution, I kept applying that pattern to almost every task because it fit the prompt rules better than using a lighter review style.

### General form of the problem
This is a **verification fan-out problem**:
- the agent does not distinguish sharply enough between high-risk implementation work and lower-risk documentation/contract maintenance,
- so it applies the same expensive loop to both,
- which multiplies token cost without proportional value.

---

## Problem 3: The agent treats state synchronization as a first-class product on every micro-step

### What the problem is
The agent did not just perform the task.
It also continuously synchronized multiple layers of session state:
- task status
- decisions
- architecture/contracts
- spec
- wrap/session continuity expectations
- approval gating
- durable truth alignment

This created a lot of procedural work around each small unit of progress.

### Why this matters
Even when each individual sync action is reasonable, the total behavioral pattern becomes expensive:
- task status changes happen frequently,
- the same change gets reflected in multiple places,
- small inconsistencies trigger more review passes,
- and the bookkeeping itself becomes a major part of the session.

In long planning sessions, the synchronization overhead can rival or exceed the actual reasoning about the feature.

### Why I acted this way
The instructions and skills strongly reward explicit state discipline:
- one task in progress at a time,
- durable truth in `plan/*`,
- no silent drift,
- documentation must stay current,
- explicit approval gates,
- explicit blockers,
- explicit convergence before declaring completion.

So I kept treating every artifact update as part of the core job, not as a secondary bookkeeping layer.
That behavior reduced ambiguity, but it also made the session much heavier.

### General form of the problem
This is a **state-management inflation problem**:
- the agent behaves as if every micro-step must fully propagate through all tracked state layers immediately,
- even when that level of synchronization is not the main objective of the session,
- and even when it significantly increases context usage.

---

## Problem 4: The agent optimizes for local correctness, not session-level efficiency

### What the problem is
The behavior was consistently conservative at the small-step level.
For each task, the agent tried to maximize explicit correctness and traceability right away.
But that local optimization produced poor global efficiency across the whole session.

### Why this matters
A long session can become inefficient even if every individual step looks reasonable in isolation.
The problem is not one bad action; it is a repeated pattern where the safest-looking next move is chosen over and over.
That compounds into very large token usage.

### Why I acted this way
The prompt stack heavily emphasized:
- maintainability,
- explicitness,
- durable truth,
- independent verification,
- no silent failure,
- no guessing,
- no undocumented divergence.

Those constraints made it natural to prioritize traceable, explicit, locally justified actions over session-level economy.
In other words, I behaved like a system whose main fear was being wrong or inconsistent, not a system whose main fear was spending too much context.

### General form of the problem
This is a **local-safety-over-global-efficiency bias**:
- the agent is pulled toward behavior that is easy to justify step-by-step,
- even when the accumulated cost across the session becomes too high.

---

## Problem 5: The agent lacks a strong built-in distinction between planning completion and coding readiness

### What the problem is
The session mixed two different goals:
1. fully locking durable planning/contracts, and
2. getting ready to start implementation.

The agent kept treating contract refinement as if it were still part of the same execution runway as coding, instead of recognizing that planning itself had become the main workload.

### Why this matters
When planning becomes detailed enough, the agent can keep expanding and validating planning artifacts indefinitely while still acting as though it is simply preparing for implementation.
That makes the process feel like forward progress, but it can keep consuming tokens long after the high-level design is already good enough.

### Why I acted this way
The task list and prompt structure rewarded complete contract locking before coding.
Because many later tasks were phrased as definition/contract tasks, and because the approval gate had not yet been crossed, I kept treating deeper planning detail as the active work.
That meant the session stayed in a planning-intensive mode for a long time without a strong internal pressure to compress or cap that effort.

### General form of the problem
This is a **planning-depth runaway problem**:
- once the agent enters durable-contract mode,
- it tends to keep refining and verifying the plan in a very detailed way,
- without a strong counterweight that says the planning layer is already sufficiently complete for the current objective.

---

## Overall Problem Statement
The main issue was not one bad tool call or one oversized file.
The deeper problem is that the agent behavior is shaped by prompts that reward:
- repeated source-of-truth rereading,
- code-grade verification loops for nearly everything,
- aggressive artifact synchronization,
- local explicit correctness,
- and deep contract-locking before implementation.

Those behaviors are individually understandable.
Together, they create a system that is **highly disciplined but context-hungry**, especially in planning-heavy sessions.

## Why this note exists
This file should be used later as input for prompt/system improvement work.
The point is to address the **general behavior pattern**, not just this single 300k-token session or the single large `architecture.md` file.
