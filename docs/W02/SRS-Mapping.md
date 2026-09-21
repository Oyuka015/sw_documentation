# IEEE-830 SRS Mapping Table for AppFlowy

| Section | IEEE-830 Section Name | Status | Justification / Notes |
| :--- | :--- | :--- | :--- |
| **1.1** | Purpose | complete | Defines the scope of AppFlowy as an open-source workspace. |
| **1.2** | Scope | complete | Outlines desktop and mobile applications with local-first storage. |
| **1.3** | Definitions, Acronyms | complete | Defines terms like Local-first, Offline-sync, and Rust-core. |
| **1.4** | References | complete | Links to Flutter, Rust, and AppFlowy GitHub repository. |
| **1.5** | Overview | complete | Describes the document organization. |
| **2.1** | Product Perspective | complete | Independent application with optional cloud synchronization. |
| **2.2** | Product Functions | complete | Document editing, Kanban board, Grid views, and Database management. |
| **2.3** | User Characteristics | complete | Developers, note-takers, and privacy-focused power users. |
| **2.4** | Constraints | complete | Must maintain offline functionality and cross-platform performance. |
| **2.5** | Assumptions & Dependencies| complete | Relies on Rust backend for performance and Flutter for cross-platform UI. |
| **2.6** | Apportioning Requirements| n-a | Post-MVP scope items are detailed in the Scope Charter, not split here. |
| **3.1** | External Interfaces | complete | File exports (Markdown, PDF), Database API, and Plugin interfaces. |
| **3.2** | System Features | complete | Core editing, offline sync, and workspace customization. |
| **3.3** | Performance Requirements | complete | Fast load times and low memory consumption via Rust core. |
| **3.4** | Logical Database Requirements | complete | Local SQLite / RocksDB storage architecture. |
| **3.5** | Design Constraints | complete | Open-source license (AGPLv3) and local-first architecture. |
| **3.6** | Software Quality Attributes| complete | Focus on Privacy, Reliability, and Maintainability. |