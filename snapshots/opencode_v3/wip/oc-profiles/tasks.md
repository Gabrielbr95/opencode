tier: script

## High-Level Plan
A PowerShell wrapper script (oc.ps1) reads a named permission profile from oc-profiles.jsonc,
serializes it to OPENCODE_PERMISSION, and launches opencode with all remaining args forwarded.
CMD and Git Bash shims call the same ps1. The user edits only oc-profiles.jsonc to add or
tune profiles.

## Blockers / Open Questions
- OPENCODE_PERMISSION behavior should be smoke-tested after build to confirm it still works
  in the installed opencode version (undocumented, could have changed).

## Tasks Checklist

- [x] Task 1: Create oc-profiles.jsonc with starter profiles
      agent: builder
      files: oc-profiles.jsonc
      depends_on: none
      outcome: File exists with "normal" (empty) and "yolo" (all tools allow) profiles.
               Open file and confirm structure is valid JSONC.

- [x] Task 2: Write oc.ps1 wrapper script
      agent: builder
      files: oc.ps1
      depends_on: Task 1
      outcome: Script reads profile arg (default "normal"), strips JSONC comments, sets
               OPENCODE_PERMISSION, and spawns opencode with remaining args forwarded.
               Running `~/.config/opencode/oc.ps1 --help` prints opencode help.
               Running `~/.config/opencode/oc.ps1 yolo` starts opencode with yolo profile active.

- [x] Task 3: Write CMD and Git Bash shims
      agent: builder
      files: oc.cmd, oc.sh
      depends_on: Task 2
      outcome: oc.cmd and oc.sh each forward all args to oc.ps1 by absolute path.
               Calling `~/.config/opencode/oc.cmd yolo` from a CMD prompt starts opencode
               with yolo profile.
