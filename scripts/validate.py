#!/usr/bin/env python3
"""Ro-Style repository contract validator."""
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
COMPONENT = "ro-style"
errors = []

for rel in ["README.md", "VERSION", "AGENTS.md", "LICENSE", ".roasd/component.json", ".roasd/upstreams.json",
            "docs/ARCHITECTURE.md", "docs/PATCH-PROVENANCE-TEMPLATE.md", "packaging/fedora/ro-style.spec", "tests/check-spec.sh"]:
    if not (ROOT / rel).exists():
        errors.append(f"missing required file: {rel}")

try:
    meta = json.loads((ROOT / ".roasd" / "component.json").read_text())
    if meta.get("component_type") != "component":
        errors.append("component_type must be 'component'")
    if meta.get("component") != COMPONENT:
        errors.append(f"component must be '{COMPONENT}'")
except Exception as exc:
    errors.append(f"invalid component metadata: {exc}")

known = set()
try:
    known = set(json.loads((ROOT / ".roasd" / "upstreams.json").read_text()).get("projects", {}))
    if not known:
        errors.append("upstreams.json must list at least one project")
except Exception as exc:
    errors.append(f"invalid upstream metadata: {exc}")

version = (ROOT / "VERSION").read_text().strip() if (ROOT / "VERSION").exists() else ""
if not re.fullmatch(r"\d+\.\d+\.\d+", version):
    errors.append("VERSION must contain a semantic version such as 0.1.0")

patches_dir = ROOT / "patches"
for patch in sorted(patches_dir.rglob("*.patch")):
    rel = patch.relative_to(ROOT)
    if patch.parent.parent != patches_dir or patch.parent.name not in known:
        errors.append(f"{rel}: patch must live in patches/<known upstream project>/")
    if not re.fullmatch(r"\d{4}-[a-z0-9][a-z0-9-]*\.patch", patch.name):
        errors.append(f"{rel}: name must look like 0001-breeze-short-description.patch")
    if not patch.with_suffix(".md").exists():
        errors.append(f"{rel}: missing provenance note {patch.with_suffix('.md').name}")

for hit in ROOT.rglob("breezestyle.cpp"):
    if ".work" not in hit.parts and ".git" not in hit.parts:
        errors.append(f"{hit.relative_to(ROOT)}: looks like vendored upstream source")
for pattern in ("*.orig", "*.rej", "*.rpm", "*.so"):
    for hit in ROOT.rglob(pattern):
        if ".work" not in hit.parts and ".git" not in hit.parts:
            errors.append(f"{hit.relative_to(ROOT)}: build or patch leftover must not be committed")

if errors:
    print("validation failed:")
    for e in errors:
        print(f"- {e}")
    sys.exit(1)
print("Ro-Style repository contract: OK")
