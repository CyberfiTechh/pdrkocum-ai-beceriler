# Yerel kanıt kaydı denetimi

Araştırmalı ve sıkı doğrulama gereken yazıda, son taslağın kaynak kaydını denetle. Basit bir yazım düzeltmesi için bu dosyaları üretme. Araç Python 3.9+ standart kütüphanesini kullanır; ağ bağlantısı kurmaz ve dosya değiştirmez.

## Kullanım

1. Tek bir çalışma klasörüne son metni `draft.txt`, gerçekten okunan kaynakların ilgili özgün metinlerini UTF-8 dosyaları olarak kaydet. Gereksiz kişisel veri veya tam telifli eser kopyalama; doğrulama için gereken kısa kısmı tut. Üçüncü taraflara gönderme yetkisi olmadan bu kayıtları yayımlama.
2. Dosyaların **ham baytlarından** SHA256 hesapla. Örneğin Python'da `hashlib.sha256(Path("draft.txt").read_bytes()).hexdigest()` kullan.
3. Aynı klasöre aşağıdaki şemayla `audit.json` oluştur. Örnek yer tutucularını gerçek değerlerle değiştir. `segments[].text` parçalarını sırayla birleştirdiğinde, boşluklar ve satır sonları dahil son metnin tamamı birebir oluşsun. Her olgusal iddiayı ayrı, kısa bir parça olarak kaydet; birleşik iddiaları böl. İddiayı denetimden kaçırmak için `other` olarak sınıflandırma.
4. `python3 <beceri-klasörü>/scripts/evidence_gate.py <çalışma-klasörü>/audit.json` çalıştır. Başarı çıkış kodu 0, kayıt/dosya hatası 1'dir. Araç ilk hatada durur; düzelt ve yeniden çalıştır.
5. Başarılı sonuçtan sonra **anlamsal incelemeyi ayrıca yap**: alıntı gerçekten bu iddiayı mı destekliyor, zaman/kapsam/olumsuzluk aynı mı, kaynak güvenilir mi, sınıflandırma doğru mu? Anlam ve doğal Türkçe son okumasını yap. Metin değişirse hash ve parçaları yeniden oluştur.

```json
{
  "version": 1,
  "draft_file": "draft.txt",
  "draft_sha256": "DOSYANIN_64_KARAKTER_SHA256_DEGERI",
  "sources": [{
    "id": "s1",
    "kind": "provided",
    "path": "source-1.txt",
    "sha256": "KAYNAK_DOSYASININ_SHA256_DEGERI",
    "origin": "Kullanıcının paylaştığı duyuru"
  }],
  "segments": [{
    "text": "Toplantı cuma 15.30'da.\n",
    "kind": "fact",
    "evidence": [{"source_id": "s1", "quote": "Toplantı cuma 15.30'da."}]
  }]
}
```

Parça türleri: `fact`, `inference`, `advice`, `opinion`, `fiction`, `uncertainty`, `other`. `fact` ve `inference` için en az bir kanıt gerekir. Çıkarımın yorum olduğu nihai yazıda anlaşılmalı; yazılım bunu denetlemez. Diğer türlerde kanıt listesi boş olabilir; önerinin içinde saklı olgusal iddia varsa onu ayrıca kaydet.

`kind: web` kaynakta `origin` gerçek HTTP(S) adresi; `retrieved_at` saat dilimli ISO 8601 erişim zamanı olmalı. Kayıt yalnızca gerçekten erişilen sayfaya dayanmalı. URL biçiminin geçmesi sayfanın açıldığını veya güvenilir olduğunu **kanıtlamaz**. `provided`, kullanıcının verdiği bilginin bağımsız doğrulandığı anlamına gelmez.

## Sınırlar ve hata davranışı

- Başarı durumu bilerek `MECHANICAL_CHECKS_PASSED_NEEDS_SEMANTIC_REVIEW` adını taşır. Bunu “doğruluk onayı” diye sunma.
- Hash, dosyanın kayıttan beri değişmediğini; alıntı kontrolü, bu dizenin kayıtlı metinde bulunduğunu gösterir. İkisi de gerçekliği veya iddia-alıntı ilişkisini kanıtlamaz. Yanlış bir iddia, ilgisiz ama dosyada bulunan alıntıyla mekanik kontrolü geçebilir.
- Parça kapsamı denetimi atlanan metni yakalar; yanlış sınıflandırılan olguyu yakalayamaz. İnsan/model incelemesi yine gerekir.
- Dosyalar UTF-8, her biri en çok 4 MiB olmalı. Mutlak yollar, klasör dışına çıkan yollar/simgesel bağlantılar ve yinelenen JSON anahtarları reddedilir. Kaydın kök klasörünü güvenilen bir çalışma klasörü olarak seç.
- Türkçe taslaktaki görünmez Unicode biçim karakterleri inceleme için durdurulur. Gereksizlerini temizle; başka dilin meşru gereksinimi varsa körlemesine silme ve otomatik kontrolün tamamlanmadığını söyle.
- Yalnızca mekanik kontrolleri geçti diye bir iddiayı yayımlama. Araç kullanılamıyorsa aynı eşleştirmeyi elle yap, otomatik doğrulama yapılmadığını açıkla. Araç sayı hesabı, intihal veya yapay zekâ dedektörü değildir.
