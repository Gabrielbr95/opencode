# Research Index

This file is the navigation map for the research tree.

For placement rules and note-writing conventions, see `README.md`.
For unresolved questions and future topics, see `backlog.md`.

## Entry Points

- `README.md` — how the research tree is organized
- `backlog.md` — open questions and candidate future topics
- `syntheses/vocabulary.md` — canonical glossary
- `syntheses/concept-capability-product-map.md` — map of canonical note ownership across the tree

## Concepts (`concepts/`)

| Concept | File | Notes |
|---|---|---|
| Agent architectures | `concepts/agent-architectures.md` | Ownership, coordination, autonomy, and architecture boundaries for agent systems. |
| Context engineering | `concepts/context-engineering.md` | Information shaping, salience, retrieval use, and context boundaries. |
| Durable execution | `concepts/durable-execution.md` | Run identity, replay, retries, checkpoints, pause/resume, and side-effect isolation. |
| Evaluation / prompt testing | `concepts/evaluation-prompt-testing.md` | Evidence-driven prompt and workflow evaluation. |
| Human-in-the-loop control points | `concepts/human-in-the-loop-control-points.md` | Review, approval, override, and escalation boundaries. |
| Instruction layering | `concepts/instruction-layering.md` | Layered ambient instruction systems as a durable idea. |
| Memory systems | `concepts/memory-systems.md` | Tiered memory, promotion, governance, and recall. |
| Observability / traceability | `concepts/observability-traceability.md` | Traces, spans, provenance, and auditability. |
| Planning systems | `concepts/planning-systems.md` | Decomposition, replanning, and stop-condition design. |
| Prompt modularity / repository architecture | `concepts/prompt-modularity-repository-architecture.md` | Prompt-repository structure, modularity, and precedence. |
| Skill systems | `concepts/skill-systems.md` | Reusable procedural capability packaging. |
| Tool-use policy and permission systems | `concepts/tool-use-policy-and-permission-systems.md` | Durable control and least-privilege principles for tool use. |

## Capabilities (`capabilities/`)

| Capability | File | Notes |
|---|---|---|
| Context attachments | `capabilities/context-attachments.md` | Explicit binding of external context surfaces. |
| Eval harnesses | `capabilities/eval-harnesses.md` | Cases, runs, graders, metrics, and release/review gates. |
| MCP | `capabilities/mcp.md` | Protocol-mediated capability expansion through tools, resources, and prompts. |
| Model routing | `capabilities/model-routing.md` | Backend routing, model catalogs, and trust/network boundaries. |
| Policy engines | `capabilities/policy-engines.md` | Structured runtime decision and enforcement planes. |
| Retrieval pipelines | `capabilities/retrieval-pipelines.md` | Ingestion, indexing, freshness, and evidence-return retrieval systems. |
| Sessions | `capabilities/sessions.md` | Interrupt/resume, compaction, and bounded rollback. |
| Tool calling | `capabilities/tool-calling.md` | Structured action contracts, call/result correlation, and invocation lifecycle. |

## Products (`products/`)

| Product / Branch | File | Notes |
|---|---|---|
| Product branch guide | `products/README.md` | Role and freshness expectations for product notes. |
| Joplin | `products/joplin.md` | Note-centric second-brain candidate with strong API/MCP retrieval surfaces. |
| Obsidian | `products/obsidian.md` | Markdown-first local knowledge product with strong file transparency and weaker official automation surface. |
| AnythingLLM | `products/anythingllm.md` | Retrieval-first local knowledge workspace with API and MCP relevance. |
| Open WebUI | `products/open-webui.md` | Knowledge-base-centric retrieval platform with strong scoped corpus model and broader API surface. |
| Khoj | `products/khoj.md` | Second-brain/search product with strong semantic retrieval fit and weaker Windows setup fit. |
| SQLite FTS5 | `products/sqlite-fts5.md` | Embedded lexical plus structured retrieval. |
| Docling | `products/docling.md` | Mixed-document parsing and chunking for ingestion pipelines. |
| Qdrant | `products/qdrant.md` | Local semantic/vector retrieval with payload filtering. |
| LanceDB | `products/lancedb.md` | Embedded full-text, vector, and hybrid retrieval engine. |
| Chroma | `products/chroma.md` | Local persistent vector retrieval with filtering support. |
| opencode branch | `products/opencode/README.md` | Navigation for product-specific opencode notes. |
| Pi branch | `products/pi/README.md` | Navigation for product-specific Pi notes. |

### opencode product notes
- `products/opencode/foundations.md`
- `products/opencode/config-and-instruction-loading.md`
- `products/opencode/instruction-layering.md`
- `products/opencode/agents-permissions-and-skills-basics.md`
- `products/opencode/references-and-external-context-basics.md`
- `products/opencode/local-first-models-and-providers.md`
- `products/opencode/permissions-and-agent-safety.md`
- `products/opencode/memory-and-retrieval.md`
- `products/opencode/session-control-and-recovery.md`
- `products/opencode/mcp-and-tooling.md`
- `products/opencode/config-surface-and-volatility-map.md`
- `products/opencode/advanced-features-map.md`
- `products/opencode/system-prompt-control.md`

### Pi product notes
- `products/pi/foundations.md`
- `products/pi/config-and-instruction-loading.md`
- `products/pi/security-and-trust.md`
- `products/pi/sessions-and-compaction.md`
- `products/pi/providers-and-programmatic-surfaces.md`
- `products/pi/extension-ecosystem-and-core-gaps.md`

### OMP product notes
- `products/omp/foundations.md`
- `products/omp/config-and-loading.md`
- `products/omp/security-and-trust.md`
- `products/omp/architecture-and-divergence.md`

## Syntheses (`syntheses/`)

| Synthesis | File | Notes |
|---|---|---|
| Concept-capability-product map | `syntheses/concept-capability-product-map.md` | Canonical ownership map for the research tree. |
| Control boundaries | `syntheses/control-boundaries.md` | Layered control model across policy, permission, guardrails, approvals, and durable writes. |
| Evaluation method comparison | `syntheses/evaluation-method-comparison.md` | Comparison of exact match, rubric, pairwise, LLM judge, and human review. |
| Local-first retrieval tool comparison | `syntheses/local-first-retrieval-tool-comparison.md` | Role comparison of SQLite FTS5, Docling, Qdrant, LanceDB, and Chroma. |
| Memory policy | `syntheses/memory-policy.md` | Repository policy for memory layers, provenance, and durable-write gates. |
| Observability schema | `syntheses/observability-schema.md` | Canonical event and trace fields for workflow observability. |
| opencode to Pi capability matrix | `syntheses/opencode-to-pi-capability-matrix.md` | Fact-only cross-product matrix of core, package, and current gap surfaces. |
| Principles only | `syntheses/principles-only.md` | Distilled durable principles across the research tree. |
| Second-brain and retrieval product comparison | `syntheses/second-brain-and-retrieval-product-comparison.md` | Decision aid for off-the-shelf local-first products under this repository's constraints. |
| Task, run, and artifact records | `syntheses/task-run-artifact-records.md` | Shared record model linking work definitions, runs, artifacts, events, and lineage. |
| Vocabulary | `syntheses/vocabulary.md` | Canonical glossary for repository terms. |
| Workflow pattern comparison | `syntheses/workflow-pattern-comparison.md` | Comparison of chain, route, parallelize, evaluator-optimizer, ReAct, and orchestrator-worker. |

## Suggested Reading Paths

### Foundations path
1. `syntheses/vocabulary.md`
2. `concepts/agent-architectures.md`
3. `concepts/planning-systems.md`
4. `concepts/context-engineering.md`
5. `concepts/memory-systems.md`

### Control and reliability path
1. `concepts/tool-use-policy-and-permission-systems.md`
2. `concepts/human-in-the-loop-control-points.md`
3. `capabilities/policy-engines.md`
4. `concepts/durable-execution.md`
5. `syntheses/control-boundaries.md`
6. `syntheses/observability-schema.md`

### Retrieval and memory path
1. `concepts/context-engineering.md`
2. `concepts/memory-systems.md`
3. `capabilities/context-attachments.md`
4. `capabilities/retrieval-pipelines.md`
5. `products/opencode/memory-and-retrieval.md`
6. `syntheses/local-first-retrieval-tool-comparison.md`

### opencode product path
1. `products/opencode/README.md`
2. `products/opencode/foundations.md`
3. `products/opencode/config-and-instruction-loading.md`
4. `products/opencode/agents-permissions-and-skills-basics.md`
5. `products/opencode/references-and-external-context-basics.md`
