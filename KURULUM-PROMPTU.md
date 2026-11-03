# Kurulum ve varsayılan kullanım promptu

Aşağıdaki metni beceriyi kuracağınız Codex ortamına yapıştırın. Depoyu indirmek, başka bir kullanıcının genel ayarlarını tek başına değiştirmez.

```text
Aşağıdaki GitHub deposundaki dogal-ve-dogrulanmis-yazi becerisini kur ve tüm doğal dil metinlerimde varsayılan kullan:
https://github.com/CyberfiTechh/pdrkocum-ai-beceriler

Kaynak klasör: .agents/skills/dogal-ve-dogrulanmis-yazi

1. Önce beceriyi oku. Bulunduğun ortamın desteklenen kişisel beceri kurulum yöntemini kullan; yalnızca bu projeye değil, destekleniyorsa kullanıcı genelinde kur. Mevcut aynı adlı beceriyi ve kullanıcı düzenlemelerini koruyarak güncelle.
2. Kurmakla yetinme: assets/AGENTS-yazi-kurali.md içindeki kuralı etkin kalıcı talimatlarıma ekle. Yerel Codex'te CODEX_HOME değerini kontrol et; tanımlı değilse ~/.codex kullan. Bu konumdaki dolu AGENTS.override.md varsa ona, yoksa AGENTS.md dosyasına mevcut içeriği silmeden ekle. Aynı işaretli kural bloğu varsa tekrar eklemek yerine güncelle. Kurulu becerinin gerçek yolunu kuralın yanına yaz. Yönetilen ortamda desteklenen kişisel beceri ve kalıcı talimat mekanizmasını kullan; desteklenmeyen bir ayarı etkinleştirmiş gibi gösterme.
3. Her görevde ürettiğin veya düzenlediğin tüm doğal dil metinlerinde bu beceriyi kullan. Kısa yanıt, açıklama, özet, çeviri, teknik açıklama, duyuru, e-posta, sosyal medya yazısı ve belge metni dahildir. Ayrıca becerinin adını söylememi bekleme.
4. Doğal yaz; anlamı, olguları, koşulları, kullanıcı sesini ve istenen biçimi koru. Bilgi, kaynak, sayı, anı veya test sonucu uydurma. Kod, formül, yapılandırılmış veri ve aynen aktarılacak alıntıları üslup amacıyla değiştirme.
5. Dedektöre her metni otomatik gönderme. Açık test talebimde 10/100 ve altını hedefle; yalnızca gerçekten ölçülen sonucu bildir ve başarı garantisi verme.
6. Kurulum sonunda hem becerinin hem kalıcı kuralın yüklendiğini doğrula. Mümkünse ayrı bir görevde beceri adı verilmeden kısa bir metin isteğiyle dene. Dosyanın varlığını otomatik kullanım kanıtı sayma. Hangi ortam ve kullanıcı kapsamında etkin olduğunu, varsa doğrulayamadığın kısmı açıkça bildir. Mevcut talimatları silme ve daha yüksek öncelikli talimatların önüne geçmeye çalışma.
```

Yerel Codex için dayanaklar (3 Kasım 2026 tarihinde kontrol edildi):
- https://learn.chatgpt.com/docs/agent-configuration/agents-md
- https://learn.chatgpt.com/docs/build-skills

Genel kural yeni görev/oturum başlangıcında yüklenir; daha yakın proje talimatları etkili olabilir. Farklı cihaz, hesap, profil ve yönetilen ortamların kapsamı ayrıca doğrulanmalıdır. Bu prompt model davranışına veya dedektör sonucuna mutlak garanti vermez.
