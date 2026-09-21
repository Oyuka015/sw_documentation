# Peer Review Аудит ба Хувилбарын зөрүү (v0.9 → v1.0) - SRS v1.0

## 1. Ерөнхий тойм
Энэхүү баримт бичигт өөр багийн (Peer Team) гишүүдээс SRS v0.9 ноорог дээр авсан шүүмж, санал хүсэлт болон тэдгээрийг хэрхэн тусгаж **SRS v1.0** хувилбар руу ахиулсан зөрүүг (Diff) баримтжуулав.

---

## 2. Peer Review-ийн сэтгэгдлүүд болон хийсэн засварууд

### Сэтгэгдэл 1: NFR-ийн хэмжигдэх стандарт тодорхойгүй
* **Шүүмжжүүлэгч:** Peer Team B (Confluence Comment #1)
* **Агуулга:** *"NFR-01 дээр 'хурдан ачаална' гэж бичсэн нь юугаар хэмжигдэх нь тодорхойгүй байна. Ямар систем дээр хэдэн секундэд ачаалах ёстой вэ?"*
* **Үйлдсэн засвар:** NFR-01-ийн тодорхойлолтод 8GB RAM-тай x86_64 компьютер дээр `< 1500 ms p95` гэсэн нарийн тоон шалгуур болон Akamai салбарын стандартын ишлэлийг нэмж засав.

### Сэтгэгдэл 2: FR-ийн шалгах дараалал дутуу
* **Шүүмжжүүлэгч:** Peer Team B (Confluence Comment #2)
* **Агуулга:** *"FR-07 (Markdown Export) болон FR-09 (Backup) дээр хэрэглэгч яаж шалгаж тест хийх нь тодорхойгүй байна."*
* **Үйлдсэн засвар:** FR-07 болон FR-09 дээр 3 алхам бүхий дарааллаар шалгах **Test Procedure** болон баталгаажуулах **Acceptance Criterion** хэсгийг шинээр нэмэв.

### Сэтгэгдэл 3: Аюулгүй байдлын шифрлэлтийн алгоритм тодорхойгүй
* **Шүүмжжүүлэгч:** Peer Team B (Confluence Comment #3)
* **Агуулга:** *"NFR-02 дээр зөвхөн 'шифрлэнэ' гэж бичсэн байна. Ямар шифрлэлтийн алгоритм ашиглахыг тодорхой болгох хэрэгтэй."*
* **Үйлдсэн засвар:** NFR-02-ийг `AES-256-GCM` болон `PBKDF2` түлхүүр үүсгэгч ашиглах ба `appflowy.db` файлыг шалгахад 0 энгийн текст олдох ёстой гэсэн заалтаар шинэчлэв.

---

## 3. Хувилбарын зөрүүний жагсаалт (v0.9 vs v1.0 Diff)

```diff
  ### NFR-01: Cold Startup Performance
- Statement: The desktop app should open quickly when clicked.
+ Statement: The desktop application shall achieve full interactive workspace readiness within 1.5 seconds (p95) on a baseline dual-core x86_64 machine with 8GB RAM.
+ Boundary: < 1500 ms p95 startup time (Benchmarked via Akamai standards).

  ### FR-07: Raw Markdown Export
  Statement: The system must export selected workspace pages into standard UTF-8 encoded .md files.
+ Test Procedure:
+   1. Create a page with H1, H2, and bullet points.
+   2. Click Export -> Markdown.
+   3. Open exported file in a raw text editor.
+ Acceptance Criterion: Output file contains valid standard Markdown formatting tags (#, ##, *).