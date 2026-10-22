## 0001-breeze-menu-frame-radius

- Upstream repository: https://invent.kde.org/plasma/breeze.git
- Upstream base tag/commit: v6.7.5 (release tarball https://download.kde.org/stable/plasma/6.7.5/breeze-6.7.5.tar.xz)
- Fedora 44 package version checked: plasma-breeze-6.7.5-1.fc44 (the style plugin ships in plasma-breeze-qt6)
- Affected upstream files:
  - kstyle/breezemetrics.h (new `Menu_FrameRadius = 16`, `Menu_ItemRadius = 12`; `Menu_FrameWidth` stays 0)
  - kstyle/breezehelper.cpp and .h (`renderMenuFrame` and `menuFrameRegion` use the menu radius; `renderFocusRect` takes an optional radius; `renderButtonFrame` uses `Menu_ItemRadius` for `menuButton`)
  - kstyle/breezestyle.cpp (the selected menu item passes `Menu_ItemRadius`; tool buttons inside a menu are marked `menuButton`)
  - kstyle/breezeshadowhelper.cpp (shadow tiles use the menu radius)
- Layer: widget style drawing only (no KIO, file operation or settings logic)
- Reason (Ro-ASD): Ro-Theme radius rule for popups and menus (docs TOK-02i); tried 12 px on the maintainer's machine and asked for rounder, so 16 px for the frame. Breeze draws every menu, context menu and tooltip frame with the fixed `Frame_FrameRadius = 5` and offers no setting for it. The selected item and the menu tool buttons take 12 px: the gap between the frame and the items is `PM_MenuHMargin` = `MenuItem_HighlightGap` = 4 px, so 16 - 4 = 12 makes them concentric and the item highlight stays inside the corners without extra padding (a first version with 6 px extra padding left the items too far from the frame). The blur region and the shadow follow the frame radius so the corners are not square under the translucent menu.
- Override considered: yes. `breezerc` has no radius key (checked against the 6.7.5 sources and the installed plugin); Kvantum was rejected in Ro-Theme-Docs APP-01.
- Upstreamable: no, design-specific.
- Verification: patch applies to the 6.7.5 tarball (`git apply --check`); `breeze6.so` built in a Fedora 44 container and loaded through `QT_PLUGIN_PATH` in a Qt test menu: first version (12 px) checked in real Dolphin on Wayland by the maintainer: rounded frame and tooltip, item highlight inside. The 16/12 version (stock 4 px gap): Qt replica next to stock Breeze, maintainer review pending.
- Upgrade risk: low to medium. Re-check `renderMenuFrame`, `menuFrameRegion`, `createShadowTiles` and `Menu_FrameWidth` users (`PM_MenuPanelWidth`) on every Plasma release. Tooltips use `renderMenuFrame` and the same shadow tiles, so they get the same radius too.
