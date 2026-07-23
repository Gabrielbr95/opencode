---
name: tier-application
description: Model-invoked. Coding guidelines for Application tier. Loads when working on long-lived, multi-user software.
---

# Tier: Application
**Optimize for:** Maintainability, safety, and team scale.

## Engineering Rules
1. **Maintain Clear Boundaries:** Keep concerns separated enough that the code stays understandable, testable, and maintainable. Do not force extra layers that add ceremony without reducing risk.
2. **Test Where It Pays Off:** Add tests for business-critical, failure-prone, or reusable logic. Do not skip testing where failures would be costly, but do not force the same test intensity on every small change.
3. **Defensive Programming:** Assume inputs, files, integrations, and external systems can fail. Handle important failure modes clearly and avoid silent corruption.
4. **Document What Future You Will Need:** Document non-obvious behavior, constraints, and decisions where they materially improve maintenance or handoff. Do not generate boilerplate comments just to satisfy a rule.
5. **Prefer Explicitness:** Use clear names, clear interfaces, and type hints or other structure where they materially improve correctness and maintainability.
