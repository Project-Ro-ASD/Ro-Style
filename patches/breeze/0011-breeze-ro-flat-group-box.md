## 0011-breeze-ro-flat-group-box

- Upstream repository: https://invent.kde.org/plasma/breeze.git
- Upstream base tag/commit: v6.7.5 (release tarball https://download.kde.org/stable/plasma/6.7.5/breeze-6.7.5.tar.xz), applied after 0001-0010
- Fedora 44 package version checked: plasma-breeze-6.7.5-1.fc44
- Affected upstream files:
  - kstyle/breezestyle.cpp (`Style::drawFrameGroupBoxPrimitive`: the group box frame; `Style::groupBoxSubControlRect`: the title geometry and font; `Style::drawGroupBoxComplexControl`: the label font)
- Layer: widget style drawing only (no KIO, file operation or settings logic)
- Reason (Ro-ASD): Ro-Theme-Docs APP-24 (decided 2026-10-23 after a side by side prototype comparison). A group box is frameless and its title is bold, one point larger and left aligned, whether or not the group box is flat; a check box in the title keeps the plain font. Upstream frames every non-flat group box, centres the title and applies the larger bold font only to a flat title without a check box.
- Override considered: yes. `breezerc` has no setting for it (checked against the 6.7.5 sources).
- Upstreamable: no, design-specific.
- Verification: applies after 0001-0010 (checked with `git apply --check` / `git apply` on a clean Breeze 6.7.5 tree carrying 0001-0010); the difference was approved in the side by side prototype comparison behind APP-24. Real Dolphin check by the maintainer pending.
- Upgrade risk: medium; the title font condition exists twice (`groupBoxSubControlRect` and `drawGroupBoxComplexControl`) and must stay in sync, and `drawFrameGroupBoxPrimitive` returns before its upstream frame code, which becomes unreachable. Check the group box title layout on the next Breeze release.