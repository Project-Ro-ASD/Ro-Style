# Architecture

## Purpose

Ro-Style keeps the few Ro-ASD differences that the Breeze Qt style cannot express through configuration.

## Where each Ro menu property lives

| Property | Owner | How |
|---|---|---|
| Colours (menu, hover, text) | Ro-Theme | colour schemes RoLight / RoDark |
| Menu translucency | Ro-Theme | `MenuOpacity` in the system `breezerc` (Breeze setting) |
| Corner radius (16 px frame, 12 px selected item and menu buttons, concentric with the stock 4 px gap), shadow and blur region radius | **this repository** | patch 0001 |
| Control corner radius (12 px) and button inner padding (8) | **this repository** | patches 0003, 0004 |
| Menu structure, quick button row | Ro-KDE-Dolphin | Dolphin patch 0012 |
| Menu icons | Ro-Theme | `ro-icons` |

## Why a patch

Checked against Breeze 6.7.5: `kstyle/breezemetrics.h` has a fixed `Frame_FrameRadius = 5`; `Helper::renderMenuFrame`, `Helper::menuFrameRegion` and `ShadowHelper` use it for menu and tooltip frames; no `breezerc` key controls it (the key list in the plugin has MenuOpacity, shadow keys, animation keys and flags only). Kvantum was rejected in Ro-Theme-Docs APP-01.

## Downstream model

Two options were considered. (A) name-preserving rebuild of Fedora `plasma-breeze` / `plasma-breeze-qt6`: replaces the style every Plasma user loads,
needs a Ro-Repo override authorisation (`critical-desktop`) and a rebase on every Plasma update. (B) a separate style: the plugin is built under its own
name `ro6.so` with the factory key `Ro`, installed next to Breeze and selected with `widgetStyle=Ro`. B was chosen (patch 0002): no Fedora package is
replaced, no override authorisation, opt-in per user; if Ro-Theme sets `widgetStyle=Ro`, uninstalling `ro-style` falls back to the default style.

Open risk of B: KDE code that tests the style name for "breeze" will treat Ro as an unknown style. Check on the test machine (Dolphin, Kate, System Settings,
Plasma shell popups) before making Ro the default.

## Out of scope

Behaviour, accessibility, input handling, the KDE settings pages, window decoration code.
