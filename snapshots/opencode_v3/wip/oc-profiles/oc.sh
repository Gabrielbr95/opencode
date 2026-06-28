#!/usr/bin/env bash
# oc.sh — Git Bash shim for oc.ps1
# Forwards all arguments to oc.ps1 by absolute path.
# Usage: ~/.config/opencode/oc.sh [profile] [opencode-args...]

# Convert this script's directory to a Windows path for PowerShell.
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd -W 2>/dev/null || pwd)"

powershell.exe -NoProfile -ExecutionPolicy Bypass -File "${SCRIPT_DIR}/oc.ps1" "$@"
