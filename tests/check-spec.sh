#!/usr/bin/env bash
# The spec lists every patch in order, matches VERSION and the pinned Breeze version, and the tarball checksum is pinned.
set -euo pipefail
cd "$(dirname "$0")/.."
spec=packaging/fedora/ro-style.spec
version=$(tr -d '[:space:]' < VERSION)
spec_version=$(awk '/^Version:/ { print $2; exit }' "$spec")
[[ "$spec_version" == "$version" ]] || { echo "spec Version $spec_version != VERSION $version"; exit 1; }

breeze=$(awk '/^%global breeze_version/ { print $3; exit }' "$spec")
tag=$(python3 -c "import json;print(json.load(open('.roasd/upstreams.json'))['projects']['breeze']['base_tag'])")
[[ "v$breeze" == "$tag" ]] || { echo "spec breeze_version v$breeze != upstreams base_tag $tag"; exit 1; }
sha=$(python3 -c "import json;print(json.load(open('.roasd/upstreams.json'))['projects']['breeze']['tarball_sha256'])")
[[ "$sha" =~ ^[0-9a-f]{64}$ ]] || { echo "tarball_sha256 is not a sha256"; exit 1; }

n=0
for p in patches/breeze/*.patch; do
  b=$(basename "$p")
  grep -q "^Patch$n:[[:space:]]*$b\$" "$spec" || { echo "spec does not list $b as Patch$n"; exit 1; }
  n=$((n + 1))
done
[[ "$(grep -c '^Patch[0-9]*:' "$spec")" -eq "$n" ]] || { echo "spec lists patches that do not exist"; exit 1; }
grep -q '^%changelog' "$spec"
echo "Spec check passed."
