# Ro-Style

Ro-ASD'nin **Qt widget stili: "Ro"**. KDE Breeze'in türevidir; Ro'nun köşe, boşluk ve saydamlık dilini Breeze'in ayarlarla yapamadığı yerlerde
uygular. Sistem Ayarları, Uygulama Stili listesinde **Ro** adıyla, Breeze'in yanında ayrı bir stil olarak görünür; Fedora'nın Breeze paketini
değiştirmez.

## Köken ve lisans

Ro stili sıfırdan yazılmış bir stil değildir: KDE Breeze'in Qt widget stilinden (`kstyle`, GPL-2.0-or-later, © KDE katkıcıları) türetilir. Breeze'in
telif ve lisans başlıkları korunur; Ro-ASD'nin değişiklikleri aynı lisansla (GPL-2.0-or-later, Ro-Theme GPL-3.0-or-later ile uyumlu) yayınlanır.
Depo Breeze kaynağını içermez; yalnızca Ro yamalarını tutar, paket derlenirken Breeze kaynak arşivine uygulanır.

## Ne değiştirir?

| Yama | Ne yapar |
|---|---|
| `0001-breeze-menu-frame-radius` | Menü ve araç ipucu çerçevesi, gölgesi ve bulanıklık bölgesi 16 px köşe; seçili satır ve menüdeki araç düğmeleri 12 px (16 − 4 px stok boşluk, eşmerkezli) |
| `0002-breeze-ro-style-plugin` | Eklentiyi ayrı bir stil yapar: `ro6.so`, stil adı **Ro**, `ro.themerc` |
| `0003-breeze-ro-corner-radius` | Düğme, giriş alanı, açılır kutu, sekme, çerçeve ve liste seçimi köşesi 12 px (Breeze 5); onay kutusu köşesi 4 |
| `0004-breeze-ro-button-padding` | Düğme iç boşluğu 8 (Breeze 6) |
| `0005-breeze-ro-accent-scrollbar` | Kaydırma çubuğu tutamağı durgunken de vurgu renginde |
| `0006-breeze-ro-pill-tabs` | Etkin sekme nötr hap, diğer sekmeler zeminsiz |
| `0007-breeze-ro-flat-buttons` | Durgun düğmede kenarlık ve gölge yok |
| `0008-breeze-ro-list-selection-radius` | Liste ve ağaç seçim köşesi 8 |
| `0009-breeze-ro-accent-slider-handle` | Sürgü tutamağı vurgu renginde ve gölgesiz; kenar yalnız üzerine gelince veya odakta |
| `0010-breeze-ro-borderless-line-edit` | Giriş alanı durgunken kenarlıksız |
| `0011-breeze-ro-flat-group-box` | Grup kutusu çerçevesiz, kalın başlığı solda |
| `0012-breeze-ro-plain-header` | Tablo başlığı liste zemininde, dikey ayraçsız |

Ayarlar Breeze ile aynı `breezerc`'den okunur: `MenuOpacity` (menü saydamlığı), gölge ve animasyon anahtarları Ro-Theme'in `/etc/xdg/breezerc`
varsayılanlarından gelir; Sistem Ayarları'ndaki Breeze "Yapılandır" sayfası Ro stilinde de açılır.

## Bu depo ne değildir?

- Breeze'in fork'u değildir; KDE kaynak ağacı vendörlenmez.
- Renk şemaları, Plasma teması, ikon ve imleç temaları, `breezerc` varsayılanları: `Ro-Theme`.
- Dolphin düzeni ve sağ tık menüsü yapısı: `Ro-KDE-Dolphin`.

## Deneme (kurmadan)

Derlenmiş `ro6.so` bir klasöre `styles/ro6.so` olarak konup yalnız bir uygulamada denenebilir (önce açık Dolphin'i kapatın):

    QT_STYLE_OVERRIDE=Ro QT_PLUGIN_PATH=/yol/plugins dolphin

Kalıcı kullanım: `kdeglobals` içinde `[KDE] widgetStyle=Ro` (Ro-Theme varsayılanlarına paket kurulunca eklenir).

## Yapı

```text
.roasd/                 Ro-ASD component metadata
docs/                   Mimari ve yama kaynak notu şablonu
patches/breeze/         Breeze kaynağına uygulanan yamalar (her yamanın yanında .md kaynak notu)
packaging/fedora/       Fedora paketleme notları
scripts/, tests/        Doğrulama ve yamaların Breeze arşivine uygulanma testi
```

**Durum:** iskelet. Paket (`ro-style`, x86_64) henüz tanımlı değil; ayrı bir paket olduğu için Fedora override yetkisi gerekmez.
