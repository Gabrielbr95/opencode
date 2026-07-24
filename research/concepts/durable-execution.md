# Durable Execution

## Freshness
- Last reviewed: 2026-07-24
- Stability: Medium
- Likely drift areas:
  - framework-specific determinism rules and orchestration APIs
  - checkpoint storage shapes and replay tooling
  - pause/resume and human-approval runtime semantics

## Summary
- Workflow state and durable execution is the capability that lets a multi-step run survive time, failure, retries, and interruption without losing its identity or corrupting side effects.
- The durable lesson is not any one product's orchestration syntax. It is the runtime model: one run has a stable identity, an inspectable state model, a durable progress record, and explicit boundaries between deterministic orchestration and real-world effects.
- This is broader than session persistence alone. Session continuity is one use case inside a larger execution problem that also includes replay, retries, pause/resume, idempotency, and long-running control flow.

## Motivation
- Many product notes treat durable execution as a special platform feature, but the reusable mechanism is more general.
- Once a workflow can run longer than a single request, machine uptime, or uninterrupted human attention span, it needs a real execution model rather than a best-effort loop.
- This note fills the gap between memory/session notes and product-specific orchestration behavior.

## Problem Statement
- Multi-step AI and automation workflows fail in predictable ways when the runtime cannot answer basic questions:
  - what run is this?
  - what state is authoritative right now?
  - what already happened?
  - what can be replayed safely?
  - what must never happen twice?
  - where may humans pause, approve, or resume work?
- Without durable execution semantics, systems drift into fragile retry loops, duplicate side effects, hidden state corruption, and hard-to-debug partial completion.

## Core Function
- Represent a workflow run as a durable execution object rather than a disposable request.
- Persist enough state to resume, inspect, retry, or replay progress.
- Separate deterministic control logic from non-deterministic external effects.
- Make long-running work safe enough to survive crashes, worker restarts, human pauses, and transient faults.

## Minimal Durable Model

### 1. Run identity
Every durable execution needs a stable identifier.

Minimum useful fields:
- workflow or task type
- logical workflow ID
- run or attempt ID
- parent or triggering run ID when relevant
- created time and current status

Why this matters:
- retries are not the same as new business intent
- one logical workflow may span several execution attempts
- observability and approvals need a stable object to attach to

### 2. State model
The runtime needs an explicit state model, not just free-text history.

Typical states:
- pending
- running
- waiting
- paused
- retry_scheduled
- completed
- failed
- cancelled

Useful sub-state distinctions:
- waiting on timer
- waiting on tool or remote call
- waiting on human approval
- compensating or recovering

### 3. Durable progress record
The system needs some durable record of how it got here.

Common shapes:
- append-only event history
- state snapshots or checkpoints
- hybrid event history plus periodic snapshots

This record is what makes recovery, replay, and audit possible.

## Event History vs Snapshotting

### Event history
Store the sequence of workflow-relevant events or commands.

Strengths:
- rich audit trail
- good replay support
- easier causality inspection
- clearer temporal debugging

Costs:
- replay cost can grow with history length
- event schemas become durable contracts
- external effects must be isolated carefully during replay

### Snapshots or checkpoints
Store the materialized state at intervals or boundaries.

Strengths:
- faster resume
- simpler recovery for large histories
- easier state loading for long-running workflows

Costs:
- weaker causal detail unless paired with events
- stale or incomplete snapshots can mislead recovery
- rollback semantics may be less obvious

### Hybrid model
Many practical systems use both:
- event history for provenance and deterministic reconstruction
- snapshots/checkpoints for speed and bounded replay cost

This is usually the most reusable mental model.

## Deterministic Orchestration Boundary
- A durable workflow runtime usually works best when the orchestrator layer is deterministic enough to replay safely.
- The durable distinction is:
  - orchestration code decides what should happen next
  - side-effecting workers, activities, or tools perform the real-world action
- During replay, the runtime should be able to rebuild orchestration state without redoing external effects.

Typical non-determinism hazards:
- reading wall-clock time directly in orchestration logic
- generating random values without durable recording
- depending on unordered iteration or unstable APIs
- reading mutable external state directly during replayable logic
- changing orchestration code in incompatible ways while old runs still exist

## Side-Effect Isolation
- Durable execution depends on isolating side effects from replayable control flow.
- The runtime must distinguish between:
  - deterministic state transition
  - proposed external action
  - confirmed external result
- This matters most for:
  - tool calls
  - API requests
  - file mutations
  - notifications and messages
  - durable memory writes

Common isolation patterns:
- execute side effects only in dedicated activity or worker boundaries
- record an idempotency key before mutation
- treat external responses as inputs recorded into run history
- gate high-risk effects behind approval checkpoints

## Replay, Recovery, and Checkpointing
- Replay means rebuilding workflow state from durable history.
- Recovery means continuing progress after interruption or failure.
- Checkpointing means persisting enough state that replay or resume is practical.

Durable questions to ask:
- can this run resume from the last known good boundary?
- what data is recomputed versus restored?
- what happens if code changed since the checkpoint was written?
- which effects are suppressed, reissued, or reconciled during recovery?

This is where this note differs from `sessions.md`:
- that note focuses on session continuity and bounded rollback
- this note focuses on the runtime execution model underneath long-running work

## Pause, Resume, and Waiting Semantics
- Long-running workflows often spend more time waiting than actively computing.
- Useful runtimes model waiting states explicitly rather than treating them as failures or hidden sleeps.

Common wait types:
- timers and scheduled wake-ups
- external callback or signal arrival
- tool or service completion
- human approval or edit checkpoint
- resource availability or dependency completion

Good pause/resume semantics usually include:
- a durable record of why the run is paused
- a clear resume condition or resume token
- stable run identity across the pause
- observability that shows waiting versus broken states

## Retries and Idempotency
- Durable execution is not just about resuming state. It is also about retrying safely.
- Retries should attach to a known run or step identity, not become silent duplicate intent.

Durable distinctions:
- retrying transport failure is not the same as reissuing business intent
- retrying a deterministic step is not the same as retrying an external mutation
- an idempotent operation can be retried safely within a defined identity window

Common retry patterns:
- per-step retry policy with backoff
- retry budgets or max attempts
- dead-letter or escalation after bounded failure
- caller-provided or runtime-generated idempotency keys
- semantic equivalence for duplicate requests under the same key

## Long-Running Execution Semantics
- A durable runtime treats long duration as normal, not exceptional.
- That usually requires explicit rules for:
  - retention and compaction of run history
  - code-version compatibility across old in-flight runs
  - splitting one logical workflow across several linked runs when history grows too large
  - expiration, cancellation, and timeout policy
  - operator or human inspection of blocked work

Durable execution is therefore partly a control-plane problem, not only a storage problem.

## Common Patterns
- workflow ID plus run ID
- event log plus periodic snapshot
- deterministic orchestrator plus side-effecting workers
- durable wait states for human-in-the-loop and timers
- explicit retry policy per side-effect class
- idempotency keys for external mutations
- replay-safe recovery after worker failure
- compensation or reconciliation after partial external success

## Typical Components
- workflow/run registry
- state store
- event history store
- snapshot or checkpoint store
- scheduler or wake-up mechanism
- worker/activity executor
- idempotency record store
- signal/callback ingestion path
- trace and audit metadata
- code-version compatibility strategy

## Durable Distinctions

### Run identity vs session identity
A session may contain several runs. A run is the execution object whose state machine must remain coherent.

### Event history vs memory
Event history records what happened in the run. Memory stores facts or summaries meant to help future work. They are related but not interchangeable.

### Replayability vs reproducibility
A system can replay a recorded run state machine without making the whole environment perfectly reproducible.

### Retry vs resume
Resume continues a paused or interrupted run. Retry re-attempts a failed step or attempt under policy.

### Snapshot rollback vs business compensation
Restoring internal state does not automatically undo external effects.

### Deterministic orchestration vs dynamic planning freedom
More runtime freedom can improve flexibility, but it makes replay and long-lived correctness harder.

## Portability
- Portable across tools:
  - durable runs need stable identity
  - explicit state machines beat implicit transcript state
  - event history and snapshotting are complementary, not competing, patterns
  - replay requires isolation of side effects
  - retries need idempotency semantics to stay safe
  - human pauses and long waits should be first-class runtime states
- Product-shaped:
  - exact event schema and checkpoint format
  - determinism rules and code constraints
  - signal/callback APIs
  - operator UI for inspecting blocked runs
  - built-in compensation and versioning features

## Advantages
- better crash tolerance and resumability
- safer long-running execution
- clearer audit trail for what happened and why
- more predictable retries under failure
- cleaner human approval and resume points
- better debugging of partial completion and blocked work

## Risks / Failure Modes
- hidden state models that users cannot inspect
- non-deterministic orchestration that breaks replay
- duplicated side effects during recovery or retry
- event histories that grow faster than replay budgets allow
- snapshots trusted beyond their real correctness boundary
- version drift between old runs and new code
- confusing retry identity with new user intent
- pause states that cannot resume deterministically
- assuming internal rollback undoes external consequences

## Tradeoffs
- **Event history vs snapshots**: richer provenance versus cheaper resume.
- **Strict determinism vs dynamic flexibility**: safer replay versus looser runtime freedom.
- **Automatic retries vs explicit operator review**: lower toil versus higher duplicate-side-effect risk.
- **Long retention vs aggressive compaction**: better auditability versus lower storage and replay cost.
- **Single long-lived run vs chained runs**: simpler conceptual continuity versus bounded history growth.

## Relationships to Other Notes
- `../capabilities/sessions.md`
- `../capabilities/tool-calling.md`
- `../concepts/memory-systems.md`
- `../concepts/observability-traceability.md`
- `../concepts/planning-systems.md`
- `../concepts/human-in-the-loop-control-points.md`
- `../syntheses/control-boundaries.md`
- `../syntheses/observability-schema.md`
- `../syntheses/workflow-pattern-comparison.md`
- `../syntheses/concept-capability-product-map.md`

## Practical Applications for This Repository
- Treat long-running agent work as runs with explicit state and checkpoints, not just as chat continuity.
- Keep pause/resume, approval, and durable-write boundaries explicit enough that a later reread can explain them.
- Prefer event or trace records for run behavior, and keep durable project truth in repository artifacts rather than hidden runtime state.
- Assume retries need idempotency or human review before touching authoritative files or external systems.
- Be cautious about orchestration patterns that are hard to replay, inspect, or recover after a 14-day gap.

## Open Questions
- What is the minimum run-state schema worth standardizing in this repository?
- Which actions need explicit idempotency keys versus simple review-before-retry rules?
- How much replay capability is actually worth implementing for local-first workflows here?
- When should a long task stay one run versus be split into chained bounded runs?

## References
- [Temporal Workflow Execution overview](https://docs.temporal.io/workflow-execution) - Temporal docs. Useful evidence for run identity, event history, replay, and long-running workflow chains.
- [Durable Functions Overview: Stateful Serverless Workflows](https://learn.microsoft.com/en-us/azure/durable-task/durable-functions/durable-functions-overview) - Microsoft docs. Clear product example of orchestrator/activity separation, checkpoints, retries, and recovery.
- [Orchestrator code constraints](https://learn.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-code-constraints) - Microsoft docs. Useful evidence that deterministic orchestration boundaries are a real engineering requirement, not a stylistic preference.
- [Event Sourcing](https://martinfowler.com/eaaDev/EventSourcing.html) - Martin Fowler. Durable explanation of event history, rebuild, replay, and external-system complications.
- [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/) - AWS Builders' Library. Strong practical reference for retry safety, idempotency keys, and semantic equivalence.
- [LangGraph persistence](https://docs.langchain.com/oss/python/langgraph/persistence) - LangGraph docs. Useful current example of thread-scoped checkpoints versus cross-thread durable stores.
