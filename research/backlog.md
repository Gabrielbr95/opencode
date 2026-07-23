# Research Backlog

## Open Questions
- Which workflow ideas are durable principles versus tool-specific implementations?
- Which evaluation methods are lightweight enough for day-to-day prompt maintenance?
- When does a skill system outperform a larger monolithic agent prompt?
- What is the minimum useful memory/context architecture for a local-first workflow?
- When do multi-agent patterns outperform a strong single-agent + skills architecture in practice?
- What should be stored as durable memory versus regenerated or re-retrieved each session?
- Which permission and tool-governance patterns best fit a local-first corporate environment?
- What should be traced by default versus only on failure or audit demand?
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
- Create a comparison matrix of workflow patterns: chain, route, parallelize, orchestrator-worker, evaluator-optimizer, ReAct.
- Create a comparison matrix of evaluation methods: exact match, rubric, pairwise, LLM judge, human review.
- Distill a repository-specific vocabulary: workflow, agent, skill, project context, MCP, memory, evaluation. [Done: `research/vocabulary.md`]
- Add a “principles only” note that extracts durable rules from the first five topics. [Done: `research/principles-only.md`]
- Add a “control boundaries” note connecting permissions, HITL, and side-effect classes. [Done: `research/control-boundaries.md`]
- Add an “observability schema” note defining canonical trace/span fields for this repository.
- Add a “memory policy” note defining write gates, provenance, and retirement rules.
