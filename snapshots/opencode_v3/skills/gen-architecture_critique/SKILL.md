---
name: gen-architecture_critique
description: Treat every architecture as guilty until proven innocent. Find unnecessary abstraction, indirection, and complexity.
---

# gen-architecture_critique

## When to load

Load when reviewing a design, architecture document, or plan before implementation begins. Also useful post-implementation when reviewing structural decisions.

## Stance

Every architectural decision is guilty of unnecessary complexity until proven otherwise. The burden of proof is on the architecture, not the critic.

## What to Look For

**Unnecessary abstraction**
- Interfaces with one implementation
- Abstract base classes used for a single concrete type
- Generic solutions to non-generic problems

**Unnecessary indirection**
- Data that passes through more layers than needed
- Functions whose only job is to call another function
- Modules that exist only to re-export other modules

**Unnecessary dependencies**
- Services or systems pulled in for minor utility
- Frameworks that own too much of the call stack
- Dependencies between components that have no business knowing about each other

**Unnecessary complexity**
- Config systems where hardcoded defaults would work for 90% of cases
- Async where sync would be fine
- Distributed where monolithic would be fine
- Pluggable where fixed would be fine

## Output Format

For each finding:
```
Finding: <what was found>
Evidence: <where in the design/code>
Why it's a problem: <specific cost — maintainability, debugging, onboarding>
Simpler alternative: <concrete suggestion>
```

## Guiding Principle

Every layer of abstraction has a maintenance cost. An abstraction that saves 10 lines of code but requires a new maintainer to read 3 files to understand one operation is not a win.
