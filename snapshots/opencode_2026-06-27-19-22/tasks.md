tier: script

## High-Level Plan
A single stdlib-only Python script (`export.py`) at the repo root. On each run it generates a local timestamp, walks the repo tree excluding `.gitignore`'d paths plus `.git/` and `snapshots/`, copies the surviving files into `snapshots/opencode_YYYY-MM-DD-HH-mm/`, then zips that folder alongside it. A `--dry-run` flag lists what would be copied without writing. No import/merge logic — the receiving side unzips and merges by hand.

## Blockers / Open Questions
- None. All design decisions resolved with user.

## Tasks
- [ ] **1. Scaffold export.py: CLI, timestamp, paths**
  - **Description**: Create `export.py` at repo root. Parse `--dry-run` and `--help`. Compute snapshot name `opencode_YYYY-MM-DD-HH-mm` from local time. Resolve repo root (script's parent dir), `snapshots/` dir, and per-run snapshot folder + zip path. Print the planned paths.
  - **Tier**: script
  - **Files**: `export.py`
  - **Acceptance**: `python export.py --help` prints usage. `python export.py --dry-run` prints the intended snapshot folder path and zip path with a valid `YYYY-MM-DD-HH-mm` timestamp, and exits without creating anything.

- [ ] **2. Implement .gitignore-aware file selection**
  - **Description**: Walk the repo tree from repo root. Skip `.git/`, `snapshots/`, and any path matching patterns parsed from `.gitignore` (currently: `node_modules`, `package.json`, `package-lock.json`, `bun.lock`, `.gitignore`). Force-include `.gitignore` itself (see spec assumption). Also exclude the script file `export.py`'s own output but **include** `export.py` in the snapshot. Return a list of `(src, rel)` pairs.
  - **Tier**: script
  - **Files**: `export.py`
  - **Acceptance**: In `--dry-run` mode, the printed file list contains `opencode.jsonc`, `AGENTS.md`, `export.py`, `.gitignore`, and entries under `agents/`, `skills/`, `command/`, `plugins/`, `docs/`. The list does **not** contain `node_modules/`, `package.json`, `package-lock.json`, `bun.lock`, `.git/`, or `snapshots/`.

- [ ] **3. Implement copy to snapshot folder**
  - **Description**: Create `snapshots/opencode_<ts>/` if absent. Copy each selected file from the selection list into it, preserving the relative directory structure. Use `shutil.copy2` to preserve mtimes. Refuse to overwrite an existing snapshot folder of the same name (exit non-zero with a clear message).
  - **Tier**: script
  - **Files**: `export.py`
  - **Acceptance**: After a non-dry-run, `snapshots/opencode_<ts>/` exists and contains the same file count as the dry-run list. `diff -r` between source dirs (excluding ignored paths) and the snapshot reports no differences for included files. Directory tree (relative paths) is preserved.

- [ ] **4. Implement zip creation**
  - **Description**: After the copy, zip the snapshot folder to `snapshots/opencode_<ts>.zip` (sibling of the folder). Use `zipfile` with `ZIP_DEFLATED`. The archive's internal paths must be relative to the snapshot folder (no absolute paths, no leading `snapshots/opencode_<ts>/` prefix inside the zip — files appear at their relative position).
  - **Tier**: script
  - **Files**: `export.py`
  - **Acceptance**: `snapshots/opencode_<ts>.zip` exists. `unzip -l` on it lists the same file count and relative paths as the snapshot folder. Extracting the zip into a temp dir produces a tree identical to the snapshot folder (`diff -r` clean). Zip opens in Windows Explorer without errors.

- [ ] **5. Logging, summary, and error handling**
  - **Description**: Print a human-readable summary at the end: number of files copied, total bytes copied, snapshot folder path, zip path, elapsed time. Wrap filesystem operations in try/except that prints a clear message and exits non-zero (e.g. snapshot folder already exists, permission denied, disk full). Do not leave a half-written snapshot folder on failure — clean it up.
  - **Tier**: script
  - **Files**: `export.py`
  - **Acceptance**: A successful run prints exactly: file count, total size (human-readable, e.g. `1.2 MB`), snapshot folder path, zip path. Triggering a duplicate-timestamp run (e.g. by mocking the clock) exits non-zero with a message naming the conflicting folder and leaves the existing snapshot intact. Triggering a permission error (e.g. read-only `snapshots/`) exits non-zero with a message and leaves no partial folder behind.

- [ ] **6. Usage docstring + manual-merge note**
  - **Description**: Add a module docstring at the top of `export.py` explaining: what the script does, how to run it (`python export.py [--dry-run]`), where output lands, and the manual workflow on the receiving side (unzip, visually compare with live config, copy desired files by hand — no auto-merge). Mention the API-key-ships-in-plaintext caveat as a warning.
  - **Tier**: script
  - **Files**: `export.py`
  - **Acceptance**: Docstring present at top of file. Mentions `--dry-run`. Mentions bidirectional manual merge. Contains an explicit warning that `opencode.jsonc` (including API keys) ships in plaintext inside the zip. `python export.py --help` reflects the same usage.
