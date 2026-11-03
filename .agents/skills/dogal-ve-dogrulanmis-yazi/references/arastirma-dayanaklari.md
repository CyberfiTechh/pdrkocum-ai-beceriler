# Araştırma dayanakları

Araştırma tarihi: 3 Kasım 2026. Özgün Türkçe iş akışına uyarlanan yöntemlerdir; bu becerinin etkinliğini doğrudan sınayan yayımlanmış bir çalışma yoktur. Kaynak içerikleri kopyalanmamıştır.

## İddia düzeyinde doğruluk

Min ve arkadaşları, *FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation*, EMNLP 2023.
https://aclanthology.org/2023.emnlp-main.741/

İncelenen: PDF'deki yöntem açıklamaları ve özet. Uzun metni küçük olgusal iddialara ayırıp kanıtla eşleştirme yaklaşımı. Uygulama: önemli iddiaları tek tek kontrol et. Özgün FActScore yazılımını çalıştırmış gibi davranma; geçmiş model sonuçlarını bu beceriye aktarma. Kaynak desteği, gerçekliğin eksiksiz ölçüsü değildir.

## Taslaktan ayrı kontrol

Dhuliawala ve arkadaşları, *Chain-of-Verification Reduces Hallucination in Large Language Models*, Findings of ACL 2024.
https://aclanthology.org/2024.findings-acl.212/

İncelenen: 16 sayfalık PDF'nin ilk 5 sayfası, yöntem ve deney kurulumu. Uygulama: taslak → kontrol sorusu → kanıta bakma → düzeltme. Makaledeki yaklaşım dış araç kullanmaz; burada eklenen web/belge doğrulaması bir tasarım tercihidir. Öz eleştiriyi bağımsız doğrulama sayma. Bütün deney sonuçları okunmuş değildir.

## Belirsizliği kabul etme

OpenAI, *Why language models hallucinate*, 5 Eylül 2025.
https://openai.com/index/why-language-models-hallucinate/

İncelenen: Araştırma açıklaması; tahmini belirsizlik ifadesine tercih eden değerlendirme teşviklerinin sorunları. Uygulama: bilinmeyeni açık bırak, kaynak veya rakam tamamlama. Kaynak, uydurmayı tamamen engelleyen prompt kanıtı değildir.

## Dedektör sınırları

Sadasivan ve arkadaşları, *Can AI-Generated Text be Reliably Detected?*, arXiv:2303.11156, v4, 17 Ocak 2025.
https://arxiv.org/abs/2303.11156

İncelenen: Özet ve sürüm bilgisi; tüm deneyler ve ispatlar değerlendirilmedi. Uygulama: tek puanı yazarlık kanıtı sayma, geçme garantisi verme. “Hiçbir dedektör çalışmaz” sonucunu da çıkarma. Türkçe için ayrı veri ve dil desteği gerekir.

## Açık anlatım

GOV.UK, *Use clear language*.
https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/writing-guidelines/clear-language/

İncelenen: Resmî içerik rehberi. Uygulama: gereksiz soyutluğu, jargonu ve dolgu cümlelerini azalt. İngilizce sözcük uzunluğu eşiklerini Türkçeye taşıma. Dedektör performansı kanıtı değildir.

## Türkçe noktalama

Türk Dil Kurumu, *Noktalama İşaretleri (Açıklamalar)*.
https://tdk.gov.tr/icerik/yazim-kurallari/noktalama-isaretleri-aciklamalar/

Erişim: Arama sonucu sayfayı ve giriş kurallarını gösterdi; tam sayfa açma girişimi 502 hatası verdi. Tam metin okunmuş değildir. Ayrıntı gerektiğinde resmî kaynağa yeniden eriş; erişilemeyen kuralı uydurma.

## Codex biçimi

OpenAI, *Build skills*.
https://learn.chatgpt.com/docs/build-skills

İncelenen: Resmî beceri biçimi, aşamalı yükleme ve yerel yükleme bölümleri. Uygulama: kısa SKILL.md ve gerektiğinde okunan references. Haricî ücretli hizmet bağımlılığı yok. Standart Codex kullanıcı yolu ~/.agents/skills, proje yolu .agents/skills. ChatGPT Work kişisel becerileri kendi yönetilen kurulumu üzerinden yükler.
