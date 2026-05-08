# Architecture - USTP Nexus

## Project: USTP Nexus
## Version: v1.0
## Last Updated: Week 15
## Author: Mesa (Documentation Lead)

---

## 1. Overview

USTP Nexus is a REST API built with Flask and deployed on Render. It allows landlords near the USTP campus to register, manage pads, and track tasks through HTTP endpoints. All business logic lives in src/main.py and is exposed through app.py.

---

## 2. Architecture Diagram

```
Client (curl / browser / Postman)
            |
            | HTTP Request
            v
+---------------------------+
|        Render             |
|   (Cloud Hosting - SG)    |
|                           |
|  +---------------------+  |
|  |    Gunicorn WSGI    |  |
|  +--------+------------+  |
|           |               |
|  +--------v------------+  |
|  |     app.py          |  |
|  |  Flask Application  |  |
|  |                     |  |
|  |  Routes:            |  |
|  |  GET  /             |  |
|  |  POST /register     |  |
|  |  POST /login        |  |
|  |  POST /logout       |  |
|  |  GET  /tasks        |  |
|  |  POST /tasks        |  |
|  |  DEL  /tasks/<id>   |  |
|  +--------+------------+  |
|           |               |
|  +--------v------------+  |
|  |     src/main.py     |  |
|  |  Business Logic     |  |
|  |                     |  |
|  |  register_user()    |  |
|  |  login_user()       |  |
|  |  logout_user()      |  |
|  |  create_task()      |  |
|  |  delete_task()      |  |
|  |  hash_password()    |  |
|  |  sanitize_input()   |  |
|  +--------+------------+  |
|           |               |
|  +--------v------------+  |
|  |  In-Memory Storage  |  |
|  |  users_db (dict)    |  |
|  |  tasks_db (list)    |  |
|  +---------------------+  |
+---------------------------+
            |
     GitHub Actions
   (CI/CD on push to main)
   test -> deploy -> smoke test
```

---

## 3. Components

### app.py - API Layer
- Handles all HTTP routing and request/response formatting
- Validates JSON input on all POST endpoints
- Applies require_login() decorator to protected routes
- Configures session security (HTTPONLY, SECURE, SAMESITE)
- Handles 404 and 500 errors with generic messages

### src/main.py - Business Logic Layer
- Contains all core functions for user and task management
- Handles password hashing (SHA-256) and input sanitization
- Validates email format and password strength
- Keeps logic decoupled from the HTTP layer for testability

### In-Memory Storage
- users_db: Python dict mapping email to hashed password
- tasks_db: Python list of task objects with id, title, and due_date
- Note: data resets on server restart - database integration is planned for Sprint 2 (TD-01)

### Render (Cloud Hosting)
- Python 3.10 web service in Singapore region
- Gunicorn WSGI server
- Auto-deploys on push to main via deploy hook
- Free tier with spin-down on inactivity

### GitHub Actions (CI/CD)
- Trigger: push to main
- Jobs: Run Tests - Deploy to Render - Smoke Test
- Smoke test confirms GET / returns HTTP 200 after every deploy

---

## 4. Data Flow

### Registration
1. Client sends POST /register with JSON body (email, password)
2. app.py validates JSON content type and sanitizes inputs
3. register_user() checks for duplicate email and validates password strength
4. Password is hashed and stored in users_db
5. Response returned: success true or false with message

### Login
1. Client sends POST /login with JSON body (email, password)
2. app.py validates and sanitizes inputs
3. login_user() hashes the provided password and compares to stored hash
4. On success, email is stored in Flask session cookie
5. Response returned: success true or false

### Task Management
1. Client sends request to /tasks (GET, POST, or DELETE)
2. require_login() decorator checks for active session - returns 401 if not found
3. create_task() or delete_task() in src/main.py processes the request
4. tasks_db is updated and response returned

---

## 5. Security Architecture

- Authentication: Flask session with signed cookies
- Password storage: SHA-256 hashing (bcrypt planned for v1.1)
- Input validation: sanitize_input() with html.escape() and length limits
- Session hardening: HTTPONLY, SECURE, SAMESITE=Lax
- Secrets: FLASK_SECRET_KEY loaded from environment variables
- Error handling: Generic 404 and 500 messages prevent information disclosure

---

## 6. Known Limitations (Sprint 2 Targets)

- TD-01: In-memory storage resets on restart - no persistence
- TD-03: SHA-256 not suitable for production password hashing - upgrade to bcrypt
- SEC-09: No rate limiting - brute force attacks possible
- No frontend UI - API only in current version
