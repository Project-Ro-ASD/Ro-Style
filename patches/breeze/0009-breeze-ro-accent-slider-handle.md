## 0009-breeze-ro-accent-slider-handle

- Upstream repository: https://invent.kde.org/plasma/breeze.git
- Upstream base tag/commit: v6.7.5 (release tarball https://download.kde.org/stable/plasma/6.7.5/breeze-6.7.5.tar.xz), applied after 0001-0008
- Fedora 44 package version checked: plasma-breeze-6.7.5-1.fc44
- Affected upstream files:
  - kstyle/breezestyle.cpp (`Style::drawSliderComplexControl`: the slider handle fill and render call; `Style::drawDialComplexControl`: the dial handle render call)
- Layer: widget style drawing only (no KIO, file operation or settings logic)
- Reason (Ro-ASD): Ro-Theme-Docs APP-22 (decided 2026-10-23 after a side by side prototype comparison). The slider handle is filled with the accent colour and has no drop shadow; the outline is drawn only while the handle is hovered or the slider has focus. The dial handle keeps its button colour fill but follows the same shadow and outline rule. Upstream fills the handle with the button colour, always drops a shadow and draws the outline from `sliderOutlineColor`.
- Override considered: yes. `breezerc` has no setting for it (checked against the 6.7.5 sources).
- Upstreamable: no, design-specific.
- Verification: applies after 0001-0008 (checked with `git apply --check` / `git apply` on a clean Breeze 6.7.5 tree carrying 0001-0008); the difference was approved in the side by side prototype comparison behind APP-22. Real Dolphin check by the maintainer pending.
- Upgrade risk: low; one fill colour and one render call in two functions. Check `Helper::renderSliderHandle` on the next Breeze release: its `sunken` parameter is what suppresses the drop shadow here.