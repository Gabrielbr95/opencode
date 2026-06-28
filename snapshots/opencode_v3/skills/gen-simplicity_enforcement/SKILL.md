---
name: gen-simplicity_enforcement
description: Continuously challenge complexity. Every abstraction must justify its existence.
---

# gen-simplicity_enforcement

## When to load

Load when reviewing a plan or implementation for over-engineering, or when an agent has proposed a solution that feels heavier than the problem warrants.

## Core Question

At every decision point, ask: **is this the simplest thing that correctly solves the problem?**

## Evaluation Checklist

Run through this for every significant element of the design or code:

- [ ] Can this be a function instead of a class?
- [ ] Can this be a module instead of a package?
- [ ] Can a stdlib solution replace this dependency?
- [ ] Is this abstraction used in more than one place? (If not, it probably shouldn't exist yet.)
- [ ] Does this config option solve a real problem that has occurred, or a hypothetical one?
- [ ] Is this indirection making the code easier or harder to follow?
- [ ] Would a new reader know why this exists without being told?

## Red Flags

- Base classes with only one subclass
- Factories that create only one type of object
- Config systems for values that never change
- Wrappers around single function calls
- "Framework" where a loop would do
- Abstraction that exists "for future extensibility"
- More than 3 layers of indirection for a single operation

## How to Report

Flag each violation with:
- What it is
- Why it's unnecessary
- The simpler alternative
