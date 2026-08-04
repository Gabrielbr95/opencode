# OMP Architecture and Divergence

## Freshness
- Last verified: 2026-08-04
- Verified against: OMP GitHub repository README, OMP `docs/porting-from-pi-mono.md`, OMP `docs/native-crates.md`, OMP repository layout, upstream Pi repository/README
- Product version: current docs snapshot; exact installed local version not verified
- Stability: Low
- Recheck triggers:
  - OMP porting or native-crates docs change materially
  - monorepo structure changes materially
  - OMP built-in tool/runtime claims change materially
  - upstream Pi architecture changes in ways that shrink or expand divergence

## Scope
- whether OMP is merely a bundle versus a real forked product
- concrete signs of author-written code and architectural divergence
- what that means for reachability from baseline Pi plus packages

## Canonical Boundary
This note owns the product-specific answer to:
- "is OMP just Pi plus extensions?"

It is not the main home for:
- detailed trust review
- feature-by-feature reachability matrix work
- a final migration recommendation

## Why This Matters Here
- If OMP were just a curated bundle, then studying Pi package assembly would likely be enough.
- If OMP contains substantial first-party engineering and runtime divergence, then some of its value cannot be understood only as package selection.

## Current Findings
- OMP is explicitly a fork of Pi, but it is not best described as merely a bundle or preset.
- Official OMP materials show substantial author-written code, including a native systems layer and monorepo components beyond baseline Pi's minimal-core posture.
- OMP includes explicit documentation about porting from upstream Pi and preserving intentional divergences.
- OMP presents major workflow capabilities as part of the built-in product surface rather than only as separately installable packages.
- The strongest current evidence points to OMP being a real forked product with integrated architecture, not just a packaged extension stack.

## Concrete Architecture Signals

### 1. Explicit fork with explicit divergence
OMP's official materials describe it as a fork of Pi, but they do not stop there.

The `porting-from-pi-mono.md` document explicitly discusses:
- intentional divergences
- what upstream changes should and should not be carried forward
- features/files that should be skipped or preserved

That is strong evidence of a maintained fork with its own design direction, not just a downstream preset.

### 2. Mixed-language monorepo with native systems layer
OMP's repository structure and docs show a larger mixed-language system than a thin package layer.

Signals include:
- monorepo layout with multiple first-party packages
- first-party Rust/native crate documentation
- native addon/runtime language boundary

This matters because a native systems layer is a different class of product work than simply composing TS extensions around a minimal upstream harness.

### 3. Built-in tool/runtime claims
OMP's README markets a broad built-in surface, including capabilities such as:
- many built-in tools
- persistent eval runtimes
- debugger / DAP integration
- browser and desktop control surfaces
- memory features
- collaboration
- richer code-editing/runtime integration

Even where some analogous capabilities may exist in Pi packages, OMP presents them as integrated product behavior rather than separately assembled ecosystem choices.

### 4. Native architectural direction
OMP docs about native crates point to first-party ownership of lower-level infrastructure rather than just relying on shell-outs or package glue.

This suggests that part of OMP's value proposition is not only which features exist, but also how tightly they are integrated.

## Why OMP Is Not Just a Bundle
The current evidence supports three distinct layers:

### Layer A: Pi lineage
OMP clearly inherits from Pi.

### Layer B: package-like batteries-included posture
Some OMP-visible value could, in principle, be approximated by Pi plus a curated package set.

### Layer C: real forked product work
OMP also contains enough first-party code and architectural divergence that it should be treated as a product in its own right.

The presence of Layer C is the key conclusion.

## Relationship to Reachability
This architectural conclusion matters because it changes the answer to the practical question:

- If OMP were only Layer B, then Pi package assembly would likely be the whole story.
- Because OMP also appears to include Layer C, full parity is less likely to be reachable through off-the-shelf package installation alone.

So the best current conclusion is:
- Pi plus packages can likely approximate meaningful parts of OMP
- but OMP still appears to have an irreducible integrated product layer

## Relationships to Other Notes
- `research/products/omp/README.md`
- `research/products/omp/foundations.md`
- `research/products/omp/security-and-trust.md`
- `research/syntheses/pi-vs-omp-comparison.md`
- `research/syntheses/omp-reachability-matrix.md`
- `research/syntheses/pi-to-omp-reachability.md`
- `research/products/pi/foundations.md`

## Repository Relevance
- This note prevents future analysis from flattening OMP into "just Pi with plugins."
- It also supports a more honest evaluation of what can be reproduced by package assembly versus what would require custom engineering or adopting OMP directly.

## Open Questions
- Which OMP built-ins are thin wrappers over package-like capability composition versus genuinely deep native/runtime integration?
- Which OMP architectural divergences materially improve day-to-day workflow versus just increasing product complexity?
- Which OMP-specific integrated surfaces matter enough to care about in this repository's environment?

## References
- [OMP GitHub repository README](https://github.com/can1357/oh-my-pi/blob/main/README.md) — fork identity, bundled capability claims, and built-in product framing.
- [OMP porting-from-pi-mono](https://github.com/can1357/oh-my-pi/blob/main/docs/porting-from-pi-mono.md) — explicit divergence and upstream-porting policy.
- [OMP native crates documentation](https://github.com/can1357/oh-my-pi/blob/main/docs/native-crates.md) — native systems layer and crate-level architecture clues.
- [OMP repository root](https://github.com/can1357/oh-my-pi) — monorepo structure and first-party package layout.
- [Pi GitHub repository README](https://github.com/earendil-works/pi/blob/main/README.md) — upstream platform framing for contrast.
