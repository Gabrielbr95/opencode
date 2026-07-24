# opencode: Session Control and Recovery

## Freshness
- Last verified: 2026-07-24
- Verified against: Context7 `/anomalyco/opencode`, current source excerpts, v2 session/config excerpts
- Product version: current docs/source snapshot; exact installed local version not verified
- Stability: Medium-Low
- Recheck triggers:
  - session API changes
  - compaction/revert behavior changes
  - local behavior differs from docs

## Scope
- What session control and recovery features opencode appears to have
- Why they matter for interrupted work and long-gap resumability
- Which parts seem practically useful before deeper customization work

## Canonical Boundary
This note is for **how opencode implements session continuity today**.

For the reusable capability pattern, see:
- `research/capabilities/sessions.md`

## Why This Matters Here
- This workflow has long interruptions and heavy context decay.
- A harness that supports interruption, recovery, and controlled rollback is more valuable than one that only feels powerful in the moment.
- Session control is one of the most practically important advanced areas for this repository.

## Current Findings
- opencode appears to have a real session model, not just a transient chat buffer.
- It supports durable session creation and prompting semantics.
- It appears to support interrupt/resume behavior.
- Undo/redo behavior is tied to snapshots and message-level revert logic.
- Compaction appears to be configurable and part of the session lifecycle.

## Session Model: Practical View
Current v2 session excerpts suggest operations such as:
- create a session
- prompt a session
- interrupt a session
- list active sessions

Practical takeaway:
- opencode is treating sessions as first-class runtime objects
- this is more than just a single terminal transcript

## Interrupt and Resume
Current session excerpts suggest:
- active execution can be interrupted
- durable inbox rows can remain for later wake/resume
- resume is a real execution path, not just a UI fiction

Practical takeaway:
- interruption is expected behavior in the model
- that fits this workflow better than a harness that assumes uninterrupted active use

## Undo / Redo / Revert
Current source excerpts suggest:
- revert asserts the session is not busy
- filesystem snapshots are captured for possible redo
- file patches are reverted
- revert metadata is persisted
- redo restores the saved snapshot
- cleanup can remove or trim messages and parts after the revert boundary

Practical takeaway:
- undo/redo is not a shallow text-only feature
- it appears tied to actual file-state management and session history management

This is especially important because it means:
- the feature is powerful
- but also more stateful than a casual “undo button” sounds

## Compaction
Current config/spec excerpts suggest:
- compaction is configurable
- recent history can be kept within token limits
- buffer/headroom can be configured

Practical takeaway:
- compaction is a core control for long sessions
- it should be understood as part of the harness memory strategy, not just token cleanup

## Recovery Value for This Repository
The most important practical value here is not novelty. It is:
- interruptibility
- resumability
- bounded rollback
- cost control over longer sessions

For this workflow, those matter more than fancy autonomous behavior.

## Practical Guidance

### 1. Treat sessions as durable work objects
If opencode uses real session semantics, then session hygiene matters.

### 2. Learn revert behavior before relying on it in stressful moments
Because undo/redo appears to involve snapshots and message cleanup, it is worth understanding rather than assuming it behaves like a text editor.

### 3. Treat compaction as part of reliability
Compaction is not only about cost; it changes what context remains visible in active operation.

### 4. Prefer explicit resumption habits
If long gaps are common, session naming, summaries, and related documentation discipline still matter even with a strong session model.

## Local-First / Corporate Notes
- Snapshot-heavy behavior may have disk and state implications.
- File-revert features are more trustworthy when the repository is also under Git.
- Recovery features reduce risk, but they do not replace durable external documentation.

## What Still Needs Practical Verification
- How comfortable and reliable undo/redo feels in daily use.
- How compaction behaves in a real long-running workflow.
- How much session recovery helps after a true 14-day gap versus just a short interruption.

## Relationship to Other Notes
- `research/capabilities/sessions.md`
- `research/syntheses/memory-policy.md`
- `research/syntheses/observability-schema.md`
- `research/products/opencode/advanced-features-map.md`
- `research/products/opencode/system-prompt-control.md`
- `research/concepts/memory-systems.md`

## Open Questions
- Which session-control features are worth making part of daily workflow habits?
- How much explicit wrap-up is still needed if session recovery is strong?
- What is the best balance between opencode session history and external durable notes?

## References
- Context7 `/anomalyco/opencode` — v2 session operations, revert implementation, and compaction config excerpts.
