# Pi Config and Instruction Loading

## Freshness
- Last verified: 2026-07-28
- Verified against: Pi usage docs, settings docs, skills docs, prompt-template docs
- Product version: current docs snapshot
- Stability: Low-Medium
- Recheck triggers:
  - context-file discovery changes
  - project trust behavior changes
  - settings schema changes for resources

## Scope
- how Pi loads context files, system prompt files, settings, skills, and prompt templates
- which locations are global versus project-local
- where project trust gates loading

## Canonical Boundary
This note owns Pi's instruction/config loading surfaces.

It is not the main home for:
- session branching and compaction internals
- extension API event semantics
- cross-tool instruction-layer theory

## Why This Matters Here
- Reproducing a harness depends on where behavior is loaded from and what is always-on versus on-demand.

## Current Findings
- Pi loads `AGENTS.md` or `CLAUDE.md` at startup from the global agent directory, ancestor directories, and the current directory.
- Pi can replace the default system prompt with `SYSTEM.md` or append with `APPEND_SYSTEM.md`, at project and global scope.
- Project-local `.pi` settings and resources are trust-gated.
- Skills, prompts, themes, extensions, and packages can all be declared through settings and CLI flags in addition to default discovery locations.

## Context Files

Pi loads `AGENTS.md` or `CLAUDE.md` from:
- `~/.pi/agent/AGENTS.md`
- parent directories walking up from the current working directory
- the current directory

Loading can be disabled with `--no-context-files` or `-nc`.

## System Prompt Files

Pi supports:
- `.pi/SYSTEM.md` — project-level system prompt replacement
- `~/.pi/agent/SYSTEM.md` — global system prompt replacement
- `.pi/APPEND_SYSTEM.md` — project-level prompt append
- `~/.pi/agent/APPEND_SYSTEM.md` — global prompt append

CLI flags also exist:
- `--system-prompt <text>` — replace the default prompt
- `--append-system-prompt <text>` — append to the system prompt

## Settings Files

Pi uses JSON settings files at:
- `~/.pi/agent/settings.json`
- `.pi/settings.json`

Project settings override global settings, and nested objects are merged.

## Project Trust Loading Boundary

Project trust controls whether Pi loads:
- `.pi/settings.json`
- `.pi` resources such as extensions, skills, prompts, themes, and system prompt files
- missing project packages configured through project settings
- project-local extensions and project package-managed extensions

Before trust resolution, Pi still loads context files plus user/global extensions and CLI `-e` extensions.

## Skills Discovery

Pi loads skills from:
- `~/.pi/agent/skills/`
- `~/.agents/skills/`
- `.pi/skills/`
- project `.agents/skills/` in cwd and ancestors up to repo root or filesystem root
- package manifests/directories
- settings `skills`
- CLI `--skill`

Pi documents compatibility with skills from other harnesses by adding directories such as `~/.claude/skills` and `~/.codex/skills` to settings.

Pi states that it implements the Agent Skills standard leniently and allows skill names to differ from the parent directory.

## Prompt Templates

Pi loads prompt templates from:
- `~/.pi/agent/prompts/*.md`
- `.pi/prompts/*.md`
- packages
- settings `prompts`
- CLI `--prompt-template`

Prompt-template discovery in `prompts/` is non-recursive.

## Extensions and Themes

Extensions auto-discover from:
- `~/.pi/agent/extensions/*.ts`
- `~/.pi/agent/extensions/*/index.ts`
- `.pi/extensions/*.ts`
- `.pi/extensions/*/index.ts`
- package manifests/directories
- settings `extensions`
- CLI `--extension`

Themes load from analogous settings/package/discovery paths, with `.json` theme files.

## Packages as Resource Bundles

Pi packages can provide:
- `extensions`
- `skills`
- `prompts`
- `themes`

Packages may declare resources under a `pi` manifest in `package.json` or through convention directories.

## Relationships to Other Notes
- `research/products/pi/foundations.md`
- `research/products/pi/security-and-trust.md`
- `research/products/pi/extension-ecosystem-and-core-gaps.md`
- `research/concepts/instruction-layering.md`
- `research/concepts/skill-systems.md`

## Repository Relevance
- This note identifies which Pi surfaces map to always-on instructions, skill-style procedures, prompt shortcuts, and installable behavior bundles.

## Open Questions
- Which current repository artifacts map most directly onto Pi context files, system prompt files, skills, prompt templates, and extensions?

## References
- [Using Pi](https://pi.dev/docs/latest/usage) — context files, system prompt files, CLI resource flags.
- [Settings](https://pi.dev/docs/latest/settings) — settings locations, trust behavior, resource arrays.
- [Skills](https://pi.dev/docs/latest/skills) — skill locations and compatibility notes.
- [Prompt Templates](https://pi.dev/docs/latest/prompt-templates) — template locations and format.
- [Extensions](https://pi.dev/docs/latest/extensions) — extension locations and auto-discovery.
- [Pi Packages](https://pi.dev/docs/latest/packages) — package resource bundling.
