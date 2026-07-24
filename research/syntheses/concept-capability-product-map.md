# Concept -> Capability -> Product Map

This document turns the current research tree into an operational knowledge map.

Its goal is not to repeat every note. Its goal is to answer:

- which durable concepts explain the repository best
- which capabilities sit between those concepts and specific tools
- how the current opencode product branch fits into that stack
- what conclusions seem justified now, while still leaving room for near-term drift

---

## Summary

The current research supports a simple structural conclusion:

> **The most useful mental model is a four-layer stack: concepts -> capabilities -> products -> syntheses.**

Where that means:

- **concepts** explain stable ideas and boundaries
- **capabilities** explain reusable mechanisms that several tools can implement
- **products** explain how one tool behaves today
- **syntheses** capture the conclusions this repository should carry forward

The main cleanup lesson from the current pass is:

> **Most prior duplication came from capability-level reasoning being stored inside product notes.**

That does not mean the product notes were bad. It means the middle layer was missing.

---

## Operating Conclusion

When a fact is being documented, ask three questions in order:

1. **Is this a durable idea or boundary?**
   - Put it in `concepts/`.
2. **Is this a reusable mechanism that several tools could implement differently?**
   - Put it in `capabilities/`.
3. **Is this an exact current behavior, config surface, or quirk of one tool?**
   - Put it in `products/`.

Then ask one final question:

4. **What should this repository conclude or standardize from that knowledge?**
   - Put that in `syntheses/`.

---

## Current Knowledge Map

### 1. Prompt and instruction shaping

#### Concept
- `../concepts/prompt-modularity-repository-architecture.md`
- `../concepts/instruction-layering.md`

#### Product
- `../products/opencode/config-and-instruction-loading.md`
- `../products/opencode/instruction-layering.md`
- `../products/opencode/system-prompt-control.md`

#### Repository conclusion
- Always-on instructions should stay small, inspectable, and separated from procedures.
- Skills are the preferred home for conditional reusable procedure.
- Product-specific prompt surgery should stay exceptional and heavily justified.

---

### 2. Tool access, permissions, and control boundaries

#### Concepts
- `../concepts/tool-use-policy-and-permission-systems.md`
- `../concepts/human-in-the-loop-control-points.md`

#### Capability
- `../capabilities/tool-calling.md`

#### Product
- `../products/opencode/agents-permissions-and-skills-basics.md`
- `../products/opencode/permissions-and-agent-safety.md`

#### Syntheses
- `../syntheses/control-boundaries.md`
- `../syntheses/vocabulary.md`

#### Repository conclusion
- The safest durable control model is layered, not monolithic:
  - policy tells the model what it should do
  - permissions tell the runtime what it may do
  - approvals/HITL gate consequential actions
- Product prompts are never enough as the real safety boundary.
- Structured action contracts are the missing middle layer between abstract tool policy and product-specific tool implementations.

---

### 3. Runtime policy, approvals, and enforcement

#### Concepts
- `../concepts/tool-use-policy-and-permission-systems.md`
- `../concepts/human-in-the-loop-control-points.md`

#### Capability
- `../capabilities/policy-engines.md`

#### Syntheses
- `../syntheses/control-boundaries.md`
- `../syntheses/observability-schema.md`

#### Repository conclusion
- Prompt guidance is not the real safety boundary.
- A reusable control plane needs:
  - structured policy inputs
  - explicit decision outputs
  - real enforcement hooks
  - audit and replay surfaces
- `allow` / `deny` alone is often too weak; `approve`, `escalate`, and `rewrite` are also first-class outcomes.

---

### 4. Context, references, and external attachment

#### Concept
- `../concepts/context-engineering.md`

#### Capability
- `../capabilities/context-attachments.md`
- `../capabilities/retrieval-pipelines.md`

#### Product
- `../products/opencode/references-and-external-context-basics.md`
- `../products/opencode/mcp-and-tooling.md`

#### Syntheses
- `../syntheses/memory-policy.md`

#### Repository conclusion
- The right default is not “give the system more context.”
- The right default is **attach bounded external context deliberately**.
- In this workflow, references come before heavier integrations like MCP.
- Attachment and retrieval are related but not identical:
  - attachments decide what outside context surface is available
  - retrieval decides how relevant evidence is selected from a larger available corpus
- Memory is broader still: persistence and promotion across time belong in memory architecture, not in attachment notes.

---

### 5. Provider choice and model routing

#### Concepts
- `../concepts/context-engineering.md`
- `../concepts/agent-architectures.md`

#### Capability
- `../capabilities/model-routing.md`

#### Product
- `../products/opencode/local-first-models-and-providers.md`
- `../products/opencode/config-surface-and-volatility-map.md`

#### Repository conclusion
- Provider configuration is infrastructure, not just product setup trivia.
- Backend choice affects trust boundary, latency, token limits, and debugging quality.
- Stable understanding should focus on routing concepts, not on today's exact field names.

---

### 6. Runtime durability, continuity, and recovery

#### Concepts
- `../concepts/memory-systems.md`
- `../concepts/observability-traceability.md`
- `../concepts/planning-systems.md`
- `../concepts/durable-execution.md`

#### Capability
- `../capabilities/sessions.md`

#### Product
- `../products/opencode/session-control-and-recovery.md`

#### Syntheses
- `../syntheses/memory-policy.md`
- `../syntheses/observability-schema.md`

#### Repository conclusion
- Durable execution is broader than session continuity.
- The underlying runtime model needs:
  - run identity
  - explicit state
  - replay/checkpoint semantics
  - side-effect isolation
  - retry and idempotency rules
- Good session continuity is valuable, but it is not a substitute for durable external documentation.
- Recovery features are strongest when paired with explicit wrap-up habits and Git-backed file history.

---

### 7. Evaluation infrastructure and release evidence

#### Concepts
- `../concepts/evaluation-prompt-testing.md`
- `../concepts/observability-traceability.md`
- `../concepts/human-in-the-loop-control-points.md`

#### Capability
- `../capabilities/eval-harnesses.md`

#### Syntheses
- `../syntheses/evaluation-method-comparison.md`
- `../syntheses/observability-schema.md`

#### Repository conclusion
- Evaluation methods alone are not enough; they need infrastructure.
- Durable eval practice depends on:
  - versioned cases
  - captured trajectories/evidence
  - score schemas
  - threshold or baseline comparison
  - explicit gate decisions
- Workflow-level eval must judge more than final answers.

---

### 8. MCP as capability expansion

#### Concepts
- `../concepts/context-engineering.md`
- `../concepts/tool-use-policy-and-permission-systems.md`

#### Capability
- `../capabilities/mcp.md`

#### Product
- `../products/opencode/mcp-and-tooling.md`

#### Repository conclusion
- MCP should be treated as capability expansion, not as simple “extra context.”
- In this environment, adoption should be incremental, local-first, and justified by a concrete use case.

---

## What Seems Stable Versus Likely To Drift

### Stable enough to build around
- separate always-on instructions from on-demand skills
- use permissions as runtime safety boundaries
- use explicit action contracts and policy decisions instead of relying on prompt prose alone
- keep external context bounded and named
- treat provider choice as a trust and routing decision
- treat long-running work as runs with state, not just chat sessions
- treat evaluation as infrastructure, not only as ad hoc review
- prefer resumability plus external durable notes over transcript replay

### Likely to drift soon
- exact opencode config key names and nesting
- exact MCP config shape
- extension/plugin hook details
- experimental system-prompt transform usage patterns

---

## Practical Rules For Future Notes

### Add a concept note when
- the idea should survive vendor churn mostly unchanged

### Add a capability note when
- several product notes keep re-explaining the same mechanism
- the mechanism is more stable than one product's syntax

### Add a product note when
- exact behavior, defaults, config, or drift matter

### Add a synthesis when
- the repository needs a settled distinction, policy, or decision aid

---

## Remaining Gaps

The tree is cleaner now, but the following capability-level gaps still exist:

- `task-artifact-and-run-record-models.md`
- `delegation-contracts-and-agent-interoperability.md`
- `approval-pause-resume-and-human-gates.md`
- possibly `plugin-and-hook-extensibility.md`
- possibly a future note on eval harnesses once there are more product branches to compare

Those are worth adding only if repetition actually reappears.

---

## Final Conclusion

The research is no longer just a pile of notes about AI workflow ideas and one active tool.

It now supports a more durable repository belief:

> **A maintainable local-first AI workflow is mostly a control-and-structure problem, not a novelty-feature problem.**

The highest-value knowledge so far points toward:

- small ambient instructions
- modular procedures in skills
- explicit permission envelopes
- bounded external context
- explicit provider routing
- resumable work with external durable truth
- cautious adoption of advanced extension surfaces

That is a more useful operational conclusion than any one product feature list.
