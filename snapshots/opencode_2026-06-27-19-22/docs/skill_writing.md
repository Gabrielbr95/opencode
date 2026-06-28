# Writing Agent Skills

A practical reference for authoring agent skills, built around the open `SKILL.md`
specification that OpenCode (and 20+ other tools — Claude Code, Cursor, Gemini CLI,
Codex, Windsurf, Cline, Goose, etc.) all implement.

---

## 1. What a Skill Is

A skill is a **directory** containing a `SKILL.md` file. That's the only required
artifact. Everything else (scripts, references, assets, evals) is optional and loaded
on demand via **progressive disclosure** — so it does not bloat the agent's context
window until the skill is activated.

OpenCode discovers skills from these locations (in priority order):

| Scope | Path |
| --- | --- |
| Project (OpenCode) | `.opencode/skills/<name>/SKILL.md` |
| Project (Claude-compatible) | `.claude/skills/<name>/SKILL.md` |
| Project (agent-compatible) | `.agents/skills/<name>/SKILL.md` |
| Global (OpenCode) | `~/.config/opencode/skills/<name>/SKILL.md` |
| Global (Claude-compatible) | `~/.claude/skills/<name>/SKILL.md` |
| Global (agent-compatible) | `~/.agents/skills/<name>/SKILL.md` |

For project paths, the agent walks up from the current working directory to the git
worktree root, loading matching skills along the way.

---

## 2. Anatomy of `SKILL.md`

Every `SKILL.md` has two parts:

1. **YAML frontmatter** — metadata (always in context).
2. **Markdown body** — instructions (loaded only when the skill is activated).

```markdown
---
name: my-skill
description: What this skill does and when to use it
license: MIT
compatibility: opencode
metadata:
  author: your-name
  version: "1.0"
---

## When to use this skill
...

## Instructions
...
```

---

## 3. Frontmatter Fields

### Required

| Field | Rules |
| --- | --- |
| `name` | 1–64 chars; lowercase alphanumeric with single hyphens; cannot start/end with `-`; no consecutive `--`; **must match the parent directory name**. Regex: `^[a-z0-9]+(-[a-z0-9]+)*$` |
| `description` | 1–1024 chars. The **routing signal** — the agent uses this to decide whether to activate the skill. Be specific about *what* and *when*. |

### Optional

| Field | Purpose |
| --- | --- |
| `license` | Open-source license name (e.g. `MIT`) |
| `compatibility` | Compatibility notes (e.g. `opencode`) |
| `metadata` | Free-form string-to-string map |
| `allowed-tools` | Experimental — restrict which tools the skill may use |
| `mcp_servers` | OpenCode-specific — embedded MCP server configs that auto-load on activation |

Unknown frontmatter fields are silently ignored by most platforms.

---

## 4. Helper Files (Bundled Resources)

Helper files alongside `SKILL.md` are **allowed and encouraged**. The `SKILL.md` is
the "brain" for high-level navigation; bulky detail should be offloaded into
subdirectories.

### Standard folder layout

```
.opencode/skills/my-skill/
├── SKILL.md              # required — navigation + primary procedure
├── references/           # longer docs loaded just-in-time
│   └── api.md
├── scripts/              # deterministic, repeatable logic
│   └── extract.py
├── assets/               # templates, example outputs, schemas
│   └── output-template.json
└── evals/                # prompts + expected outputs for testing
    └── case-1.md
```

### Rules

1. **Keep `SKILL.md` lean — under ~500 lines / ~5000 tokens.** Offload detail to helpers.
2. **Subdirectories must be flat — one level deep only.** `references/schema.md` is fine; `references/db/v1/schema.md` breaks discovery on some platforms.
3. **Reference helpers explicitly from `SKILL.md`.** The agent won't see them until you direct it:
   > For the full API, see [references/api.md](references/api.md).
4. **Use standard folder names** (`references/`, `scripts/`, `assets/`, `evals/`) for cross-platform portability.
5. **Scripts should be deterministic.** Bundle them for fragile/repetitive ops where variation is a bug. Do not bundle library code the agent could just `import`.

### How the agent accesses helpers

| Tool | Purpose |
| --- | --- |
| `skill` / `load_skill` | Loads the `SKILL.md` body |
| `read_skill_resource` | Reads a referenced helper file when needed |
| `run_skill_script` | Executes a bundled script |

In OpenCode, these surface as ordinary file operations (read/bash tools) — the agent
reads or runs your helper files when the `SKILL.md` body instructs it to.

---

## 5. Progressive Disclosure

Skills load in stages to minimize context usage:

| Stage | Tokens | What happens |
| --- | --- | --- |
| 1. Advertise | ~100 per skill | `name` + `description` injected into the system prompt at run start |
| 2. Load | < 5000 recommended | On match, the full `SKILL.md` body is retrieved |
| 3. Read resources | as needed | Supplementary files (references, templates, assets) fetched only when required |
| 4. Run scripts | as needed | Bundled scripts executed on demand |

**Implication:** the `description` is the most important text in the entire file. If it's vague, the skill won't trigger. If it's too broad, it'll trigger when irrelevant.

---

## 6. Writing the Body

### Format

- **Imperative voice** — "Extract the text…", not "The results should be analyzed."
- **Third person** — not "I will…" or "You should…"
- **Numbered steps for rigid workflows** — fragile tasks, decision trees, anything where skipping a step breaks things.
- **Guidelines/heuristics for flexible workflows** — tasks with multiple valid approaches.

### Recommended sections

1. **When to use this skill** — explicit trigger criteria.
2. **Step-by-step instructions** — chronological, with decision branches mapped out.
3. **Examples** — expected inputs and outputs.
4. **Edge cases / Gotchas** — highest-value section for reliability.
5. **References** — pointers to bundled helper files.

### Patterns that work

- **Give defaults, not menus.** Agents handle explicit defaults better than open choices.
- **Provide concrete templates.** Agents pattern-match well — drop a template in `assets/` and instruct them to copy its structure rather than describing the shape in prose.
- **Just-in-Time (JiT) loading.** Explicitly instruct the agent *when* to read each helper file. It won't see them until you direct it.

---

## 7. Permissions (OpenCode-specific)

Control which skills agents can access via pattern-based rules in `opencode.json`:

```json
{
  "permission": {
    "skill": {
      "*": "allow",
      "code-review": "allow",
      "dangerous-*": "ask",
      "internal-*": "deny"
    }
  }
}
```

| Value | Effect |
| --- | --- |
| `allow` | Skill available without prompting |
| `ask` | User prompted for approval before loading |
| `deny` | Skill hidden from agent; access rejected |

Pattern matching supports `*` wildcards; specific names take precedence over wildcards.
Permissions can be overridden per-agent.

---

## 8. Authoring Checklist

- [ ] `name` is lowercase alphanumeric with single hyphens, 1–64 chars, matches directory
- [ ] `description` is 1–1024 chars, specific about *what* and *when* to use
- [ ] `description` is semantically distinct from sibling skills
- [ ] Body starts with explicit trigger conditions
- [ ] Instructions are procedural (imperative voice), not documentation
- [ ] Core steps are numbered and explicit
- [ ] Edge cases documented
- [ ] Realistic input/output examples included
- [ ] `SKILL.md` is under 500 lines — bulky detail moved to `references/`, `scripts/`, `assets/`
- [ ] Helper subdirectories are one level deep only
- [ ] Helper files explicitly referenced from `SKILL.md` body
- [ ] Only relevant tools assigned (if using `allowed-tools`)
- [ ] Skill tested against real prompts — trigger first, then output quality

---

## 9. Common Mistakes

- **Writing documentation instead of procedures.** A skill is an operating manual, not a README.
- **Vague descriptions.** "Helps with code" → never triggers.
- **Overly broad descriptions.** "Does everything" → triggers when irrelevant.
- **Deeply nested helper folders.** Breaks discovery on some platforms.
- **Bundling library code in `scripts/`.** Use scripts only for deterministic ops; let the agent `import` libraries normally.
- **Long `SKILL.md` files.** Exceeds ~5000 tokens and wastes context on every activation.
- **Untested triggers.** A skill that never activates is invisible. Verify the description actually causes activation before trusting the body.

---

## 10. Troubleshooting

If a skill does not show up:

1. Verify `SKILL.md` is spelled in **all caps**.
2. Check that frontmatter includes both `name` and `description`.
3. Ensure skill names are unique across all discovery locations.
4. Check permissions — skills with `deny` are hidden from agents.
5. Confirm `name` matches the parent directory name exactly.
6. Validate YAML — wrap strings in quotes if they contain special characters.

---

## 11. References

- **OpenCode Skills Docs** — <https://opencode.ai/docs/skills/>
- **Open Agent Skills Specification** — <https://openagentskills.dev/docs/writing-skill-md>
- **Microsoft Learn: Agent Skills** — <https://learn.microsoft.com/en-us/agent-framework/agents/skills>
- **OpenCode source (skills.mdx)** — <https://github.com/sst/opencode/blob/dev/packages/web/src/content/docs/skills.mdx>
- **mgechev/skills-best-practices** — <https://github.com/mgechev/skills-best-practices>
- **Lalit Madan: The SKILL.md Guide** — <https://lalitmadan.com/post/the-skill-md-guide>
- **Serghei Iakovlev: Agent Skills 101** — <https://blog.serghei.pl/posts/agent-skills-101/>
- **DigitalOcean: How to Implement Agent Skills** — <https://www.digitalocean.com/community/tutorials/how-to-implement-agent-skills>
- **Elastic: Skill creation guidelines** — <https://www.elastic.co/docs/explore-analyze/ai-features/agent-builder/skill-creation-guidelines>
- **JP Caparas: Writing OpenCode Agent Skills** — <https://blog.devgenius.io/writing-opencode-agent-skills-a-practical-guide-with-examples-870ff24eec66>
