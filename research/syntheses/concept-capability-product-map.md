# Concept -> Capability -> Product Map

This document maps canonical ownership across the research tree.

Its purpose is structural:
- where each kind of idea belongs
- which note currently owns each repeated topic cluster
- where nearby notes should defer instead of re-explaining

It is not meant to be a second home for domain conclusions already captured elsewhere.

---

## The Four-Layer Model

The repository uses four research layers:

- **concepts** — durable ideas and boundaries
- **capabilities** — reusable cross-tool mechanisms
- **products** — current tool-specific behavior
- **syntheses** — glossary, comparisons, maps, and distilled repository-level views

When a note starts drifting, the most useful diagnostic question is usually:

> Is this note explaining a concept, a mechanism, a product behavior, or a repository synthesis?

---

## Placement Questions

Use these in order.

1. **Is this a durable idea or boundary?**
   - canonical home: `concepts/`
2. **Is this a reusable mechanism several tools could implement differently?**
   - canonical home: `capabilities/`
3. **Is this an exact current behavior or configuration surface of one tool?**
   - canonical home: `products/`
4. **Is this a glossary, comparison, ownership map, or repository-level conclusion?**
   - canonical home: `syntheses/`

---

## Canonical Ownership by Topic Cluster

### Instruction and prompt structure
- **Concept owners**
  - `../concepts/instruction-layering.md`
  - `../concepts/prompt-modularity-repository-architecture.md`
- **Product owners**
  - `../products/opencode/config-and-instruction-loading.md`
  - `../products/opencode/instruction-layering.md`
  - `../products/opencode/system-prompt-control.md`

Primary rule:
- durable layering theory lives in the concept notes
- opencode loader mechanics live in `config-and-instruction-loading.md`
- advanced prompt-surgery evidence lives in `system-prompt-control.md`

### Control and safety boundaries
- **Concept owners**
  - `../concepts/tool-use-policy-and-permission-systems.md`
  - `../concepts/human-in-the-loop-control-points.md`
- **Capability owner**
  - `../capabilities/policy-engines.md`
- **Synthesis owners**
  - `../syntheses/vocabulary.md`
  - `../syntheses/control-boundaries.md`
- **Product owner**
  - `../products/opencode/permissions-and-agent-safety.md`

Primary rule:
- principles live in the concept notes
- explicit runtime decision/enforcement mechanics live in `policy-engines.md`
- control-stack terminology and boundary summaries live in the syntheses

### Memory, context, attachment, and retrieval
- **Concept owners**
  - `../concepts/context-engineering.md`
  - `../concepts/memory-systems.md`
- **Capability owners**
  - `../capabilities/context-attachments.md`
  - `../capabilities/retrieval-pipelines.md`
  - `../capabilities/sessions.md`
- **Synthesis owner**
  - `../syntheses/memory-policy.md`
- **Product owners**
  - `../products/opencode/references-and-external-context-basics.md`
  - `../products/opencode/memory-and-retrieval.md`
  - `../products/opencode/session-control-and-recovery.md`

Primary rule:
- theory of memory and context lives in the concept notes
- explicit binding of external context lives in `context-attachments.md`
- indexed corpus consultation lives in `retrieval-pipelines.md`
- repository write/promotion rules live in `memory-policy.md`

### Runs, sessions, observability, and evaluation
- **Concept owners**
  - `../concepts/durable-execution.md`
  - `../concepts/observability-traceability.md`
  - `../concepts/evaluation-prompt-testing.md`
- **Capability owners**
  - `../capabilities/sessions.md`
  - `../capabilities/eval-harnesses.md`
- **Synthesis owners**
  - `../syntheses/observability-schema.md`
  - `../syntheses/evaluation-method-comparison.md`

Primary rule:
- run/session/execution theory lives in the concept notes
- session-continuity mechanics live in `sessions.md`
- canonical event/trace fields live in `observability-schema.md`
- eval-method comparison lives in `evaluation-method-comparison.md`

### Workflow and planning patterns
- **Concept owners**
  - `../concepts/agent-architectures.md`
  - `../concepts/planning-systems.md`
  - `../concepts/skill-systems.md`
- **Synthesis owners**
  - `../syntheses/workflow-pattern-comparison.md`
  - `../syntheses/principles-only.md`

Primary rule:
- durable theory lives in the concept notes
- side-by-side pattern selection lives in `workflow-pattern-comparison.md`
- compressed durable rules live in `principles-only.md`

### Retrieval product stack
- **Capability owner**
  - `../capabilities/retrieval-pipelines.md`
- **Product owners**
  - `../products/sqlite-fts5.md`
  - `../products/docling.md`
  - `../products/qdrant.md`
  - `../products/lancedb.md`
  - `../products/chroma.md`
- **Synthesis owner**
  - `../syntheses/local-first-retrieval-tool-comparison.md`

Primary rule:
- general retrieval mechanism lives in the capability note
- each tool note records product facts about one tool
- cross-tool role comparison lives in the synthesis note

---

## Notes That Act as Canonical Glue

- `../syntheses/vocabulary.md` — canonical glossary
- `../syntheses/control-boundaries.md` — canonical control-stack summary
- `../syntheses/memory-policy.md` — canonical repository memory policy
- `../syntheses/observability-schema.md` — canonical trace/event vocabulary

These notes should be referenced when neighboring notes need the distinction, instead of rewriting the same boundary in full.

---

## Current Structural Gaps

- run/session/checkpoint terminology still depends heavily on `vocabulary.md`
- some opencode branch notes still carry roadmap or guidance text better kept in branch README or dedicated map notes
- some concept and capability notes still use older “Practical Applications” phrasing that reads more prescriptive than descriptive

---

## Maintenance Rule

When a new duplication hotspot appears, fix the canonical owner first.

Then trim neighboring notes so they:
- keep only local detail
- point back to the canonical note
- stop behaving like a second source of truth
