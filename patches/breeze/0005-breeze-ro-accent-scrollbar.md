## 0005-breeze-ro-accent-scrollbar

- Upstream repository: https://invent.kde.org/plasma/breeze.git
- Upstream base tag/commit: v6.7.5 (release tarball https://download.kde.org/stable/plasma/6.7.5/breeze-6.7.5.tar.xz), applied after 0001-0004
- Fedora 44 package version checked: plasma-breeze-6.7.5-1.fc44
- Affected upstream files:
  - kstyle/breezehelper.cpp (`Helper::scrollBarHandleColor`: the idle handle colour)
- Layer: widget style drawing only (no KIO, file operation or settings logic)
- Reason (Ro-ASD): Ro-Theme-Docs APP-20a (decided 2026-10-23 after a side by side prototype comparison). The idle scroll bar handle uses the accent colour (75 %), the same language as the Plasma style scroll bar (PST-19). Upstream uses 50 % of the window text and switches to the accent only on hover or focus.
- Override considered: yes. `breezerc` has no setting for it (checked against the 6.7.5 sources).
- Upstreamable: no, design-specific.
- Verification: applies after 0001-0004; `ro6.so` built in a Fedora 44 container and rendered in a PySide6 gallery next to stock Breeze and Ro 0.1.1, dark and light (Ro-Theme-Docs APP-20a screenshots). Real Dolphin check by the maintainer pending.
- Upgrade risk: low; one colour in one function.
