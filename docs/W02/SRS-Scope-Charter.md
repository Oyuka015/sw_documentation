# AppFlowy SRS Scope Charter

## 1. Included Features (In Scope)
* **Local-First Core:** Full offline functionality using local SQLite database engine.
* **Core Views:** Document editor (Rich Text), Kanban Board, and Grid Table view.
* **Data Export:** Exporting pages to Markdown (.md) and Plain Text (.txt) formats.
* **Cross-Platform Support:** Desktop clients (Windows, macOS, Linux).

## 2. Excluded Features (Out of Scope & Justification)
* **Multi-user Real-time Web Editing:** Excluded to maintain local-first security architecture and avoid complex WebSockets overhead in scope.
* **Third-party Plugin Marketplace:** Excluded to focus strictly on core editing stability for initial documentation milestones.

## 3. Postponed Features (Deferred)
* **Mobile App Synchronization (iOS/Android):** Deferred to W08+ sprint cycles to prioritize desktop document workflow stability.
* **Custom End-to-End Encrypted Cloud Sync:** Deferred pending local database schema stabilization.