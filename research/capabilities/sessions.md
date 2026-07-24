# Sessions

## Freshness
- Last reviewed: 2026-07-24
- Stability: Medium
- Likely drift areas:
  - exact snapshot implementation details
  - compaction and resume APIs

## Summary
- Some harnesses treat sessions as durable work objects rather than disposable chat transcripts.
- The reusable capability is controlled continuity: interrupt, resume, compact, checkpoint, and sometimes revert.
- This matters most in workflows with long interruptions and heavy context decay.

## Motivation
- Product notes often describe session mechanics as if they are unique product features, but the more durable lesson is the capability pattern: resumable state with bounded rollback.
- This note captures that middle layer once.

## Problem Statement
- Long-running work fails when the system cannot pause safely, resume clearly, or recover after a bad turn.
- At the same time, overly stateful systems can become hard to inspect or trust.

## Core Function
- Preserve enough session state to resume work without replaying everything.
- Bound long histories through compaction or summary.
- Support interruption and, in stronger systems, rollback or redo.

## Common Patterns
- durable session IDs
- explicit interrupt/resume
- summary or compaction checkpoints
- snapshot-backed revert
- separation between active context and durable external notes

## Typical Components
- session store
- state machine for active/busy/interrupted/completed
- summary/compaction mechanism
- snapshot or revert mechanism
- provenance for what changed and when

## Portability
- Portable across tools:
  - resumability and compaction are general harness concerns
  - sessions do not replace durable project documentation
  - rollback is more trustworthy when paired with external version control
- Product-shaped:
  - exact session APIs
  - what is checkpointed
  - whether revert is message-only or file-state-aware

## Advantages
- better interruption tolerance
- lower need to replay huge histories
- potential rollback safety when experiments go bad

## Risks / Failure Modes
- stale summaries driving later work
- hidden state that users forget exists
- over-trust in undo/redo semantics
- compaction that removes context users expected to remain visible

## Tradeoffs
- Rich session state improves continuity but increases hidden complexity.
- Aggressive compaction saves tokens but risks losing nuance.
- Strong recovery features help confidence but require more implementation trust.

## Relationships to Other Notes
- `../concepts/memory-systems.md`
- `../concepts/observability-traceability.md`
- `../syntheses/memory-policy.md`
- `../syntheses/observability-schema.md`
- `../products/opencode/session-control-and-recovery.md`

## Practical Applications for This Repository
- Treat resumable sessions as helpful runtime state, not as the only durable truth.
- Keep external wrap-up artifacts even if the harness has good resume features.
- Verify revert behavior before relying on it under stress.

## Open Questions
- Which recovery features are worth making part of daily habits here?
- How much continuity should come from the harness versus from explicit repository artifacts?

## References
- `../concepts/memory-systems.md` — durable distinctions between active context, working memory, and long-lived memory.
- `../syntheses/memory-policy.md` — repository guidance on what should become durable versus stay transient.
- `../products/opencode/session-control-and-recovery.md` — concrete product example of sessions, compaction, and revert behavior.
