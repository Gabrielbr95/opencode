# AI Workflow Research

This directory stores structured research for improving the AI workflow over time.

Its job is to preserve durable understanding, reduce re-learning after long gaps, and keep product-specific findings separated from slower-moving ideas.

## Repository Role

The research tree is a knowledge base, not a task list and not a chat transcript.

It is meant to answer three kinds of questions:
- what the durable ideas are
- what reusable mechanisms sit between those ideas and products
- what this repository currently knows about specific tools

## The Four Research Layers

### 1. `concepts/`
Canonical home for slower-moving ideas, boundaries, and design principles.

Questions this layer answers:
- what is this idea?
- what problem does it solve?
- what distinctions and tradeoffs stay useful across tool churn?

Examples:
- agent architectures
- planning systems
- context engineering
- memory systems
- instruction layering

### 2. `capabilities/`
Canonical home for reusable cross-tool subsystems or facilities.

Questions this layer answers:
- what mechanism does this provide?
- what is the minimal durable model?
- what parts are portable across tools, and what parts drift faster?

Examples:
- tool calling
- policy engines
- sessions
- context attachments
- retrieval pipelines

### 3. `products/`
Canonical home for product-specific snapshots.

Questions this layer answers:
- how does one tool implement a concept or capability today?
- what exact behavior or config surface matters here?
- what looks volatile and likely to need rechecking?

Examples:
- opencode
- SQLite FTS5
- Docling
- Qdrant
- LanceDB
- Chroma

### 4. `syntheses/`
Canonical home for cross-note vocabulary, comparison docs, repository-level maps, and distilled conclusions.

Questions this layer answers:
- how should the repository classify this body of knowledge?
- which distinctions should remain stable across future notes?
- what comparison or glossary reduces future re-learning?

Examples:
- vocabulary
- control boundaries
- workflow-pattern comparison
- evaluation-method comparison
- concept-capability-product map

## Entry Points and Their Jobs

- `README.md` — repository architecture, placement rules, and note-writing conventions
- `index.md` — inventory and reading paths
- `backlog.md` — unresolved questions and candidate future topics
- `syntheses/vocabulary.md` — canonical glossary for overloaded operating terms

These files should not duplicate each other.

## Canonical Ownership Rule

Each idea should have one primary home.

Use this test before writing or expanding a note:

1. Is this mainly a durable idea or boundary?
   - put it in `concepts/`
2. Is this mainly a reusable mechanism several tools could implement?
   - put it in `capabilities/`
3. Is this mainly current behavior of one tool?
   - put it in `products/`
4. Is this mainly a glossary, comparison, map, or repository-level conclusion?
   - put it in `syntheses/`

If a note needs several paragraphs to re-explain another note's core idea, that is a sign the canonical home is wrong or the reference should be tighter.

## Referencing Rule

When an idea already has a canonical note:
- summarize it in one or two sentences at most
- link to the canonical note
- only add local detail that is genuinely specific to the current note's layer

Do not let the same explanation become authoritative in several places.

## Terminology Rule

Use `syntheses/vocabulary.md` as the canonical source for overloaded terms such as:
- workflow
- agent
- skill
- session
- run
- memory
- retrieval
- attachment
- approval
- permission
- durable truth

If a source uses a term differently, record that source-local meaning explicitly instead of silently redefining the repository meaning.

## Note Shape and Tone

Research notes are descriptive first.

They should prefer:
- definitions
- boundaries
- tradeoffs
- relationships
- implications for this repository
- open questions

They should avoid turning into:
- hidden task lists
- recommendation dumps
- implementation instructions unless the note is explicitly product-specific and evidence-backed

Repository-specific implications are useful, but they should still read as structured knowledge rather than as marching orders.

## Minimal Conventions

- Keep one topic per note.
- Put scope boundaries near the top when confusion is likely.
- Use explicit relationship links to canonical neighboring notes.
- Keep product notes dated with freshness metadata.
- Prefer shorter, more focused notes over omnibus essays.
- Update `index.md` when a new durable note is added.
- Update `backlog.md` when a gap or unresolved question becomes visible.

## Subtree Guides

- `concepts/README.md`
- `capabilities/README.md`
- `products/README.md`
- `syntheses/README.md`
- `templates/README.md`
