## 0006-breeze-ro-pill-tabs

- Upstream repository: https://invent.kde.org/plasma/breeze.git
- Upstream base tag/commit: v6.7.5 (release tarball https://download.kde.org/stable/plasma/6.7.5/breeze-6.7.5.tar.xz), applied after 0001-0005
- Fedora 44 package version checked: plasma-breeze-6.7.5-1.fc44
- Affected upstream files:
  - kstyle/breezehelper.cpp (`Helper::renderTabBarTab`: the whole tab drawing)
- Layer: widget style drawing only (no KIO, file operation or settings logic)
- Reason (Ro-ASD): Ro-Theme-Docs APP-20b (decided 2026-10-23 after a side by side prototype comparison). Tabs follow the Plasma style tab bar (PST-25): the selected tab is a neutral pill (window colour mixed with 15 % text) inset by 3 px, the other tabs have no background and a faint pill on hover. Upstream draws a framed selected tab with a 3 px accent line and darker unselected tabs. The tab widget frame is unchanged.
- Override considered: yes. `breezerc` has no setting for it (checked against the 6.7.5 sources).
- Upstreamable: no, design-specific.
- Verification: applies after 0001-0005; `ro6.so` built in a Fedora 44 container and rendered in a PySide6 gallery next to stock Breeze and Ro 0.1.1, dark and light (Ro-Theme-Docs APP-20b screenshots). Real Dolphin check by the maintainer pending.
- Upgrade risk: medium; the function body is replaced, re-check its parameters (`stateProperties` keys, `corners`) on every Plasma release.
