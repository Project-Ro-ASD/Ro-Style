#!/usr/bin/env bash
# Every patch applies, in order, to the upstream tarball named in .roasd/upstreams.json.
set -euo pipefail
cd "$(dirname "$0")/.."
url=$(python3 -c "import json;print(json.load(open('.roasd/upstreams.json'))['projects']['breeze']['tarball'])")
work=$(mktemp -d); trap 'rm -rf "$work"' EXIT
curl -fsSL -o "$work/src.tar.xz" "$url"
tar -xf "$work/src.tar.xz" -C "$work"
src=$(find "$work" -maxdepth 1 -mindepth 1 -type d | head -1)
cd "$src"; git init -q
for p in "$OLDPWD"/patches/breeze/*.patch; do
  echo "applying $(basename "$p")"
  git apply --check "$p" && git apply "$p"
done
echo "all patches apply"
