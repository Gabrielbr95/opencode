# Research Backlog

## Open Questions
- Which workflow ideas are durable principles versus tool-specific implementations?
- Which evaluation methods are lightweight enough for day-to-day prompt maintenance?
- Which minimal eval stack gives the best signal-to-effort ratio for routine repository changes?
- When should pairwise comparison beat rubric scoring for prompt or workflow iteration?
- Which qualities should never rely on LLM judge alone in this repository?
- When does a skill system outperform a larger monolithic agent prompt?
- What is the minimum useful memory/context architecture for a local-first workflow?
- When do multi-agent patterns outperform a strong single-agent + skills architecture in practice?
- What should be stored as durable memory versus regenerated or re-retrieved each session?
- Which memory items deserve explicit metadata fields versus lightweight inline provenance?
- When should a memory item be superseded in place versus retired and left as historical record?
- Which memory writes should be allowed automatically versus only proposed for review?
- Which permission and tool-governance patterns best fit a local-first corporate environment?
- What should be traced by default versus only on failure or audit demand?
- Which observability events deserve durable retention versus short-lived diagnostic retention?
- How much raw prompt/output content should ever be stored versus replaced by summaries and IDs?
- What is the smallest stable default event vocabulary that still supports audit, debugging, and resumption?
- Which prompt repository metadata is worth standardizing versus leaving informal?
- Which decisions should be enforced as policy-as-code instead of only documented in prompts?

## Candidate Future Topics
- Reflection and self-critique
- Multi-agent collaboration patterns
- Model routing
- RAG for prompt repositories
- Knowledge representation / ontology for prompt repositories
- Policy-as-code for agent governance
- Provenance models for prompts, memory, and evaluations

## Follow-Up Ideas From Initial Research
- Create a comparison matrix of workflow patterns: chain, route, parallelize, orchestrator-worker, evaluator-optimizer, ReAct. [Done: `research/workflow-pattern-comparison.md`]
- Create a comparison matrix of evaluation methods: exact match, rubric, pairwise, LLM judge, human review. [Done: `research/evaluation-method-comparison.md`]
- Distill a repository-specific vocabulary: workflow, agent, skill, project context, MCP, memory, evaluation. [Done: `research/vocabulary.md`]
- Add a “principles only” note that extracts durable rules from the first five topics. [Done: `research/principles-only.md`]
- Add a “control boundaries” note connecting permissions, HITL, and side-effect classes. [Done: `research/control-boundaries.md`]
- Add an “observability schema” note defining canonical trace/span fields for this repository. [Done: `research/observability-schema.md`]
- Add a “memory policy” note defining write gates, provenance, and retirement rules. [Done: `research/memory-policy.md`]
