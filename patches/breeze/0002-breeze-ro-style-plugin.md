## 0002-breeze-ro-style-plugin

- Upstream repository: https://invent.kde.org/plasma/breeze.git
- Upstream base tag/commit: v6.7.5 (release tarball https://download.kde.org/stable/plasma/6.7.5/breeze-6.7.5.tar.xz), applied after 0001
- Fedora 44 package version checked: plasma-breeze-6.7.5-1.fc44
- Affected upstream files:
  - kstyle/CMakeLists.txt (the plugin target is `ro6` instead of `breeze6`; installs `ro.themerc`)
  - kstyle/breeze.json (factory key `Ro`)
  - kstyle/breezestyleplugin.cpp (`create("ro")`, `keys()` returns `Ro`)
  - kstyle/ro.themerc (new: style entry for System Settings, reuses the Breeze settings page)
- Layer: build and plugin metadata only (the style code is unchanged by this patch)
- Reason (Ro-ASD): ship the Ro changes as a separate style named "Ro" next to Breeze instead of replacing Fedora's `plasma-breeze-qt6`: no override authorisation, opt-in via `widgetStyle=Ro`, Fedora's Breeze stays untouched.
- Override considered: yes. Replacing `breeze6.so` needs a name-preserving rebuild of a core package (critical-desktop risk class in Ro-Repo).
- Upstreamable: no.
- Verification: `make ro6` in a Fedora 44 container; `QStyleFactory.keys()` lists `Ro` next to `Breeze`; a Qt test menu with `QT_STYLE_OVERRIDE=Ro` draws the Ro menu frame. Real Dolphin and Plasma shell checks pending.
- Upgrade risk: low (CMake and metadata). KDE code that tests the style name for "breeze" treats Ro as unknown; check on the test machine before making Ro the default style.
