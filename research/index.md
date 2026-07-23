# Research Index

## Synthesis Documents
- `vocabulary.md` — shared terminology and boundary definitions across the research repository.
- `control-boundaries.md` — practical control model connecting permissions, approvals, HITL, guardrails, side effects, and durable writes.
- `principles-only.md` — implementation-agnostic design rules distilled from the researched topics.
- `memory-policy.md` — practical repository policy for memory layers, durable-write gates, provenance, review thresholds, and retirement rules.
- `observability-schema.md` — minimum useful trace and event schema for tasks, tool calls, approvals, durable writes, failures, and review outcomes.
- `workflow-pattern-comparison.md` — decision-support matrix for choosing between chain, route, parallelize, orchestrator-worker, evaluator-optimizer, and ReAct.
- `evaluation-method-comparison.md` — decision-support matrix for choosing between exact match, rubric, pairwise comparison, LLM judge, and human review.

## Current Topics

| Topic | Status | File | Notes |
|---|---|---|---|
| Agent architectures | Researched | `topics/agent-architectures.md` | Foundational topic for role boundaries, orchestration patterns, and autonomy tradeoffs. |
| Skill systems | Researched | `topics/skill-systems.md` | Focus on reusable capability packaging, invocation, and progressive disclosure. |
| Context engineering | Researched | `topics/context-engineering.md` | Focus on memory boundaries, retrieval, salience, and context shaping. |
| Planning systems | Researched | `topics/planning-systems.md` | Focus on decomposition, replanning, orchestration, and stop conditions. |
| Evaluation / prompt testing | Researched | `topics/evaluation-prompt-testing.md` | Focus on reliability, regressions, workflow-level testing, and evidence-driven iteration. |
| Memory systems | Researched | `topics/memory-systems.md` | Focus on memory tiers, retrieval, durable writes, and provenance. |
| Human-in-the-loop control points | Researched | `topics/human-in-the-loop-control-points.md` | Focus on approvals, escalation, review/edit loops, and safe pause/resume. |
| Tool-use policy and permission systems | Researched | `topics/tool-use-policy-and-permission-systems.md` | Focus on least privilege, scoped autonomy, prompt-injection defense, and approval boundaries. |
| Prompt modularity / repository architecture | Researched | `topics/prompt-modularity-repository-architecture.md` | Focus on structure, layering, overrides, and eval-backed prompt maintenance. |
| Observability / traceability | Researched | `topics/observability-traceability.md` | Focus on traces, spans, provenance, auditability, and debugging. |

## Suggested Reading Order
1. `topics/agent-architectures.md`
2. `topics/planning-systems.md`
3. `topics/context-engineering.md`
4. `topics/memory-systems.md`
5. `topics/skill-systems.md`
6. `topics/tool-use-policy-and-permission-systems.md`
7. `topics/human-in-the-loop-control-points.md`
8. `topics/observability-traceability.md`
9. `topics/evaluation-prompt-testing.md`
10. `topics/prompt-modularity-repository-architecture.md`

## Cross-Cutting Themes
- Prefer simple, inspectable workflows before adding autonomy.
- Separate principles from product-specific implementations.
- Keep procedure modular and reusable.
- Treat context as a scarce resource.
- Evaluate changes with evidence, not vibes.
- Put humans at consequential boundaries.
- Preserve provenance for memory, tool use, and decisions.
- Keep permissions narrow and explicit.
- Treat traces as part of the system design, not only debugging exhaust.

## Suggested Next Topics
- Multi-agent collaboration
- Reflection and self-critique
- Model routing
- RAG for prompt repositories
- Knowledge representation / ontology for prompt repositories
- Policy-as-code for agent governance
