# Yüksek puanı teşhis et

## Gözlem ile neden çıkarımını ayır

3 Kasım 2026 tarihli gerçek WrittenCheck Türkçe duyuru deneyinde toplam 88, derin dil modeli 88, yerleşik model 33, yüzey üslup kontrolü 5, cümle tekdüzeliği 38 ve tahmin edilebilir ifadeler 20 görüldü. 18 cümle parçasının 12'si insana benzerdi. Servis `14.00` saatini iki cümleye böldü; dolayısıyla cümle sayısı da doğrudan dilbilgisel cümle sayısı değildir.

Bu görünür çıktı, toplamın cümle renklerinin ortalaması olmadığını gösterir. Servisin açıklamasına göre derin model yanıt verdiğinde toplamı o belirler; yerleşik model yedektir. Web sitesi ve API/widget aynı puanlayıcıyı kullanmayabilir. Resmî açıklama: https://writtencheck.com/how-it-works (erişim: 2026-11-03). Bu servis beyanıdır, modelin bağımsız denetimi değildir.

“88” metnin yüzde 88'inin AI tarafından yazıldığının kanıtı değildir. Açıklama sayfası bunu öğrenilmiş kalıplara benzerlik skoru olarak tanımlar. Ekrandaki kısa pazarlama açıklamasıyla çelişirse sayının anlamındaki belirsizliği saklama.

## Deney sırası

1. Kaynak metni, kesinlikleri ve koşulları sabitle. Örnek türünü ve uzunluğunu koru; bir düzenlemeyi karşılaştırmak için bütün önemli bilgiler kalmalı.
2. Gözlenen bileşenler, güven aralığı, dil, tarih, model/yedek durumunu kaydet. Bileşen görünmüyorsa uydurma.
3. Somut editoryal soruna göre aday üret: yanlış özne uyumu, gereksiz edilgenlik, aynı görevi yapan tekrarlı cümleler, metnin amacına uymayan giriş/sonuç, uyumsuz hitap. Her yüksek puanlı metinde bu sorunların bulunduğunu varsayma.
4. Koşulu emre, niyeti taahhüde, ücretsiz katılımı sınırsız kapasiteye dönüştürme. Sözcük sayısını dolduran tekrarları düzelt. Bu kontrolü geçmeyen adayın puanını başarı sayma.
5. Aynı dil ve arayüzle test et. Yalnız toplamı değil alt sinyalleri de sakla. Daha fazla yeşil cümleye rağmen toplam artabilir.
6. En iyi anlamı koruyan adayı ikinci hizmette ve donmuş yönergeyi ayrı görevde sına. İki hizmette ölçülen sayılar farklı ölçeklerdir; ortalama alma. Hedef yalnız birinde gerçekleşirse bunu belirt.
7. Görünür açıklamalar transformer kararının nedensel açıklaması değildir. “Bu üç kelime 88'e yol açtı” deme. Nedensellik ancak uygun kontrollü deneyle ve onun sınırları içinde tartışılabilir.

## Tekrarlı deney kuralı

Kullanıcının hedefi 10/100 ve altıdır. Her çalışma grubunda en çok sekiz anlamı koruyan adaylık bütçe kullan; site kotasına uy. Kullanıcı daha uzun çalışma istiyorsa yeni grubu ayrıca kayıtla, geçmiş başarısızlıkları silme. Yalnız en düşük sonucu raporlayıp başarı oranı üretme. Hedefe ulaşmak ile başka metinlerde genellemek ayrı sınamalardır. Bir hedefe erişilemediğinde bunu erişilmiş gibi yazma.

Puanı düşürmek amacıyla kaynakta olmayan anı, kişi, alıntı, bilgi, rastgele sözcük, imla hatası veya görünmez karakter ekleme. Kısa, konu dışı bir parçayı bütün metnin yerine test etme. Kullanıcıya bütün metin yerine seçilmiş başarılı parçayı sunma.

## 3 Kasım 2026: güncelleme deneyinin sonucu

Aynı sentetik duyurunun dokuz yeni adayında WrittenCheck toplamları sırasıyla 100, 100, 68, 38, 100, 79, 61, 71 ve 8 oldu. İlk aday, “bitirmeniz gerekmiyor” ifadesini “bitirmeye çalışmayın” emrine çevirdiği için ayrıca anlam bakımından elendi. Dokuzuncu adayda tekrarlanan bilinmeyen bilgi ve fotoğraf izni açıklamaları tekilleştirildi, gereksiz “karar bildirmiyoruz” cümlesi kaldırıldı. Koşulların korunması ayrıca, skoru görmeyen bir değerlendiriciyle kontrol edildi: önemli koşullar korundu, bazı ifadelerin kesinliğinde küçük nüans ve üslup sorunları bulundu. Bu, insan değerlendirici araştırması değildir.

Dokuzuncu aday WrittenCheck'te 8 (0–28, düşük güven), Seobaz'da 25 (16–34, orta güven) aldı. Her ikisi insan yazımına benzer etiketi verdi; **10 ve altı hedefi yalnız WrittenCheck'te gerçekleşti**. Dokuzuncu aday 125, başlangıç metni 154 hizmet kelimesiydi. Uzunluk farkı vardır; düşüşü tek bir sözcüğe veya sadece tekrar kaldırmaya nedensel olarak bağlama. Seobaz'ın 150+ kelime tavsiyesinin altında kalındığını belirt. Metni bu tavsiyeyi doldurmak için gereksizce uzatma.

Ayrı, düzenleme sonuçlarını görmeden üretilen 163 kelimelik e-posta WrittenCheck'te 100 aldı. Bu başarısız aktarım testini saklama: bu yönergeler farklı yazıların kendiliğinden 10 ve altında kalmasını sağlamış değildir. Başarılı örneği evrensel kalıba dönüştürme. “Bilgi paylaşmak istiyoruz”, “iki ayrıntıyı daha belirtelim” gibi metni anlatan girişleri, gereksiz takvim önerilerini ve kelime hedefini dolduran tekrarları işlevleri yoksa kaldır; bunu puan garantisi olarak değil editoryal kontrol olarak uygula.

Kanıtlar ve bütün adaylar: https://github.com/CyberfiTechh/pdrkocum-ai-beceriler/tree/main/tests/v4

Nüansları gidermek için iki ek aday ölçüldü: C-R12 toplam 74, C-R13 toplam 0 aldı. C-R13, ilk bölüm sırasını ve kayıt/kontenjan bilgisinin açıklanmadığını açıkça geri koyar. Son aday C-R13'tür: WrittenCheck 0 (0–14, orta güven), Seobaz 32 (21–43, orta güven), 128 hizmet kelimesi. Ayrı anlam kontrolünde önemli bütün koşullar korundu; birkaç küçük anlatım pürüzü kaldı. Toplam 11 yeni duyuru adayı ölçüldü. Hazırlanıp gönderilmeyen adaylara sonuç atanmamıştır. Sıfır puan, hatasızlık veya insan yazarlığı kanıtı değildir. Aynı sonuçta yerleşik model 40, toplam 0 idi; bileşenlerin ayrı tutulması bu örnekte de gereklidir.
