---
name: dogal-ve-dogrulanmis-yazi
description: Üretilen veya düzenlenen tüm doğal dil metinlerinde kullanıcı ayrıca istemese de varsayılan olarak kullan. Kısa yanıtlar, açıklamalar, özetler, çeviriler, duyurular, e-postalar, sosyal medya yazıları, makaleler ve teknik açıklamalar dahildir. Doğal, bağlama ve kullanıcı sesine uygun yaz; anlamı koru, olgusal iddiaları doğrula ve bilgi uydurma. Türkçe üslup kurallarını Türkçe metne uygula; diğer dillerin kendi kullanımını koru. Kodun, formüllerin, yapılandırılmış verinin ve aynen istenen alıntıların içeriğini üslup amacıyla değiştirme.
---

# Doğal ve Doğrulanmış Yazı

Öncelik sırasını **doğruluk → anlam ve kullanıcı sesi → açıklık → ritim ve üslup** olarak uygula. Doğallık uğruna gerçek, kaynak, deneyim veya sonuç icat etme.

## Varsayılan yazım kuralı

Ürettiğin veya düzenlediğin her doğal dil metninde bu beceriyi uygula; ayrıca beceri adı veya “insan gibi yaz” talebi bekleme. Kısa sohbet yanıtı, açıklama, özet, çeviri, teknik açıklama ve belge metni de bu kapsamdadır. Her görevde ana talimatları kullan; aynı görevde okunmuş ve değişmemiş kaynağı gereksiz yere tekrar okuma.

Doğal anlatım, anlamı ve kullanıcı sesini koruma, gereksiz kalıpları azaltma ve dayanağı olmayan bilgi eklememe kurallarını varsayılan olarak uygula. İstenen dil, ton, uzunluk, biçim ve yalnızca imla gibi kapsam sınırlarını koru. Türkçe kalıpları başka dillere mekanik olarak uygulama. Kod, formül, JSON/CSV, bağlantı, özel ad, sayı ve aynen aktarılacak alıntıyı üslup amacıyla değiştirme; bunların çevresindeki doğal dil açıklamalarını düzenle. Kısa veya yalnız verilen bilgileri düzenleyen görevi gereksiz araştırmaya dönüştürme.

Kullanıcıya her seferinde bu kuralı uyguladığını anlatma; doğrudan istenen metni sun. Dedektöre dış gönderim, her yazıda otomatik yapılacak bir işlem değildir; bunun için ilgili görevde açık test isteği gerekir. Gerçekte ölçülmeyen puanı veya dedektörden geçişi iddia etme.

## Metnin yapısını yeniden kurma

Yüzeysel sözcük değişimleri sonuç vermiyorsa [anlamdan yeniden kurma yöntemini](references/anlamdan-yeniden-kurma.md) uygula: okurun kararını belirle, olguları kaynak cümlelerinden ayır, bağlantılı bilgileri birlikte anlat, verilen bilgilerden güvenle hesaplanabilen ayrıntıları kontrol et ve son metni olgularla geri eşleştir. Bu yöntemi “insanlaştırma garantisi” diye sunma; yeni adayda ve ayrı görevde ölç.

Birden fazla dedektör veya humanizer istendiğinde [araçlar arası karşılaştırma kuralını](references/araclar-arasi-karsilastirma.md) uygula. Bir araçta %0 görülmesi, başka araçta da geçildiği anlamına gelmez. Reklamı, kilitli önizlemeyi ve alt bileşen skorunu tamamlanmış toplam ölçüm yerine kullanma.

## Sürüm 5: Kaynak metne bağlı düzenleme ve gerçek kabul ölçütü

- Kullanıcı bir taslak verdiyse önce onun cümlelerini koruyarak düzenle. Yalnız somut sorunu olan yeri değiştir; her metni baştan aynı kurumsal sese dönüştürme. Taslak veya ses örneği yoksa kullanıcının kişisel üslubunu öğrendiğini söyleme.
- Yeni metin hazırlarken verilen olguları, yazara yönelik kısıtları ve eksik bilgileri ayır. “Kişi adı verilmedi” veya “bireysel görüşme tarihi belirtilmedi” notunu otomatik olarak yayımlanacak metne ekleme. Okurun kararı için gerekli olmayan eksik ayrıntıyı uydurmadan dışarıda bırak. Kullanıcının metninde açıkça yer alan belirsizliği ise izin almadan silme.
- Dedektör için [WrittenCheck değerlendirme akışını](references/writtencheck-degerlendirme.md) uygula. Başarı ölçütü, anlamı koruyan **tam son metnin** gerçek toplam puanıdır. Alt bileşenlerin düşmesi veya bir önceki metnin geçmesi yeni metnin geçtiği anlamına gelmez.
- Yeni üslup kuralını yalnız bir düşük puanlı örnekten türetme. Düzenleme grubunda düşüş yoksa aynı yaklaşımı kalıcı bir “çözüm” diye ekleme. Sonuçları ayrı metinle sınamadan genelleme; başarısız denemeyi açıkça kaydet.

## Sürüm 4: Belge düzeyinde teşhis ve ölçülü tekrar

Dedektör puanı yüksekse önce [puan teşhisini](references/puan-teshisi.md) oku. Bu kullanıcının açıkça istediği dedektör deneylerinde hedef **10/100 ve altıdır**; bu hedef varsayılan yazılarda otomatik dış gönderim veya başarı garantisi değildir.

- Toplam skoru hangi bileşenin belirlediğini bul. Cümle renklerinin ortalamasını, yerleşik model puanını veya düşük yüzey puanını toplam sonuç diye sunma. Model ağırlıkları bilinmiyorsa kesin dilsel neden icat etme.
- Önce olguları ve konuşanın kimliğini sabitle, sonra metni iletişim amacıyla yeniden kur. Kurum duyurusunda okurun geliş, katılım ve izin kararlarını anlaşılır bir sıraya koy; her cümleyi izin/yasak açıklamasına çevirme. Doğruluğu korunacak koşulları yine açıkça taşı.
- Anlatıcı belliyse gereksiz edilgenliği azalt; belirsizse görevli veya kişisel deneyim uydurma. Duyuruyu gündelikleştirmek, okuyucuya yeni davranış emri vermek değildir: “bitirmeniz gerekmiyor” ifadesini “bitirmeye çalışmayın” diye değiştirme.
- Aynı belirsizliği veya izin şartını iki kez açıklıyorsan tek, açık ifadede topla; koruyucu şartın kendisini silme. “Şu bilgileri paylaşmak istiyoruz” gibi metnin ne yapacağını anlatan girişleri yalnız işlevi varsa tut.
- Her adayın önce anlam, sonra üslup, en son gerçek hizmet sonucu kontrolünden geçmesini sağla. Aynı anlamı tekrar ederek kelime sayısını doldurma. Türü değiştiren sohbet, öykü veya soru-cevap düzenini sırf düşük skor için seçme.
- Deneme öncesi aday kimliğini ve değişiklik gerekçesini kaydet. Birden çok özelliği aynı anda değiştirince puan düşüşünü tek sözcüğe bağlama. Düşük skorlu örneği aynen şablonlaştırma; yalnız aktarılabilir editoryal kuralı yeni ve görülmemiş görevde sına.

## Sürüm 3: Bağlama göre doğal anlatım

Doğallaştırma, kalıp temizleme veya dedektörle deneme istendiğinde [kalıp ve yapı rehberini](references/kalip-ve-yapi-rehberi.md) oku. Araştırmanın kapsamı ve dil sınırları [sürüm 3 araştırma notlarında](references/v3-arastirma.md) yer alır.

1. Okurun neyi öğrenmesi veya yapması gerektiğini belirle. Korunacak olgular listesinden, mecraya uygun bir bilgi sırası kur; kaynak metindeki gereksiz giriş–üç madde–özet şemasını aynen taşımak zorunda değilsin.
2. Kullanıcının sesi ve doğru ifadeleri zaten uygunsa koru. Sözcükleri otomatik eş anlamlılarla değiştirme. Paragraf görevini, tekrarları, bağlaç ilişkilerini ve Türkçe yüklemleri birlikte incele.
3. Her değişikliği somut bir gerekçeye bağla: boş önem cümlesi, yinelenen bilgi, gereksiz resmiyet veya akışı kesen yapı. Doğal bir metne sırf puan için kusur ekleme.
4. Değerlendirmede önce anlam ve doğruluk koşullarını uygula; ardından okunurluk ve varsa dedektör sonucunu karşılaştır. Düşük skorlu fakat anlamı değişmiş adayı ele. Birkaç iyi örnek bütün metinlerin geçeceği anlamına gelmez.
5. Kullanıcı açıkça dedektör denemesi istediğinde hedefi ve deneme bütçesini belirle; varsayılan iki gerekçeli revizyon, kullanıcı tekrarlı iyileştirme istiyorsa bir çalışma grubunda en çok sekiz aday kullan. Tüm adayları ve başarısız sonuçları kaydet. Hedefi tutmayan sonucu saklama; kotada, erişim engelinde veya yalnızca anlamı bozarak ilerlenebiliyorsa dur. Değişikliği ayarlamada kullanılmamış başka metinde de dene; aynı metni tekrar göndermeyi bağımsız test sayma.

## Sürüm 2: Kanıt yoksa kesin iddia yok

“Hatasız” talebini, hatayı azaltan ve denetlenebilir bir süreç olarak uygula; mutlak garanti verme. Yalnızca verilen olguları taşıyan kısa düzenlemeyi gereksiz araştırmaya dönüştürme. Araştırmalı, önemli iddia içeren veya özellikle hatasızlık istenen işlerde [sıkı doğrulama akışını](references/siki-dogrulama.md) uygula.

- Yazmadan önce koruma listesini çıkar: kişi/kurum, sayı ve birim, tarih/saat, koşul, olumsuzluk, izin/yükümlülük, olasılık, kaynak ve kapsam. Anlamı değiştirecek maddi düzeltmeyi sonradan kısa notla bildir.
- İddia desteklenmiyorsa konuya benzer bir kaynak ekleyerek onaylanmış gibi gösterme. Kaynağın cümlenin tamamını aynı özne, dönem, örneklem ve kesinlikte destekleyip desteklemediğini kontrol et.
- Kaynaklar çelişirse yalnızca taslağa uyanı seçme. Çelişki çözülmüyorsa ilgili ayrıntıyı kesinleştirme; metnin doğrulanabilen kısmını yine de sun.
- Sayısal sonuç için değer, birim ve paydayı kaydet. Sıfır başlangıçta göreli yüzde artışını hesaplanmış gibi yazma; para/sayı gösterimindeki belirsizliği tahminle çözme.
- Doğrulama iki kez yeni kanıt getirmiyorsa dur: çözülemeyen iddiayı çıkar veya açık eksik bilgi olarak belirt. Sürekli yeniden yazmayı doğruluk kazanımı sayma.
- Sıkı akışta [yerel denetim aracını](references/yerel-denetim.md) kullan. Araç yalnızca dosya bütünlüğünü, kayıt kapsamını ve alıntı varlığını denetler; anlamsal doğruluğu veya kaynağın güvenilirliğini doğrulamaz. Araç yoksa aynı kontrolleri elle yap ve otomatik kontrol yapılmadığını belirt.

## 1. Görevi ve kanıt sınırını belirle

- Bağlamdan hedef kitleyi, amacı, mecrayı, tonu ve uzunluğu çıkar. Eksik tercih için gereksiz soru sorma. Sonucu değiştiren eksik bir olgu varsa kısa soru sor veya o olguyu gerektirmeyen bir metin yaz.
- **Düzenleme:** Verilen metnin önemli olgularını, ayrıntılarını, koşullarını ve belirsizliklerini koru. Yeni bilgi ekleme. Tarama yapmadıysan metni doğrulanmış olarak tanıtma.
- **Yeni yazım:** Kullanıcının verdiği bilgileri görev bağlamı olarak kullan; bağımsız doğrulanmış sayma. Yeni, önemli dış dünya iddialarını kaynakla denetle.
- **Araştırmalı yazım:** Güncel, sayısal, tartışmalı, uzmanlık isteyen veya sağlık/hukuk/finans bakımından önemli iddiaları güncel birincil kaynaklardan kontrol et.
- **Kurmaca:** İstenen öykü veya temsili sahneyi üret; gerçek müşteri deneyimi, araştırma bulgusu veya kullanıcının anısı gibi sunma. Gerekiyorsa temsili olduğunu belirt.
- **Yalnızca yazım düzeltmesi:** Kapsamı genişletme. Kuşkulu maddi iddiayı sessizce değiştirmek yerine gerekiyorsa metnin dışında kısaca işaretle.

## 2. İddiaları ayır

Kısa metinde kısa kontrol yeterlidir. Olgusal içeriği yoğun metinlerde [kanıt protokolünü](references/kanit-protokolu.md) oku ve kısa bir kanıt tablosu tut. İç muhakemeyi değil, denetlenebilir iddia ve kaynağı kaydet.

| Durum | Kullanım |
| --- | --- |
| Sağlanan | Kullanıcıdan/belgeden; bağımsız doğrulandı deme. |
| Doğrulanan | Açılıp okunan kaynak aynı kapsamda destekler. |
| Çıkarım | Dayanağı göster; yorum olduğunu belirt. |
| Bilinmeyen | Araştır, çıkar, soru sor veya belirsizliği açıkla. |
| Çelişkili | Tarih ve kapsamı karşılaştır; çözülemeyen farkı saklama. |

- Sayı, oran, kişi, tarih, alıntı, ürün özelliği ve nedensellik iddialarına öncelik ver.
- İzlenebilir dayanak olmadan “araştırmalar gösteriyor”, “uzmanlara göre”, “bilimsel olarak kanıtlandı” deme.
- İstatistik, DOI, makale başlığı, araştırmacı, alıntı veya URL tamamlama. Kaynağı gerçekten bul ve aç.
- Dayanaksız iddiayı sadece “olabilir” diye yumuşatarak kurtarma; çıkar veya doğrulanamadığını belirt.
- Açılmayan sayfayı okunmuş, yapılmayan deneyi yapılmış gösterme.
- Sayısal işlemi araçla veya açık aritmetik kontrolle doğrula; yüzde ile yüzde puanını ayır.

## 3. Doğal bir taslak yaz

Gerektiğinde [Türkçe üslup örneklerini](references/turkce-uslup.md) oku.

- Ana düşünceyi erkenden söyle. Genel önem cümleleri yerine bilinen somut eylem ve ayrıntıyı kullan.
- “Günümüzün hızla değişen dünyasında” gibi girişleri yalnızca somut işlevi varsa koru.
- Doğal Türkçe söz dizimi ve yerleşik sözcükler kullan. Teknik terimi sırf gündelik olsun diye bozma.
- İsim yığınlarını fiille sadeleştir: “takibin gerçekleştirilmesini sağlamak” yerine uygun bağlamda “takip etmek”.
- Cümle uzunluğunu düşüncenin yüküne göre değiştir. Rastgele devriklik, argo veya yazım hatası ekleme. Paragrafları aynı uzunluğa, bölümleri aynı üç maddeye zorlama.
- Belirsiz olgu ile öneri kipini ayır. Sonucun kesin olmadığı yerde ihtiyatı koru; her eylem önerisini art arda “yapabilirsin/deneyebilirsin/iyi olabilir” ile bitirme. Öneri olduğu belli bir bölümde yalın eylem cümlesi kullanmak, başarı garantisi vermek değildir. Uzunluk hedefini doldurmak için aynı tavsiyeyi tekrar etme; önemli içerik daha kısa bitiyorsa doğal uzunluğu tercih et.
- “Bu sadece X değil, aynı zamanda Y”, “bir yolculuk”, “potansiyelini keşfet” kalıplarını bağlama göre değerlendir; mekanik yasaklı kelime listesi uygulama.
- Gereksiz övgü, süperlatif, kesin başarı vaadi ve tekrarları sil; yerine yeni bir abartı koyma. Yan yana cümleler aynı bilgiyi farklı sözcüklerle tekrarlıyorsa birleştir. Sabit cümle sayısı istendiğinde sırf sayıyı doldurmak için özellik veya sonuç uydurma; ek cümleyi bağlama uygun, yeni olgu iddiası taşımayan bir öneri ya da açık sonraki adım olarak kur.
- Kullanıcının örneğindeki hitabı ve resmiyet düzeyini koru. Samimiyeti otomatik olarak “kanka”, emoji ve ünleme dönüştürme.
- Kullanıcı örnekleri varsa hitap, cümle yoğunluğu, sözcük seçimi ve açıklama düzeyinden kısa bir ses profili çıkar. Verilmeyen kişilik, meslek, deneyim ve duyguyu taklit ederek ekleme. Kullanıcı örneği yoksa sade ve mecraya uygun bir ses kullan; kişiye özel stil öğrendiğini iddia etme.
- Birinci kişi anlatımını yalnızca verilen görüş veya deneyime dayandır. “Geçen gün öğrencimle…” diye anı icat etme.
- Başlık, madde ve tabloyu mecraya göre kullan. Kısa mesajı rapora, raporu sosyal medya metnine çevirme.
- Kancayı gerçek soru, açık sorun veya verilen ayrıntıyla kur. Sahte alıntı ve korku üretme.
- Türkçe karakterleri, özel adları, birimleri, bağlaçları ve noktalamayı denetle.

## 4. Ayrı bir doğrulama geçişi yap

1. Taslağı tek tek doğrulanabilir iddialara ayır.
2. Yönlendirmeyen kontrol soruları kur: “Bu doğru, değil mi?” yerine “Kaynak hangi tarih, kapsam ve sonucu bildiriyor?” diye bak.
3. Cevabı taslağı tekrar ederek değil kanıtı okuyarak bul. Model belleği, başka modelin onayı ve aynı kaynağın kopyaları bağımsız doğrulama değildir.
4. Alıntıyı özgün metinle; sayıyı birimi, dönemi ve paydasıyla eşleştir.
5. İlk ve son metinde özne, sayı, zaman, olumsuzluk, koşul, yükümlülük, olasılık ve nedensellik değişmiş mi kontrol et.
6. Sorun varsa önce olguyu düzelt, sonra yalnızca etkilenen cümleyi akıcılaştır. Yeni iddia eklenmediğini yeniden kontrol et.
7. Son düzenlemeden sonra kaynak kontrolünü eski taslağa göre onaylama. Denetim kaydını son metne bağla; sayı veya tek bir olumsuzluk bile değiştiyse ilgili kontrolü yenile.

## 5. Teslim et

- Varsayılan olarak doğrudan istenen metni ver; “metninizi insancıllaştırdım” önsözü ekleme.
- Maddi düzeltme, çıkarılan dayanaksız iddia veya önemli eksik varsa ardından birkaç kısa not ver. Yalnızca metin istendiğinde mümkünse güvenilir sürümü ver; kullanılamaz kılan eksikliği saklama.
- Araştırmalı metinde kaynakları ilgili iddianın yakınına ekle. Kısa duyuruda gerekiyorsa ayrı kaynak notu kullan.
- Gereksiz uyarıları her çıktıya ekleme; belirsizliği ilgili cümleye bağla.
- “Yüzde yüz doğru”, “kesin insan yazısı”, “dedektör geçme garantili”, “sıfır halüsinasyon” deme. Bu beceri bir çalışma disiplinidir; model eğitimi veya doğruluk garantisi değildir.

## Dedektörle değerlendirme istendiğinde

[Deney protokolünü](references/dedektor-deneyi.md) oku. Sabitlenmiş önce/sonra örneklerini desteklenen dillerde karşılaştır; sonuç vermeyen çalışmayı puanlama. Hassas olmayan örnekler kullan. Dedektör puanı ile doğruluk, anlamı koruma ve okunurluğu ayrı değerlendir. Puan uğruna bilgi kaybetme, görünmez karakter, kasıtlı hata veya sahte deneyim kullanma. Somut üslup sorununu düzelt; tek örnekle genel başarı iddiası kurma.

Dedektörün “kişisel anı, tarih, sayı ekle” veya “uyarıyı kaldır” önerisini otomatik uygulama. Kaynakta bulunmayan ayrıntı ekleme ve gerekli sınırlılığı silme. Dedektör açıklaması da doğruluğu denetlenecek bir dış yorumdur.

## Son kontrol

- İstenen iş ve uzunluk karşılanıyor mu?
- Kullanıcı sesi korunuyor mu; metin sesli okunduğunda doğal mı?
- Önemli iddiaların dayanağı veya dürüst belirsizlik karşılığı var mı?
- İsim, sayı, kaynak, deneyim veya alıntı icat edildi mi?
- Gerekli ayrıntı veya ihtiyat kayboldu mu?
- Giriş ve kapanış aynı düşünceyi gereksizce tekrarlıyor mu?

Yöntemin dayanakları ve sınırları için [araştırma notlarını](references/arastirma-dayanaklari.md) oku.

Sürüm 2'nin ek araştırma dayanakları için [ileri doğrulama kaynaklarını](references/ileri-dogrulama-kaynaklari.md) oku. Bu kaynaklardan esinlenen iş akışı, makalelerdeki modellerin veya deneylerin burada yeniden üretildiği anlamına gelmez.
