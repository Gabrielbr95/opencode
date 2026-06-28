<#
.SYNOPSIS
    Launch opencode with a named permission profile.

.DESCRIPTION
    Reads oc-profiles.jsonc, looks up the requested profile, serializes it to
    OPENCODE_PERMISSION, then spawns opencode with all remaining args forwarded.

    Profile definitions live in oc-profiles.jsonc in the same directory as this
    script. Edit that file to add or tune profiles — no changes here needed.

.PARAMETER Profile
    Name of the profile to activate (default: "normal").
    Must match a top-level key in oc-profiles.jsonc.
    Pass "--" before opencode flags if the first flag looks like a profile name.

.EXAMPLE
    ~/.config/opencode/oc.ps1
    # Starts opencode with "normal" profile (no overrides).

.EXAMPLE
    ~/.config/opencode/oc.ps1 yolo
    # Starts opencode with "yolo" profile (all tools allowed).

.EXAMPLE
    ~/.config/opencode/oc.ps1 yolo --help
    # Starts opencode --help with yolo profile active.

.EXAMPLE
    ~/.config/opencode/oc.ps1 --help
    # Passes --help directly to opencode (no profile arg detected).
#>

param(
    [Parameter(Position = 0)]
    [string]$Profile = "normal",

    [Parameter(ValueFromRemainingArguments)]
    [string[]]$RemainingArgs
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

# --- Locate profile file ---
$scriptDir   = Split-Path -Parent $MyInvocation.MyCommand.Path
$profileFile = Join-Path $scriptDir "oc-profiles.jsonc"

if (-not (Test-Path -LiteralPath $profileFile)) {
    Write-Error "Profile file not found: $profileFile"
    exit 1
}

# --- Handle the case where Profile looks like a flag, not a profile name ---
# If the first positional arg starts with "-", treat it as an opencode arg,
# fall back to "normal", and prepend it back to RemainingArgs.
if ($Profile.StartsWith("-")) {
    $RemainingArgs = @($Profile) + @($RemainingArgs | Where-Object { $_ -ne $null })
    $Profile = "normal"
}

# --- Read and strip JSONC comments ---
# Strip // line comments (Decision 002: JSONC comments must be stripped before JSON parse).
$raw = Get-Content -LiteralPath $profileFile -Raw
$stripped = $raw -replace '(?m)//[^\n]*', ''

# --- Parse JSON ---
try {
    $profiles = $stripped | ConvertFrom-Json
} catch {
    Write-Error "Failed to parse $profileFile : $_"
    exit 1
}

# --- Look up profile ---
if (-not ($profiles.PSObject.Properties.Name -contains $Profile)) {
    $available = ($profiles.PSObject.Properties.Name) -join ", "
    Write-Error "Profile '$Profile' not found in $profileFile. Available: $available"
    exit 1
}

$profileData = $profiles.$Profile

# --- Serialize to JSON and set env var ---
# ConvertTo-Json depth 10 handles nested permission objects.
$permissionJson = $profileData | ConvertTo-Json -Depth 10 -Compress

# Empty profile (like "normal") serializes to "null" or "{}"; pass empty string
# so OPENCODE_PERMISSION is set but effectively a no-op.
if ($permissionJson -eq $null -or $permissionJson -eq "null") {
    $permissionJson = "{}"
}

$env:OPENCODE_PERMISSION = $permissionJson

# --- Launch opencode ---
$opencode = "opencode"

$forwardArgs = @($RemainingArgs | Where-Object { $_ -ne $null })

if ($forwardArgs.Count -gt 0) {
    & $opencode @forwardArgs
} else {
    & $opencode
}

exit $LASTEXITCODE
