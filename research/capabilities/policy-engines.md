# Policy Engines

## Freshness
- Last reviewed: 2026-07-24
- Stability: Medium
- Likely drift areas:
  - exact hook APIs and callback shapes in agent SDKs
  - policy languages, hosted policy services, and approval frameworks
  - built-in guardrail and human-review orchestration features

## Summary
- A policy decision and enforcement plane is the reusable runtime layer that evaluates proposed actions, returns an explicit control decision, and applies that decision at real execution boundaries.
- The durable idea is not any one policy engine, rule language, or vendor feature. It is the separation between:
  - model guidance about what should happen
  - runtime policy decisions about what may happen now
  - enforcement hooks that decide what actually happens next
- Good planes emit more than a boolean. Typical outputs include `allow`, `deny`, `approve`, `escalate`, and `rewrite`, ideally with reasons, evidence, and audit metadata.

## Motivation
- This repository already has the concept layer for policy and permissions, plus a synthesis of control boundaries.
- What was missing was the capability-layer note for the reusable mechanism that sits between those ideas and a concrete product surface.
- In practice, many agent systems fail here by mixing prompt guidance, permission checks, approvals, guardrails, and ad hoc tool wrappers into one blurry control path.

## Problem Statement
- A model can be told what it should do, but prompts alone do not create a dependable safety boundary.
- A runtime can have permissions, but scattered allow/deny checks are hard to reason about, audit, and test.
- A system can have approvals and guardrails, but without a common decision layer it becomes unclear:
  - which control made the decision
  - which data the decision used
  - which hook enforced it
  - how similar decisions are kept consistent across tools and workflows

## Core Function
- Accept a proposed action, state transition, or artifact write together with runtime context.
- Evaluate policy using explicit inputs rather than only natural-language instructions.
- Return a machine-usable decision envelope.
- Enforce that envelope at model, tool, workflow, data, and persistence boundaries.
- Record enough evidence that the decision can be explained, replayed, and tested later.

## Minimal Durable Model

### 1. Proposal
The plane needs a concrete thing to evaluate.

Typical proposals include:
- a tool call request
- a file edit or durable memory write
- an outbound message or network request
- a workflow transition such as auto-continue, retry, or handoff
- a model output that is about to be shown, stored, or executed downstream

Useful proposal fields:
- action or event type
- actor or agent identity
- requested target or resource
- arguments or payload
- side-effect class
- run/session/task correlation IDs

### 2. Policy Inputs
The decision layer needs structured facts, not just a free-text prompt.

Common inputs:
- actor identity and role
- declared autonomy scope
- tool or action contract metadata
- target resource and sensitivity
- side-effect class and reversibility
- provenance and trust level of upstream content
- user intent and any explicit approvals already granted
- environment facts such as machine, tenant, repo, branch, network zone, or time window
- budget and rate limits such as cost, tokens, call count, or retry count
- prior history such as repeated failures, previous denials, or escalation state

This is one of the biggest durable distinctions in the space:

- **model guidance** is usually natural language and behavior-shaping
- **policy input** is structured runtime evidence used for a real decision

### 3. Decision Function
The plane evaluates the proposal against rules, risk logic, approvals, and guardrails.

Implementation styles vary:
- inline code callbacks
- rule engines
- policy-as-data tables
- central policy services
- mixed models where deterministic checks call out to approval or review workflows

The portable part is not the implementation style. The portable part is that the decision is explicit, inspectable, and separate from the raw proposal.

### 4. Decision Envelope
The output should be explicit enough for downstream enforcement.

Common decision outcomes:
- `allow` — proceed automatically
- `deny` — block execution
- `approve` — pause and request explicit approval for this instance
- `escalate` — hand off to a human, higher-trust agent, or exception workflow
- `rewrite` — modify or narrow the request before execution

Useful envelope fields:
- decision outcome
- reason code
- human-readable rationale
- rule or policy version
- conditions or constraints
- rewritten payload when applicable
- required approver or escalation target
- trace IDs and timestamps

### 5. Enforcement
The decision has to attach to a real boundary.

Typical effects:
- continue unchanged
- block and return an error/refusal
- interrupt and wait for approval
- transform arguments or redact content
- route to a safer tool or narrower action
- require review before persistence or downstream execution

Without a clear enforcement hook, the plane is only advisory.

## Decision Outputs Are Not Just Allow/Deny
- `allow` handles low-risk or already-authorized work.
- `deny` creates a hard boundary.
- `approve` supports instance-level consent for consequential actions.
- `escalate` handles ambiguity, repeated failure, conflict, or policy uncertainty.
- `rewrite` supports bounded autonomy by narrowing a request instead of only blocking it.

Examples of `rewrite` behavior:
- strip forbidden parameters
- downgrade a broad filesystem request to a narrower path scope
- redact sensitive fields before a model or external service sees them
- convert an external side effect into a draft artifact that still needs review

This is one reason a reusable decision plane is more capable than a simple permission map.

## Enforcement Hook Points
Different products expose different APIs, but the reusable hook classes are fairly stable.

### Pre-exposure hooks
Control what the model or workflow can even see or select.

Examples:
- which tools are advertised
- which model routes are available
- which resources are attachable

### Pre-execution hooks
The most common enforcement point.

Examples:
- before tool execution
- before file or data mutation
- before network access
- before memory or config writes

### Mid-workflow hooks
Used when a run should pause, reroute, or change mode.

Examples:
- approval interruptions
- retry suppression after repeated failure
- escalation into review mode

### Post-execution hooks
Useful when outputs must be validated before propagation.

Examples:
- output validation
- post-tool result screening
- redaction before display or storage
- preventing untrusted results from becoming durable truth

### Persistence hooks
Often under-protected, but highly important.

Examples:
- before storing memory
- before updating policy/config/instructions
- before promoting draft artifacts into durable records

## Relationship to Permissions, Approvals, and Guardrails

### Permissions
- Permissions usually answer whether an actor may perform a class of actions on a resource.
- In many systems, permissions are one major input to the decision plane or one subset of its rules.
- A permission check alone is narrower than the full plane because it often does not cover escalation, rewrite, or post-execution handling.

### Approvals
- Approval is usually a decision outcome, not the whole policy system.
- The plane decides when approval is required and what state must be captured to pause and resume safely.
- Approval is instance-specific: it answers whether this run may continue now.

### Guardrails
- Guardrails are automated checks on inputs, outputs, or actions.
- They can feed the plane, be invoked by the plane, or serve as enforcement helpers.
- A guardrail trip is not always a simple denial. It may trigger rewrite, escalation, or review.

### Prompt guidance and system instructions
- Prompt guidance shapes model behavior upstream.
- The decision plane enforces runtime boundaries downstream.
- Well-designed systems use both, but do not confuse them.

## Separation From Nearby Notes
- `../concepts/tool-use-policy-and-permission-systems.md` explains the durable principles: least privilege, fail-safe defaults, complete mediation, and approval boundaries.
- `../syntheses/control-boundaries.md` explains how policy, permissions, guardrails, approvals, HITL, and durable-write controls fit together conceptually.
- This note explains the reusable implementation layer that turns those ideas into a runtime mechanism:
  - structured policy inputs
  - explicit decision outputs
  - hook points for enforcement
  - audit and test surfaces

## Common Patterns
- centralized policy decision point with distributed enforcement hooks
- local per-tool or per-workflow policy callbacks
- risk-tiered policy using side-effect class and target sensitivity
- approval workflows for high-consequence actions
- rewrite/sanitize steps before execution or storage
- post-execution validation before downstream propagation
- resumable interruption state for approval and escalation paths
- decision logging with trace IDs and rule versions

## Typical Components
- proposal/event normalizer
- policy input collector
- rule engine or decision callback
- permission and resource metadata adapter
- guardrail validators
- approval workflow adapter
- enforcement hook adapters
- decision log / audit sink
- replay and policy test harness

## Auditability
Auditability is one of the strongest reasons to separate the decision plane from prompts.

Minimum useful audit record:
- what proposal was evaluated
- what inputs were used
- what decision was returned
- which rule set or policy version applied
- what enforcement action actually happened
- whether a human approved, overrode, or rejected the action
- correlation IDs linking the decision to the run, tool call, and resulting side effects

Good auditability supports:
- incident review
- permission debugging
- policy drift detection
- compliance evidence
- evaluation and regression testing

## Testability
Good policy systems are testable because they are explicit functions over structured inputs.

Useful testing patterns:
- table-driven tests for policy cases
- golden cases for approval, denial, rewrite, and escalation behavior
- replay tests using captured decision inputs from real runs
- boundary tests for sensitive targets, high-risk side effects, and ambiguous requests
- regression tests for prior incidents or prompt-injection attempts

Weakly testable signs:
- the main control logic only exists in prompt prose
- tool wrappers each implement their own hidden checks
- approval behavior depends on UI state but is not represented in runtime state

## Durable Distinctions

### Model suggestion vs runtime decision
The model can propose an action. The runtime still decides what actually happens.

### Authorization vs approval
Authorization answers whether an actor may ever do this class of thing.
Approval answers whether this specific instance may proceed now.

### Validation vs policy
A request can be schema-valid and still be denied, escalated, or rewritten.

### Policy decision vs enforcement
The decision answer and the hook that applies it are separate concerns.

### Durable-write controls vs ordinary execution controls
Writing long-lived truth often deserves stronger gating than ordinary drafting.

## Portability
- Portable across tools:
  - clear separation between behavior guidance and runtime control
  - explicit decision envelopes instead of hidden booleans
  - stable hook classes around proposal, execution, output, and persistence
  - audit logs tied to policy version and run context
  - replayable, testable decision logic
- Product-shaped:
  - exact rule syntax or policy language
  - embedded versus centralized policy services
  - synchronous versus asynchronous approval handling
  - exact plugin, middleware, or hook APIs
  - whether rewrite is first-class or implemented indirectly

## Advantages
- clearer runtime safety boundary
- more consistent handling across tools and workflows
- easier approval and permission integration
- better audit trails and incident review
- more testable control logic
- cleaner separation between model behavior shaping and enforcement

## Risks / Failure Modes
- treating prompts as the real policy plane
- collapsing permissions, approvals, and guardrails into one vague callback
- collecting too little structured input for reliable decisions
- rewrite behavior becoming hidden mutation instead of explicit policy
- inconsistent enforcement where a decision is logged but not actually applied
- missing pause/resume state for approvals or escalations
- under-protecting durable writes compared with obvious external side effects
- central policy that is consistent but too detached from local context

## Tradeoffs
- **Centralized policy vs local policy**: central policy improves consistency; local policy improves relevance and latency.
- **Strict denial vs rewrite/escalate options**: richer outcomes improve usability, but make reasoning and testing more complex.
- **More inputs vs simpler decisions**: richer context improves fit, but increases maintenance burden and audit surface.
- **Inline checks vs dedicated plane**: inline checks are faster to start; dedicated planes are easier to inspect, reuse, and test.

## Relationships to Other Notes
- `../concepts/tool-use-policy-and-permission-systems.md`
- `../concepts/human-in-the-loop-control-points.md`
- `../concepts/observability-traceability.md`
- `../concepts/evaluation-prompt-testing.md`
- `../capabilities/tool-calling.md`
- `../concepts/instruction-layering.md`
- `../syntheses/control-boundaries.md`
- `../syntheses/observability-schema.md`

## Relevance to This Repository
- Keep prompt guidance for behavior shaping, but put real execution control in explicit runtime decisions.
- Represent control outcomes as a small standard envelope such as `allow` / `deny` / `approve` / `escalate` / `rewrite` with reason codes.
- Put enforcement hooks near consequential boundaries:
  - tool execution
  - durable writes
  - external actions
  - approval pause/resume points
- Log policy decisions with enough context to replay incidents and build regression tests.
- Treat memory writes, repo-rule updates, and config changes as first-class policy targets, not just ordinary edits.

## Open Questions
- What is the smallest useful decision envelope for this repository's workflows?
- Which decisions should be centralized versus kept close to specific tools or artifact classes?
- Where is `rewrite` genuinely safer and more usable than a simple denial?
- How much policy input context is worth standardizing before complexity outweighs clarity?
- Which approval and escalation events deserve durable storage by default?

## References
- [Basic Principles of Information Protection](https://web.mit.edu/Saltzer/www/publications/protection/Basic.html) — Saltzer and Schroeder. Classic source for complete mediation, least privilege, and fail-safe defaults.
- [NIST SP 800-162: Guide to Attribute Based Access Control (ABAC)](https://csrc.nist.gov/pubs/sp/800/162/upd2/final) — NIST. Useful for the idea that policy decisions are made from structured attributes about subject, object, action, and environment.
- [NIST SP 800-207: Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final) — NIST. Useful for policy decision point and policy enforcement point separation.
- [Open Policy Agent Documentation](https://www.openpolicyagent.org/docs/latest/) — OPA docs. Practical example of a general-purpose policy decision layer without tying this note to one engine.
- [Cedar](https://www.cedarpolicy.com/en) — Cedar policy language site. Useful as evidence that explicit policy inputs and authorization decisions are now common design patterns.
- [Guardrails and human review](https://platform.openai.com/docs/guides/agents/guardrails-approvals) — OpenAI docs. Helpful current example of guardrails, approvals, and interrupt/resume control points.
- [Model Spec](https://model-spec.openai.com/) — OpenAI. Useful framing for scope of autonomy, side effects, and chain-of-command boundaries.
- [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) — Anthropic Engineering. Supports keeping control boundaries explicit and composable instead of burying them in prompt complexity.
