# İnsan kaynaklarından ilerleme deneyi — v8

Tarih: 3 Kasım 2026. Sekiz ayrı metin üzerinde WrittenCheck'te sekiz, aynı Nutuk uyarlaması üzerinde ZeroGPT'de bir olmak üzere **dokuz tamamlanmış ölçüm** yapıldı. Ölçümler gerçek web arayüzlerinden alındı. Alt bileşen puanları toplam sonuç yerine kullanılmadı.

**Sonuç:** İnsan eseri kaynaklı Nutuk uyarlaması iki araçta da 0 aldı. Ancak başka konuda sıfırdan hazırlanan öykü ve duyuru WrittenCheck'te 100 aldı. Bu çalışma, her yeni metinde 10 ve altını sağlayan bir yöntem ortaya koymadı.

## Kaynakların seçimi

- **Ömer Seyfettin, Falaka:** [Vikikaynak sabit sürümündeki](https://tr.wikisource.org/w/index.php?title=Falaka&oldid=170798) açılıştan 122 kelime. [Boğaziçi Üniversitesi GETEM kaydı](https://gserv1.getem.boun.edu.tr/?q=node/3807) 1993 tarihli ikinci baskıyı ve 6 Şubat 2007 katalog girişini gösteriyor; aynı açılış metni de kayıtta yer alıyor. İlk yayın için 19 Temmuz 1917 tarihi [ikincil incelemede](https://edebiyatvesanatakademisi.com/post/omer-seyfettin-falaka-oykusu-hakkinda-inceleme-ve-metni/111823) bildiriliyor; ilk dergi basımını bu çalışmada incelemedik.
- **Mustafa Kemal Atatürk, Nutuk:** [Vikikaynak sabit sürümündeki](https://tr.wikisource.org/w/index.php?title=Nutuk/1._bölüm/Samsun%27a_çıktığım_gün_umumî_vaziyet_ve_manzara&oldid=174609) ilk beş paragraftan 152 kelime. [MEB eser bilgisi](https://tmek.gov.tr/ataturk/Hayati/YaziliEserleri) 1927 konuşmasını ve ilk basımını açıklıyor; [Atatürk Araştırma Merkezi](https://atam.gov.tr/nutuk-dunya-dillerine-kazandiriliyor/) eserin Atatürk tarafından yazıldığını belirtiyor.

Eserlerin tarihsel insan yazarlığı, dedektör skorlarından bağımsız olarak belgelendi. Web aktarımlarının her karakteri özgün basımlarla karşılaştırılmadı. Siyasi değerlendirmeler Nutuk'un yazarına aittir; deney bunları bağımsız tarih hükmü olarak onaylamaz.

## Eşleştirilmiş ölçümler

| Metin | İşlem | WrittenCheck toplam | Site kelime sayısı | Yerleşik model | Yüzey kontrolü |
|---|---|---:|---:|---:|---:|
| F0 | Falaka özgün alıntı | 0 | 122 | 77 | 5 |
| F1 | Aynı kesitte yalnız noktalama | 0 | 122 | 73 | 5 |
| F2 | Aynı kesitin AI ile yeniden anlatımı | 100 | 113 | 84 | 5 |
| N0 | Nutuk özgün alıntı | 0 | 152 | 0 | 4 |
| N1 | Aynı kesitte yalnız noktalama | 0 | 152 | 0 | 5 |
| N2 | Aynı kesitin AI ile günümüz dilinde uyarlaması | 0 | 137 | 1 | 10 |
| H1 | Başka konuda yeni kurmaca öykü | 100 | 131 | 100 | 5 |
| H2 | Başka konuda yeni kütüphane duyurusu | 100 | 90 | 85 | 5 |

WrittenCheck, 0 sonuçlarında güveni **orta**, olası aralığı **0–14%**; 100 sonuçlarında güveni **yüksek**, aralığı **92–100%** gösterdi. Gösterilen 0, kesin insan yazarlığı kanıtı değildir. N2 açıkça AI tarafından uyarlanmıştır.

N2'nin birebir aynı girdisi **ZeroGPT'de 0% AI GPT** aldı. ZeroGPT 136, WrittenCheck 137 kelime gösterdi; araçların kelime sayma yöntemleri farklı. Girdi değiştirilmedi: SHA-256 `e044ee257c52ae08b6f18b2c822a88837ad59c5af750e969374bb4c9e0af9253`.

H1 ve H2, ölçüm sonuçları paylaşılmayan ayrı bir yazım oturumunda, kaynak metinleri ve yazım akışını kullanarak hazırlandı. H1 açıkça kurmaca olarak etiketlendi. H2'de verilen bütün koşullar korundu; uzunluk hedefi için yeni bilgi veya tekrar eklenmedi. H2 boşlukla sayıldığında 85 kelimedir. Bu iki yeni örneğin başarılı olmaması, düşük skorlu uyarlamanın başka görevlere aktarılabilirliğinin gösterilmediği anlamına gelir.

## Çıkarılabilen ve çıkarılamayan sonuçlar

1. İnsan metnini korunacak bir taban olarak tutmak bu iki örnekte düşük skoru korudu; fakat yalnızca birkaç noktalama değişikliği denendi. Bu sonuç kapsamlı editörlüğün tamamına genellenemez.
2. Falaka'yı kısa ve devrik cümlelerle yeniden anlatmak toplam skoru düşürmedi. Nutuk'u günümüz diline uyarlamak ise bu kesitte düşük kaldı. Dolayısıyla tek bir evrensel cümle şablonu saptanmadı.
3. Falaka özgün metninde yerleşik model 77 iken toplam 0; Nutuk uyarlamasında yüzey kontrolü 10 iken toplam 0. Alt puanların toplam kararı doğrudan açıkladığı varsayılamaz.
4. Somut ayrıntı, tutarlı bakış açısı, bilgi ilişkileri ve işlevli tekrar, editoryal çalışma soruları olarak eklendi. Bunlar deneyin kanıtladığı bir dedektör aşma formülü olarak sunulmuyor.
5. Klasiklerin eğitim verilerinde bulunması, tarihsel konu ve kelime seçimi, uzunluk farkı ve tür etkisi ayrıştırılmadı. İki eser temsili bir derlem değildir. Aynı adayı tekrar ölçerek servis değişkenliği veya insan editör karşılaştırması da yapılmadı.

## Dosyalar ve kullanım

`plan.json` ilk altı ölçümden önceki kapsamı; `forward-plan.json` yeni iki görevden önceki kapsamı; `meaning-review.json` anlam incelemesini içerir. `results.json` bütün tamamlanmış sonuçları, girdi özetlerini ve kelime sayılarını kaydeder. `evidence/*.json` görünür arayüzden çıkarılan sonuç alanları ve tam gönderilen metindir; tam sayfa dökümü değildir. Her `.txt` dosyasının baş/son boşluğu kırpılarak gönderilmiştir.

F0/N0, tarihsel eserlerden alıntıdır. F1/N1 noktalama düzenlemesidir. F2/N2 AI uyarlamasıdır; yazarların birebir sözleri olarak alıntılanamaz. Bu altı dosyada kaynak yazar, eser ve sabit sürüm bağlantıları korunmalıdır. Vikikaynak aktarımları için [CC BY-SA](https://creativecommons.org/licenses/by-sa/4.0/) atfı ve benzer paylaşım koşulları saklıdır; depo genel lisansı üçüncü taraf eser atfını ortadan kaldırmaz. H1/H2 yeni AI metinleridir.

Özgün insan metinlerinin veya az değiştirilmiş kopyalarının düşük skorları, becerinin sıfırdan üretim başarısı değildir. Kaynaklardan cümle kopyalayıp yeni metne ekleyerek puan düşürme yöntemi kullanılmadı.
