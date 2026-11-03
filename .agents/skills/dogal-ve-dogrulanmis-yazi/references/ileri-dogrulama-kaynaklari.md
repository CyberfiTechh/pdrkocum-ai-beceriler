# İleri doğrulama araştırması

İnceleme: 3 Kasım 2026. Aşağıdaki sonuçlar kendi çalışma koşullarıyla sınırlıdır; bu becerinin performansını kanıtlamaz. Özgün metinler kopyalanmamıştır.

| Kaynak ve erişilen kapsam | Bulgudan alınan ilke | Uygulama ve sınır |
| --- | --- | --- |
| Gao ve ark., ALCE, EMNLP 2023. PDF, §3.3 ve sonuç tartışması. https://aclanthology.org/2023.emnlp-main.398/ | Akıcılık, doğruluk ve atıf desteği farklı ölçülerdir; bir atfın varlığı yeterli değildir. | Her iddianın kaynak pasajıyla desteklenmesini kontrol et. ALCE/NLI modeli bu pakette çalıştırılmıyor. |
| Gao ve ark., RARR, ACL 2023. PDF, yöntem özeti ve §8–9. https://aclanthology.org/2023.acl-long.910/ | Kanıtla düzeltirken metni korumak değerlidir; atıf yapılabilmesi kaynağın güvenilirliğini çözmez. Çelişkiler ayrı sorundur. | Kaynak güvenilirliği ve çelişki kontrolü ekle. Metni koruma, yanlış iddiayı koruma gerekçesi olamaz. |
| Huang ve ark., Large Language Models Cannot Self-Correct Reasoning Yet, ICLR 2024. Resmî konferans özeti. https://proceedings.iclr.cc/paper_files/paper/2024/hash/8b4add8b0aa8749d80a34ca5d941c355-Abstract-Conference.html | Dış geri bildirim olmadan öz düzeltme, incelenen akıl yürütme koşullarında başarısız olabilir. | Kaynağa geri dön; kendine tekrar sormayı doğrulama sayma. Tam makale okunmadı; bütün modern modeller için imkânsızlık sonucu çıkarılmıyor. |
| Farquhar ve ark., Detecting hallucinations in large language models using semantic entropy, Nature 2024. Tam metnin giriş, sınırlar ve yöntem başlangıcı. https://pmc.ncbi.nlm.nih.gov/articles/PMC11186750/ | Anlamsal belirsizlik bazı uydurma türlerini yakalayabilir; tutarlı ve sistematik yanlışları garantiyle çözmez. | Tutarlılığı gerçeklik sayma; öznel güven yüzdesi uydurma. Semantik entropi veya model eğitimi uygulanmış değildir. |
| Madhusudhan ve ark., Do LLMs Know When to NOT Answer?, COLING 2025. Özet ve PDF §7 sınırlar. https://aclanthology.org/2025.coling-main.627/ | Yanıtlanabilir sorulara cevap verme ile yanıtsız bırakılması gerekenleri ayırma birlikte değerlendirilmelidir. | Bilinmeyeni uydurma; bilinen kısmı gereksiz reddetme. Çalışmanın çoktan seçmeli düzenini açık Türkçe yazı performansına taşımıyoruz. |
| Wang ve ark., M4GT-Bench, ACL 2024. Resmî özet ve kaynak bilgisi. https://aclanthology.org/2024.acl-long.218/ | Alan ve üretici değişimi tespit performansını etkiler. | İki dedektör ve iki örnekten bütün metinlere geçme garantisi çıkarma. Tüm deney tabloları incelenmedi. |

TDK Sayıların Yazılışı sayfası ayrıca arandı. Arama özetine erişildi; doğrudan sayfa 502 verdi. Tam kılavuz okunmuş gibi sunulmadı: https://tdk.gov.tr/icerik/yazim-kurallari/sayilarin-yazilisi/

## Neden tek bir süper komut yeterli değil?

Kaynağın güvenilirliği, cümlenin kaynağı doğru aktarması, sayı işlemleri, son düzenlemenin anlamı koruması ve yazarın sesi farklı hata alanlarıdır. Bu beceri bunları ayrı kontrol eder. Mekanik kontroller dosya bütünlüğünü ve alıntı varlığını sınar; doğruluğun tamamını sınamaz. Ayrıca test seti hataları bulabilir, gelecekte hiç hata olmayacağını kanıtlayamaz.

## Bu sürümde seçilmeyen yöntemler

Modeli yeniden eğitme, API temelli semantik entropi, tüm metinleri dış dedektöre otomatik gönderme ve dedektör sıfıra inene kadar yeniden yazma uygulanmadı. Bu işlemler mevcut bir yönerge paketinden farklı altyapı, veri, izin ve değerlendirme gerektirir. Araştırılan yöntem ile gerçekten uygulanmış mekanizma ayrımı korundu.
