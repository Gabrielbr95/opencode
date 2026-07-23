# Specification

## Objective
Build a local, incremental research knowledge base for improving the AI workflow, starting with a small batch of foundational topics researched from web sources and documented with citations.

## Core Requirements
- Create a durable `research/` directory structure that can grow incrementally over time.
- Research the approved starting topics: agent architectures, skill systems, context engineering, planning systems, and evaluation/prompt testing.
- Expand the research base over time by prioritizing the highest-value backlog topics and adding newly discovered adjacent topics when they appear repeatedly across sources.
- Revisit already researched topics to deepen understanding, clarify misconceptions, and sharpen boundaries between related concepts instead of only adding breadth.
- Add synthesis documents when the topic set is mature enough to justify them, starting with a shared vocabulary to reduce terminology drift.
- Add higher-level synthesis notes that connect multiple researched topics into practical design guidance, starting with control boundaries for actions, approvals, and durable writes.
- Distill implementation-agnostic design principles from the researched topics so the repository accumulates portable rules, not just topic summaries.
- Write one structured Markdown note per topic with clear sections for summary, problem, patterns, tradeoffs, practical implications, open questions, and references.
- Cite sources in every research note so findings can be traced and revisited later.
- Keep the structure simple, local-first, and easy to extend without a major reorganization.

## Out of Scope (Crucial)
- No implementation changes to agents, skills, prompts, or config files yet.
- No attempt to exhaustively cover every topic listed in `ai-workflow-improvement.md` in one pass.
- No full knowledge management system, database, or automation pipeline for research capture.

## User Interaction
The user asks for research on selected topics. The agent creates and maintains local Markdown files under `research/`, performs web research, writes structured notes with citations, and can extend the repository in later sessions by adding new topics or refining existing notes.
