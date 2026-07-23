# Permission Policy

## Purpose
This document records the intended permission model for the harness.

It exists because OpenCode permissions are partly enforceable in config and partly only expressible as prompt policy or user discipline. This file is the human-readable map of what each agent should be allowed to do, what should require approval, and what should be denied.

## Scope
This policy covers:
- agent tool permissions
- bash permission patterns
- repo-local vs external-directory boundaries
- where OpenCode can enforce the rule directly
- where the harness must rely on prompt policy or user approval instead

It does **not** replace `opencode.jsonc` or agent frontmatter. Those remain the actual enforcement layer.

## Design Rules
- Prefer the lightest workable permissions for each role.
- Keep read/search/test work low-friction.
- Increase friction for durable mutation, external effects, privileged actions, and outside-workspace access.
- Prefer the `edit` tool for repo-local file mutation over broad shell mutation.
- Do not pretend OpenCode can semantically classify every bash command. When the runtime cannot distinguish safe from unsafe behavior reliably, use narrower allowlists and document the gap.

## Enforcement Reality
OpenCode can natively enforce:
- allow / ask / deny by tool
- per-agent permission overrides
- bash permission patterns by command string
- path-based `external_directory` controls

OpenCode does **not** natively understand all of the following with full precision:
- whether a bash command is truly read-only
- whether a bash command mutates only inside the repo
- whether a bash command mutates outside the repo indirectly
- whether a command is user-invoked versus autonomously chosen

Because of that, some desired rules can only be approximated by config and must be reinforced by prompt policy.

## Intended Model by Agent

### Generalist
Role: primary session owner.

Desired default:
- Allow: read, edit, write, glob, grep, list, task, skill, todowrite, lsp
- Allow: common read/search shell commands
- Allow: common local test commands
- Allow: local git workflow commands needed to avoid repeated approval spam during explicitly user-invoked git work
- Ask: broader shell execution, package-manager commands, general interpreters, risky git commands, and commands with external or unclear side effects

Practical bash categories:
- **Allow**
  - `git status*`
  - `git diff*`
  - `git log*`
  - `git show*`
  - `git add*`
  - `git commit*`
  - `rg *`
  - `cat *`
  - `type *`
  - `where *`
  - `which *`
  - `pytest *`
- **Ask**
  - `git push*`
  - `git reset*`
  - `git clean*`
  - `git rebase*`
  - `git checkout*`
  - `git merge*`
  - `python *`
  - `node *`
  - `npm *`
  - `pip *`
  - everything else not explicitly allowlisted

Important policy note:
- The Generalist should only use commit/push workflows when the user explicitly asked. OpenCode permissions cannot fully enforce the "user explicitly asked" condition by themselves.

### Coder
Role: bounded implementation subagent.

Desired default:
- Allow: repo-local edits through the `edit` tool
- Allow: read/search tools
- Allow: common local test commands
- Ask: broader bash execution and commands that may mutate beyond the intended scoped work
- Deny: subagent spawning, external web research

Practical bash categories:
- **Allow**
  - `pytest *`
  - `rg *`
  - `cat *`
  - `type *`
- **Ask**
  - `python *`
  - `node *`
  - `npm *`
  - `pip *`
  - `git *`
  - everything else not explicitly allowlisted

Important policy note:
- The Coder should be free to edit files inside the repo via `edit`, but should **not** have unrestricted bash mutation power.

### Reviewer
Role: fresh-context critique subagent.

Desired default:
- Allow: read/search tools
- Allow: review skills
- Allow: read-only git inspection commands and light verification commands
- Ask: other shell commands
- Deny: edits, writes, subagent spawning, web research

Practical bash categories:
- **Allow**
  - `git status*`
  - `git diff*`
  - `git log*`
  - `git show*`
  - `rg *`
  - `cat *`
  - `type *`
  - `pytest *`
- **Ask**
  - everything else not explicitly allowlisted

### Explorer
Role: local scouting only.

Desired default:
- Allow: read, glob, grep, list, lsp
- Deny: edit, write, bash, task, web tools

### Researcher
Role: external scouting only.

Desired default:
- Allow: webfetch, websearch
- Deny: local file tools, bash, edit/write, task

## External Directory Policy
- External directory access should remain more restrictive than repo-local work.
- No agent should freely mutate outside the main working directory.
- If outside-workspace access is needed, it should generally be read-only by default and explicitly approved or allowlisted by path.
- Bash commands that touch outside paths may still be difficult to classify reliably, so `external_directory` should remain an important hard boundary.

## Known Gaps
- Bash pattern matching is not the same as semantic command classification.
- Some command families, especially `python *`, `node *`, `npm *`, and PowerShell-heavy commands, can be either harmless or mutating depending on arguments.
- The policy "allow git commit only when the user explicitly asked" remains partly behavioral, not fully enforceable by config.
- Stronger enforcement of repo-local-only shell mutation would likely require a custom plugin or wrapper-command approach.

## Current Hardening Outcome
- `generalist` now has low-friction local git inspection plus local `git add*` / `git commit*`, and also allows `git branch*`, `git bundle*`, and simple PowerShell path checks with `Test-Path *`, while broader git, interpreter, and package-manager commands still ask.
- `coder` now uses the `edit` tool freely for repo-local changes, but broad bash is no longer fully open; only a small read/test allowlist remains automatic.
- `reviewer` now has a read/test-oriented bash allowlist instead of unrestricted shell access.
- `explorer` and `researcher` were already aligned closely enough and were left unchanged.
- `external_directory` is now explicitly `ask` in the global baseline and again on the agents where broader mutation risk mattered most.

## Remaining Practical Limits
- OpenCode does not provide a native separate include file for permission maps; the enforced rules still live in `opencode.jsonc` and agent frontmatter.
- A bash command that mutates files inside the repo versus outside the repo cannot always be distinguished reliably from pattern matching alone.
- Session approval friction for some command families will still remain unless those commands are explicitly allowlisted or approved with the session-level `always` option.
- If local git workflow still feels too chatty after this change, the next low-risk adjustment would be to selectively allow a few more non-destructive git commands rather than broadening all shell access.

## Future Improvement Path
If the current permission model still feels too coarse after hardening:
1. add a small custom plugin using `tool.execute.before` and/or `permission.ask`
2. inspect bash commands before execution
3. block or reroute commands that target outside-workspace paths or risky command families

That should be justified only if the config-only approach still leaves a meaningful real-world gap.
