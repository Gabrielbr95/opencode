---
name: gen-dependency_police
description: Challenge every dependency. Prefer removal over addition. Every dep must justify its existence.
---

# gen-dependency_police

## When to load

Load when evaluating a new dependency being added, reviewing a requirements file, or auditing an existing project for dependency bloat.

## Rules

- Every dependency must justify its existence with a concrete, specific reason.
- Prefer stdlib solutions. The bar for adding a third-party package is: stdlib cannot do this, or doing it in stdlib requires substantially more code with meaningfully higher risk of bugs.
- Prefer removing dependencies over adding them.
- Small utility packages (one function wrappers) are almost never justified.

## Evaluation Questions

For each dependency, answer:
1. What specific problem does it solve that stdlib cannot?
2. Is it actively maintained? (Check last commit date, open issues)
3. Does it have Windows compatibility? (Relevant to corporate laptop environment)
4. Does it make network calls, phone home, or require external services for core function?
5. What is the transitive dependency cost? (How many packages does it pull in?)
6. What is the failure mode if this package breaks or disappears?

## Tiers of Scrutiny

| Dep type | Scrutiny level |
|---|---|
| Replaces 5+ lines of stdlib | Low — likely justified |
| Provides complex domain functionality (PDF parsing, HTTP, crypto) | Medium — validate Windows compat and maintenance |
| Adds convenience over stdlib | High — probably not justified |
| Wraps a single function | Reject — write the function |
| Requires a running service or external API | Flag — check data residency rules |

## Output Format

For each flagged dependency:
```
Dependency: <name>
Issue: <why it's questionable>
Recommendation: <remove / replace with stdlib / keep with justification>
```
