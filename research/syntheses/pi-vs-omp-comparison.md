# Pi vs OMP Comparison

This note compares baseline Pi with Oh My Pi (OMP) for the specific evaluation questions that matter in this repository.

Its purpose is practical:
- distinguish upstream Pi from a Pi-family batteries-included fork
- compare their default product posture rather than only raw capability lists
- highlight where the choice affects migration effort, trust review, and local Windows fit

It is not a final recommendation.

---

## Freshness
- Last verified: 2026-08-04
- Derived from:
  - `research/products/pi/*` notes verified 2026-07-28
  - `research/products/omp/*` notes verified 2026-08-04
- Stability: Low
- Recheck triggers:
  - Pi core adds features currently treated as omissions
  - OMP bundled-surface or trust posture changes materially
  - either product changes Windows/runtime assumptions materially

---

## Scope
- product-level comparison only
- evaluation-relevant differences for this repository
- no implementation plan and no procurement-style decision memo

## Canonical Boundary
This is a synthesis note.

Use the product branches for exact details:
- `../products/pi/README.md`
- `../products/omp/README.md`

---

## Short Version
- **Pi** currently looks like a **minimal-core agent platform** that expects important workflow surfaces to be recovered through extensions, skills, themes, and packages.
- **OMP** currently looks like a **Pi-family batteries-included fork/product** that tries to ship more of the useful coding workflow directly.

So the practical tradeoff is roughly:

- **Pi** = more assembly, clearer separation between core and add-ons, likely better for understanding the platform itself
- **OMP** = less assembly, faster time-to-utility, but a broader default surface and a larger trust/review burden

---

## Comparison Table

| Dimension | Pi | OMP | Why it matters here |
|---|---|---|---|
| Product posture | Minimal core | Batteries included | This changes whether the main job is assembling packages or evaluating a bundled default surface. |
| Relationship | Upstream platform/toolkit | Forked Pi-family product | Prevents collapsing OMP into either "just Pi" or "just one Pi package." |
| Built-in capability breadth | Narrower; several important surfaces explicitly omitted from core | Broader; many workflow capabilities marketed as bundled | Directly affects time-to-utility and the size of the default local side-effect surface. |
| Extension stance | Core part of the model; omissions often intentionally recovered through packages | Still open/extensible, but less dependent on extension assembly for first usefulness | Matters for maintenance burden and how much composition work is needed up front. |
| Permission/trust research posture | Current notes show no built-in sandbox and no core runtime permission popup system | Current notes suggest a powerful local product surface, but formal trust/permission behavior is still less clear in this repository | Trust review is a bigger blocker for OMP adoption than raw feature discovery. |
| Migration path from current harness | Likely requires picking and validating several packages to recover missing surfaces | May reduce migration work if bundled capabilities and import claims hold up | The real question is not only capability coverage but operational simplification. |
| Windows relevance | Explicit bash requirement already documented | Windows support is claimed, but practical fit of the broader feature set still needs validation | Corporate Windows fit is a hard constraint here. |
| Research value | Strong for understanding the platform and ecosystem structure | Strong for understanding an opinionated Pi-derived default workflow | Both are useful, but for different reasons. |

---

## Highest-Value Distinctions

### 1. Platform research vs product evaluation
Pi is useful when the question is:
- what does the upstream architecture provide?
- what is core versus extension?
- what packages are needed to recreate a missing harness surface?

OMP is useful when the question is:
- does a Pi-family product already bundle the missing pieces?
- can migration effort be reduced by starting from a richer default?

These are different evaluation paths.

### 2. Assembly cost vs review cost
Pi likely demands more assembly work:
- choose packages
- validate package maturity
- compose the desired surface intentionally

OMP may reduce that assembly cost, but it shifts effort into review:
- which built-ins are enabled?
- what are the trust implications?
- how safe and practical is the bundled surface on the target machine?

### 3. Minimal-core clarity vs batteries-included convenience
Pi's main conceptual strength in the current research is clarity:
- the omissions are explicit
- the ecosystem role is explicit
- the boundaries between core and add-on are easier to reason about

OMP's main conceptual strength is convenience:
- it appears closer to an immediately useful daily-driver surface
- it may reduce how much package assembly is needed before real use

### 4. Trust conclusions do not transfer automatically
It would be a mistake to assume:
- Pi trust findings fully describe OMP
or
- OMP bundled convenience automatically makes it the better local choice

OMP diverges enough from Pi that it needs separate trust review.

---

## Candidate Evaluation Questions

If the goal is **platform understanding**, Pi is probably the cleaner primary subject.

If the goal is **replacement-harness fit**, the next questions are more OMP-shaped:
- Does OMP's bundled surface cover the missing workflow pieces you care about?
- Can its powerful features be constrained acceptably on a corporate Windows laptop?
- Are its import/reuse claims actually helpful for the current local prompt/config assets?

If the goal is **lowest-maintenance practical use**, the winner may depend less on feature count and more on:
- default safety posture
- Windows reliability
- how much of the workflow can stay boring and local

---

## Current Working Conclusion
At the current evidence level:

- **Pi** remains the better branch for understanding the upstream minimal-core architecture and ecosystem replacement routes.
- **OMP** deserves separate tracking because it may be the more realistic candidate if the real objective is a more complete ready-to-use Pi-family harness.

So for now, the right framing is not "Pi or OMP?" as a single immediate choice.

It is:
- use **Pi research** to understand the platform and missing-core architecture
- use **OMP research** to test whether a batteries-included Pi-family fork changes the practical migration equation

---

## Relationships to Other Notes
- `../products/pi/foundations.md`
- `../products/pi/security-and-trust.md`
- `../products/pi/extension-ecosystem-and-core-gaps.md`
- `../products/omp/foundations.md`
- `../products/omp/security-and-trust.md`
- `../syntheses/opencode-to-pi-capability-matrix.md`

---

## Open Questions
- Which OMP built-ins most directly replace the current harness surfaces you care about?
- Does OMP have a documented permission/approval model strong enough for this environment?
- Is Pi plus carefully chosen packages actually simpler to reason about than OMP's richer default surface?
- Which path produces the smallest boring setup that you can still maintain after long interruptions?
