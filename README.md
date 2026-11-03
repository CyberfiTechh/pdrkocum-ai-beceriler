# PDR Koçum AI Beceriler

Codex için doğal Türkçe yazım ve bilgi doğrulama becerileri. Bu depo, PDR Koçum uygulamasından bağımsız olarak yalnızca yazım becerisini, araştırma notlarını ve test sonuçlarını içerir.

## İlk beceri: Doğal ve Doğrulanmış Yazı

[Beceriyi incele](.agents/skills/dogal-ve-dogrulanmis-yazi/SKILL.md)

- Metni amacına, okuruna ve kullanıcının sesine göre düzenler.
- Gereksiz kalıpları ve tekrarları azaltır; anlamı, koşulları ve olasılığı korur.
- Yeni olgusal iddiaları kaynaklarla denetler; bulunmayan kaynağı, sayıyı, kişisel deneyimi veya alıntıyı uydurmaz.
- İnternete erişilemiyorsa neyin doğrulanamadığını belirtir.
- Dedektör puanlarını doğruluk ve anlam kontrolünden ayrı değerlendirir.

Bu bir yönerge paketidir. Model ağırlıklarını değiştirmez; dedektör geçme veya sıfır hata garantisi vermez. Ücretli servis veya API anahtarı gerektirmez. Sıkı doğrulamadaki yerel denetim aracı Python 3.9+ kullanır; üçüncü taraf paket gerekmez. Python olmayan ortamda kontroller elle uygulanır ve otomatik denetim yapılmadığı belirtilir. Araştırmalı yazım, kullandığınız Codex ortamının web erişimine bağlıdır.

## Sürüm 4: Puan teşhisi ve tekrarlı deneme

Doğal ve doğrulanmış Türkçe yazım artık bu kullanıcı için varsayılan kuraldır. Açık dedektör deneylerinde hedef 10 ve altıdır; bu hedef garanti değildir. Belge modelini yüzey puanından ayıran teşhis, anlam/izin koruması ve tüm denemeleri kaydetme kuralları eklendi.

11 yeni duyuru adayı test edildi. Son aday **WrittenCheck 0 (0–14, orta güven), Seobaz 32 (21–43, orta güven)** aldı. İki araç da insan yazımına benzer dedi; 10 hedefi yalnız WrittenCheck'te sağlandı. Ayrı e-posta **100** aldığı için genel başarı iddiası yoktur. [V4 raporu, bütün sonuçlar ve gerçek ekranlar](tests/v4/SONUCLAR.md).

## Sürüm 3: Türkçe yapı ve gerçek dedektör denemeleri

[12 ailede 36 editoryal örnek](.agents/skills/dogal-ve-dogrulanmis-yazi/references/kalip-ve-yapi-rehberi.md), paragraf işlevi, kullanıcı sesi ve en az müdahale kuralları eklendi. Örnekler evrensel bir yasak listesi veya tüm internetten çıkarılmış bir veri kümesi değildir. [Araştırma notları](.agents/skills/dogal-ve-dogrulanmis-yazi/references/v3-arastirma.md) okunan kaynakları ve sınırlarını açıklar.

İki hizmette B/C metinleri için 10 gerçek ölçüm yapıldı. Son e-posta Seobaz38/WrittenCheck100; son duyuru Seobaz37/WrittenCheck88 aldı. **İki dedektörden birden geçen aday elde edilmedi.** İlk adayın kötüleşen sonucu ve eski çıktı nedeniyle geçersiz girişim de kaydedildi. [V3 test raporu, ham sonuçlar ve ekran görüntüleri](tests/v3/SONUCLAR.md).

## Sürüm 2: Daha sıkı doğrulama

Son metne bağlı iddia–kaynak kaydı, alıntı kontrolü, sayı/koşul koruması, çelişki yönetimi ve tekrarları azaltan üslup kuralları eklendi. Araç kaynak güvenilirliğini veya anlamsal doğruluğu otomatik kanıtlamaz.

- [Altı ek akademik kaynaktan alınan ilkeler](.agents/skills/dogal-ve-dogrulanmis-yazi/references/ileri-dogrulama-kaynaklari.md)
- [Sıkı doğrulama akışı](.agents/skills/dogal-ve-dogrulanmis-yazi/references/siki-dogrulama.md)
- [Yerel aracın kullanımı ve sınırları](.agents/skills/dogal-ve-dogrulanmis-yazi/references/yerel-denetim.md)
- [V2 test raporu: 21 araç testi, 12 ilk örnek ve 3 hedefli revizyon örneği](tests/v2/SONUCLAR.md)

İlk yazım turunda 11 örnek ölçütleri karşıladı, bir örnekte tekrar bulundu; düzeltme sonrası üç yeni hedefli örnek geçti. Küçük örneklemdeki sonuçlar gelecekte hatasızlık garantisi değildir. Bu tur yeni dedektör ölçümü yapılmadı.

## Codex'te kullanma

Bu depoyu indirdikten sonra Codex'i depo klasöründe açın. Beceri bu klasörün `.agents/skills` dizinindedir.

Bütün projelerde kullanmak için yalnızca `.agents/skills/dogal-ve-dogrulanmis-yazi` klasörünü kendi bilgisayarınızda `~/.agents/skills/` altına kopyalayın. Aynı isimde mevcut beceri varsa önce karşılaştırın; üzerine körlemesine yazmayın. Bu GitHub yüklemesi bilgisayarınızdaki Codex'e otomatik kurulum anlamına gelmez.

Örnek komut:

```text
$dogal-ve-dogrulanmis-yazi
Aşağıdaki yazıyı velilere yönelik doğal ve saygılı bir dille düzenle.
Anlamı ve önemli ayrıntıları koru. Kaynağı olmayan iddia ekleme.
Metin: ...
```

Araştırmalı kullanım:

```text
$dogal-ve-dogrulanmis-yazi
Bu konuda kısa bir bilgilendirme yaz. Önce güncel birincil kaynakları oku.
Sayıları ve iddiaları doğrula; kaynak bulamazsan bilgi uydurma.
```

## Kaynaklar ve testler

- [Araştırma dayanakları](.agents/skills/dogal-ve-dogrulanmis-yazi/references/arastirma-dayanaklari.md)
- [Türkçe üslup örnekleri](.agents/skills/dogal-ve-dogrulanmis-yazi/references/turkce-uslup.md)
- [Kanıt protokolü](.agents/skills/dogal-ve-dogrulanmis-yazi/references/kanit-protokolu.md)
- [Dedektör deney protokolü](.agents/skills/dogal-ve-dogrulanmis-yazi/references/dedektor-deneyi.md)
- [İlk sürümün dedektör deney raporu](tests/SONUCLAR.md)
- [Güncel dosya bütünlüğü kaydı](tests/manifest.json)

Hazırlama tarihi: 3 Kasım 2026. Araştırma erişim sınırları kaynak notlarında, gerçek dedektör sonuçları ve başarısız denemeler test raporunda tutulur. Her iki metin sürümü de yapay zekâ ile oluşturulmuştur; insan kontrol grubu yoktur. Küçük örneklem genel başarı oranı değildir.
