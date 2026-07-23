# Memory Policy

This document defines the practical memory policy for this repository.

Its goal is not to describe every possible memory pattern. Its goal is to answer the operational questions that matter in day-to-day work:

- what counts as memory
- what may be written durably
- what should stay transient
- what requires review or approval
- what provenance must be preserved
- how memory should be corrected, retired, or superseded

This policy is meant for a local-first, interruption-tolerant workflow where durable truth must survive session gaps without turning the repository into a dump of stale summaries and guesses.

---

## Summary

The main rule is simple:

> **Store selectively, retrieve deliberately, and protect durable writes more than transient drafting.**

Memory is useful only when it improves future work enough to justify its maintenance cost and correction burden.

This repository should prefer:

- small, inspectable durable artifacts
- source-linked memory
- stable facts, decisions, and reusable lessons
- retrieval over replaying large histories
- explicit review for memory that will shape later behavior

This repository should avoid:

- writing every interaction into long-term memory
- storing low-confidence inferences as truth
- keeping memory with unclear provenance
- letting stale summaries silently override better source artifacts

---

## 1. Memory Layers

This repository should treat memory as layered rather than as one undifferentiated store.

### A. Active context
The information loaded for the current step or current session.

- Purpose: immediate continuity
- Typical form: working notes, current task state, currently relevant files
- Durability: temporary by default
- Example: live session context or scratch planning state

This is **context**, not durable memory, unless explicitly promoted.

### B. Session or working memory
Short-horizon state that helps complete the current slice of work.

- Purpose: keep local continuity during active work
- Typical form: in-progress task state, temporary summaries, intermediate decisions
- Durability: limited and revisable
- Example: current task markers in `plan/tasks.md`

This may persist for convenience, but it should not be mistaken for durable truth.

### C. Durable project memory
Cross-session information intentionally retained because it is likely to matter later.

- Purpose: preserve reusable truth across interruptions
- Typical form: decisions, vocabulary, stable policies, synthesis notes, authoritative project records
- Durability: high
- Example: `plan/*`, stable research syntheses, authoritative design notes

This is the highest-value memory layer and deserves the strongest write controls.

---

## 2. What Counts as Durable Memory Here

For this repository, durable memory includes:

- explicit project decisions
- stable terminology and boundary definitions
- authoritative plans and task state meant to survive interruption
- stable user or workflow preferences that were explicitly stated or clearly ratified
- reusable lessons that have enough evidence to matter later
- long-lived synthesis notes that compress multiple sources into reviewable guidance

Durable memory does **not** mean “anything that was written to disk.”

Some files are temporary, exploratory, or procedural. Durable memory is the subset intended to shape future behavior or future understanding.

---

## 3. What Should Usually Be Written Durably

The default durable write targets are:

### A. Explicit facts with stable source backing
Examples:
- repository rules
- user-stated constraints
- environment constraints
- known project structure

### B. Decisions
Examples:
- agreed tier choice
- accepted architecture boundary
- chosen workflow rule
- approved policy change

### C. Reusable synthesis
Examples:
- vocabulary
- control-boundary model
- principles-only synthesis
- memory policy itself

### D. Stable preferences with clear origin
Examples:
- “update `activeContext.md` only at end of session”
- “durable truth lives in `plan/*`”

These are durable only when they are stable enough to guide future work and clear enough to verify later.

---

## 4. What Should Usually Stay Transient

The following should usually remain outside durable memory unless explicitly promoted:

- scratch reasoning
- temporary brainstorming
- one-off hypotheses
- low-confidence interpretation of user intent
- draft summaries that have not been reviewed
- repeated chat history with no lasting value
- redundant copies of facts already preserved in a better source artifact

If something is only useful for the current turn or current slice, it belongs in context or temporary working memory, not durable memory.

---

## 5. What Must Not Be Written Durably Without Review or Approval

The following are high-risk durable writes and should not be auto-promoted:

- inferred user preferences from a single interaction
- speculative explanations presented as settled truth
- low-confidence summaries that may hide uncertainty or conflict
- policy changes that alter future autonomy or control boundaries
- memory entries with no clear source or authorizing event
- copied sensitive data that does not need to persist
- synthesized conclusions that materially affect future work but were not reviewed

Durable memory should be treated almost as carefully as other consequential side effects because it silently changes future behavior.

---

## 6. Memory Write Gates

Before writing or promoting durable memory, apply these gates.

### Gate 1: Stability
Ask:
- Is this likely to matter beyond the current task?
- Is it stable enough to survive a later reread?

If not, keep it transient.

### Gate 2: Reusability
Ask:
- Will this help a future session or future task?
- Is it more useful than simply re-retrieving the source later?

If not, do not promote it.

### Gate 3: Provenance
Ask:
- Can this be linked to a source artifact, user statement, decision, or research note?
- Would a later reviewer know where it came from?

If not, it is not ready for durable storage.

### Gate 4: Trust level
Ask:
- Is this explicitly stated, directly observed, reviewed, or merely inferred?
- How damaging would it be if wrong?

Low-trust, high-impact memory requires stronger review.

### Gate 5: Duplication and conflict
Ask:
- Does this duplicate existing durable memory?
- Does it conflict with a better source?

If yes, reconcile before writing.

### Gate 6: Correction path
Ask:
- If this is wrong later, how will it be corrected, superseded, or removed?

If there is no practical correction path, be conservative about writing it.

---

## 7. Default Write Rules by Memory Type

### Facts
- Auto-write only when directly supported by an authoritative source already inside the repository.
- Otherwise prefer review before promotion.

### Decisions
- Write durably when the decision is explicit and materially affects future work.
- Include the decision source, not just the conclusion.

### Preferences
- Write durably only when clearly stated, repeated, or explicitly confirmed.
- Do not infer long-term preferences from one-off local behavior unless the user ratifies them.

### Summaries
- Write durably only when the summary is source-linked and scoped.
- Prefer summaries that point back to richer source artifacts.

### Lessons / heuristics
- Write durably only when they have enough evidence to be reused.
- A single successful run may suggest a heuristic, but should not automatically canonize it.

### Procedural know-how
- Durable procedural memory belongs in explicit workflow docs, skills, or policy notes when it is repeatable and intentional.
- Do not let accidental habits become hidden policy.

---

## 8. Provenance Requirements

Important memory should preserve enough provenance to support trust and correction.

Minimum useful provenance fields are:

- **source type** — user statement, repository artifact, research synthesis, observed run, derived summary
- **source reference** — file path, note, decision record, task, or traceable conversation point
- **author or origin** — user-provided, agent-synthesized, jointly agreed, or copied from source material
- **time or session marker** — when it entered durable memory
- **confidence or status** — explicit, reviewed, inferred, provisional, superseded

Not every note needs formal metadata blocks, but the provenance should be obvious enough that a future reread can answer:

1. where did this come from?
2. how trustworthy is it?
3. what should override it if it becomes stale?

---

## 9. Review and Approval Rules

### Usually safe to write with light review
- stable repository facts
- explicit user constraints
- scoped project decisions
- synthesis notes that clearly cite their source docs

### Should usually be review-before-promote
- memory candidate summaries
- behavior-changing workflow guidance
- reusable lessons extracted from prior runs
- durable interpretations of ambiguous discussions

### Should usually be explicit approval-before-write
- inferred preferences that will steer future behavior
- policy changes that alter permissions, approvals, or autonomy
- durable memory created from uncertain or conflicting evidence
- anything that stores sensitive data beyond what is operationally necessary

The stronger the future effect of the memory, the stronger the expected human checkpoint.

---

## 10. Retrieval and Promotion Policy

This repository should prefer:

- retrieving relevant durable artifacts when needed
- promoting compact, reviewable summaries rather than replaying whole histories
- keeping authoritative sources more important than derivative summaries

Promotion should usually follow this pattern:

1. observe or generate temporary information
2. decide whether it is stable and reusable
3. link it to source evidence
4. review if impact is meaningful
5. promote it into the appropriate durable artifact

That means the normal path is **events -> temporary notes -> reviewed synthesis or decision**, not **events -> automatic permanent memory**.

---

## 11. Retirement, Supersession, and Conflict Handling

Memory must be correctable.

### Retire memory when:
- it is obsolete
- the underlying environment changed
- the policy changed
- the memory was only provisional and the final answer now exists
- a better authoritative source replaced it

### Supersede memory when:
- a newer decision overrides an older one
- a clearer synthesis replaces a rough earlier summary
- explicit user guidance overrides inferred preference

### Handle conflicts by preferring, in order:
1. explicit current user instruction
2. current authoritative repository artifact
3. explicit recorded decision
4. reviewed synthesis
5. older or inferred memory

When conflict exists, do not silently merge incompatible statements into one vague summary. Preserve the conflict long enough to resolve it explicitly.

---

## 12. Local-First and Corporate Data Rules

Because this workflow runs in a corporate environment, memory policy must respect local-first constraints.

### Default rule
Keep durable memory local unless there is an explicitly approved reason to do otherwise.

### Do not durably replicate sensitive data without need
- avoid unnecessary duplication of corporate content
- avoid storing broad raw extracts when smaller references or summaries are enough
- avoid pushing memory contents to external services unless the path is approved

### Prefer references over copies
When practical, store:
- the location of the source
- a bounded summary
- the decision derived from the source

instead of large copied content.

This reduces governance burden and makes later cleanup easier.

---

## 13. Practical Default Policy for This Repository

### Auto or near-auto acceptable
- temporary working notes
- in-session task state
- source-linked summaries that stay inside clearly scoped draft artifacts
- explicit facts copied into the correct authoritative file when low risk and reversible

### Review before durable promotion
- synthesis notes
- durable summaries
- reusable lessons
- workflow guidance that may affect future behavior
- structured memory candidates derived from several sources

### Explicit approval or confirmation preferred
- inferred preferences that steer future default behavior
- changes to governance or control policy
- durable memory written from uncertain interpretation
- persistent storage of sensitive material beyond minimal operational need

### Forbid or strongly resist
- blind logging of every conversation into durable memory
- memory writes with no provenance
- hidden memory that cannot be inspected or corrected
- treating chat history alone as authoritative durable truth

---

## 14. Common Failure Modes

### 1. Treating storage as memory design
Saving more text is not the same as building useful memory.

### 2. Confusing current context with durable truth
What is visible now is not automatically what should persist.

### 3. Promoting summaries without source links
This makes correction and trust much harder.

### 4. Under-protecting inferred memory
Inferred preferences and synthesized conclusions can silently distort later behavior.

### 5. Keeping obsolete memory alive too long
Stale memory creates false confidence.

### 6. Duplicating truth in too many places
When multiple files claim authority, drift becomes likely.

---

## 15. Policy Test Questions

Before adding new durable memory behavior, ask:

1. Is this information better stored, or better re-retrieved later?
2. Is the memory type fact, decision, preference, lesson, or summary?
3. What source backs it?
4. What is its trust level?
5. Who should review it before it becomes durable?
6. Where is the authoritative home for it?
7. How will it be corrected, retired, or superseded?

If those questions cannot be answered clearly, the write is probably premature.

---

## Relationship to Other Documents

- `research/principles-only.md`
- `research/control-boundaries.md`
- `research/vocabulary.md`
- `research/topics/memory-systems.md`
- `research/topics/observability-traceability.md`
