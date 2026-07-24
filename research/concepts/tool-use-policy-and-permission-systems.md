# Tool-Use Policy and Permission Systems

## Summary
- Tool-use policy is about what an agent may do, under what conditions, with what authority, and when it must pause for approval.
- The durable principles come mostly from classic security design: least privilege, fail-safe defaults, complete mediation, separation of privilege, and strong audit trails.
- For AI systems, these principles must be adapted to prompt injection, scoped autonomy, tool schemas, and human approval before risky side effects.

## Motivation
- This is high value for a local-first, corporate-safe workflow where tool access and data handling matter as much as output quality.
- It directly affects how safe agent automation can become without turning into bureaucracy.

## Problem Statement
- Tool-using agents can misunderstand intent, misuse tools, act on untrusted content, or perform side effects with too much authority.
- The design problem is how to grant useful autonomy while keeping the blast radius small and making decisions inspectable.

## Key Concepts
- Least privilege
- Fail-safe defaults
- Complete mediation
- Separation of privilege
- Scope of autonomy
- Guardrails
- Human approval
- Prompt injection resistance
- Audience-bound authorization
- Auditability

## Principles vs Implementations
### Principles
- Default deny; explicit allow.
- Grant the narrowest capability that solves the task.
- Check authority at every sensitive boundary.
- Treat external/fetched content as untrusted.
- Distinguish low-risk reasoning from high-risk side effects.
- Pause for confirmation on destructive, costly, or ambiguous actions.
- Keep policy visible and auditable.

### Implementations / Examples
- OpenAI Model Spec scope-of-autonomy framing
- MCP authorization patterns
- Input/output/tool guardrails
- Tool parameter validation
- Approval interruptions
- OWASP-style prompt injection defenses

## Design Patterns
- **Capability-based tool exposure**: narrow tools instead of broad access.
- **Risk-tiered execution**: read-only, mutating, and external side-effect classes.
- **Preflight / runtime / postflight controls**: checks before, during, and after actions.
- **Scoped autonomy contract**: allowed tools, cost limits, stop conditions.
- **Dual-channel trust model**: trusted instructions separate from untrusted retrieved content.
- **Human approval for side effects**: pause before consequential actions.
- **Defense in depth**: combine schemas, validation, least privilege, guardrails, and logging.

## Advantages
- Reduces blast radius from mistakes.
- Makes risky behavior inspectable and auditable.
- Supports governance and compliance.
- Improves trust in tool-using workflows.

## Disadvantages
- Adds engineering complexity and some latency.
- Strict policies can make agents feel brittle.
- Tool/policy upkeep becomes ongoing work.
- Prompt-injection defenses remain imperfect.

## Tradeoffs
- **Autonomy vs control**: flexibility versus safety.
- **General tools vs narrow tools**: capability versus validation simplicity.
- **Model-based guardrails vs deterministic checks**: nuance versus predictability.
- **Central policy vs local policy**: consistency versus relevance.

## Relationships to Other Topics
- Policy boundaries define where [Human-in-the-loop control points](./human-in-the-loop-control-points.md) should exist.
- Tool actions should be captured in [Observability / Traceability](./observability-traceability.md).
- Policy is part of repository structure; see [Prompt Modularity / Repository Architecture](./prompt-modularity-repository-architecture.md).
- Tool-policy effectiveness should be measured via [Evaluation / Prompt Testing](./evaluation-prompt-testing.md).

## Relevance to This Repository
- Maintain a tool registry with purpose, schema, sensitivity, side-effect class, and approval rules.
- Separate read-only and mutating tools.
- Define a simple policy matrix: auto / review / approve / forbidden.
- Keep prompt-injection tests for tools that consume external content.
- Store approval rules near the tool definition, not only in high-level prompts.
- Define standard autonomy profiles such as research-only, read-only, edit-limited, and external-action approval required.

## Open Questions
- What is the right permission granularity: tool, method, parameter, or data domain?
- How much policy belongs in prompts versus runtime enforcement?
- How should scope of autonomy be represented so it is both human-readable and machine-enforceable?
- How should permissions propagate across subagents?

## Clarifications and Common Misconceptions
- **Tool-use policy and permissions are related but not identical.** Policy shapes when/how the model should use tools; permissions decide what the runtime will actually allow.
- **Schema validity is not business validity.** A tool call can match the JSON schema and still be the wrong, unsafe, or unauthorized action.
- **Approval is not the same as authorization.** Approval is a workflow control point; authorization is a security/access-control decision.
- **Seeing a tool does not mean the model will use it correctly.** Tool descriptions, examples, `tool_choice`, and trust boundaries matter.
- **Prompt steering is not the same as hard enforcement.** Natural-language guidance can bias tool use, but runtime constraints and approval gates are the real safety boundary.

## References
- [Basic Principles of Information Protection](https://web.mit.edu/Saltzer/www/publications/protection/Basic.html) — MIT, year not visible. Classic source for least privilege, fail-safe defaults, complete mediation, and separation of privilege.
- [NIST SP 800-53 Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) — NIST, 2020. Broad control catalog grounding permissions and audit practices.
- [Model Spec](https://model-spec.openai.com/2025-09-12.html) — OpenAI, 2025. Defines chain of command, scope of autonomy, and side-effect control.
- [MCP Authorization](https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization) — Model Context Protocol, 2025. OAuth/resource indicator/audience validation patterns for MCP servers.
- [Guardrails and human review](https://platform.openai.com/docs/guides/agents/guardrails-approvals) — OpenAI docs, year not visible. Practical guidance for input/output/tool guardrails and approval interruptions.
- [OpenAI Agents SDK guardrails](https://openai.github.io/openai-agents-python/ref/guardrail/) — OpenAI Agents SDK docs, year not visible. API-level example of tripwires and guardrails.
- [LLM Prompt Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html) — OWASP, year not visible. Practical threat model and layered defenses.
- [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) — Anthropic Engineering, 2024. Supports simple, composable workflows and careful tool/interface design.
- [Anthropic tool use overview](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview) — Anthropic docs, year not clearly visible. Useful distinction between client and server tool execution boundaries.
- [Anthropic define tools](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/define-tools) — Anthropic docs, year not clearly visible. Helpful nuance on descriptions, `tool_choice`, and parameter handling.
