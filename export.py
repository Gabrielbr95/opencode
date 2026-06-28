"""opencode config export script.

Packages the live opencode config (the directory this script lives in) into a
timestamped, portable snapshot for transfer between machines via pendrive or
email. Replaces manual, drift-prone hand-copying between home (Manjaro) and
work (Windows).

Usage:
    python export.py [--dry-run]

Output:
    snapshots/opencode_YYYY-MM-DD-HH-mm/        # flat copy of selected files
    snapshots/opencode_YYYY-MM-DD-HH-mm.zip     # zipped copy for transport

File selection respects .gitignore (node_modules, package.json,
package-lock.json, bun.lock, .gitignore) and additionally excludes .git/ and
the snapshots/ output folder. .gitignore itself is force-included so the
receiving side can re-establish ignore rules. export.py is included so the
receiving machine can run its own future exports.

Bidirectional manual merge (IMPORTANT):
    There is NO import or auto-merge logic. On the receiving side you unzip the
    archive, visually compare it with your live config, and copy the files you
    want by hand. The script does not touch your live config on import.

SECURITY WARNING:
    opencode.jsonc ships in PLAINTEXT inside the zip, including any API keys
    defined in it (e.g. CONTEXT7_API_KEY). If you transport the zip over email
    or store it on a shared pendrive, those secrets travel with it. The script
    does NOT scrub secrets. Accept this exposure before running.
"""

import argparse
import shutil
import sys
import time
import zipfile
from datetime import datetime
from pathlib import Path

# --- Globals (edit here if the layout ever changes) -------------------------
REPO_ROOT = Path(__file__).resolve().parent
SNAPSHOT_DIR_NAME = "snapshots"
TIMESTAMP_FMT = "%Y-%m-%d-%H-%M"
SNAPSHOT_PREFIX = "opencode_"

# Patterns always excluded, on top of whatever .gitignore says.
ALWAYS_EXCLUDE_DIRS = {".git", SNAPSHOT_DIR_NAME}
# .gitignore lists itself; we override that and force-include it.
FORCE_INCLUDE = {".gitignore"}


def parse_args():
    p = argparse.ArgumentParser(
        prog="export.py",
        description="Package the opencode config into a timestamped snapshot + zip.",
    )
    p.add_argument(
        "--dry-run",
        action="store_true",
        help="List the files that would be copied without writing anything.",
    )
    return p.parse_args()


def timestamp() -> str:
    return datetime.now().strftime(TIMESTAMP_FMT)


def parse_gitignore(repo_root: Path) -> list[str]:
    """Return the list of non-empty, non-comment patterns from .gitignore."""
    gi = repo_root / ".gitignore"
    if not gi.is_file():
        return []
    patterns = []
    for line in gi.read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        patterns.append(s)
    return patterns


def pattern_matches(rel_parts: tuple[str, ...], patterns: list[str]) -> bool:
    """True if any component of the rel path matches a gitignore pattern.

    The current .gitignore uses simple filename patterns (node_modules,
    package.json, etc.), so basename matching against each path component is
    sufficient. We do not implement full gitignore semantics (anchoring,
    negation, ** globs) — YAGNI for this repo's ignore file. A pattern like
    `node_modules` therefore excludes the directory and everything under it.
    """
    import fnmatch

    for part in rel_parts:
        for pat in patterns:
            if pat in FORCE_INCLUDE:
                continue  # never let a self-ignore exclude .gitignore
            if fnmatch.fnmatch(part, pat):
                return True
    return False


def select_files(repo_root: Path, ignore_patterns: list[str]) -> list[tuple[Path, Path]]:
    """Walk repo_root and return [(src_abs, rel_path), ...] for files to copy."""
    selected: list[tuple[Path, Path]] = []

    for path in repo_root.rglob("*"):
        if path.is_dir():
            continue
        if not path.is_file():
            continue

        rel = path.relative_to(repo_root)
        parts = rel.parts

        # Exclude anything under an always-excluded directory.
        if any(part in ALWAYS_EXCLUDE_DIRS for part in parts):
            continue

        # Exclude gitignore-matched paths (any component matches).
        if pattern_matches(parts, ignore_patterns):
            # But force-include overrides for the specific file.
            if path.name not in FORCE_INCLUDE or len(parts) > 1:
                continue

        selected.append((path, rel))
    return selected


def human_size(n: int) -> str:
    size = float(n)
    for unit in ("B", "KB", "MB", "GB"):
        if size < 1024:
            return f"{size:.1f} {unit}" if unit != "B" else f"{int(size)} {unit}"
        size /= 1024
    return f"{size:.1f} TB"


def copy_to_snapshot(selected, snapshot_folder: Path) -> int:
    """Copy each selected file into snapshot_folder, preserving relative paths.

    Returns total bytes copied.
    """
    total = 0
    for src, rel in selected:
        dst = snapshot_folder / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        total += src.stat().st_size
    return total


def make_zip(snapshot_folder: Path, zip_path: Path) -> None:
    """Zip snapshot_folder into zip_path. Internal paths are relative to the
    snapshot folder (no absolute prefix), so the archive extracts to a clean
    tree on Windows Explorer.
    """
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for f in snapshot_folder.rglob("*"):
            if f.is_file():
                arcname = f.relative_to(snapshot_folder)
                zf.write(f, arcname)


def main() -> int:
    args = parse_args()
    ts = timestamp()
    snapshot_name = f"{SNAPSHOT_PREFIX}{ts}"
    snapshots_root = REPO_ROOT / SNAPSHOT_DIR_NAME
    snapshot_folder = snapshots_root / snapshot_name
    zip_path = snapshots_root / f"{snapshot_name}.zip"

    print(f"Repo root:      {REPO_ROOT}")
    print(f"Snapshot folder: {snapshot_folder}")
    print(f"Snapshot zip:    {zip_path}")
    print()

    ignore_patterns = parse_gitignore(REPO_ROOT)
    selected = select_files(REPO_ROOT, ignore_patterns)

    print(f"Selected {len(selected)} file(s):")
    for _src, rel in selected:
        print(f"  {rel}")
    print()

    if args.dry_run:
        print("[dry-run] No files written.")
        return 0

    # --- Guard: refuse to overwrite an existing snapshot folder ------------
    if snapshot_folder.exists():
        print(
            f"ERROR: snapshot folder already exists: {snapshot_folder}\n"
            "Refusing to overwrite. Wait a minute and rerun, or delete it first.",
            file=sys.stderr,
        )
        return 1
    if zip_path.exists():
        print(
            f"ERROR: snapshot zip already exists: {zip_path}\n"
            "Refusing to overwrite. Wait a minute and rerun, or delete it first.",
            file=sys.stderr,
        )
        return 1

    snapshots_root.mkdir(parents=True, exist_ok=True)

    # --- Copy + zip, with cleanup-on-failure -------------------------------
    t0 = time.monotonic()
    try:
        total_bytes = copy_to_snapshot(selected, snapshot_folder)
        make_zip(snapshot_folder, zip_path)
    except Exception as e:
        print(f"ERROR during export: {e}", file=sys.stderr)
        # Clean up partial outputs so we never leave a half-written snapshot.
        if snapshot_folder.exists():
            shutil.rmtree(snapshot_folder, ignore_errors=True)
        if zip_path.exists():
            zip_path.unlink(missing_ok=True)
        return 1

    elapsed = time.monotonic() - t0

    print("Export complete.")
    print(f"  Files copied:   {len(selected)}")
    print(f"  Total size:      {human_size(total_bytes)}")
    print(f"  Snapshot folder: {snapshot_folder}")
    print(f"  Snapshot zip:    {zip_path}")
    print(f"  Elapsed:         {elapsed:.2f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
