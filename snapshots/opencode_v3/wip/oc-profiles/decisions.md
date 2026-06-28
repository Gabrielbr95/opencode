## Decision 001: Use OPENCODE_PERMISSION env var as the permission override mechanism

**Date**: 2026-06-25

**Context**
Need a way to switch permission profiles at session start without editing agent frontmatter
files. Several upstream approaches were evaluated: `OPENCODE_YOLO` env var, a `"yolo": true`
config field, and per-agent blocks in `opencode.jsonc`.

**Decision**
Use the `OPENCODE_PERMISSION` environment variable. It accepts a JSON object that is
deep-merged after all file-based config (global, project, agent frontmatter), making it
last-write-wins over every agent simultaneously.

**Reasoning**
- Confirmed in `config.ts` source (`packages/opencode/src/config/config.ts`, `loadGlobal()`).
- `OPENCODE_YOLO` was confirmed non-functional in shipped builds by a third-party maintainer
  (jim60105/AIr-Friends commit b50b996, March 2026) who explicitly removed it.
- PR #11833 (YOLO mode) was auto-closed May 2026, never merged.
- Per-agent overrides in `opencode.jsonc` require restating full permission trees and break
  on upstream agent changes.
- `OPENCODE_PERMISSION` requires no file editing and works with any profile definition.

**Tradeoffs**
- Undocumented in public docs — could be removed or renamed in a future opencode release.
- Cannot target individual agents differently within a single profile (all agents get the
  same override). Accepted: user confirmed "switch everything to the same level" is sufficient.

**Consequences**
- The wrapper script sets `OPENCODE_PERMISSION` to the profile's JSON before spawning opencode.
- If `OPENCODE_PERMISSION` ever stops working, fallback is to patch `opencode.jsonc` at
  launch and revert after — more complex but achievable in the same script structure.

**Status**: Active

---

## Decision 002: Profile definitions live in a separate oc-profiles.jsonc file

**Date**: 2026-06-25

**Context**
Profiles will be tuned over time as the user learns which permissions to unlock. The wrapper
script itself should not need editing when profiles change.

**Decision**
Store profiles in `~/.config/opencode/oc-profiles.jsonc`. The script reads this file at
runtime, looks up the requested profile by name, and serializes it to `OPENCODE_PERMISSION`.

**Reasoning**
- Separates configuration from logic — edit profiles without touching script code.
- JSONC (JSON with comments) allows inline documentation of why each rule is set.
- Co-located with `opencode.jsonc` in the same directory — one place for opencode config.

**Tradeoffs**
- One extra file to manage. Acceptable at script tier.
- JSONC comments must be stripped before passing to `OPENCODE_PERMISSION` (JSON only).
  PowerShell handles this with a simple regex strip.

**Consequences**
- `oc-profiles.jsonc` is the only file the user edits day-to-day.
- `oc.ps1` parses JSONC by stripping `//` comments before deserializing.

**Status**: Active

---

## Decision 003: Invoke as explicit path, no PATH modification

**Date**: 2026-06-25

**Context**
Script lives at `~/.config/opencode/`. User wants to call it from VS Code terminal
(PowerShell primary, CMD and Git Bash secondary). Adding `~/.config/opencode` to PATH
is a future option but not required now.

**Decision**
No PATH modification. Script is called as `~/.config/opencode/oc.ps1 yolo` or via a
shell alias. CMD and Git Bash shims are provided in the same directory.

**Reasoning**
- No machine config changes needed — works immediately after file creation.
- User explicitly deferred PATH option to later.
- A $PROFILE alias can be added later in a single line if PATH approach is adopted.

**Tradeoffs**
- More verbose invocation from project directories.
- Switching to PATH later requires adding one line to PowerShell profile — low friction.

**Consequences**
- Shims (oc.cmd, oc.sh) call the .ps1 by absolute path.
- If PATH is added later, Decision 003 should be superseded.

**Status**: Active
