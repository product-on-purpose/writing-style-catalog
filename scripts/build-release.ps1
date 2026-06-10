<#
.SYNOPSIS
  Package the installable plugin into a release ZIP (Windows / PowerShell parity
  with build-release.sh).

.DESCRIPTION
  Produces dist/writing-style-catalog-v<version>.zip with .claude-plugin/, library.json,
  skills/, taxonomy/, README.md, LICENSE, NOTICE, and CHANGELOG.md staged at the ARCHIVE ROOT
  (no wrapper directory). taxonomy/ ships because build-instruction.py reads
  REPO_ROOT/taxonomy at runtime (parents[3]); the flat root keeps that path correct
  after unzip.

.EXAMPLE
  ./scripts/build-release.ps1 0.2.0
#>
param(
  [Parameter(Mandatory = $true, Position = 0)]
  [string]$Version
)

$ErrorActionPreference = "Stop"
$RepoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
Set-Location $RepoRoot

$Name = "writing-style-catalog-v$Version"
$Dist = Join-Path $RepoRoot "dist"
$Stage = Join-Path $Dist $Name
$Zip = Join-Path $Dist "$Name.zip"

$Members = @(".claude-plugin", "library.json", "skills", "taxonomy", "README.md", "LICENSE", "NOTICE", "CHANGELOG.md")

if (Test-Path $Stage) { Remove-Item -Recurse -Force $Stage }
if (Test-Path $Zip) { Remove-Item -Force $Zip }
if (Test-Path "$Zip.sha256") { Remove-Item -Force "$Zip.sha256" }
New-Item -ItemType Directory -Force -Path $Stage | Out-Null

foreach ($m in $Members) {
  if (-not (Test-Path $m)) { throw "release member not found: $m" }
  Copy-Item -Recurse -Force -Path $m -Destination $Stage
}

# Drop Python bytecode caches.
Get-ChildItem -Path $Stage -Recurse -Directory -Filter "__pycache__" |
  ForEach-Object { Remove-Item -Recurse -Force $_.FullName }

# Zip from the stage root so the archive root is flat.
Compress-Archive -Path (Join-Path $Stage "*") -DestinationPath $Zip -Force

# Checksum + manifest.
$hash = (Get-FileHash -Algorithm SHA256 $Zip).Hash.ToLower()
"$hash  $Name.zip" | Set-Content -NoNewline -Path "$Zip.sha256"
Get-ChildItem -Path $Stage -Recurse -File |
  ForEach-Object { $_.FullName.Substring($Stage.Length + 1).Replace("\", "/") } |
  Sort-Object |
  Set-Content -Path (Join-Path $Dist "manifest.txt")

Remove-Item -Recurse -Force $Stage

Write-Output "Built: $Zip"
Write-Output "       $Zip.sha256"
Write-Output "       $(Join-Path $Dist 'manifest.txt')"
