# Tech Debt – USTP Nexus

## Project: USTP Nexus
## Sprint: 1
## Author: Mesa (Documentation Lead)
## Last Updated: Week 8

---

## What is Technical Debt?

Technical debt refers to shortcuts or suboptimal decisions made during development that will need to be addressed later. Left unresolved, tech debt slows down future development and increases the risk of bugs.

---

## Identified Technical Debts

| # | Debt | Location | Priority | Description |
|---|------|----------|----------|-------------|
| TD-01 | In-memory storage instead of a real database | `app.py` | High | `users_db` and `tasks_db` are plain Python lists/dicts that reset every time the server restarts. No data is persisted. |
| TD-02 | No input sanitization beyond basic validation | `src/main.py` | High | Inputs are only checked for empty values and format. No protection against injection or malicious strings. |
| TD-03 | Weak password hashing (SHA-256) | `src/main.py` | High | SHA-256 is not suitable for password hashing. Should use bcrypt or argon2 which include salting and work factors. |
| TD-04 | No error handling on API routes | `app.py` | Medium | If a request sends malformed JSON or missing fields, the app will crash with an unhandled exception instead of returning a clean error. |
| TD-05 | Functions have no docstrings | `src/main.py` | Low | Most functions lack documentation comments, making the codebase harder to maintain and onboard new developers into. |

---

## Selected Debt to Fix This Sprint

**TD-05 Functions have no docstrings**

This was chosen because it is low-risk, does not require changing logic, and immediately improves code readability and maintainability. It is a safe refactor to practice the process without breaking existing tests.

---

## Remaining Debts (Deferred)

| # | Debt | Target Sprint |
|---|------|--------------|
| TD-01 | In-memory storage | Sprint 2 (database integration) |
| TD-02 | Input sanitization | Sprint 2 |
| TD-03 | Weak password hashing | Sprint 2 |
| TD-04 | No error handling on API routes | Sprint 2 |
