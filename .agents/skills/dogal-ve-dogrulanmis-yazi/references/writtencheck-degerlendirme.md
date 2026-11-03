# WrittenCheck değerlendirme akışı

## Hedef ve kapsam

Açık test isteğinde hedef 10/100 ve altıdır. Bu, bir hizmetin tek bir metne verdiği deneysel puandır; yazarlık, doğruluk veya gelecekteki geçiş garantisi değildir. Kullanıcının özellikle belirttiği hizmeti önceliklendir. API, widget veya başka dil seçerek farklı puanlayıcıyı aynı ölçüm gibi sunma.

## Ölçüm

1. Girdi metnini, olguları, amaç ve türü kaydet. Yeni taslakta eksik bilgiye ilişkin yazara verilmiş notları okura yönelik bilgi sanma. Düzenlemede ise kaynakta yayımlanmış koşulları koru.
2. Düzeltme gerekçesini ve aday kimliğini göndermeden önce yaz. Varsayılan iki gerekçeli revizyon; açık tekrar isteğinde bir grupta en çok sekiz aday. Sonucu olmayan adaya null yaz.
3. Türkçe metinde Türkçe dilini seç. Analizin bittiğini ve sonuçtaki alıntıların o adaya ait olduğunu kontrol et. Aynı metni önbellekten tekrar almak yeni deney değildir.
4. Toplamı, derin modeli, yerleşik modeli, yüzey sinyallerini, aralığı, güveni ve hizmet kelime sayısını ayrı kaydet. Düşük yüzey skoru ile yüksek belge skoru birlikte bulunabilir.
5. Anlam kontrolünden geçmeyen adayı düşük puan alsa bile ele. Gizlilik, gönüllülük, ücret, saat, süre, kayıt ve izin koşullarını puan uğruna çıkarma. Bir katılma seçeneğini emre dönüştürme.
6. Bütçe sonunda hedef tutmadıysa bunu açıkça söyle. Deneme grubunu gizlice büyütme; aynı sonucu veren eş anlamlı değişimlerini ilerleme sayma. Kullanıcının kendi taslağını küçük müdahalelerle korumak uygun bir sonraki yoldur; bunun da düşük puanı garanti ettiğini söyleme.
7. Bir değişiklik işe yararsa yönergeyi dondur, ayrı ve daha önce skoru görülmemiş görevde dene. Düzeltmede kullanılan örneğe bağımsız test deme. Yeni örnek başarısızsa genel çözüm iddiasında bulunma.

## Gözlemler ve sınırlar

3 Kasım 2026 tarihindeki kurulum sonrası 159 boşluk-kelimesi içeren sentetik veli duyurusu WrittenCheck'te 100 (92–100, yüksek güven), Seobaz'da 32 (18–46, orta güven) aldı. WrittenCheck 161 kelime saydı. Aynı WrittenCheck sonucunda derin model 100, yerleşik model 5 ve yüzey üslup sinyali 4 idi. Bu, hangi sözcüğün derin model kararına neden olduğunu açıklamaz.

Resmî açıklamaya göre derin model yanıt verdiğinde belge puanını o belirler; API/widget yerleşik modeli kullanır. Hizmetin 14 Ekim 2026 testinde yeniden sözcüklenmiş 35 Türkçe AI örneğinin 28'i 70 ve üzerinde işaretlenmişti. Bu hizmetin kendi beyanıdır, bağımsız doğrulama değildir. Kaynak: https://writtencheck.com/how-it-works (erişim 3 Kasım 2026).

Düşük skorlu bir metni evrensel şablon hâline getirme. Sözcük yasakları, rastgele cümle uzunluğu, yazım hataları, görünmez karakter, sahte anı, kişi veya kurum ekleme kullanma.

## Sürüm 5 sınaması

Aynı veli duyurusunun sekiz yeni düzenlemesi WrittenCheck’te ayrı ayrı 100 aldı. Hizmet kelime sayıları sırasıyla 126, 132, 129, 144, 144, 135, 116 ve 142 idi. Bilgi sırasını değiştirmek, kısaltmak, gündelik veya daha resmî anlatım kullanmak bu grupta toplamı düşürmedi. Ayrı bir görevde güncel yönergeyle üretilen 99 hizmet kelimelik servis e-postası da 100 aldı. Bu sürümün WrittenCheck hedefini çözdüğü söylenemez. Yeni kaynak-taslak koruma kuralları editoryal iyileştirmedir; dedektör başarısı kanıtı değildir. Ham çıktılar ve adaylar: https://github.com/CyberfiTechh/pdrkocum-ai-beceriler/tree/main/tests/v5

Son aday R8 ikinci hizmet Seobaz’da 23 (13–33, orta güven) aldı; 10 hedefi orada da tutmadı. Seobaz açıklaması ön kayıt yaptırmamak ile toplantının kaydının alınmamasını tekrar saydı. Bunlar ayrı olgulardır. Dedektörün yorumunu uygulamadan önce denetle; bu gerekçeyle iki bilgiden birini silme. Yeni metinlerde gerektiğinde “ön kayıt” ile “ses/görüntü kaydı” ayrımını açık yaz.
