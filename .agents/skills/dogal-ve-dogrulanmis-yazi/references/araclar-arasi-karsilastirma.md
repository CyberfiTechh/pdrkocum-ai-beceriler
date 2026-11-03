# Araçlar arası karşılaştırma

Kullanıcı dış test istediğinde aynı başlangıç ve son metni, değiştirmeden, erişilebilen araçlara gönder. Her araç için metin kimliği, SHA-256, dil, kelime sayısı, tarih, toplam puan, görünür etiket ve erişim durumunu ayrı kaydet. Puanları ortalayıp bir insanlık yüzdesi üretme. Bir araçta düşük skor başka araçta başarı anlamına gelmez.

Humanizer hizmetinin reklamı, örnek animasyonu veya kilitli sonuç kartı gerçek karşılaştırma ölçümü değildir. Tam çıktı görülmeden anlam denetimi ve bağımsız dedektör testi yapılmış sayılmaz. Hizmetin kendi “her dedektörü geçer” iddiasını garanti olarak aktarma. Üyelik, ücret ve insan doğrulaması engellerini puan yerine açık durum olarak kaydet; sonuç alanı boş/null kalır.

## 3 Kasım 2026 deneyi

Kimliksiz veli duyurusu R0: ZeroGPT %93,1. Aynı olguları okurun katılım kararına göre yeniden düzenleyen A3: ZeroGPT %0, WrittenCheck %100. A3 WrittenCheck alt bileşenleri: yerleşik model 10, yüzey 5; toplamı belirleyen derin model 100. Bu tek çift, üslup değişikliklerinin bir araçta etkili olup diğerine taşınmayabileceğini gösterir; genel başarı oranı veya kesin dilsel neden çıkarılamaz. Metinler eşit uzunlukta değildir (159 → 127 boşluk-kelimesi).

TextGuard tam çıktıyı hesap oluşturma ekranının arkasında tuttu; doğrulanmış humanizer çıktısı elde edilmedi. Copyleaks ve Pangram insan doğrulaması istedi; puan alınmadı. Listede yer alan diğer araçlar bu turda çalıştırılmadı.

Deney kayıtları: https://github.com/CyberfiTechh/pdrkocum-ai-beceriler/tree/main/tests/v6

Araç seçim kaynağı: https://aimultiple.com/tr/ai-generated-text-detector

Hizmetler: https://www.zerogpt.com/ · https://copyleaks.com/tr/ai-detector · https://www.pangram.com/tr · https://textguardai.com/humanizer

Bu kayıt, WrittenCheck için %10 hedefinin karşılandığını söylemez. Yeni metinlerde anlamı koruyan editoryal yöntem uygulanır; dedektör başarısı ancak o son metin gerçekten ölçülürse bildirilir.
