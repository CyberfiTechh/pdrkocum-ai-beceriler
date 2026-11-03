# Sürüm 6: Aynı Türkçe metin, farklı araçlar

3 Kasım 2026. Tüm metinler kimliksiz, yapay zekâ ile oluşturulmuş temsili örneklerdir. Amaç: anlamı koruyarak doğal yazmak ve kullanıcının istediği 10/100 hedefini gerçek ölçümlerle sınamak.

| Örnek | Araç | Gerçek toplam sonuç |
|---|---|---:|
| R0 başlangıç | ZeroGPT | 93,1 |
| A3 son düzenleme | ZeroGPT | 0 |
| A1 | WrittenCheck | 100 |
| A2 | WrittenCheck | 100 |
| A3 son düzenleme | WrittenCheck | 100 |
| R0 | Copyleaks | Sonuç yok: insan doğrulaması |
| R0 | Pangram | Sonuç yok: insan doğrulaması |
| R0 | TextGuard humanizer | Tam çıktı hesap ekranında kilitli; karşılaştırılabilir puan yok |

## Ne değişti?

R0'daki resmî davet girişi kısaldı. A3, oturumun akışını soruların nasıl sorulacağıyla birlikte anlatıyor; bağlantı, ön kayıt ve cihaz bilgisini aynı yerde topluyor. Çarşamba/cuma ve 20.10 bitiş saati verilen perşembe, bir gün önce/sonra ve 40 dakika bilgilerinden çıkarıldı. Yeni deneyim, kişi, başarı iddiası veya olay eklenmedi. 19.30 + 40 dakika = 20.10; 15 + 25 = 40 kontrol edildi.

Başlangıç 159, A3 127 boşluk-kelimesi. WrittenCheck A3'ü 131 kelime saydı. Bu kontrollü uzunluk deneyi değildir; puan farkını yalnız bir sözcüğe ya da belirli bir tekniğe bağlayamayız. Türkçe metin çevrilmeden gönderildi. ZeroGPT arayüzü İngilizceydi; WrittenCheck Türkçeydi. Araçların yüzdeleri aynı istatistiksel ölçü olarak birleştirilmedi.

A3 WrittenCheck: toplam/derin model 100; olası aralık 92–100, güven yüksek; yerleşik model 10, yüzey 5. Dolayısıyla düşük yüzey puanı toplam başarı değildir. ZeroGPT'de hedef sağlandı; kullanıcının özellikle istediği WrittenCheck'te sağlanmadı. Aynı anlam grubunda daha önceki sekiz düzenleme ve ayrı e-posta da WrittenCheck 100 aldı (../v5/SONUCLAR.md). Tek başarılı araç sonucu bütün metinlere genellenemez.

## Anlam denetimi

Sınıflar, konu, çevrim içi ortam, gün/saat, 40 dakika toplam, 15+25 sırası, ücretsiz ve isteğe bağlı katılım, notlara etkisizlik, ön kayıt gerekmemesi, bağlantının paylaşım günü/kanalı, cihazlar, isteğe bağlı 19.20 kontrolü, kamera tercihi, mikrofon kuralı, soru kanalları, kayıt alınmaması, gizlilik, ayrı görüşme ve tarih belirsizliği, sonraki gün yazılı özet A3'te korunuyor. Son iki zaman ayrıntısı doğrudan eşdeğer çıkarımdır. Bu inceleme elle yapıldı; bağımsız insan değerlendirmesi değildir.

A1'in ilk üretiminde ayrı görüşmenin tarih belirsizliği eksikti; test öncesinde eklendi. İlk çıktı A1-agent-original.txt olarak saklandı. A2'deki “talep edin” ifadesi izin kipini değiştirdiği için A3'te “talep edebilirsiniz” yapıldı. A2 nihai aday değildir. A3 ayrı görülmemiş görev değildir; aynı metnin düzenlemesidir. Bütçe en çok altı adaydı; üç adaydan sonra kullanıcı yönlendirmesiyle araç karşılaştırmasına geçildi.

## TextGuard ve listedeki araçlar

TextGuard'a R0, standart modda gönderildi. Tam yeniden yazım açılmadı; hesap oluşturma/giriş ekranı gösterildi. Kilit ekranındaki “her dedektörü geçer” ve önizlemedeki sayılar doğrulanmış test sonucu sayılmadı. Üyelik oluşturulmadı, ödeme yapılmadı.

AIMultiple listesinden ZeroGPT, Copyleaks ve Pangram denendi. Copyleaks yükleme görünümünde Cloudflare insan doğrulaması gösterdi. Pangram “Verify you are human” kutusunu istedi. Bu iki engel çözülmediği için puanları null bırakıldı. Listedeki diğer araçlar bu turda çalıştırılmadı; tüm liste test edilmiş değildir.

Kaynak sayfalar: https://aimultiple.com/tr/ai-generated-text-detector · https://textguardai.com/humanizer · https://www.zerogpt.com/ · https://copyleaks.com/tr/ai-detector · https://www.pangram.com/tr · https://writtencheck.com/how-it-works

## Kayıtlar

results.json gerçek puanları, metin SHA-256 değerlerini ve görünür kanıt dosyalarını içerir. Kanıt kayıt zamanı, hizmetin kendi işlem zamanı olarak sunulmaz. Ekran görüntüleri kullanıcıya ayrıca teslim edildi. Yöntem güncellemesi anlamdan yeniden kurma ve araçlar arası dürüst değerlendirmeyi ekler; WrittenCheck sorununun çözüldüğünü iddia etmez.
