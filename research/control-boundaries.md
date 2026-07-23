# Control Boundaries

This document synthesizes the practical control model across:

- permissions / authorization
- tool-use policy
- guardrails
- approvals
- human-in-the-loop control points
- side effects
- durable memory writes

Its goal is to answer a simple question:

> **What should be allowed automatically, what should be checked automatically, what should require explicit approval, and what should be forbidden or heavily constrained?**

---

## Summary

The main control mistake in agent systems is collapsing several different safeguards into one vague idea of “safety.”

These layers do different jobs:

- **Tool-use policy** tells the model when and why it should use tools.
- **Permissions / authorization** determine what the runtime will actually allow.
- **Guardrails** automatically check or constrain risky inputs, outputs, or tool calls.
- **Approvals** explicitly gate execution before sensitive actions continue.
- **HITL** defines where a human may review, edit, reject, override, or stop the workflow.
- **Side-effect classification** determines how much control is needed before an action occurs.
- **Memory-write controls** decide what may become durable truth.

Good control design does not mean maximum friction everywhere.

The durable rule is:

> **low-risk reasoning should flow easily; high-risk side effects and durable writes should cross stronger control boundaries.**

---

## The Boundary Stack

### 1. Policy Boundary
**Question:** Should the model even try to do this?

This is where the system encodes intent-level guidance:
- when to use a tool
- when to ask for clarification
- when to avoid acting
- when to prefer drafting over execution

Typical controls:
- prompt instructions
- workflow rules
- autonomy scope declarations
- tool descriptions and examples

**Failure mode:** the model chooses an inappropriate action even though the call is syntactically valid.

**Key distinction:** policy shapes model behavior, but does not by itself enforce runtime safety.

---

### 2. Permission Boundary
**Question:** Is this action allowed at all?

This is the hard enforcement layer.

Typical controls:
- allow/deny rules
- per-tool or per-path permission rules
- runtime authorization
- network/data access boundaries
- environment-specific execution limits

**Failure mode:** an agent attempts an action outside its allowed scope.

**Key distinction:** a policy-compliant action can still be forbidden by permission rules.

---

### 3. Guardrail Boundary
**Question:** Does this input/output/action violate safety or validity constraints?

Guardrails are automated checks that happen before or after an action.

Typical controls:
- schema validation
- format checks
- prompt injection detection
- allowlists/blocklists
- content filters
- output validation
- parameter sanity checks

**Failure mode:** the action is permitted in principle but malformed, unsafe, or suspicious in practice.

**Key distinction:** schema-valid is not the same as appropriate or safe.

---

### 4. Approval Boundary
**Question:** Must someone explicitly allow this specific execution to continue?

Approval is a run-time gate placed before consequential actions.

Typical controls:
- yes/no approval dialog
- per-call approval requirement
- approval policy callback
- resumable interruption state

**Failure mode:** the system proceeds with a risky action without explicit confirmation.

**Key distinction:** approval is not authorization. Authorization says “may this actor ever do this?” Approval says “may this specific run do it now?”

---

### 5. HITL Boundary
**Question:** Where can a human intervene meaningfully?

HITL includes more than approval. It also includes:
- review/edit draft
- override proposed action
- clarify ambiguous instructions
- reject and stop
- resolve exception states

**Failure mode:** humans are nominally “in the loop” but cannot actually inspect or change what matters.

**Key distinction:** guardrails are automatic; HITL inserts human judgment.

---

### 6. Durable-Write Boundary
**Question:** Should this become persistent truth or memory?

This is often under-protected.

Durable writes include:
- memory entries
- repository rules
- accepted defaults
- learned preferences
- long-lived summaries
- durable status or decision records

**Failure mode:** transient model guesses or low-confidence conclusions become institutional truth.

**Key distinction:** a workflow may allow drafting freely while still requiring stronger control for durable writes.

---

## Side-Effect Classes

Not all actions deserve the same controls.

### Class 0 — Pure reasoning / draft generation
Examples:
- brainstorming
- summarization draft
- classification draft
- planning draft
- explanation

**Typical controls:** policy + light guardrails.

**Usually no approval needed** unless the output is automatically propagated to a high-risk downstream step.

---

### Class 1 — Read-only observation
Examples:
- reading files
- searching documents
- retrieval over local sources
- querying a non-mutating API
- reading logs or traces

**Typical controls:** permission boundary + prompt injection / query guardrails.

**Approval usually not needed**, but sensitive-data access may still require stronger rules.

---

### Class 2 — Internal draft mutation
Examples:
- editing a draft file
- updating a temporary plan
- changing non-authoritative working notes
- writing temporary artifacts

**Typical controls:** permissions + guardrails.

**Approval depends on reversibility** and whether the target is authoritative.

---

### Class 3 — Durable internal mutation
Examples:
- changing authoritative docs
- updating repository rules
- writing durable memory
- changing config that affects later behavior
- modifying long-lived prompt/skill definitions

**Typical controls:** permissions + stronger guardrails + review or approval.

This is a high-value boundary because mistakes persist.

---

### Class 4 — External or irreversible side effect
Examples:
- sending emails/messages
- uploading data
- deleting files or records
- changing production-like settings
- writing to external systems
- spending money / placing orders / scheduling actions

**Typical controls:** strict permissions + approval + HITL visibility + audit log.

This should be the highest-friction class by default.

---

## Durable Memory Write Rules

Durable writes deserve their own model because they silently shape future behavior.

### What should usually be allowed
- storing clearly attributable factual artifacts
- storing user-approved stable preferences
- storing explicit project decisions with provenance
- storing reusable lessons that passed review

### What should usually be constrained
- inferred preferences from one-off interactions
- model-generated summaries with no provenance
- speculative explanations presented as durable fact
- low-confidence pattern inferences
- auto-promotion of transient notes into durable memory

### Good write gate questions
Before writing durable memory, ask:
- Is this stable enough to matter later?
- Is it attributable to a source?
- Is it reusable, or just transient session noise?
- Does it duplicate existing memory?
- Is it reviewed, user-approved, or otherwise trustworthy?
- How would it be corrected or deleted later?

---

## Approval Placement Rules

Good approval placement is risk-based.

### Approve-before-act is best for:
- external communication
- destructive file or data operations
- privileged tool calls
- changing shared or authoritative artifacts
- high-cost actions
- durable memory promotion from inferred content

### Review/edit is best for:
- plans
- prompt changes
- summaries that may become durable
- user-facing drafts
- policy text

### Clarify-before-continue is best for:
- ambiguous user instructions
- conflicting constraints
- missing required business inputs
- unclear target system or scope

### Exception escalation is best for:
- repeated failure loops
- conflicting evidence
- invalid or contradictory retrieved data
- uncertain policy fit
- suspicious tool behavior

---

## What Practitioners Commonly Get Wrong

### 1. Treating all safety controls as one thing
This causes confusion like:
- “we have approvals, so permissions are covered”
- “we have schemas, so actions are safe”
- “we have guardrails, so humans are unnecessary”

These are different boundaries.

### 2. Only protecting external actions
Durable internal mutations are often under-protected even though they can poison future behavior.

### 3. Overusing approval
If every small action needs approval, people stop reading and the control becomes ceremonial.

### 4. Under-protecting memory writes
Bad durable memory is often harder to detect than a visibly bad answer.

### 5. Confusing model guidance with enforcement
Natural-language instructions do not replace runtime allow/deny enforcement.

### 6. Treating schema validity as full safety
A well-formed tool call can still be the wrong action.

### 7. Forgetting pause/resume semantics
An approval boundary without deterministic resume behavior is fragile and easy to misuse.

---

## Minimal Practical Control Model

For a local-first prompt/agent repository, a useful baseline model is:

### Auto
Allowed automatically:
- pure reasoning
- low-risk drafting
- read-only retrieval/search
- reversible internal scratch work

### Guarded Auto
Allowed automatically with automated checks:
- structured tool reads
- temporary file edits
- low-risk internal transforms
- retrieval over semi-trusted content

### Review/Edit
Human reviews or edits before promotion:
- prompt changes
- durable summaries
- policy changes
- long-lived docs
- memory candidates

### Approve-Before-Act
Explicit approval required:
- destructive changes
- external side effects
- privileged or sensitive tool calls
- durable writes based on inference rather than explicit source truth

### Escalate / Stop
Stop and hand off when:
- permissions conflict
- policy fit is unclear
- retries loop without evidence of progress
- retrieved evidence conflicts materially
- the action is outside declared scope

---

## Example Mapping Table

| Scenario | Main Boundary | Typical Control |
|---|---|---|
| Draft a plan | Policy / guardrail | Auto or review/edit |
| Search local docs | Permission / guardrail | Auto |
| Update active working notes | Permission / guardrail | Auto or guarded auto |
| Change durable prompt instructions | Durable-write / HITL | Review/edit |
| Add inferred user preference to memory | Durable-write / approval | Review or approve-before-write |
| Call privileged external system | Permission / approval | Approve-before-act |
| Delete files or records | Permission / approval | Approve-before-act or forbid |
| Retry repeated failing tool calls | HITL / escalation | Escalate or stop |

---

## Design Heuristics

- Protect **persistence** almost as seriously as **external side effects**.
- Use **permissions** for hard limits, **policy** for model guidance.
- Use **guardrails** for automated screening, not as a substitute for approval.
- Put **humans** where consequence or ambiguity is high.
- Keep low-risk work smooth enough that people do not bypass the system.
- Log approvals, overrides, and durable writes with provenance.
- If a control point cannot be resumed safely, redesign it before relying on it.

---

## Relationship to Other Documents
- `research/vocabulary.md`
- `research/topics/tool-use-policy-and-permission-systems.md`
- `research/topics/human-in-the-loop-control-points.md`
- `research/topics/memory-systems.md`
- `research/topics/evaluation-prompt-testing.md`
- `research/topics/observability-traceability.md`
