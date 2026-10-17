#!/usr/bin/env bash
# Usage: bash scripts/scan.sh before|after
# Runs both Snyk scans (dependencies + Docker image) for one version of the app
# and saves the JSON reports into results/.
set -u

VERSION="${1:-}"
if [ "$VERSION" != "before" ] && [ "$VERSION" != "after" ]; then
  echo "Usage: bash scripts/scan.sh before|after"
  exit 1
fi

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
mkdir -p "$ROOT/results"
cd "$ROOT/$VERSION"

echo "=== [$VERSION] 1/3  Installing dependencies from lockfile ==="
npm ci --no-audit --no-fund

echo "=== [$VERSION] 2/3  Snyk Open Source scan (dependencies) ==="
snyk test --json-file-output="$ROOT/results/$VERSION-deps.json"

echo "=== [$VERSION] 3/3  Snyk Container scan (Docker image) ==="
docker build -t "snyk-demo:$VERSION" . || { echo "Docker build failed - fix it, then re-run."; exit 1; }
snyk container test "snyk-demo:$VERSION" --file=Dockerfile \
  --json-file-output="$ROOT/results/$VERSION-image.json"

echo
echo "Done. Reports saved in results/$VERSION-deps.json and results/$VERSION-image.json"
