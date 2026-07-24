# Observability / Traceability

## Summary
- Observability for AI systems is best treated as an extension of distributed-systems observability.
- The durable foundation is traces, spans, context propagation, structured attributes, and semantic conventions.
- For AI workflows, useful observability must include prompts, model calls, retrievals, tool calls, token/cost usage, and evaluation or review feedback—not just latency and errors.

## Motivation
- Your workflow needs auditability, debugging, and resumability.
- Observability kept appearing indirectly in evaluation, memory provenance, human review, and agent debugging, so it deserves its own topic.

## Problem Statement
- AI workflows fail across many boundaries: prompt rendering, retrieval, orchestration, model selection, tool use, queues, retries, and human intervention.
- Plain logs rarely preserve enough causal structure to explain what happened end-to-end.

## Key Concepts
- Trace
- Span
- Context propagation
- Attributes
- Events
- Links
- Baggage
- Semantic conventions

## Principles vs Implementations
### Principles
- Represent one workflow run as one root trace.
- Represent each meaningful step as a span.
- Propagate trace context across boundaries.
- Use structured metadata, not only free-text logs.
- Capture AI-specific metadata such as prompt version, model, tokens, retrieval docs, tool arguments, and eval results.
- Correlate traces with logs, metrics, and human feedback.
- Design redaction, privacy, and sampling deliberately.

### Implementations / Examples
- W3C Trace Context
- OpenTelemetry traces/spans/attributes/events
- OpenInference AI-specific semantic conventions
- MLflow tracing
- Langfuse tracing

## Design Patterns
- **One workflow run = one root trace**.
- **One meaningful step = one span**.
- **Propagate trace context everywhere**: HTTP, queues, callbacks, tools, human review resumes.
- **Separate identifiers from rich payloads**: keep stable IDs even if raw text is redacted.
- **Capture orchestration and content metadata**: not just timing.
- **Use events for incidents**: retries, fallbacks, moderation blocks, human overrides.
- **Use links for async or fan-out work**.
- **Redact before export** and sample intelligently.
- **Join execution traces to evaluation traces**.

## Advantages
- Faster debugging.
- Better root-cause isolation.
- Better cost and latency visibility.
- Better auditability of tool use and human review.
- Better portability when based on standards.
- Better dataset creation for future evals.

## Disadvantages
- Rich traces can be expensive.
- Trace data can leak sensitive information if handled badly.
- Good instrumentation takes deliberate effort.
- Too much tracing creates noisy, low-value data.
- AI-specific conventions are still less standardized than generic tracing.

## Tradeoffs
- **Richness vs privacy**: detailed traces help debugging but raise data risk.
- **Completeness vs cost**: full traces for everything are expensive.
- **Standardization vs AI-specific expressiveness**: portability versus detail.
- **Tree simplicity vs real workflow shape**: simple traces are cleaner, but real workflows often branch and resume.

## Relationships to Other Topics
- Observability supports [Evaluation / Prompt Testing](./evaluation-prompt-testing.md) by linking quality results to exact runs.
- It improves provenance in [Memory Systems](./memory-systems.md).
- It records review and approval events from [Human-in-the-loop control points](./human-in-the-loop-control-points.md).
- It helps debug [Agent Architectures](./agent-architectures.md), [Planning Systems](./planning-systems.md), and [Tool-Use Policy and Permission Systems](./tool-use-policy-and-permission-systems.md).

## Practical Applications for This Repository
- Define a canonical trace shape for runs, model calls, retrievals, tool calls, and evaluators.
- Attach prompt version, workflow name, model, tool version, and repo revision to traces.
- Treat prompt rendering as a traceable step, not just the final model call.
- Capture retrieval provenance and tool-call metadata.
- Link human review and evaluator feedback back to the same trace.
- Define a repo-level redaction and retention policy before capturing raw content.

## Open Questions
- How standardized will AI-specific tracing semantics become?
- How much raw prompt/output text should be stored by default?
- What is the right retention model for rich AI traces?
- How should human-in-the-loop pauses and resumptions be visualized clearly?

## Clarifications and Common Misconceptions
- **Observability is not just logs.** Traces, spans, events, metadata, and linked evaluation/review signals matter more for multi-step AI workflows.
- **Traceability is not the same as reproducibility.** A trace can explain what happened without making the run deterministic or perfectly replayable.
- **More captured data is not automatically better.** Rich traces raise privacy, retention, and cost issues fast.
- **Flat request logging is not enough for agents.** Handoffs, retries, approvals, retrieval steps, and tool calls need structured trace boundaries.
- **Observability and evaluation are different layers.** Observability records behavior; evaluation judges whether the behavior was good.

## References
- [Dapper, a Large-Scale Distributed Systems Tracing Infrastructure](https://research.google/pubs/pub36356/) — Google Research, 2010. Foundational tracing paper.
- [Trace Context](https://www.w3.org/TR/trace-context/) — W3C, 2021. Standard for `traceparent` and `tracestate` propagation.
- [Observability primer](https://opentelemetry.io/docs/concepts/observability-primer/) — OpenTelemetry docs, year not visible. Clear framing of observability goals.
- [Traces](https://opentelemetry.io/docs/concepts/signals/traces/) — OpenTelemetry docs, year not visible. Core trace/span model.
- [Context propagation](https://opentelemetry.io/docs/concepts/context-propagation/) — OpenTelemetry docs, year not visible. Central to keeping multi-step workflows connected.
- [Baggage](https://opentelemetry.io/docs/concepts/signals/baggage/) — OpenTelemetry docs, year not visible. Useful with explicit warnings about sensitivity and leakage.
- [Semantic Conventions](https://arize-ai.github.io/openinference/spec/semantic_conventions.html) — OpenInference, year not visible. AI-specific span kinds and metadata conventions.
- [MLflow tracing for LLM and Agent Observability](https://mlflow.org/docs/latest/genai/tracing/) — MLflow docs, 2025 footer shown. Example of OpenTelemetry-compatible AI tracing.
- [Langfuse tracing](https://langfuse.com/docs/tracing) — Langfuse docs, year not visible. Practical articulation of AI application tracing and sessions.
- [OpenAI tracing](https://openai.github.io/openai-agents-python/tracing/) — OpenAI Agents SDK docs, year not clearly visible. Useful nuance on spans, sensitive data, and tracing availability limits.
- [LangSmith observability quickstart](https://docs.langchain.com/langsmith/observability-quickstart) — LangSmith docs, year not clearly visible. Helpful distinction between trace and span in AI workflow observability.
