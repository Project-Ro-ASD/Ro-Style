## 0012-breeze-ro-plain-header

- Upstream repository: https://invent.kde.org/plasma/breeze.git
- Upstream base tag/commit: v6.7.5 (release tarball https://download.kde.org/stable/plasma/6.7.5/breeze-6.7.5.tar.xz), applied after 0001-0011
- Fedora 44 package version checked: plasma-breeze-6.7.5-1.fc44
- Affected upstream files:
  - kstyle/breezestyle.cpp (`Style::drawHeaderSectionControl`: the section fill and the section separators; `Style::drawHeaderEmptyAreaControl`: the empty area fill)
- Layer: widget style drawing only (no KIO, file operation or settings logic)
- Reason (Ro-ASD): Ro-Theme-Docs APP-25 (decided 2026-10-23 after a side by side prototype comparison). The table header sits on the list base colour instead of the button colour, and the vertical separators between header sections are gone; the bottom outline of a horizontal header stays. Upstream paints the header with the button colour and draws a separator on the trailing edge of every section but the last.
- Override considered: yes. `breezerc` has no setting for it (checked against the 6.7.5 sources).
- Upstreamable: no, design-specific.
- Verification: applies after 0001-0011 (checked with `git apply --check` / `git apply` on a clean Breeze 6.7.5 tree carrying 0001-0011); the difference was approved in the side by side prototype comparison behind APP-25. Real Dolphin check by the maintainer pending.
- Upgrade risk: low; one colour and one disabled block in the header painting. The `if (false)` block also lets the vertical-header separator branch run for horizontal headers, which only repeats the bottom outline already drawn there; keep it that way, it is what the approved prototype renders.