# opencode Config Export Script

## Purpose
A small Python script that packages the live opencode config (from `~/.config/opencode/`) into a timestamped, portable snapshot for transfer between the home (Manjaro) and work (Windows) machines via pendrive or email. Replaces manual, drift-prone hand-copying.

## Scope
### In Scope
- A single Python script (`export.py`) living at the repo root.
- Creating a timestamped snapshot folder `snapshots/opencode_YYYY-MM-DD-HH-mm/` containing the live config.
- Producing a `.zip` of that folder for transport.
- Respecting `.gitignore` exclusions when selecting files.
- Excluding the `snapshots/` output folder and `.git/` from the copy (no recursion).
- Human-readable console summary after each run.

### Out of Scope
- Import / merge logic on the receiving side (fully manual: unzip, eyeball, copy by hand).
- Secret scrubbing or templating of `opencode.jsonc` (shipped as-is).
- Auto-sync, scheduling, or 3-way merge.
- A Windows-side runner (the script is Linux-authored; the Windows laptop only receives zips).
- Reorganizing the existing `opencode_v3/` / `opencode_v4/` folders (user handles manually).

## Inputs & Outputs
- **Input**: the opencode config directory (the script's parent / cwd) and its `.gitignore`.
- **Output**:
  - `snapshots/opencode_YYYY-MM-DD-HH-mm/` — flat copy of selected files, tree preserved.
  - `snapshots/opencode_YYYY-MM-DD-HH-mm.zip` — zipped copy of the above for transport.

## Constraints
- Python 3 standard library only (`pathlib`, `shutil`, `zipfile`, `datetime`, `fnmatch`/`pathspec`). No `pip install` — must run on Manjaro with zero setup.
- Must run from the repo root (`~/.config/opencode/`).
- Timestamp uses local system time, format `YYYY-MM-DD-HH-mm` (zero-padded, 24-hour).
- Must not recursively include prior snapshots or the script's own output.
- Zip must be extractable on Windows without any tooling beyond built-in Explorer support.

## Success Criteria
- Running `python export.py` from the repo root produces both `snapshots/opencode_<timestamp>/` and the matching `.zip`.
- `node_modules/`, `package.json`, `package-lock.json`, `bun.lock`, `.git/`, and `snapshots/` are absent from the snapshot.
- The snapshot contains the live config: `opencode.jsonc`, `AGENTS.md`, `agents/`, `skills/`, `command/`, `plugins/`, `workflow.md`, `README.md`, `docs/` (i.e. everything not ignored).
- Re-running produces a new timestamped snapshot; prior snapshots are left untouched.
- The `.zip` extracts cleanly and its file list matches the folder byte-for-byte (same file count, same relative paths).
- Console output states: file count, total size, output folder path, output zip path.

## Assumptions
- `.gitignore` itself is **included** in the snapshot (it's self-ignored in the repo, but the receiving side needs it to re-establish ignore rules). Builder: force-include `.gitignore` even though it appears in its own ignore list.
- The export script (`export.py`) is **included** in the snapshot so the receiving machine has it for its own future exports (it is not in `.gitignore`).
- User explicitly accepts that the `CONTEXT7_API_KEY` in `opencode.jsonc` ships in plaintext inside the zip — including over email. No scrubbing.
- Import/merge on the receiving side is fully manual: unzip, visually compare, copy desired files. No staging dir, no diff report, no manifest.
- The `snapshots/` folder is created by the script if it does not exist.
- The existing `opencode_v3/` and `opencode_v4/` directories will be relocated/renamed by the user outside this script; until that happens they will appear in snapshots as regular tracked content (they are not in `.gitignore`). Builder: do not special-case them.
