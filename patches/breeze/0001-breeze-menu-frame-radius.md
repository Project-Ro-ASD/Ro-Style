## 0001-breeze-menu-frame-radius

- Upstream repository: https://invent.kde.org/plasma/breeze.git
- Upstream base tag/commit: v6.7.5 (release tarball https://download.kde.org/stable/plasma/6.7.5/breeze-6.7.5.tar.xz)
- Fedora 44 package version checked: plasma-breeze-6.7.5-1.fc44 (the style plugin ships in plasma-breeze-qt6)
- Affected upstream files:
  - kstyle/breezemetrics.h (new `Menu_FrameRadius = 16`, `Menu_ItemRadius = 10`; `Menu_FrameWidth` 0 to 6)
  - kstyle/breezehelper.cpp and .h (`renderMenuFrame` and `menuFrameRegion` use the menu radius; `renderFocusRect` takes an optional radius; `renderButtonFrame` uses `Menu_ItemRadius` for `menuButton`)
  - kstyle/breezestyle.cpp (the selected menu item passes `Menu_ItemRadius`; tool buttons inside a menu are marked `menuButton`)
  - kstyle/breezeshadowhelper.cpp (shadow tiles use the menu radius)
- Layer: widget style drawing only (no KIO, file operation or settings logic)
- Reason (Ro-ASD): Ro-Theme radius rule for popups and menus (docs TOK-02i); tried 12 px on the maintainer's machine and asked for rounder, so 16 px for the frame and 10 px for the selected item. Breeze draws every menu, context menu and tooltip frame with the fixed `Frame_FrameRadius = 5` and offers no setting for it. The inner padding of 6 px keeps the item highlight inside the rounder corners; the blur region and the shadow follow the same radius so the corners are not square under the translucent menu.
- Override considered: yes. `breezerc` has no radius key (checked against the 6.7.5 sources and the installed plugin); Kvantum was rejected in Ro-Theme-Docs APP-01.
- Upstreamable: no, design-specific.
- Verification: patch applies to the 6.7.5 tarball (`git apply --check`); `breeze6.so` built in a Fedora 44 container and loaded through `QT_PLUGIN_PATH` in a Qt test menu: first version (12 px) checked in real Dolphin on Wayland by the maintainer: rounded frame and tooltip, item highlight inside. The 16/10/6 version: see README.
- Upgrade risk: low to medium. Re-check `renderMenuFrame`, `menuFrameRegion`, `createShadowTiles` and `Menu_FrameWidth` users (`PM_MenuPanelWidth`) on every Plasma release. Tooltips use `renderMenuFrame` and the same shadow tiles, so they get the same radius too.
