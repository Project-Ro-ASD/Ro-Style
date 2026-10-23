## 0003-breeze-ro-corner-radius

- Upstream repository: https://invent.kde.org/plasma/breeze.git
- Upstream base tag/commit: v6.7.5 (release tarball https://download.kde.org/stable/plasma/6.7.5/breeze-6.7.5.tar.xz), applied after 0001 and 0002
- Fedora 44 package version checked: plasma-breeze-6.7.5-1.fc44 (the style plugin ships in plasma-breeze-qt6)
- Affected upstream files:
  - kstyle/breezemetrics.h (`Frame_FrameRadius` 5 -> 12, `CheckBox_Radius` = `Frame_FrameRadius - 1` -> 4)
- Layer: widget style drawing constants only (no KIO, file operation or settings logic)
- Reason (Ro-ASD): Ro-Theme-Docs APP-17 (decided 2026-10-23, 12 px). Breeze draws buttons, line edits, combo boxes, tabs, frames and list selections with the one constant `Frame_FrameRadius = 5`. Ro's Plasma style already uses the `md` radius 12 for buttons and fields (PST-22, PST-23); Qt applications looked sharp next to Plasma popups. The menu and tooltip frame keep the radius of patch 0001 (`Menu_FrameRadius` 16, `Menu_ItemRadius` 12), which does not depend on this constant. The check box keeps 4 (token `xs`): `Frame_FrameRadius - 1` would make the 20 px box nearly round at 12. List and tree rows share the constant and become 12 too; the `sm` 8 of PST-26 needs a per-control radius (APP-20f, not part of this patch).
- Override considered: yes. `breezerc` has no radius key (checked against the 6.7.5 sources); Kvantum was rejected in Ro-Theme-Docs APP-01.
- Upstreamable: no, design-specific.
- Verification: patch applies after 0001 and 0002 to the 6.7.5 tarball; `ro6.so` built in a Fedora 44 container and rendered with a small PySide6 gallery (buttons, fields, check boxes, tabs, list, group box, menu) next to stock Breeze in dark and light (Ro-Theme-Docs APP-17 screenshots). Real Dolphin check by the maintainer pending.
- Upgrade risk: low. One constant and one derived constant; re-check that Breeze has not started deriving other radii from `Frame_FrameRadius` (tab bar overlap code uses it for geometry, `breezestyle.cpp` tab base).
