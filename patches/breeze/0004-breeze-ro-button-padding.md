## 0004-breeze-ro-button-padding

- Upstream repository: https://invent.kde.org/plasma/breeze.git
- Upstream base tag/commit: v6.7.5 (release tarball https://download.kde.org/stable/plasma/6.7.5/breeze-6.7.5.tar.xz), applied after 0001-0003
- Fedora 44 package version checked: plasma-breeze-6.7.5-1.fc44
- Affected upstream files:
  - kstyle/breezemetrics.h (`Button_MarginWidth` 6 -> 8)
- Layer: widget style drawing constants only
- Reason (Ro-ASD): Ro-Theme-Docs APP-19 (decided 2026-10-23): only the button inner padding changes (token `sm` 8), layout margins and spacing stay at Breeze's values so application layouts and window sizes do not change. With the 12 px corner the buttons look better with a little more room inside. The constant is used for both directions (buttons grow a few pixels in width and height); dialogs with tight layouts should be checked.
- Override considered: yes. No setting exists for it in `breezerc`.
- Upstreamable: no, design-specific.
- Verification: built together with 0003 in a Fedora 44 container; gallery screenshot next to stock Breeze (Ro-Theme-Docs APP-19, APP-17). Real Dolphin, Kate and System Settings check pending.
- Upgrade risk: low.
