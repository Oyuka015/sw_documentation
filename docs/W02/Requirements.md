# AppFlowy Requirements (ISO/IEC/IEEE 29148)

### FR-01: Offline Document Editing
* **Statement:** The system **shall** allow users to create and edit workspace documents without an active internet connection.
* **Priority:** `shall`
* **Verification Method:** Test
* **Owner/Source:** Persona Alex (W1 Pain Point: Needs reliable offline access without network latency).

### FR-02: Kanban Board View
* **Statement:** The system **shall** render a Kanban board view that allows drag-and-drop task card reassignment.
* **Priority:** `shall`
* **Verification Method:** Test
* **Owner/Source:** Persona Alex (W1 Pain Point: Needs visual task tracking integrated with documentation).

### FR-03: Markdown Export
* **Statement:** The system **must** enable users to export any document page into a raw `.md` (Markdown) file.
* **Priority:** `must`
* **Verification Method:** Inspection
* **Owner/Source:** Persona Alex (W1 Pain Point: Avoids vendor lock-in and needs easy file portability).

### NFR-01: Application Startup Time
* **Statement:** The desktop application **shall** fully load the initial workspace in less than 2.0 seconds on standard hardware.
* **Priority:** `shall`
* **Verification Method:** Analysis
* **Owner/Source:** Persona Alex (W1 Pain Point: Frustrated by slow, electron-based desktop applications).

### NFR-02: Local Data Encryption
* **Statement:** The system **must** encrypt stored local user database files using AES-256 at rest.
* **Priority:** `must`
* **Verification Method:** Inspection
* **Owner/Source:** Persona Alex (W1 Pain Point: Data privacy concerns with cloud-hosted note apps).