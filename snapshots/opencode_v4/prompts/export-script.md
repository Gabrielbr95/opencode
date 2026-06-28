# Export Script — Prompt

## Problem

Copying opencode config between home and work by hand causes the two setups to diverge over time. Need a deterministic, repeatable way to package the relevant files from the git repo into a portable folder (or zip) for transfer.

## Context

- Home setup: Manjaro Linux, git repo at `~/.config/opencode/`
- Work setup: Corporate Windows laptop, no admin, no direct GitHub access. Downloads are allowed.
- Transport: TBD (USB, Nextcloud, cloud storage — clarify with user)
- Direction: likely home→work, possibly bidirectional (clarify)
- `opencode.jsonc` has environment-specific provider configs (localhost URLs, API keys) that differ between home and work

## Open Questions (ask before planning)

1. Target path on the Windows work laptop?
2. Transport method (USB, Nextcloud, email, other)?
3. One-way (home→work) or bidirectional?
4. How to handle env-specific files like `opencode.jsonc`? Manual edit after copy, or template/override system?
5. How often will you export?

## Initial Options to Evaluate

1. **`git archive`** — built-in git command that exports tracked files respecting `.gitignore`. Zero custom code. Produces a zip/tar. May be sufficient if env-specific handling is manual.
2. **Python export script** — reads `.gitignore`, copies tree to `export/` or zip, optionally handles env-specific file exclusion/templating. More flexible.
3. **Makefile + rsync** — Linux-native, simple, but doesn't help on the Windows side.

## Suggested Tier

`script` — recurring automation, needs to be reliable, but simple.
