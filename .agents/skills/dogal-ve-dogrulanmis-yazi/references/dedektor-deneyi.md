# Dedektör karşılaştırma protokolü

Dedektör, belirli metnin bir araç tarafından nasıl sınıflandırıldığını gösterir. Yazarlığı, doğruluğu, özgünlüğü veya etik uygunluğu kanıtlamaz. Türkçe arayüz ile Türkçe analiz desteğini ayır; dil desteği beyanını bağımsız doğrulama sayma.

1. En az iki amaçta kimliksiz örnek hazırla. Önce/sonra sürümlerini testten önce sabitle. İkisi de yapay zekâ üretimiyse kaydet; “insan örneği” deme.
2. Özel öğrenci, müşteri veya kişisel veriyi üçüncü tarafa taşıma. Gerçek hassas metin gerekirse hizmet ve veri için belirli izin al.
3. Dil desteğini, asgari uzunluğu, kotayı ve giriş gereksinimini güncel arayüzde kontrol et. Destek belirsizse deneysel de.
4. Aynı çifti mümkünse iki hizmette karşılaştır. Etiket ve puanı aynen kaydet. AI olasılığı, AI metin payı ve insan olasılığı aynı ölçü değildir; ortalamasını alma.
5. Tarih/saat, URL, örnek kimliği, sözcük sayısı, SHA-256, puan, etiket ve görünen sürümü kaydet. Sürüm yoksa “açıklanmıyor” yaz. Ekran görüntüsü veya ham görünür sonuçla kanıt bırak.
6. Giriş, kota, CAPTCHA veya erişim engelini bildir. Sonuç yoksa puan null; sıfır değil. Engelleri aşmaya çalışma.
7. Anlamı, olgusal eklemeleri/çıkarmaları, dilbilgisini ve okunurluğu ayrıca kontrol et. Düşük puanlı ama yanlış metni başarısız say.

Tek puana göre sonsuz yeniden yazım yapma. Varsayılan iki gerekçeli düzeltme turu uygula; kullanıcı tekrarlı iyileştirme istiyorsa hedefi ve en çok sekiz adaylık çalışma grubunu kaydet. Hedefe ulaşılırsa anlam ve ayrı örnek kontrolüne geç; ulaşılmazsa tüm sonuçlarla birlikte açıkça bildir. Her adayı ayrı sürüm olarak kaydet. İkinci örneği ayar yaparken kullanma; değişikliği onda sına. Ayrılmamışsa bağımsız doğrulama deme.

Yazım hatası, sahte anı, görünmez karakter veya rastgele kelime ekleme. Düzeltmeyi açıklanabilir yap: dolgu giriş kaldırıldı, soyut ifade somutlaştırıldı, tekrar azaldı, belirsizlik korundu. Olumsuz sonuçları da raporla. Küçük örneklerden genel başarı oranı veya sıfır halüsinasyon sonucu çıkarma.

İnternetsiz yerel kelime sayımı ve anlam kontrolünü gerçek hizmet puanı yerine sunma.

## Sürüm 3: Sonucun doğru metne ait olduğunu kontrol et

Formdaki metnin değişmesi, analiz sonucunun yenilendiğini kanıtlamaz. Yeni çalışmanın tamamlandığını ve görünen alıntıların gönderilen metinde bulunduğunu kontrol et. Eski metne ait alıntı, sabit kalmış eski çıktı veya belirsiz işlem durumu varsa puanı yeni adaya yazma; `null` ve açıklama kaydet. Güvenli bir form yenilemesiyle tekrar dene; engel veya kota varsa dur.

Toplam belge skoru ile cümle renklerini ayrı kaydet. Çok sayıda yeşil cümle, belgenin insan etiketinde olduğunu göstermez. Hizmetin hazır insan örneği yalnızca bir işlev kontrolüdür; bağımsız, aynı tür ve uzunlukta insan kontrol grubu değildir.

Aynı gün, aynı metnin önbellekten dönmesi bağımsız tekrar ölçümü sayılmaz. Hizmetin kelime sayımı ile yerel boşluk tabanlı sayım farklıysa ikisini de belirt. Kalıp eşleşmesi sıfırken yüksek skor çıkabilir; bunu “yasak kelimeler bitti, artık kesin geçer” diye yorumlama.
