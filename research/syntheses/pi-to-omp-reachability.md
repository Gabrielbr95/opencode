# Pi to OMP Reachability

This note answers a practical question for this repository:

Can a user start from baseline Pi, install extensions/packages incrementally, and effectively reach OMP?

The answer is not binary.

---

## Freshness
- Last verified: 2026-08-04
- Derived from:
  - `research/products/pi/*` notes verified 2026-07-28
  - `research/products/omp/*` notes verified 2026-08-04
  - `research/syntheses/omp-reachability-matrix.md`
- Stability: Low
- Recheck triggers:
  - Pi package ecosystem gains stronger matches for current OMP-specific areas
  - OMP changes its built-in/runtime surface materially
  - Windows or trust findings materially change the practical recommendation

---

## Scope
- practical reachability from Pi to OMP-like workflow behavior
- where extension stacking works
- where extension stacking stops being honest parity and becomes custom engineering

## Canonical Boundary
This note is a synthesis and practical judgment call.

It is not:
- a full migration plan
- proof that every package combination will work smoothly
- a recommendation to adopt either product today

---

## Short Answer
- **Yes, partly:** a user can install Pi extensions/packages and get meaningfully closer to OMP.
- **No, not fully:** current evidence does not support a clean off-the-shelf package path to full OMP parity.
- **The break point:** once you want OMP's deeper integrated runtime/tooling behavior, you appear to move from package assembly into custom engineering or direct OMP adoption.

---

## What Pi Can Likely Reach Through Package Assembly
Using currently reviewed official packages, Pi can get quite far toward OMP-like workflow coverage in areas such as:
- subagents
- plan mode
- web research/fetching
- browser automation
- memory
- todo tracking
- permission gates
- some LSP support

This is enough to say that OMP is not magic. A meaningful fraction of its workflow value is conceptually reachable in the Pi ecosystem.

---

## Where Package Assembly Starts to Break Down
The reachability story gets weaker in three recurring situations.

### 1. Integration-sensitive capabilities
Some capabilities are not just present/absent. Their usefulness depends on deep integration.

Examples:
- richer LSP behavior
- eval/runtime bridging
- debugger integration
- review orchestration semantics

Pi may be able to approximate these, but current evidence does not show them as simple "install this package" outcomes.

### 2. Product-owned abstractions
OMP appears to own some abstractions that are more product-shaped than extension-shaped.

Examples:
- virtual path schemes
- AST preview/accept flows
- cross-ecosystem config/rule inheritance
- live collaboration relay
- desktop/computer tool

These look less like loose ecosystem add-ons and more like integrated product surfaces.

### 3. Architectural/runtime differences
OMP's native/runtime layer matters.

If a capability depends on:
- first-party native code
- a unified runtime/tooling engine
- tightly coordinated UI/runtime behavior

then package stacking on top of baseline Pi becomes a less convincing parity story.

---

## Practical Levels of Reachability

### Level 1: OMP-like in broad workflow shape
This is the strongest case for Pi plus packages.

You can likely achieve:
- planning lane
- delegation lane
- research lane
- memory lane
- browser lane
- approval lane

For many practical workflows, this may be "good enough" even without full OMP parity.

### Level 2: OMP-like in feature checklist terms
This is mixed.

You can check many boxes, but some boxes will only match loosely.

This is where words like "similar," "adjacent," and "partial parity" become more honest than "equivalent."

### Level 3: OMP-like as a coherent integrated product
This is the weakest case for Pi-plus-packages.

The current evidence does not support the idea that baseline Pi can simply be stacked into the same integrated product character as OMP without substantial extra engineering.

---

## When Pi-plus-Packages Is the Right Path
Pi-first exploration makes more sense when:
- you want to understand the upstream platform clearly
- you prefer explicit assembly over adopting a larger pre-integrated fork
- you only need a subset of OMP's surface
- you want tighter control over what gets installed
- you are willing to trade convenience for modularity and transparency

---

## When Direct OMP Evaluation Makes More Sense
OMP-first evaluation makes more sense when:
- the real question is replacement-harness fit, not platform study
- you care about integrated behavior more than compositional purity
- the interesting part is exactly the built-in/runtime-heavy layer Pi packages do not clearly reproduce
- you want to test whether the batteries-included approach actually reduces work enough to justify its broader trust/review burden

---

## Practical Conclusion for This Repository
Given this repository's environment and working style, the most honest current conclusion is:

- **Study Pi** to understand the platform and the reachable extension surface.
- **Evaluate OMP directly** when the question becomes practical harness replacement, because some of the most interesting parts of OMP are precisely the parts that do not currently look package-equivalent.

So the right move is usually not:
- build Pi all the way until it becomes OMP

It is more like:
- use Pi research to understand the floor
- use OMP evaluation to test the ceiling you actually care about

---

## Relationships to Other Notes
- `../products/pi/foundations.md`
- `../products/pi/extension-ecosystem-and-core-gaps.md`
- `../products/omp/foundations.md`
- `../products/omp/architecture-and-divergence.md`
- `../products/omp/security-and-trust.md`
- `../syntheses/omp-reachability-matrix.md`
- `../syntheses/pi-vs-omp-comparison.md`

---

## Open Questions
- Which small subset of OMP capabilities would actually matter enough to test locally first?
- Which OMP-specific integrated surfaces are deal-makers versus just interesting extras?
- Would a carefully chosen Pi package stack already meet the real workflow need without the complexity of OMP?
