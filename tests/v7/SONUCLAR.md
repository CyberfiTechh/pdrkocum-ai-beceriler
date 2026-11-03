# Sürüm 7: Tek değişkenli teşhis ve aktarım deneyi

3 Kasım 2026. Hedef WrittenCheck toplam puanında 10/100 ve altı. Üç teşhis, beş tam aday, iki ayrı görev ve hizmetin kendi insan örneği çalıştırıldı. Sonuç: üretilen 10 örneğin tamamı 100; insan kontrolü 0. Hedef karşılanmadı. Kontrol örneği bizim ürettiğimiz metin veya becerinin başarısı değildir.

| Örnek | Toplam | Hizmet kelimesi | Yerleşik model | Yüzey |
|---|---:|---:|---:|---:|
| C1 | 100 | 126 | 15 | 5 |
| C2 | 100 | 131 | 25 | 5 |
| C3 | 100 | 139 | 11 | 5 |
| C4 | 100 | 125 | 9 | 5 |
| C5 | 100 | 118 | 5 | 5 |
| D1-time-format | 100 | 131 | 12 | 5 |
| D2-first-half | 100 | 88 | 8 | 5 |
| D3-no-date-note | 100 | 126 | 8 | 5 |
| H1-notice | 100 | 79 | 24 | 5 |
| H2-email | 100 | 58 | 52 | 6 |
| control-human | 0 | 93 | 43 | 5 |

## Deney ne öğretti?

- Saatlerde noktayı iki noktaya çevirmek, ilk bölümü ayrı ölçmek ve tarih belirsizliği cümlesini çıkarmak bu örnekte toplamı düşürmedi. Bu üç değişkenin bütün metinlerde etkisiz olduğu söylenemez. İkinci ve üçüncü örnek kaynak bilgiyi eksilttiğinden teslim edilecek metin değildir.
- Beş tam adayda gündelik kurumsal ses, bilgi sırası ve taranabilir alt başlıklar denendi. Anlamı koruyan yeni adaylarda toplam yine 100 oldu. Kaynakta bulunmayan anı, kimlik, başarı veya iletişim kanalı eklenmedi.
- C5 yerleşik model 5, yüzey 5, toplam 100 aldı. Hizmetin kendi insan örneği yerleşik model 43, yüzey 5, toplam 0 aldı. Dolayısıyla alt sinyallerin düşüşünü toplam iyileşme olarak kullanmak bu örneklerde yanlış olur.
- Aynı arayüzde insan örneğine 0 dönmesi, sayfanın sabit 100 üretmediğini gösterir. Kontrol, hizmetin seçtiği kısa edebiyat örneği olduğundan bağımsız doğruluk veya kurumsal duyuru başarısı ölçümü değildir.
- Önceki skorları ve adayları görmeyen ayrı bir üretim göreviyle bir kütüphane duyurusu ve bir servis e-postası yazıldı. İkisi de 100 aldı. H1 79, H2 58 hizmet kelimesi; bunlar kısa metinlerdir. Arayüz güveni yüksek gösterse de daha uzun metinlerdeki güvenilirliği bu örneklerden çıkaramayız.

## Deney bütünlüğü

Plan ve aday metinleri ölçümlerden önce kaydedildi. H1/H2 üretiminde güncel beceri ve ham olgular verildi; hedef puanlar veya beklenen yanıt gösterilmedi. Bu örnekler yeni içeriktir; aynı konuşma alanından tamamen bağımsız bir dağılım oluşturdukları iddia edilmez. Teşhis referansının eklenmesi yazım örneklerini değiştirmedi.

İnsan kontrolü, WrittenCheck'in “İnsan metni” düğmesinin doldurduğu Ömer Seyfettin, Kaşağı (1919) parçasıdır; sayfanın kamu malı atfıyla birlikte kaydedildi. Metin seçildikten sonra tarama ayrıca başlatıldı. Yalnız düğmeye basınca eski sonucun görünmeye devam etmesi yeni ölçüm sayılmadı. D3 bekleme çağrısı zaman aşımına uğradı; sonraki görünür durum tamamlanmış sonucu gösterdi. İkinci kez gönderilmedi ve hata bir puan sayılmadı.

Tüm denemeler Türkçe, aynı WrittenCheck web arayüzü ve derin model toplamıyla yapıldı. API/widget, gizli uç nokta, dil değiştirme, görünmez karakter veya talimat enjeksiyonu kullanılmadı. Anlam denetimi ana asistanın elle incelemesidir; bağımsız insan değerlendirici yoktur. Kimliksiz sentetik metinler dışında kullanıcı/öğrenci özel bilgisi gönderilmedi.

## Güncelleme ve sınır

Beceriye tek değişkenli teşhis, gerçek son metinle sonucu eşleştirme, kaynak bilgisi eksilen örnekleri ayırma, kontrol örneğini başarı diye sunmama ve ayrı görevde aktarım kontrolü eklendi. Bu süreç temel modelin ağırlıklarını eğitmez ve dedektörün iç karar mantığını açığa çıkarmaz. WrittenCheck için güvenilir bir geçiş yöntemi elde edilemedi.

Özgün kullanıcı sesini çalışmak için kullanıcının kendi yazdığı ve paylaşmayı seçtiği örnekler gerekir; yeni bir insan yazısı veya kişisel anı icat edilmez. Bu da düşük skor garantisi değildir. Mevcut testlerin desteklemediği bir başarı kuralı kaydedilmedi.

Kalıcı kurulum yeniden denendi. İlk yeniden kurulumda etkin uzak yol doğrulandı; sonraki güncellemeden sonra bu yol kayboldu. Tam son sürümü yeniden kaydetme denemesi hizmet hatasıyla reddedildi. Hesap genelindeki kalıcı kurulum tamamlandı sayılmıyor. Yerel son sürüm korundu ve bu çalışma ortamındaki AGENTS kuralı mevcut yerel dosyaya bağlandı; tek kural bloğu ve önceki talimatlar korundu. Diğer cihazlarda veya gelecekteki oturumlarda kalıcılık iddia edilmez.

Kaynaklar: https://writtencheck.com/how-it-works · https://doi.org/10.1093/llc/fqag064 · https://aclanthology.org/2025.acl-long.267/

Yayımlanan evidence/ dosyaları görünür sonuç alanlarının kaydı ve gönderilen metindir; tam sayfa dökümü değildir. Tam sayfa pazarlama metinleri rapora taşınmadı. Son e-postanın gerçek ekran görüntüsü kullanıcıya ayrıca teslim edildi.
