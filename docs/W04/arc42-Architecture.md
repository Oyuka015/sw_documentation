# arc42 Architecture Documentation - AppFlowy

## 1. Requirements & Goals

### 1.1 Requirements Overview
AppFlowy нь хэрэглэгчийн мэдээллийн нууцлалыг чандлан сахисан, Local-First архитектуртай Notion-той ижил төстэй тэмдэглэл болон төслийн менежментийн нээлттэй эхийн систем юм.

### 1.2 Quality Goals
1. **Privacy & Security (Local-First):** Мэдээлэл локал төхөөрөмж дээр хадгалагдана.
2. **Performance:** Rust lifecycle дээр санах ойн ашиглалтыг хамгийн бага түвшинд барина.
3. **Cross-Platform:** Desktop болон Mobile дээр ижил хэрэглэгчийн туршлага үзүүлнэ.

---

## 3. Scope & Context

### 3.1 Technical Context & Actors
* **External Actors:**
  * **Alex (Software Developer):** Кодны блок болон офлайн горимыг голчлон ашиглагч.
  * **Team Lead:** Канбан самбар болон төслийн төлөвлөлт ашиглагч.
  * **Guest Student:** Анхан шатны тэмдэглэл хөтлөгч.
* **Neighboring Systems:**
  * **Local File System:** Төхөөрөмжийн локал файл хадгалах хэсэг (SQLite DB).
  * **AppFlowy Cloud / Sync Service:** Олон төхөөрөмжийн хооронд өгөгдөл ижилсүүлэх (WebSocket/gRPC).

---

## 5. Building Block View

### 5.1 Level 1: Whitebox Overall System
AppFlowy систем нь дараах 3 үндсэн баганаас бүрдэнэ:

| Building Block | Description | Satisfied SRS Requirement IDs |
| :--- | :--- | :--- |
| **Flutter UI Layer** | Дэлгэцийн харагдац, Канбан, Текст эдитор | FR-01, FR-05, FR-08, FR-14 |
| **Rust Core Engine** | Өгөгдлийн логик, Индексжүүлэлт, Синтакс өнгө | FR-02, FR-10, FR-13 |
| **Persistence (SQLite)** | Өгөгдөл локалд хадгалах болон хайлтын систем | FR-03, FR-04, FR-06 |
| **Sync Manager** | Сүлжээний холболт болон серверийн ижилсүүлэлт | FR-07, FR-09, FR-11, FR-12 |
 