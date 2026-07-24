# Research Index

## Synthesis Documents
- `syntheses/vocabulary.md` — shared terminology and boundary definitions across the research repository.
- `syntheses/control-boundaries.md` — practical control model connecting permissions, approvals, HITL, guardrails, side effects, and durable writes.
- `syntheses/principles-only.md` — implementation-agnostic design rules distilled from the researched concepts.
- `syntheses/memory-policy.md` — practical repository policy for memory layers, durable-write gates, provenance, review thresholds, and retirement rules.
- `syntheses/observability-schema.md` — minimum useful trace and event schema for tasks, tool calls, approvals, durable writes, failures, and review outcomes.
- `syntheses/workflow-pattern-comparison.md` — decision-support matrix for choosing between chain, route, parallelize, orchestrator-worker, evaluator-optimizer, and ReAct.
- `syntheses/evaluation-method-comparison.md` — decision-support matrix for choosing between exact match, rubric, pairwise comparison, LLM judge, and human review.
- `products/opencode/system-prompt-control.md` — finding: the `experimental.chat.system.transform` plugin hook as the untested escape hatch for trimming opencode's baked core system prompt.

## Concepts (`concepts/`)

| Concept | Status | File | Notes |
|---|---|---|---|
| Agent architectures | Researched | `concepts/agent-architectures.md` | Foundational concept for role boundaries, orchestration patterns, and autonomy tradeoffs. |
| Skill systems | Researched | `concepts/skill-systems.md` | Focus on reusable capability packaging, invocation, and progressive disclosure. |
| Context engineering | Researched | `concepts/context-engineering.md` | Focus on memory boundaries, retrieval, salience, and context shaping. |
| Planning systems | Researched | `concepts/planning-systems.md` | Focus on decomposition, replanning, orchestration, and stop conditions. |
| Evaluation / prompt testing | Researched | `concepts/evaluation-prompt-testing.md` | Focus on reliability, regressions, workflow-level testing, and evidence-driven iteration. |
| Memory systems | Researched | `concepts/memory-systems.md` | Focus on memory tiers, retrieval, durable writes, and provenance. |
| Human-in-the-loop control points | Researched | `concepts/human-in-the-loop-control-points.md` | Focus on approvals, escalation, review/edit loops, and safe pause/resume. |
| Tool-use policy and permission systems | Researched | `concepts/tool-use-policy-and-permission-systems.md` | Focus on least privilege, scoped autonomy, prompt-injection defense, and approval boundaries. |
| Prompt modularity / repository architecture | Researched | `concepts/prompt-modularity-repository-architecture.md` | Focus on structure, layering, overrides, and eval-backed prompt maintenance. |
| Observability / traceability | Researched | `concepts/observability-traceability.md` | Focus on traces, spans, provenance, auditability, and debugging. |

## Capabilities (`capabilities/`)

| Capability | Status | File | Notes |
|---|---|---|---|
| Branch scaffold | Initialized | `capabilities/README.md` | Medium-volatility layer for MCP, RAG, tool calling, routing, and similar reusable capabilities. |

## Products (`products/`)

| Product | Status | File | Notes |
|---|---|---|---|
| Product branch scaffold | Initialized | `products/README.md` | Fast-moving product snapshot layer for tool-specific notes and feature maps. |
| opencode | Initialized | `products/opencode/README.md` | Starter branch for product-specific opencode research and advanced-feature mapping. |
| opencode foundations | Researched | `products/opencode/foundations.md` | Foundation-first overview of opencode as a harness: control surfaces, reading order, and what to learn before advanced features. |
| opencode config and instruction loading | Researched | `products/opencode/config-and-instruction-loading.md` | Snapshot of merged config behavior, instruction precedence, and practical debugging heuristics. |
| opencode agents / permissions / skills basics | Researched | `products/opencode/agents-permissions-and-skills-basics.md` | Foundation note on named workers, runtime control, and on-demand procedural modules. |
| opencode references and external context basics | Researched | `products/opencode/references-and-external-context-basics.md` | Foundation note on named external context, aliasing, and how references relate to external-directory boundaries. |
| opencode local-first models and providers | Researched | `products/opencode/local-first-models-and-providers.md` | Foundation note on provider routing, local backends, and why provider clarity matters before deeper feature work. |
| opencode config surface and volatility map | Researched | `products/opencode/config-surface-and-volatility-map.md` | Snapshot of where current docs and v2 spec direction appear aligned versus in flux. |
| opencode permissions and agent safety | Researched | `products/opencode/permissions-and-agent-safety.md` | Product note on permission semantics, external boundaries, and why safety comes from the agent-plus-permission envelope. |
| opencode advanced features map | Researched | `products/opencode/advanced-features-map.md` | Ranked map of which advanced areas matter most next, and which should be deferred as higher-risk or more volatile. |
| opencode instruction layering | Researched | `products/opencode/instruction-layering.md` | Product note on how AGENTS, CLAUDE fallback, configured instructions, and skills appear to layer in practice. |
| opencode system prompt control | Researched | `products/opencode/system-prompt-control.md` | Verified note on code-built prompt assembly, confirmed plugin transform hook, and what remains untested about practical prompt surgery. |
| opencode session control and recovery | Researched | `products/opencode/session-control-and-recovery.md` | Product note on sessions, interruption, compaction, snapshots, and why recovery features matter for interrupted workflows. |
| opencode MCP and tooling | Researched | `products/opencode/mcp-and-tooling.md` | Product note on local/remote MCP, capability expansion, prompt-surface cost, and cautious adoption order. |

## Suggested Reading Order
1. `concepts/agent-architectures.md`
2. `concepts/planning-systems.md`
3. `concepts/context-engineering.md`
4. `concepts/memory-systems.md`
5. `concepts/skill-systems.md`
6. `concepts/tool-use-policy-and-permission-systems.md`
7. `concepts/human-in-the-loop-control-points.md`
8. `concepts/observability-traceability.md`
9. `concepts/evaluation-prompt-testing.md`
10. `concepts/prompt-modularity-repository-architecture.md`

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

## Maintenance Rules
- Put slower-moving, vendor-neutral ideas in `concepts/`.
- Put medium-volatility cross-tool capabilities in `capabilities/`.
- Put fast-moving tool snapshots in `products/`.
- Product notes should include freshness metadata.
