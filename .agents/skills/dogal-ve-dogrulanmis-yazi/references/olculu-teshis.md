# Sonuç değişmiyorsa teşhisi değiştir

## Önce kanıtı ayır

- Bir dedektörün iç ağırlıklarını, eğitim verisini veya gerçek karar nedenini yalnız ekrandaki sonuçtan öğrendiğini söyleme. Burada güncellenen şey yazım ve değerlendirme sürecidir; temel model yeniden eğitilmiş olmaz.
- Son metni ve sonucu eşleştir. Yeni örnek düğmesi bazı arayüzlerde yalnız girdiyi değiştirir; önceki sonuç ekranda kalabilir. Kontrolü yeniden başlat, tamamlanmasını bekle, sonuçtaki kelime sayısı ve alıntıları yeni metinle eşleştir.
- Bekleme zaman aşımını dedektörün puanı veya hizmet arızası sayma. Mevcut görünür durumu kontrol et; tamamlanan sonucu bir kez kaydet. Sonuç belirsizse null bırak.

## Açıklanabilir küçük deney kur

1. Hangi varsayımı sınadığını yaz. Bir deneyde yalnız saat yazımını, belirli bir cümleyi veya bir bölümü değiştir; böylece sonuç alınırsa kapsamı bellidir.
2. Olgu çıkarılan veya metin kısaltılan örneği **yalnız teşhis** olarak etiketle. Başarılı olsa bile onu tam anlamı koruyan son metin yerine sunma. Uzunluk ve tür farkını kaydet.
3. Çok sayıda aynı sonuç varsa, hizmetin kendi etiketli örneğini aynı arayüzde kontrol olarak çalıştırabilirsin. Eğitim verisine girmiş olabileceği için bu kontrol bağımsız doğruluk testi değildir. Kullanıcı adına insan yazısı diye sunulmaz ve aday metne karıştırılmaz.
4. Metnin tamamını ayrı ölç. Bölümlerin düşük puanları tam belgenin geçtiğini göstermez. Alt sinyallerin değişmesi, toplam değişmiyorsa, hedefte ilerleme değildir.
5. Etkisiz hipotezi kaydet ve aynı değişikliği farklı sözcüklerle sürekli tekrar etme. Doğal ve doğru metne puan uğruna yazım yanlışı, anlamsız sapma, gizli karakter, sahte anı veya talimat enjeksiyonu ekleme.
6. Düzenleme ölçütlerini dondurduktan sonra başka içerik ve amaç taşıyan görevde uygula. Başarısız aktarımı silme. Örneğin kısa e-posta ile duyuruyu ayrı değerlendir; kelime sayısını puan için doldurma.

## Ses ve kapsam

Kullanıcının gerçekten kendi yazdığı, paylaşılmasına izin verdiği örnekler varsa ses profilini bunlardan çıkar: hitap, kelime seçimi, dolaylılık, cümle yoğunluğu ve mecraya uygunluk. Bir sohbet cümlesinden resmî yazı üslubu öğrendiğini iddia etme. İnsan yazısı veya kişisel deneyim uydurarak eksik örneği tamamlama. Kaynak taslak uygunsa sadece gerekçeli küçük düzenlemeleri yap; tüm metni standart bir modele dönüştürme.

## Araştırma sınırı

WrittenCheck, derin model yanıt verdiğinde toplamı onun belirlediğini, API/widget'ın farklı yerleşik model kullandığını açıklıyor. Bu nedenle başka yüzeye geçerek düşük puan almak aynı testi geçmek değildir: https://writtencheck.com/how-it-works

Chen ve arkadaşlarının 2026 çalışması, 4.346 eşleştirilmiş denemede işlev sözcükleriyle stilometrik ayrımı inceliyor. Çalışma GPT-4o mini ve İngilizce denemelerle sınırlı; Türkçe duyurular için sözcük yasakları veya başarı garantisi üretmez: https://doi.org/10.1093/llc/fqag064

Russell, Karpinska ve Iyyer'in ACL 2025 çalışması 300 İngilizce kurmaca dışı makalede insan değerlendirmesini inceliyor. Değerlendiriciler söz varlığı yanında resmiyet, açıklık ve özgünlüğe de bakıyor. Buradan Türkçe dedektörün iç kararını bildiğimiz sonucu çıkmaz: https://aclanthology.org/2025.acl-long.267/

Bu kaynaklar deney tasarımına yardımcıdır; bu kullanıcının metinlerinin geçtiğine dair kanıt değildir. Gerçek yerel sonuçları deney kayıtlarıyla ayrı bildir.

## Bu çalışmadaki sonuç

3 Kasım 2026'da üç teşhis örneği, beş tam aday ve iki ayrı görev WrittenCheck'te 100 aldı; hizmetin kendi insan örneği 0 aldı. C5 yerleşik model 5 / toplam 100; insan kontrolü yerleşik model 43 / toplam 0. Alt skora göre en iyi adayı seçmek bu grupta işe yaramadı. Kesin dilsel neden bulunmadı; hedef karşılanmadı. Kayıt: https://github.com/CyberfiTechh/pdrkocum-ai-beceriler/tree/main/tests/v7
