## 0007-breeze-ro-flat-buttons

- Upstream repository: https://invent.kde.org/plasma/breeze.git
- Upstream base tag/commit: v6.7.5 (release tarball https://download.kde.org/stable/plasma/6.7.5/breeze-6.7.5.tar.xz), applied after 0001-0006
- Fedora 44 package version checked: plasma-breeze-6.7.5-1.fc44
- Affected upstream files:
  - kstyle/breezehelper.cpp (`Helper::renderButtonFrame`: idle outline and drop shadow)
- Layer: widget style drawing only (no KIO, file operation or settings logic)
- Reason (Ro-ASD): Ro-Theme-Docs APP-20d (decided 2026-10-23 after a side by side prototype comparison). Idle push buttons are a plain filled surface like the Plasma style button (PST-23): no outline and no drop shadow. Hover, focus, the default button and checked buttons keep their outline.
- Override considered: yes. `breezerc` has no setting for it (checked against the 6.7.5 sources).
- Upstreamable: no, design-specific.
- Verification: applies after 0001-0006; `ro6.so` built in a Fedora 44 container and rendered in a PySide6 gallery next to stock Breeze and Ro 0.1.1, dark and light (Ro-Theme-Docs APP-20d screenshots). Real Dolphin check by the maintainer pending.
- Upgrade risk: low.
