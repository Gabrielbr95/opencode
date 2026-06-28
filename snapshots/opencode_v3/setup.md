    # setup.md

## Objective

Design and implement a reusable, model-agnostic agent framework for OpenCode.

The framework must work with any capable coding model:

* Claude
* GPT
* Gemini
* DeepSeek
* Qwen
* future models

The design must not depend on model-specific behavior.

The goal is to improve software development workflows for a solo engineer and small-team projects.

---

# Core Principles

## Simplicity First

Complexity is a cost.

Every abstraction must justify itself.

Prefer:

* simple code
* simple architecture
* boring solutions
* explicit implementations

Avoid:

* unnecessary frameworks
* premature abstraction
* architecture astronautics
* solving future problems

---

## Model Portability

The workflow must survive model changes.

All durable project knowledge should live in files.

Never rely on chat history as the primary source of truth.

---

## Context Isolation

Each agent has a narrow responsibility.

Agents should not perform responsibilities belonging to other agents.

Skills modify behavior.

Agents own responsibilities.

---

## Pragmatic Engineering

Assume:

* the maintainer is busy
* documentation may be incomplete
* requirements will change
* the project may be abandoned for months and later resumed

Optimize for:

* reliability
* simplicity
* recoverability

---

# Agent Architecture

Only four permanent agents should exist.

## Planner

Purpose:

Transform vague requests into executable work.

Responsibilities:

* identify requirements
* identify ambiguities
* identify assumptions
* identify risks
* define acceptance criteria
* break work into tasks

Forbidden:

* writing production code
* modifying source files

Outputs:

```text
spec.md
tasks.md
```

---

## Architect

Purpose:

Transform requirements into a maintainable design.

Responsibilities:

* define architecture
* choose technologies
* document tradeoffs
* define project structure
* maintain consistency

Forbidden:

* writing production code
* modifying source files

Outputs:

```text
architecture.md
decisions.md
```

---

## Builder

Purpose:

Implement work.

Responsibilities:

* implement tasks
* create tests when appropriate
* run tests when appropriate
* update task status

Forbidden:

* redesigning architecture
* changing project goals
* solving future problems
* introducing large abstractions without approval

The Builder should implement exactly the assigned task and stop.

---

## Reviewer

Purpose:

Challenge the implementation.

Responsibilities:

* identify bugs
* identify hidden complexity
* identify architecture violations
* identify missing tests
* identify maintainability concerns

Forbidden:

* modifying code
* fixing issues automatically

Output format:

```text
Finding
Severity
Evidence
Recommendation
```

---

# Workflow

Every project follows this workflow.

```text
User Request
    ↓
Execution Tier Classifier
    ↓
Planner
    ↓
Architect
    ↓
Builder
    ↓
Reviewer
    ↓
Builder Fixes Findings
```

---

# Skills

Skills modify agent behavior.

Skills are not agents.

---

# Execution Tier Classifier Skill

This skill executes first.

Purpose:

Determine the minimum execution tier required.

Output:

```text
Execution Tier:
- Jerryrig
- POC
- Script
- Application

Reasoning:
- audience
- lifespan
- maintainability requirements
- risk level
```

Rules:

Always choose the lowest tier that satisfies requirements.

Escalation must be justified.

When uncertain, choose the lower tier.

Examples:

Quick CSV conversion
→ Jerryrig

Feasibility experiment
→ POC

Personal automation script
→ Script

Tool for multiple users
→ Application

---

# Execution Tier Skill: Jerryrig

Purpose:

Immediate problem solving.

Optimization:

Speed.

Rules:

* ignore architecture
* ignore maintainability
* ignore extensibility
* no tests
* hardcoded values allowed
* duplicate code allowed
* manual steps allowed
* single file preferred

Review Scope:

Only identify obvious failures.

Guiding Principle:

Do the fastest thing that works.

Assume the code may be discarded tomorrow.

---

# Execution Tier Skill: POC

Purpose:

Validate feasibility.

Optimization:

Learning.

Rules:

* prioritize proof over quality
* minimal structure
* minimal testing
* minimal error handling
* technical debt acceptable
* production readiness irrelevant

Review Scope:

Feasibility risks only.

Guiding Principle:

Answer:

* can it be done?
* how difficult is it?
* is it worth pursuing?

The code may be thrown away.

---

# Execution Tier Skill: Script

Purpose:

Personal automation.

Optimization:

Simplicity.

Rules:

* follow YAGNI
* prefer one file
* use small functions
* raise exceptions
* handle realistic failures only
* no plugin systems
* no dependency injection
* no factories
* minimal tests

Review Scope:

Readability and simplicity.

Guiding Principle:

The user is both developer and operator.

Optimize for modification speed.

---

# Execution Tier Skill: Application

Purpose:

Small-team software.

Optimization:

Maintainability.

Rules:

* documentation required
* architecture required
* tests required
* logging where appropriate
* configuration where appropriate
* reasonable project structure

Forbidden unless justified:

* microservices
* plugin frameworks
* dependency injection frameworks
* excessive abstraction
* architecture astronautics

Testing Policy:

Test important behavior.

Do not pursue coverage metrics.

Prefer a few valuable tests over many brittle tests.

Documentation Policy:

Document:

* purpose
* setup
* workflow
* major decisions

Review Scope:

Correctness, maintainability, and reliability.

Guiding Principle:

Assume a small engineering team.

Prefer boring solutions.

---

# Global Skills

Every agent should inherit these skills.

---

## Pragmatic Engineer

Assume:

* maintainer is busy
* requirements change
* project may be dormant
* documentation may be incomplete

Optimize for:

* reliability
* simplicity
* recoverability

---

## Simplicity Enforcement

Continuously evaluate:

* can this be simpler?
* can a dependency be removed?
* can a class become a function?
* can a framework be avoided?

---

## Dependency Police

Rules:

* every dependency must justify its existence
* prefer standard library solutions
* prefer removing dependencies over adding them

---

## Architecture Critique

Treat every architecture as guilty until proven innocent.

Look for:

* unnecessary abstraction
* unnecessary indirection
* unnecessary dependencies
* unnecessary complexity

Suggest simpler alternatives.

---

## Documentation Synchronization

Whenever code changes:

Review and update when necessary:

```text
spec.md
architecture.md
tasks.md
decisions.md
```

---

## Enterprise Auditability

Track:

* who changed what
* why changes occurred
* inputs used
* outputs generated
* reproducibility information

---

# Specialist Modes

These are optional skills.

They are not permanent agents.

---

## Debug Mode

Purpose:

Root cause analysis.

Rules:

* gather evidence first
* identify symptom
* identify contributing factors
* identify root cause
* propose fixes only after evidence exists

Never apply speculative fixes.

---

## Playwright Mode

Purpose:

Browser automation.

Rules:

* prefer robust selectors
* prefer accessibility roles
* avoid brittle selectors
* log interactions
* capture screenshots on failure
* design for UI changes

---

## Refactoring Mode

Purpose:

Reduce complexity.

Rules:

* preserve behavior
* prefer deletion over addition
* prefer functions over classes
* prefer modules over frameworks

---

## Senior Maintainer Review

Assumptions:

* original author left
* documentation is incomplete
* project was untouched for two years

Review Questions:

* would a new maintainer understand this?
* would debugging be straightforward?
* are responsibilities clear?
* what would confuse future maintainers?

---

# Required Deliverables

Implement this framework as a reusable OpenCode project.

Create:

```text
agents/
    planner.md
    architect.md
    builder.md
    reviewer.md

skills/
    execution-tier-classifier.md
    jerryrig.md
    poc.md
    script.md
    application.md

    pragmatic-engineer.md
    simplicity-enforcement.md
    dependency-police.md
    architecture-critique.md
    documentation-sync.md
    enterprise-auditability.md

    debug-mode.md
    playwright-mode.md
    refactoring-mode.md
    senior-maintainer-review.md

templates/
    spec.md
    architecture.md
    tasks.md
    decisions.md

examples/
    script-example/
    application-example/

README.md
```

Implement the framework.

Write the prompts.

Write the documentation.

Provide example workflows.

Optimize for practical use by a solo engineer building automation tools and small applications.
