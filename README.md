# opencode


# Agent System Refactoring

You are refactoring the implementation of an AI agent system.

The architecture is already defined by two documents:

* `workflow.md`
* `my-context.md`

Treat both as **authoritative specifications**.

Do **not** modify them.

Everything else must conform to them.

The goal is to redesign the agent system around these specifications.

---

# Files that may be modified

You may modify only:

* `agents.md`
* everything inside `agents/`
* everything inside `skills/`

No other files should be changed.

---

# Context

The current implementation evolved organically.

It contains:

* duplicated concepts
* overlapping responsibilities
* historical artifacts
* inconsistent terminology
* skills embedded inside agents
* agent responsibilities embedded inside skills
* unclear ownership

Treat the existing files as a knowledge base, not as something to preserve.

Preserve intent, not structure.

---

# Architecture

The architecture is defined by `workflow.md`.

In particular:

* Workflow defines **why** the system works.
* Agents define **who** performs work.
* Skills define **how** work is performed.

Responsibilities must remain clearly separated.

---

# Core architectural principle

Every persistent concept must have exactly one canonical owner.

Examples:

Workflow owns:

* philosophy
* governance
* workflow
* principles

Agents own:

* responsibilities
* reasoning focus
* decision boundaries

Skills own:

* reusable techniques
* procedures
* checklists
* implementation methods

If information belongs somewhere else, move it.

Do not duplicate it.

---

# Refactoring principles

* Preserve intent, not wording.
* Prefer explicit ownership over convenience.
* Prefer reusable skills over duplicated instructions.
* Keep agents focused on decision-making rather than procedures.
* Keep skills independent whenever practical.
* Keep prompts concise.
* Optimize for value rather than maximum capability.
* Reduce unnecessary context and token usage.
* Favor maintainability over cleverness.

---

# Allowed changes

You may:

* rewrite prompts
* rename agents
* rewrite skills
* split skills
* merge skills
* move content between agents and skills
* normalize terminology
* redesign the folder organization

Assume the current implementation is provisional.

---

# Deliverables

## Phase 1

Analyze the current implementation.

Produce an ownership matrix showing where every major concept belongs.

Do not rewrite anything yet.

---

## Phase 2

Identify architectural problems.

For each one explain:

* current location
* canonical owner
* proposed change
* reasoning

---

## Phase 3

Design the new agent and skill architecture.

Explain:

* each agent
* each skill
* why each exists
* how they interact

---

## Phase 4

Rewrite:

* `agents.md`
* every affected file in `agents/`
* every affected file in `skills/`

The result should feel as though it had been designed from the beginning around the principles in `workflow.md` and the constraints in `my-context.md`.

Do not optimize for minimal edits.

Optimize for long-term maintainability, clear ownership, and efficient LLM context usage.
