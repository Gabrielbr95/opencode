# Research Backlog

This file tracks unresolved research questions and candidate future topics.

It is not the place for repository structure rules, solved cleanup items, or the main note inventory.

## Open Questions

### Architecture and workflow
- Which workflow ideas are durable principles versus tool-specific implementations?
- When does a skill system outperform a larger monolithic agent prompt?
- When do multi-agent patterns outperform a strong single-agent plus skills architecture in practice?
- Which delegation contracts are worth standardizing explicitly in this repository?

### Evaluation and observability
- Which evaluation methods are lightweight enough for day-to-day prompt maintenance?
- Which minimal eval stack gives the best signal-to-effort ratio for routine repository changes?
- When should pairwise comparison beat rubric scoring for prompt or workflow iteration?
- Which qualities should never rely on LLM judge alone in this repository?
- What should be traced by default versus only on failure or audit demand?
- Which observability events deserve durable retention versus short-lived diagnostic retention?
- How much raw prompt/output content should ever be stored versus replaced by summaries and IDs?
- What is the smallest stable event vocabulary that still supports audit, debugging, and resumption?

### Memory, context, and retrieval
- What is the minimum useful memory/context architecture for a local-first workflow?
- What should be stored as durable memory versus regenerated or re-retrieved each session?
- Which memory items deserve explicit metadata fields versus lightweight inline provenance?
- When should a memory item be superseded in place versus retired and left as historical record?
- Which memory writes should be allowed automatically versus only proposed for review?
- What is the right repository-specific adoption boundary between direct navigation, attachments, retrieval pipelines, and durable memory?

### Policy and control
- Which permission and tool-governance patterns best fit a local-first corporate environment?
- Which decisions should be enforced as policy-as-code instead of only documented in prompts?
- Which persistence actions deserve the same control intensity as external side effects?

## Candidate Future Topics
- Reflection and self-critique
- Multi-agent collaboration patterns
- Knowledge representation / ontology for prompt repositories
- Provenance models for prompts, memory, and evaluations
- Delegation contracts and agent interoperability
- Approval, pause, resume, and human-gate record models

## Retrieval Follow-Ups
- Repository-specific retrieval architecture for mixed local corpora
- Source metadata minimum for any future local consultation tool
- Refresh and re-index policy that survives long interruptions
- Evidence-return format for retrieval results used in audit or debugging

## Candidate Capability Notes
- `delegation-contracts-and-agent-interoperability.md`
- `approval-pause-resume-and-human-gates.md`

## Research-Tree Maintenance Questions
- Which notes still duplicate a canonical explanation instead of linking to it?
- Which overloaded terms still need a canonical vocabulary entry?
- Which product notes are carrying capability-level explanation that should move upward?
