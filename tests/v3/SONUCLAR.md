# Sürüm 3 — gerçek dedektör denemeleri

3 Kasım 2026. Amaç: doğal Türkçe anlatımı, olguları ve koşulları koruyarak geliştirmek; gerçek dedektörlerde sonucu gözlemek. Her dedektörden geçiş elde edildiği iddia edilmiyor.

## Araştırma ve yapılan değişiklik

Beş akademik çalışmanın belirtilen bölümleri, Turnitin'in güncel kılavuzu ve iki hizmetin canlı açıklamaları incelendi. [Araştırma kapsamı](../../.agents/skills/dogal-ve-dogrulanmis-yazi/references/v3-arastirma.md) hangi kaynağın hangi bölümünün okunduğunu ve genelleme sınırını açıklar. Tüm internet taranmadı; bir dil modeli yeniden eğitilmedi.

[12 ailede 36 editoryal kalıp örneği](../../.agents/skills/dogal-ve-dogrulanmis-yazi/references/kalip-ve-yapi-rehberi.md) eklendi. Bunlar makalelerden çıkarılmış evrensel yapay zekâ kelimeleri değil. Bağlam, paragraf işlevi, yüklem, kullanıcı sesi, anlamı koruma ve en az müdahale birlikte ele alınıyor.

## Deney düzeni

B: önceki sürümün iş e-postası, geliştirme örneği. C: yeni okuma buluşması duyurusu, kural ayarlamak için kullanılmayan örnek. Metinler kimliksiz ve yapay zekâ üretimi. İnsan yazısı olarak sunulmuyor. Kriterler `criteria.json` içinde önceden kaydedildi.

İlk yeni oturum B ve C için aday hazırladı. B'de sonuçtan sonra yalnızca bir ek, gerekçeli düzenleme yapıldı: istek başa alındı ve kurumsal eylem ifadeleri sadeleştirildi. C'nin nihai sürümü ayrı yeni oturumda son yazım kurallarıyla hazırlandı; C puanlarına göre kural değiştirilmedi. Denetim protokolüne ayrıca gözlenen eski sonuç sorununu yakalayan kayıt kuralı eklendi.

B ve C aynı tarihte iki hizmette sınandı. Seobaz'ın İngilizce arayüzü Türkçe destek beyanıyla kullanıldı; WrittenCheck'te dil Türkçe seçildi. Giriş/ücret gerekmedi. Turnitin üzerinde canlı test yapılmadı. Kendi platformları için açıklanan başarı reklamları bu deneyin bulgusu sayılmadı.

## Bütün puanlar

Sayılar hizmetlerin AI olasılığı/benzerlik skorlarıdır; yazarlık kanıtı veya doğruluk ölçüsü değildir. Hizmetler arasında ortalama alınmadı.

| Metin | Yerel sözcük sayısı | Seobaz | WrittenCheck |
| --- | ---: | ---: | ---: |
| B başlangıç | 155 | 36 (27–45) | 100 (92–100) |
| B ilk V3 adayı | 155 | 41 (30–52) | 100 (92–100) |
| B ikinci düzenleme | 157 | 38 (24–52) | 100 (92–100) |
| C başlangıç | 162 | 42 (30–54) | 99 (91–100) |
| C nihai V3 | 153 | 37 (26–48) | 88 (74–100) |

Seobaz 0–39 aralığını “Most likely human-written” olarak etiketlediğinden B ikinci düzenleme ve C nihai metin bu etiketi aldı. WrittenCheck ikisini de “Büyük olasılıkla yapay zeka” olarak etiketledi. **İki araçtan birden geçen aday elde edilmedi.**

B'de son skor başlangıçtan iyi değil: Seobaz 36→38, WrittenCheck 100→100. İlk V3 adayının daha kötü sonucu gizlenmedi. C'de Seobaz 42→37 ve WrittenCheck 99→88 oldu; WrittenCheck'te etiket değişmedi. Bu küçük farkları genel başarı oranı, istatistiksel olarak güvenilir iyileşme veya gelecekte geçiş garantisi sayamayız. C'nin uzunluğu da 162→153 değişti; etkiler ayrıştırılmadı.

WrittenCheck C için sırasıyla 163 ve 154 kelime bildirdi. Yerel ölçüm UTF-8 metni boşluklardan bölerek 162 ve 153 sayıyor. Hizmetin farklı kelime/sentence ayrıştırması değiştirilmeden kaydedildi.

### Eski sonuç sorunu

B ilk adayının Seobaz formuna yazılmasından sonraki bir girişimde önceki analiz ekranda kaldı; açıklama yeni metinde olmayan eski bir cümleyi içeriyordu. Bu girişim **null** olarak kaydedildi, 36 puanı yeni adaya atanmadı. Form yenilenip gerçek yeni analiz yapıldı; sonuç 41 oldu. Ham eski ekran durumu da korunuyor. Formun değişmesi, sonucun yenilendiğini kanıtlamaz.

## Anlam ve üslup

Her aday `criteria.json` içindeki maddi koşullarla karşılaştırıldı. B ve C'de uydurma isim, tarih, deneyim veya başarı oranı eklenmedi; izin ve belirsizlikler korundu. B ikinci düzenlemede gereksiz tekrar kaldı; `assessment.json` bunu üslup kusuru olarak kaydediyor. Bu aday sadece Seobaz'ın insan etiketini aldığı için en iyi metin ilan edilmedi.

Yedi ayrı davranış görevi ve son kurallarla üç kısa kontrol görevi, belirtilen maddi ölçütleri karşıladı. Ham yanıtlar `regression-answers.json` ve `final-checks.json` içinde. Değerlendirmeyi hazırlayan asistan yaptı; bağımsız insan çalışması veya farklı model aileleri karşılaştırması değildir. Önceki mekanik aracın kodu değişmedi; önceki 21 test bu tur yeni yapılmış gibi sayılmadı.

## Dosyalar ve kanıt

- `samples/`: başlangıçlar, iki B adayı, C'nin ön ve nihai adayı.
- `detector-runs.json`: tüm geçerli/başarısız girişimler, zaman, puan, kaynak URL, metin hash'i.
- `evidence/`: gerçek tarayıcı sonuçları ve ekran görüntüleri.
- `assessment.json`: anlam kontrolü, üslup kusuru ve değerlendirme sınırları.
- `skill-version.json`: bu deneye eşlik eden nihai beceri dosyalarının hash'leri.

Sonuçların başarısız kısmı çıkarılmadı. Daha düşük puan için sahte anı, gizli karakter, kasıtlı yazım hatası veya zorunlu açıklamaların silinmesi uygulanmadı.

## Hizmetin hazır örneğiyle işlev kontrolü

WrittenCheck'in “İnsan metni” düğmesindeki 93 kelimelik örnek ayrıca çalıştırıldı: **0**, olası aralık **0–14**, “Büyük olasılıkla insan yazımı”. Site bunu Ömer Seyfettin'in Kaşağı metninden kamu malı alıntı olarak sunuyor; özgün baskıyla burada bağımsız karşılaştırma yapılmadı. Bu, becerinin ürettiği metin değildir ve bizim başarı sonucumuz olarak sayılamaz. Türü ve uzunluğu da B/C örneklerinden farklıdır. Yalnızca servisin her girdiye otomatik yüksek puan vermediğini gösteren bir işlev kontrolüdür.

Toplam: B/C için **10 geçerli ölçüm**, ayrı hazır örnek için **1 işlev kontrolü**, eski çıktı nedeniyle **1 geçersiz girişim**. Ham kayıtta 12 satır vardır.
