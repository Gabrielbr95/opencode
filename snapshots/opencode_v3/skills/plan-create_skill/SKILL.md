---
name: plan-create_skill
description: Load when creating a new OpenCode skill. Defines naming convention, directory structure, and SKILL.md template. Always requires explicit user approval before writing files.
---

# plan-create_skill

## When to load

Load when a gap in agent behavior is identified that warrants a reusable, loadable skill — not just a one-off instruction. Do not create skills for things that belong in an agent's system prompt.

## Naming Convention

```
{auto-}{category}-{name}
```

- `auto-` — optional prefix for agent-generated skills (omit for human-authored)
- `category` — required: `exec`, `plan`, or `gen`
- `name` — short, lowercase, underscore for multi-word (no dashes within name segment)

| Category | Purpose | Examples |
|---|---|---|
| `exec` | Language/framework coding standards. Loaded by builder. | `exec-python`, `exec-sql` |
| `plan` | Planning knowledge — task writing, reporting, design. | `plan-task_write`, `plan-task_report` |
| `gen` | Cross-cutting utilities. Apply across roles. | `gen-tier_classifier`, `gen-debug_mode` |

When unsure of category, ask before creating.

## Directory Structure

```
~/.config/opencode/skills/{skill-name}/SKILL.md   ← global (all projects)
.opencode/skills/{skill-name}/SKILL.md             ← per-project only
```

One directory, one `SKILL.md`. No subdirectories unless bundling reference assets — confirm with user first.

## SKILL.md Template

```markdown
---
name: {skill-name}
description: One sentence — what it does and when to use it.
---

# {skill-name}

## When to load
1-3 sentences: precise trigger condition. Avoid vague triggers like "when coding".

## {Section}
Content — prefer tables, bullets, and code blocks over paragraphs.

## Example
Concrete usage example. Always include one.
```

## Rules

- `name` in frontmatter must match the directory name exactly.
- `description` is required — skills without one are never surfaced in agent context.
- Target 60-150 lines. Split into two skills if over 200.
- Example section is required.

## Checklist Before Writing

- [ ] Name follows `{auto-}{category}-{name}` with `_` for multi-word
- [ ] Category is correct (`exec` / `plan` / `gen`)
- [ ] Global vs per-project scope is decided
- [ ] User explicitly approved creation
- [ ] No duplicate of an existing skill
- [ ] `description` and `When to load` are clear and specific
- [ ] Example is included
