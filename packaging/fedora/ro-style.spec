# Ro-Style: the Ro-ASD Qt widget style "Ro", derived from KDE Breeze.
# Built from the Breeze source archive plus the Ro patches in patches/breeze (see README.md); no Fedora package is replaced.
%global breeze_version 6.7.5

Name:           ro-style
Version:        0.1.1
Release:        1%{?dist}
Summary:        Ro-ASD Qt widget style, derived from KDE Breeze
# kstyle and libbreezecommon: GPL-2.0-or-later (some files MIT or GPL-2.0-or-later OR MIT; generated Qt files)
License:        GPL-2.0-or-later AND MIT AND LGPL-3.0-only
URL:            https://github.com/Project-Ro-ASD/Ro-Style
Source0:        https://download.kde.org/stable/plasma/%{breeze_version}/breeze-%{breeze_version}.tar.xz
# Ro patches, in order (tests/check-spec.sh checks that every patches/breeze/*.patch is listed)
Patch0:         0001-breeze-menu-frame-radius.patch
Patch1:         0002-breeze-ro-style-plugin.patch
Patch2:         0003-breeze-ro-corner-radius.patch
Patch3:         0004-breeze-ro-button-padding.patch
Patch4:         0005-breeze-ro-accent-scrollbar.patch
Patch5:         0006-breeze-ro-pill-tabs.patch
Patch6:         0007-breeze-ro-flat-buttons.patch
Patch7:         0008-breeze-ro-list-selection-radius.patch

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6ColorScheme)
BuildRequires:  cmake(KF6FrameworkIntegration)
BuildRequires:  cmake(KF6Kirigami)
BuildRequires:  cmake(KDecoration3)
BuildRequires:  gettext

# The style reads breezerc and its "Configure" page (transparency, shadows, animations) is Breeze's.
Requires:       plasma-breeze-qt6

%description
Ro is the widget style of Ro-ASD. It is KDE Breeze with a few drawing changes
that Breeze cannot be configured to do: rounder menus and tool tips (16 px
frame, 12 px selected item and menu buttons, with the shadow and the blur
region following the frame). It is a separate style plugin (ro6) next to
Breeze: select Ro in System Settings, Appearance, Application Style. It reads
the same Breeze settings file, so the menu opacity and shadow settings apply
to both styles.

%prep
%autosetup -p1 -n breeze-%{breeze_version}

%build
%cmake_kf6 \
    -DBUILD_QT5=OFF \
    -DBUILD_TESTING=OFF \
    -DWITH_DECORATIONS=OFF \
    -DWITH_WALLPAPERS=OFF \
    -DBUILD_CURSOR=OFF
%cmake_build --target ro6

%install
install -Dm0755 %{__cmake_builddir}/bin/ro6.so %{buildroot}%{_qt6_plugindir}/styles/ro6.so
install -Dm0644 kstyle/ro.themerc %{buildroot}%{_datadir}/kstyle/themes/ro.themerc

%files
%license LICENSES/*
%{_qt6_plugindir}/styles/ro6.so
%{_datadir}/kstyle/themes/ro.themerc

%changelog
* Fri Oct 23 2026 Project Ro-ASD <contact@roasd.org> - 0.1.1-1
- Controls use a 12 px corner (buttons, fields, combo boxes, tabs, frames, list
  selection; Breeze 5) and the check box corner stays 4 (patch 0003). The menu
  and tooltip frame keep 16 px / 12 px.
- Button inner padding 8 (Breeze 6) (patch 0004).

* Thu Oct 22 2026 Project Ro-ASD <contact@roasd.org> - 0.1.0-1
- First package: the Ro style (plugin ro6, style name Ro) from Breeze 6.7.5 with the menu frame (16 px) and
  plugin-name patches.
