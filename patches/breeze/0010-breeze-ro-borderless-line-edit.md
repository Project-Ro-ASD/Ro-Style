## 0010-breeze-ro-borderless-line-edit

- Upstream repository: https://invent.kde.org/plasma/breeze.git
- Upstream base tag/commit: v6.7.5 (release tarball https://download.kde.org/stable/plasma/6.7.5/breeze-6.7.5.tar.xz), applied after 0001-0009
- Fedora 44 package version checked: plasma-breeze-6.7.5-1.fc44
- Affected upstream files:
  - kstyle/breezestyle.cpp (`Style::drawFrameLineEditPrimitive`: the line edit frame outline)
- Layer: widget style drawing only (no KIO, file operation or settings logic)
- Reason (Ro-ASD): Ro-Theme-Docs APP-23 (decided 2026-10-23 after a side by side prototype comparison). An idle line edit is borderless: the outline falls back to the field colour while the field is not hovered, not focused and not animating. Upstream draws a frame outline on the idle field as well; hover, focus and the focus/hover animation keep their outline.
- Override considered: yes. `breezerc` has no setting for it (checked against the 6.7.5 sources).
- Upstreamable: no, design-specific.
- Verification: applies after 0001-0009 (checked with `git apply --check` / `git apply` on a clean Breeze 6.7.5 tree carrying 0001-0009); the difference was approved in the side by side prototype comparison behind APP-23. Real Dolphin check by the maintainer pending.
- Upgrade risk: low; one block in one function. Check that upstream still routes the idle line edit outline through `frameOutlineColor` in `Style::drawFrameLineEditPrimitive`.