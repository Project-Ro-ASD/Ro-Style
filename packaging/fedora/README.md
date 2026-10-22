# Fedora packaging (not set up yet)

Planned: a new package `ro-style` (x86_64). `%prep` downloads the Fedora 44 Breeze source archive (version pinned in `.roasd/upstreams.json`), applies `patches/breeze/*.patch` and
builds only the `ro6` target; the package ships `/usr/lib64/qt6/plugins/styles/ro6.so` and `/usr/share/kstyle/themes/ro.themerc`. Build dependencies: the Breeze `kstyle` ones
(Qt6 private headers, KF6 ConfigCore/ConfigGui/GuiAddons/IconThemes/WindowSystem/ColorScheme/CoreAddons, KF6 FrameworkIntegration, ECM). Runtime: it reads `breezerc`; the
Breeze settings page comes from `plasma-breeze-qt6`, so require that package.

It does not replace any Fedora package, so no Ro-Repo `allow_fedora_override` entry is needed; Ro-Repo still has to register the component/producer. Release workflow:
modelled on Ro-KDE-Dolphin `.github/workflows/release.yml`, to be added with the package.

Build check used so far (Fedora 44 container): configure with `-DBUILD_QT5=OFF -DBUILD_TESTING=OFF`, `make ro6`.

## Rebase onto a new Fedora Plasma

`.github/workflows/upstream-weekly.yml` runs every Monday (and on demand): when Fedora's `plasma-breeze` is newer than the pinned `breeze_version`
it tries the patches on the new Breeze archive and opens an issue (once per version) saying whether they apply. The pinned version is never changed
automatically. To rebase: refresh the failing patch (if any), then change `breeze_version` in the spec and `base_tag`, `tarball` and `tarball_sha256`
in `.roasd/upstreams.json`, add a spec changelog entry, run `tests/check-spec.sh`, build in a Fedora 44 container, check the style in Dolphin, bump VERSION and release.

