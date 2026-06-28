---
name: tier-poc
description: >-
  Coding guidelines for the proof-of-concept tier. Use when the builder agent
  is working on a task whose tier is "poc" in tasks.md. Minimal throwaway code
  to answer "can this be done?" and prove feasibility.
---

# Tier: PoC (Proof of Concept)

Build the smallest possible snippet to prove feasibility. This is exploratory, throwaway code.

## Rules

1. Focus exclusively on the riskiest unknown variable (e.g., parsing a complex sensor output, interfacing with a new library).
2. Stub, fake, or hardcode all surrounding systems (databases, network, standard file I/O).
3. Do not spend time optimizing, styling, abstracting, or structuring.
4. Insert clear uppercase warning comments next to hardcoded or stubbed components:
   - `# POC ONLY: Hardcoded database connection`
   - `# POC ONLY: Stubbed API response`
5. Explicitly list the core assumptions or risk factors being verified.

## Conclusion Additions

After the standard conclusion, also report a feasibility verdict: **SUCCESS** / **FAILED** / **RISKY**, key facts proven, and risks discovered during exploration.
