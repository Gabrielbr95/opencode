---
name: tier-poc
description: Model-invoked. Coding guidelines for Proof-of-Concept tier. Loads when working on a POC project.
---

# Tier: Proof of Concept (POC)
**Optimize for:** Learning. Answer "Can this be done?" as fast as possible.

## Engineering Rules
1. **Expect Throwaway Code:** Assume the first version may be deleted or replaced.
2. **Bias Toward Speed and Learning:** Prefer the fastest path that can answer the feasibility question clearly. Use shortcuts when they help learning, but do not force them when they would create avoidable confusion.
3. **Minimal Structure:** Keep the solution small and direct. Avoid abstractions or architecture that only pay off if the work becomes a Script or Application later.
4. **Right-Sized Verification:** Use the lightest check that clearly answers whether the POC works. Simple prints, manual checks, or one targeted script are usually enough.
5. **Edge Cases by Relevance:** Ignore non-critical edge cases unless they block the feasibility question, hide a likely failure mode, or materially distort the result.
