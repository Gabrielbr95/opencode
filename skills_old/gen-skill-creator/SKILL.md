---
name: gen-skill-creator
description: >-
  Author, revise, or audit agent skills (SKILL.md files) for OpenCode and the
  cross-platform Agent Skills standard. Use this whenever the user wants to
  create, write, build, scaffold, or rewrite a skill; says "turn this into a
  skill" / "make this a skill" / "skill for X"; describes a repeating workflow
  they keep re-explaining to the agent; or asks to improve, tighten, or audit
  an existing skill. Also self-trigger when the agent notices the user
  re-explaining the same workflow across multiple turns and a reusable skill
  would help — in that case, emit a short notification before proceeding. Also
  use when the user asks how skills work, what the SKILL.md format is, or
  where to place skills. Do NOT use for one-off tasks that won't be repeated.
---

# Skill Creator

You author agent skills: self-contained folders containing a `SKILL.md` file
that teach the agent a repeatable procedure. A well-written skill passes two
bars — it **triggers at the right moment** (description does its job) and it
**changes what the agent does** once loaded (body does its job). Most skills
fail one of those two. This skill catches both before shipping.

## When to use this skill

**User-initiated** (the user explicitly asks):
- "Create / build / scaffold / write a skill"
- "Turn this into a skill" / "make this a skill" / "skill for X"
- "Improve / tighten / revise / audit this skill"
- "How do skills work?" / "what's the SKILL.md format?" / "where do skills live?"

**Agent-initiated** (you self-trigger):
- The user has re-explained the same workflow across two or more turns
- You notice a repeating pattern that would benefit from being encoded as a skill
- The user expresses frustration about the agent "forgetting" a procedure

Do NOT use this for one-off tasks that won't be repeated — a skill for a single
run is overkill. Just do the task.

## Agent-initiated notification protocol

When you self-trigger (not when the user explicitly asks), **emit this
notification at the top of your response before doing anything else**:

```
ℹ️ Skill proposal: <proposed-name> — <1-line summary of what it would do>.
   I noticed <trigger observation>. Drafting now — say "stop" to cancel.
```

Then proceed directly to Step 2 (PLAN) using what you already know from the
conversation. Do not run the full Step 1 interview in agent-initiated mode —
you already have the pattern in context. Draft the skill, run validation, and
present it for approval. The user can redirect or cancel.

Keep the notification to 1–3 lines total. Its job is to make the autonomous
action visible, not to interrupt the flow.

## Naming scheme (mandatory)

All skills authored with this skill follow a prefix grammar:

```
[auto-] <category> - <name>
```

| Prefix | Meaning |
| --- | --- |
| `auto-` | Agent-generated skill (the agent proposed and wrote it). Omit for skills the user hand-writes manually. |
| *(none)* | Manually written by the user. |

| Category | Meaning |
| --- | --- |
| `plan-` | Planning skill — produces plans, specs, architectures; no code execution |
| `exec-` | Execution skill — runs code, performs actions, modifies files |
| `gen-` | General skill — reference, workflow, or meta-skill that doesn't fit plan or exec |

Then the skill name itself: kebab-case, descriptive, can be composite
(multiple words joined with `-`).

### Valid examples

| Name | Decoded |
| --- | --- |
| `plan-pdf-extraction` | Manual, planning, "pdf-extraction" |
| `auto-exec-deploy-script` | Agent-generated, execution, "deploy-script" |
| `gen-skill-creator` | Manual, general, "skill-creator" (this very skill) |
| `auto-gen-release-notes` | Agent-generated, general, "release-notes" |
| `exec-git-release` | Manual, execution, "git-release" |

### Rules

- The full name (including prefixes) must still satisfy the OpenCode regex:
  `^[a-z0-9]+(-[a-z0-9]+)*$` — lowercase alphanumeric, single hyphens, no
  leading/trailing `-`, no `--`.
- The full name **must match the directory name** exactly.
- Total length 1–64 chars.
- When agent-initiated, always use `auto-`. When user-initiated, ask the user
  whether the skill is manual or auto-generated if it's ambiguous; default to
  manual (no `auto-`) when the user is directing the authoring.
- Pick the category by what the skill *does*, not by where it's used:
  - Produces a plan/spec → `plan-`
  - Runs/edits/executes → `exec-`
  - Reference, workflow, or meta → `gen-`

## What you produce

A directory at one of:

- `.opencode/skills/<name>/SKILL.md` (project — preferred for repo-specific skills)
- `~/.config/opencode/skills/<name>/SKILL.md` (global — preferred for personal skills)
- `.claude/skills/<name>/SKILL.md` or `~/.claude/skills/<name>/SKILL.md` (cross-platform)

containing:

```
<name>/
├── SKILL.md              # required — navigation + procedure
├── references/           # optional — longer docs loaded just-in-time
├── scripts/              # optional — deterministic, repeatable logic
└── assets/               # optional — templates, example outputs
```

After writing, **remind the user to quit and restart opencode** so the new
skill is discovered. Running sessions keep using the already-loaded config.

## The format (baked in)

Every `SKILL.md` has two parts: YAML frontmatter, then a markdown body.

### Frontmatter

| Field | Required | Rules |
| --- | --- | --- |
| `name` | yes | 1–64 chars; follows the naming scheme above; **must match the parent directory name**. Regex: `^[a-z0-9]+(-[a-z0-9]+)*$` |
| `description` | yes | 1–1024 chars. The **routing signal** — the only thing the agent sees before deciding to load the skill. State *what* it does AND *when* to use it. |
| `license` | no | e.g. `MIT` |
| `compatibility` | no | e.g. `opencode` |
| `metadata` | no | string-to-string map |
| `allowed-tools` | no | experimental; restrict tool access |

Unknown fields are silently ignored — don't rely on custom fields for routing.

### Body

The body loads only after the skill triggers. Keep it under **500 lines / 5000
tokens** — offload bulk to helper files. Write in **imperative voice** ("Extract
the text…", not "The results should be analyzed").

### Progressive disclosure (why structure matters)

| Stage | Token budget | What loads |
| --- | --- | --- |
| 1. Advertise | ~100 per skill | `name` + `description` injected at run start |
| 2. Load | < 5000 recommended | Full `SKILL.md` body on match |
| 3. Read resources | as needed | Helper files the body explicitly references |
| 4. Run scripts | as needed | Bundled scripts the body tells the agent to run |

The `description` is therefore the most important text in the entire file. A
vague description → never triggers. A broad description → triggers when
irrelevant. Write it carefully.

## Authoring workflow

### Step 1 — DISCOVER: gather the requirements

Two branches depending on how this skill was invoked.

#### Branch A: User-initiated (interview mode)

Do not skip the interview. Skills written from assumptions fail. Ask, in one
batch:

1. **What task** does this skill encode? (the repeatable procedure, not the
   one-off instance)
2. **When** should it trigger? What words or situations in the user's request
   should activate it? What adjacent topics should NOT activate it?
3. **What does the agent already do wrong** without this skill — what's the
   specific failure mode you're fixing? (This tells you what the body must
   change.)
4. **What does "done" look like?** What's a passing example input/output?
5. **Are there helpers** the agent will need — scripts to run, references to
   consult, templates to copy? Or is this pure instruction?

If the user gives you source material (a doc, a transcript, a previous chat),
read it first, then ask only the gaps the material doesn't answer.

If the user's answers are vague, ask one sharper follow-up rather than
proceeding on guesses. Do not begin drafting until you can state, in one
sentence, the specific failure this skill prevents.

#### Branch B: Agent-initiated (extraction mode)

You self-triggered because the user re-explained a workflow across turns.
Extract the pattern from the conversation context:

1. **What task**: the repeatable procedure the user keeps describing.
2. **When it triggers**: the situations that prompted the user to re-explain.
3. **The failure mode**: what you (the agent) did wrong that forced the
   re-explanation.
4. **Done criteria**: what the user accepted as correct in the conversation.
5. **Helpers**: usually none in this mode — keep it lean.

You already emitted the notification (see "Agent-initiated notification
protocol" above). Proceed to Step 2.

In both branches, do not begin drafting until you can state, in one sentence,
the specific failure this skill prevents.

### Step 2 — PLAN: decide the lightest viable structure

Before writing, decide:

- **Name**: follow the naming scheme. Pick `auto-` if agent-initiated; ask
  the user if unclear. Pick `plan-`/`exec-`/`gen-` by what the skill does.
- **Scope**: one skill = one task. If the workflow has two distinct
  procedures, split into two skills.
- **Rigid vs. flexible body**: rigid (numbered steps, checklists, exact
  commands) for fragile tasks where skipping a step breaks things; flexible
  (guidelines, heuristics, decision frameworks) for tasks with multiple valid
  approaches.
- **Helpers needed?** Default to none. Add `scripts/` only for deterministic
  ops where variation is a bug. Add `references/` only for docs too long to
  inline. Add `assets/` only for templates the agent should copy. Don't
  bundle library code the agent could `import`.
- **Location**: project (`.opencode/skills/`) for repo-specific; global
  (`~/.config/opencode/skills/`) for personal. Confirm with the user if
  unclear.

### Step 3 — GENERATE: write the SKILL.md

Write frontmatter first, then body.

#### Frontmatter rules

- `name` follows the naming scheme: `[auto-]<category>-<name>`, matches the
  directory.
- `description` must cover **what** + **when**. Front-load concrete trigger
  keywords the user is likely to say.
- Use third person: "Use when…" — not "I help with…"
- If the skill should stay quiet on adjacent topics, gate it: "Use ONLY when…"
- Slightly "pushy" descriptions trigger more reliably than modest ones — name
  the implied cases, not just the explicit ones. (e.g. not "for dashboards"
  but "whenever the user mentions dashboards, data visualization, internal
  metrics, or wants to display any kind of company data, even if they don't
  explicitly ask for a 'dashboard'")

#### Body template

```markdown
# <Skill Title>

[1–2 sentences: the specific failure this skill prevents. Not "helps with X"
— the actual bad thing that happens without it.]

## When to use this

[Concrete triggers, including the implied cases. Restate even though it's in
the description — this confirms to the agent it loaded the right skill.]

## Procedure

1. [Step. Imperative voice. Exact command or decision branch.]
2. [Step. If conditional, map the branch explicitly: "If X, do Y. Otherwise,
   skip to step N."]
3. ...

## Output format

[The exact shape, where output shape matters. Drop a template in assets/ and
reference it rather than describing the shape in prose.]

## Examples

[1–2 realistic input/output pairs. Not placeholders — real specifics.]

## Edge cases / Gotchas

- [Encrypted inputs / missing deps / large files / etc. — the things that
  break naive execution.]

## References

- [Pointers to bundled helper files. "For the full API, see references/api.md."]
```

#### Body rules

1. **Imperative voice.** "Extract the text" — not "The text should be extracted".
2. **Numbered steps for rigid workflows.** Fragile tasks, decision trees,
   anything where skipping a step breaks things.
3. **Guidelines for flexible workflows.** Tasks with multiple valid approaches.
4. **Give defaults, not menus.** Agents handle explicit defaults better than
   open choices.
5. **Reference helpers explicitly.** The agent won't see `references/api.md`
   until you write: "For the full API, see [references/api.md](references/api.md)."
6. **Keep under 500 lines.** Move bulk to helpers.
7. **Subdirectories flat — one level deep only.** `references/schema.md` yes;
   `references/db/v1/schema.md` no — breaks discovery on some platforms.
8. **Standard folder names** (`references/`, `scripts/`, `assets/`) for
   cross-platform portability.

### Step 4 — VALIDATE: run the pre-ship checklist

Before showing the user the finished skill, verify every box:

- [ ] `name` follows the naming scheme: `[auto-]<category>-<name>`, where
      category is `plan`/`exec`/`gen`; `auto-` present iff agent-generated
- [ ] `name` satisfies `^[a-z0-9]+(-[a-z0-9]+)*$`, 1–64 chars, matches the
      directory name exactly
- [ ] `description` is 1–1024 chars, covers *what* + *when*, semantically
      distinct from any sibling skill in the same directory
- [ ] `description` front-loads concrete trigger keywords the user would
      actually say
- [ ] Body starts with trigger conditions (restates the "when")
- [ ] Body is procedural (imperative voice), not documentation prose
- [ ] Steps are numbered and explicit where the task is fragile
- [ ] Edge cases documented
- [ ] Realistic input/output examples included — not placeholders
- [ ] `SKILL.md` is under 500 lines; bulky detail moved to helpers
- [ ] Helper subdirectories are one level deep only
- [ ] Helper files are explicitly referenced from the body
- [ ] Only relevant tools assigned (if using `allowed-tools`)

Then run the **two-bar self-test**:

1. **Trigger test.** Re-read only the `description`. Would an agent reading
   this, given a realistic user request that *should* activate the skill,
   actually load it? Would it wrongly load on an adjacent request that
   *shouldn't*? If either fails, rewrite the description.
2. **Would-have-anyway test.** For each line in the body, ask: would a
   competent agent already do this without the skill? If yes, the line is
   wasted context — cut it or sharpen it into a specific the agent wouldn't
   guess.

If either test fails, iterate. Do not ship until both pass.

### Step 5 — INSTALL: write the files

1. Create the skill directory at the chosen location, named exactly as the
   `name` field.
2. Write `SKILL.md` (all caps filename — case-sensitive).
3. Write any helper files the plan called for.
4. Verify the files exist and are readable.

Optional — register permissions in `opencode.json` if the skill should be
gated:

```json
{
  "permission": {
    "skill": {
      "*": "allow",
      "auto-exec-*": "ask",
      "dangerous-skill": "deny"
    }
  }
}
```

Permissions support `allow` / `ask` / `deny` with `*` wildcards; specific
names take precedence over wildcards. Per-agent overrides go under
`agent.<name>.permission.skill`. A common pattern: gate `auto-exec-*` skills
to `ask` since they execute autonomously.

### Step 6 — HANDOFF: explain what was built

Report to the user:

```
SKILL CREATED

Name:        <name>
Category:    <plan|exec|gen>
Origin:      <manual|auto>
Path:        <full path>
What it does: <one sentence>
When it triggers: <paraphrase the description>
Helpers:     <list, or "none">
Lines:       <n>/500

Trigger test:  PASS
Body test:     PASS

Next: restart opencode to load the skill, then test it on a real request.
```

Remind the user that **opencode must be restarted** for the new skill to be
discovered — running sessions keep using already-loaded config.

## Modes

This skill operates in three modes. Detect which from the user's request.

### Create (default)

Extract the workflow from the conversation or source material, run Step 1
(interview or extraction depending on origin), plan, generate, validate,
install, hand off.

### Rewrite

User has an existing skill that underperforms — doesn't trigger, or triggers
but doesn't change behavior. Read it, run both self-tests on every line, and
report:

- which lines fail the **would-have-anyway test** (candidates to cut or sharpen)
- whether the `description` fails the **trigger test** (too narrow / too vague)
- what real specifics are missing
- whether the name still fits the naming scheme (rename only if the user
  agrees — renaming changes the directory and may break `opencode.json`
  permission references)

Then rewrite. If renaming, move the directory and update any `opencode.json`
permission entries that reference the old name.

### Audit

User wants a score, not a rewrite. For each line of the existing skill, mark:

- **keeps** — specific, survives both tests
- **weak** — too generic, would-have-anyway
- **trigger-risk** — description too narrow or too vague
- **naming** — does the name follow the scheme? (flag but don't fix)

Summarize with concrete fixes. Do not rewrite unless asked.

## Common mistakes (do not make these)

- **Documentation instead of procedure.** A skill is an operating manual, not
  a README. If the body reads like a tutorial, rewrite it as commands.
- **Vague description.** "Helps with code" → never triggers.
- **Overly broad description.** "Does everything" → triggers when irrelevant.
- **"When to use" sections in the body that aren't also in the description.**
  The body only loads *after* triggering — body-only "when to use" info is
  invisible at routing time. Put all trigger keywords in the `description`.
- **Wrong naming scheme.** Forgetting `auto-` on agent-generated skills, or
  mis-categorizing (e.g. `plan-` for a skill that executes code).
- **Deeply nested helper folders.** Breaks discovery on some platforms. One
  level deep only.
- **Bundling library code in `scripts/`.** Use scripts for deterministic ops;
  let the agent `import` libraries normally.
- **Long `SKILL.md`.** Exceeds ~5000 tokens and wastes context on every
  activation. Move bulk to `references/`.
- **Untested triggers.** A skill that never activates is invisible. Always run
  the trigger test before shipping.
- **Placeholder examples.** "Do X with Y" is not an example. Use real
  specifics so the agent can pattern-match.
- **Skipping the interview (user-initiated mode).** Skills written from
  assumptions fail. Always discover the actual failure mode first.
- **Skipping the notification (agent-initiated mode).** Autonomous skill
  creation must be visible. Always emit the notification before drafting.

## Troubleshooting (if a skill doesn't appear)

1. Verify `SKILL.md` is spelled in **all caps** — case-sensitive.
2. Check that frontmatter includes both `name` and `description`.
3. Ensure skill names are unique across all discovery locations.
4. Check permissions in `opencode.json` — skills with `deny` are hidden.
5. Confirm `name` matches the parent directory name exactly (including
   `auto-` prefix and category).
6. Validate YAML — wrap strings in quotes if they contain special characters.
7. Restart opencode — running sessions don't hot-reload config.

## References

The full authoring reference (deeper than this skill's body) lives at
[docs/skill_writing.md](docs/skill_writing.md) in the workspace root — consult
it for edge cases, the full permission matrix, and the cross-platform
specification links.
