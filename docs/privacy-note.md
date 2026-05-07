# Privacy Note — USTP Nexus

## Project: USTP Nexus
## Version: v0.8
## Last Updated: Week 12
## Author: Mesa (Documentation Lead)

---

## 1. Overview

This document describes what data USTP Nexus collects, why it is collected, how long it is retained, and what rights users have over their data. This applies to the current demo version of the system.

---

## 2. Data Collected

| Data | Where Collected | Why |
|------|-----------------|-----|
| Email address | `/register` endpoint | Used as the unique identifier for user accounts |
| Password | `/register` endpoint | Used for authentication; stored as SHA-256 hash, never plaintext |
| Task title | `/tasks` POST endpoint | Stores user-created tasks |
| Task due date | `/tasks` POST endpoint | Associates a deadline with each task |
| Session token | Browser cookie (server-side session) | Maintains login state across requests |

---

## 3. Data Not Collected

- Full name
- Phone number
- Physical address
- Payment information
- Device or browser information
- IP addresses (not logged)

---

## 4. Data Retention

USTP Nexus currently uses **in-memory storage only** (`users_db`, `tasks_db` in `app.py`). This means:

- All data is lost when the server restarts
- No data is written to a database or file system
- No backups are created
- Data does not persist between sessions

This will change if a persistent database is added in a future version.

---

## 5. Data Sharing

- No user data is shared with third parties
- No analytics services are integrated
- No advertising is used

---

## 6. User Rights

Even in this demo system, the following principles apply:

| Right | Status |
|-------|--------|
| Right to access their data | Not yet implemented - planned for future version |
| Right to delete their account | Not yet implemented - data clears on server restart |
| Right to know what is collected | Covered by this document |
| Right to opt out | Users can simply not register |

---

## 7. Security Measures

- Passwords are hashed using SHA-256 before storage
- Sessions use `HTTPONLY`, `SECURE`, and `SAMESITE=Lax` cookie flags
- All inputs are sanitized using `html.escape()` and length limits
- Sensitive configuration (e.g., `FLASK_SECRET_KEY`) is stored in environment variables, not in code

---

## 8. Contact

For privacy-related concerns, contact the Security Lead:
- **Galleros** - Security Lead, CS326 SIAM Team
