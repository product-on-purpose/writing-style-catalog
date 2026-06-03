#!/usr/bin/env bash
# build-release.sh - package the installable plugin into a release ZIP.
#
# Produces dist/writing-style-catalog-v<version>.zip with these members staged
# at the ARCHIVE ROOT (no wrapper directory):
#   .claude-plugin/  skills/  taxonomy/  README.md  LICENSE  NOTICE  CHANGELOG.md
#
# taxonomy/ ships because skills/writing-instruction-builder/scripts/build-instruction.py
# reads REPO_ROOT/taxonomy at runtime (REPO_ROOT = parents[3] of the script), so a
# flat root is required: after unzip, parents[3] must land on the unzip dir where
# taxonomy/ sits. Any wrapper directory would push parents[3] one level too high.
#
# Usage:  ./scripts/build-release.sh <version>     e.g. ./scripts/build-release.sh 0.2.0
set -euo pipefail

VERSION="${1:?usage: build-release.sh <version>}"
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_ROOT"

NAME="writing-style-catalog-v${VERSION}"
DIST="${REPO_ROOT}/dist"
STAGE="${DIST}/${NAME}"
ZIP="${DIST}/${NAME}.zip"

MEMBERS=(.claude-plugin skills taxonomy README.md LICENSE NOTICE CHANGELOG.md)

rm -rf "$STAGE" "$ZIP" "${ZIP}.sha256"
mkdir -p "$STAGE"

for m in "${MEMBERS[@]}"; do
  if [[ ! -e "$m" ]]; then
    echo "::error::release member not found: $m" >&2
    exit 1
  fi
  cp -R "$m" "$STAGE/"
done

# Drop Python bytecode caches so the archive is reproducible and lean.
find "$STAGE" -type d -name "__pycache__" -prune -exec rm -rf {} + 2>/dev/null || true

# Zip from inside the stage dir so the archive root is flat.
( cd "$STAGE" && zip -r -q "$ZIP" . )

# Checksum + manifest.
( cd "$DIST" && sha256sum "${NAME}.zip" > "${NAME}.zip.sha256" )
( cd "$STAGE" && find . -type f | sed 's|^\./||' | sort > "${DIST}/manifest.txt" )

rm -rf "$STAGE"

echo "Built: ${ZIP}"
echo "       ${ZIP}.sha256"
echo "       ${DIST}/manifest.txt"
