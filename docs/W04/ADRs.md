# Architecture Decision Records (ADRs) - AppFlowy

Энэхүү баримт бичигт AppFlowy төслийн архитектурын гол шийдвэрүүдийг MADR (Markdown Architectural Decision Records) стандартын дагуу баримтжуулав.

---

## ADR Index

1. [ADR-01: Choice of Tech Stack (Flutter + Rust)](#adr-01-choice-of-tech-stack-flutter--rust)
2. [ADR-02: Local-First Persistence Strategy via SQLite](#adr-02-local-first-persistence-strategy-via-sqlite)
3. [ADR-03: Interface Communication via Dart-Rust FFI Bridge](#adr-03-interface-communication-via-dart-rust-ffi-bridge)

---

## ADR-01: Choice of Tech Stack (Flutter + Rust)

* **Status:** Accepted
* **Context:** 
  Notion зэрэг Electron дээр суурилсан тэмдэглэлийн програмууд нь RAM-г маш их хэмжээгээр ашиглаж, компьютерийг гацаадаг асуудалтай. Энэ нь манай **Persona Alex (Software Developer)**-ийн гол гомдол, бэрхшээл буюу pain point байсан. Бидэнд олон платформ дээр адил харагдах UI болон санах ойн өндөр гүйцэтгэл шаардлагатай байсан.
* **Decision:** 
  Frontend-д **Flutter (Dart)**, backend болон бизнес логик, тооцоололд **Rust** хэлийг хослуулан ашиглахаар шийдвэрлэв.
* **Consequences:** 
  * **Эерэг тал:** Rust дээр санах ойн ашиглалт эрс багасаж, Electron-той харьцуулахад хурд мэдэгдэхүйц нэмэгдсэн.
  * **Сөрөг тал:** Dart болон Rust хоёр өөр хэлний хооронд өгөгдөл солилцох нарийн тохиргоо шаардлагатай.

---

## ADR-02: Local-First Persistence Strategy via SQLite

* **Status:** Accepted
* **Context:** 
  Хэрэглэгчид сүлжээгүй эсвэл интернэт тогтворгүй орчинд тэмдэглэл болон Канбан самбараа ямар ч сааталгүйгээр үргэлжлүүлэн ашиглах шаардлагатай байсан.
* **Decision:** 
  Өгөгдлийг хамгийн эхэнд төхөөрөмж дээр **Local-First** зарчмаар **SQLite** баазад хадгалж, интернэтэд холбогдсон үед л cloud сервер рүү sync хийдэг бүтэц сонгов.
* **Consequences:** 
  * **Эерэг тал:** Офлайн орчинд 100% найдвартай, маш хурдан ажиллана. Мэдээллийн нууцлал өндөр.
  * **Сөрөг тал:** Олон төхөөрөмжийн хооронд нэгэн ижил өгөгдлийг зэрэг засах үед үүсэх зөрчлийг шийдвэрлэх хэрэгтэй болсон.

---

## ADR-03: Interface Communication via Dart-Rust FFI Bridge

* **Status:** Accepted
* **Context:** 
  Flutter UI болон Rust Core Engine хооронд өгөгдөл дамжуулахдаа дотоод REST API/HTTP ашиглавал latency үүсэж, хэрэглэгчийн туршлагад сөргөөр нөлөөлөх эрсдэлтэй байв.
* **Decision:** 
  UI болон Engine хооронд санах ойн түвшний шууд харилцаа үүсгэдэг **Dart-Rust FFI (Foreign Function Interface)** гүүрийг сонгон ашиглав.
* **Consequences:** 
  * **Эерэг тал:** Хоцролтгүй, санах ойн түвшинд шууд харилцах тул маш өндөр хурдтай.
  * **Сөрөг тал:** C-ABI болон аюулгүй санах ойн заагчийг (pointers) зөв удирдаж хөгжүүлэхэд ахисан түвшний мэдлэг шаардлагатай.