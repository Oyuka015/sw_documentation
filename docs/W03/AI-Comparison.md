# AI ба Хүний SRS Аудит харьцуулалт (Use-Verify-Cite Workflow) - SRS v1.0

## 1. Ерөнхий тойм
Энэхүү баримт бичигт GPT-4 загвараар AppFlowy төсөлд зориулан үүсгүүлсэн SRS сурагч заалтуудыг багийн гишүүдийн боловсруулсан SRS-тэй харьцуулж, AI-ийн гаргасан зөрүү болон алдааг (Discrepancies) хэрхэн засаж сайжруулсныг аудитын лог хэлбэрээр баримтжуулав.

---

## 2. GPT-4 ба Хүний SRS харьцуулсан аудитын лог

| № | Оруулсан асуудал / Алдааны төрөл | GPT-4-ийн өгсөн эх сурвалж (AI Quote) | Зассан хувилбар (Proposed Correction) | Тайлбар ба зарчим (Bhatti / Chinchilla) |
|---|---|---|---|---|
| **1** | **Хэмжигдэх хязгааргүй тодорхойгүй заалт** *(Ambiguous & Unmeasurable NFR)* | *"The system should start quickly and provide a smooth user experience without long delays."* | *"The desktop application shall achieve full interactive workspace readiness within 1.5 seconds (p95) on a baseline dual-core x86_64 machine with 8GB RAM."* | GPT-4 нь "quickly", "smooth" гэх мэт хэмжиж болохгүй ерөнхий үг ашигласан. Chinchilla Ch. 7 (p. 97)-ийн дагуу нарийн хэмжигдэх хязгаар (`< 1500ms p95`) оруулав. |
| **2** | **Шаардлагын бүтэц буруу бичсэн** *(Violating 'Important info first')* | *"To ensure data safety, the app checks for inactivity and then if 300ms has passed, it saves the file into SQLite database."* | *"The system shall save all workspace document modifications directly to the local SQLite database within 300ms of user inactivity."* | AI нь баталгаажуулах логикийг эхэнд нь бичсэн. Bhatti Ch. 3 (p. 58)-ийн "State most important info first" зарчмаар шууд хэрэгжүүлэгдэх үр дүнг эхэнд нь оруулж засав. |
| **3** | **Тестийн процедур ба UI мок-ап хаягдсан** *(Missing Verification & Artifacts)* | *"FR-05: Users can drag and drop cards in Kanban view to change their status."* | *"FR-05: The system shall update a task card's status field immediately when the user drags the card into a different Kanban column."* <br>*(+ 3 алхамт тестийн дараалал болон UI Мок-ап зураг хавсаргав)* | AI нь зөвхөн хэрэглэгчийн хүслийг товч бичээд шалгах процедур болон шалгуур үзүүлэлтийг хаясан. Bhatti Ch. 5 (p. 96) "Use-Verify-Cite" зарчмаар тестийн алхмуудыг гүйцээв. |

---

## 3. Дүгнэлт ба рефлекс
AI нь шаардлагын анхны нооргийг хурдан гаргахад тустай ч хэмжигдэхүйц нарийн хязгаар (Measurable boundaries), шалгах тест процедур болон баримт бичгийн бүтцийн стандартыг баримтлахдаа алдаа гаргаж байв. Хүний оролцоотойгоор AI-ийн гаргасан тодорхойгүй заалтуудыг засаж, шалгаж болохуйц шаардлага болгон засав.