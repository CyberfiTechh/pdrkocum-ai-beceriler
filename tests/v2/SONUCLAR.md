# Sürüm 2: doğruluk ve doğal anlatım değerlendirmesi

Tarih: 3 Kasım 2026. Bu rapor bir başarı garantisi değil, yapılan işin izlenebilir kaydıdır.

## Araştırmadan uygulamaya

Altı ek birincil akademik kaynağın erişilen bölümleri incelendi. [Kaynaklar, okunan kapsam ve sınırlılıklar](../../.agents/skills/dogal-ve-dogrulanmis-yazi/references/ileri-dogrulama-kaynaklari.md) ayrı kaydedildi. Araştırma algoritmaları yeniden uygulanmış veya bilimsel sonuçları bu beceri için tekrar edilmiş değildir.

| Hata alanı | Uygulanan önlem | Kalan sınır |
| --- | --- | --- |
| Kaynak var ama iddiayı desteklemiyor | İddiayı böl; aynı özne, dönem, kapsam ve kesinlikte pasajla karşılaştır | Anlamsal değerlendirme yine hata yapabilir |
| Kaynak veya alıntı uydurma | Gerçek erişimi izle; alıntıyı kayıtlı metinde ara | Kayıtlı metnin gerçekliğini hash kanıtlamaz |
| Doğallaştırırken anlam kaybı | Sayı, birim, olumsuzluk, koşul, izin ve olasılığı önce sabitle | Mekanik araç bütün dil anlamını çözmez |
| Güncel olmayan/çelişen veri | Tarihleri karşılaştır; çözülemeyen iddiayı kesinleştirme | Web erişimi ve güvenilir kaynak gerekir |
| Son taslak eski onayla teslim | Son metin hash'i ve tam parça kapsamı denetimi | Doğru hash, doğru bilgi anlamına gelmez |
| Bilinmeyen bilgi yüzünden tüm görevi bırakma | Belirsiz parçayı çıkar; doğrulanabilen kısmı sun | Yanıtsız bırakma kararını bağlam belirler |
| Doğal görünmek için ayrıntı uydurma | Kullanıcı sesinden yalnızca gözlenen özellikleri al; tekrarları düzelt | Okur değerlendirmesinin yerini tutmaz |

## Yazım örnekleri

Ölçütler, yanıtlar görülmeden önce `rubric.json` dosyasına kaydedildi. İki yeni oturum, yalnızca beceri ve altışar görev aldı; beklenen yanıtlar/değerlendirme ölçütleri paylaşılmadı. Üretilen yanıtlar `answers-a.json` ve `answers-b.json` dosyalarında değiştirilmeden saklandı. Kaynaklar sentetik kullanıcı belgeleridir; gerçek kurum/ürün performansının kanıtı değildir.

Değerlendirmeyi beceriyi hazırlayan asistan yaptı. Bu çalışma bağımsız insan incelemesi, farklı model aileleri karşılaştırması veya istatistiksel performans ölçümü değildir. Aynı görevler becerisiz koşulda çalıştırılmadığından iyileşmenin büyüklüğü hesaplanamaz.

| Vaka | Konu | Sonuç |
| --- | --- | --- |
| T01 | Öz bildirimden nedensellik üretmeme | Geçti |
| T02 | Kısmen desteklenen birleşik iddiayı ayırma | Geçti |
| T03 | Çelişen tarihler | Geçti |
| T04 | Kaynak içine gömülü yönlendirme | Geçti |
| T05 | Onay, izin ve zorunluluk ayrımı | Geçti |
| T06 | Birebir alıntı | Geçti |
| T07 | Türkçe para gösterimi ve çarpım | Geçti |
| T08 | Sıfır tabandan yüzde artışı | Geçti |
| T09 | Kaynaksız güncel sıralama | Geçti |
| T10 | Tarihsel sayıyı bugüne taşımama | Geçti |
| T11 | Az bilgili ürün tanıtımı | Küçük üslup kusuru: ikinci cümle tekrar |
| T12 | Kullanıcı sesi ve ihtiyat | Geçti |

İlk tur: **11 geçti, 1 küçük üslup kusuru, 0 maddi hata**. Bu sayı yalnızca bu 12 örneğin belirtilen ölçütlerle değerlendirmesidir.

T11 nedeniyle, yan yana cümlelerin aynı bilgiyi yinelememesi ve sabit uzunluğu uydurma ayrıntıyla doldurmaması kuralı güçlendirildi. Üç yeni, düşük bilgi içeren görev başka bir yeni oturumda çalıştırıldı: ürün tanıtımı, buluşma duyurusu, kitap bülteni. Üçü de revizyon ölçütlerini karşıladı. Ham yanıtlar `revision-answers.json`, önceden kaydedilmiş ölçütler `revision-rubric.json`, gerekçeli değerlendirme `assessment.json` içindedir. İlk tur kusuru sonradan başarı olarak değiştirilmedi.

İlk ve son beceri dosyalarının hash kayıtları `tested-version-initial.json` ve `tested-version-final.json` içindedir. İlk tur sonrasında yalnızca tekrar/uzunluk maddesi genişletildi ve bir referanstaki İngilizce zaman terimi Türkçeleştirildi. Son revizyon için tüm 12 örneğin tekrar çalıştırıldığı iddia edilmez; üç hedefli yeni örnek kullanıldı.

## Mekanik araç

Python standart kütüphanesiyle çalışan `evidence_gate.py` için **21 birim testi geçti**. Çalıştırma çıktısı `unit-test-output.txt`, testler `test_evidence_gate.py` dosyasında.

Testler dosya değişikliğini, sahte alıntıyı, eksik kanıtı, metnin bir bölümünün kayıttan atlanmasını, bilinmeyen/yinelenen kaynağı, yol taşmasını, klasör dışına çıkan simgesel bağlantıyı, görünmez karakteri, eksik saat dilimini, bozuk JSON'u, yanlış veri türlerini ve dosya sınırını kapsar. Komut satırı başarı/hata çıkışları da çalıştırılarak denetlendi.

**İki karşı örnek özellikle önemlidir:** yanlış bir iddia doğru kaynaktaki ilgisiz alıntıyla; olgusal iddia ise yanlışlıkla `other` olarak etiketlenerek mekanik kontrolden geçebiliyor. Testlerin bu davranışı göstermesi, anlamsal inceleme gereğini görünür kılar. “21 test geçti” ifadesi “21 yanlış iddia yakalandı” demek değildir.

Ayrıca yazım görevlerinde üretilen yedi gerçek denetim kaydı tekrar çalıştırıldı; hepsi mekanik kontrolleri geçti (`audit-rerun-results.json`). Bunlar T01, T02, T03, T06, T07, T08 ve T10 kayıtlarıdır. Yazarın verdiği anlamsal not, bağımsız inceleme sayılmaz. Sayısal örnekler ayrıca aritmetik olarak kontrol edildi.

Depodaki bu bölümün kökünden çalıştırma:

```bash
python3 tests/v2/test_evidence_gate.py .agents/skills/dogal-ve-dogrulanmis-yazi/scripts/evidence_gate.py
python3 .agents/skills/dogal-ve-dogrulanmis-yazi/scripts/evidence_gate.py tests/v2/a-audits/T01/audit.json
```

## Dedektör sonuçlarıyla ilişki

Bu tur yeni dedektör ölçümü yapılmadı. Önceki sürümün [gerçek dedektör deneyi](../SONUCLAR.md), ham ölçümleri ve başarısız servis çağrısı korunuyor. Seobaz'da bazı skorların düşmesi, WrittenCheck'te skorların yüksek kalması raporda birlikte gösteriliyor. Eski puanlar bu revizyonun puanı veya doğruluk kanıtı sayılmıyor.

Sıfır hata, sıfır yapay zekâ skoru veya her dedektörü geçme garantisi yok. Kaynak eşleştirme, anlam koruma ve kullanıcıya uygun anlatım; dedektör puanından ayrı kabul ölçütleridir.
