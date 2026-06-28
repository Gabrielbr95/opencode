---
name: gen-senior_maintainer_review
description: Review code as a new maintainer who has never seen the project. Original author is gone. Docs may be incomplete.
---

# gen-senior_maintainer_review

## When to load

Load when reviewing code for long-term maintainability — especially before handing off a project, resuming work after a long gap, or deciding whether to keep or rewrite something.

## Assumptions

- The original author has left. There is no one to ask.
- Documentation may be incomplete, outdated, or missing.
- The project has not been touched for at least a year.
- The new maintainer is competent but has zero prior context on this codebase.

## Review Questions

Work through these systematically:

**Understandability**
- Can a new maintainer understand what this code does within 10 minutes?
- Are the entry points obvious? (What do you run? What does it need?)
- Are non-obvious decisions explained in comments?
- Are there "magic values" with no explanation?

**Debuggability**
- If this fails at 11pm, can someone diagnose it without the original author?
- Are error messages specific enough to point to the cause?
- Is logging sufficient to reconstruct what happened?
- Is there a way to reproduce failures with known inputs?

**Responsibility clarity**
- Is it clear what each module/function is responsible for?
- Are there functions doing two unrelated things?
- Is there code that clearly belongs somewhere else but ended up here?

**Fragility**
- What assumptions does this code make that could break silently?
- What happens when the input is slightly different from expected?
- Are there hardcoded paths, credentials, or environment assumptions?

**Abandonment risk**
- If the dependencies were not updated for two years, would this still run?
- Are there dependencies that are likely to be abandoned or break?

## Output Format

```
Finding
- What: <description>
- Where: <file, function, line if relevant>
- Severity: HIGH / MEDIUM / LOW
- Evidence: <quote or specific observation>
- Recommendation: <concrete suggestion>
```

Severity guide:
- **HIGH**: a new maintainer would be blocked or misled
- **MEDIUM**: would cause confusion or slow debugging
- **LOW**: minor clarity improvement
