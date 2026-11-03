#!/usr/bin/env bash
# Every patch applies, in order, to the upstream tarball named in .roasd/upstreams.json.
# Same strictness as rpmbuild %autosetup (patch --fuzz=0): a patch that only applies with fuzz fails here.
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
  patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f --dry-run < "$p" && patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f < "$p"
done
echo "all patches apply"
