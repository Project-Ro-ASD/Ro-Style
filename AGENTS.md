# AGENTS.md

This repository holds the patches that turn KDE Breeze's Qt widget style into Ro-ASD's own widget style "Ro" (a derived work: Breeze's copyright and licence notices stay).

## Read first

Before making any implementation change, read README.md, docs/ARCHITECTURE.md, docs/PATCH-PROVENANCE-TEMPLATE.md, .roasd/component.json and .roasd/upstreams.json.

## Scope

This repository may own only Breeze **style drawing** changes (`kstyle/`) that Ro-Theme cannot express as configuration.

Do not move these responsibilities into this repository:
- colour schemes, Plasma themes, icon themes, cursors, wallpapers, `breezerc` defaults: Ro-Theme
- window decoration (Aurorae): Ro-Theme
- Dolphin layout and context menu structure: Ro-KDE-Dolphin
- generic desktop/system defaults: ro-asd-defaults

## Working rules

- Never vendor a full KDE source tree into this repository.
- Prefer `breezerc` configuration (Ro-Theme) over a source patch; prefer a narrow patch over a fork.
- Patches stay in `kstyle/` drawing code. Do not change setting semantics, accessibility or input behaviour.
- One patch should have one reason; every patch needs a provenance note (docs/PATCH-PROVENANCE-TEMPLATE.md).
- Do not commit build directories, `.so` files, RPMs, `.orig`/`.rej` files.
- Production packaging is a new package `ro-style` (plugin `ro6.so`, style name Ro) built from the Breeze source archive plus these patches; it does not replace any Fedora package. No signing keys here.
- Never remove or rewrite Breeze copyright/licence headers; describe the work as Breeze-derived.

## Git workflow

Do not work directly on main. Use feature/, patch/ or docs/ branches, open a pull request, keep commits scoped and use conventional prefixes.

## Validation

    python3 scripts/validate.py
    bash tests/check-patches.sh
