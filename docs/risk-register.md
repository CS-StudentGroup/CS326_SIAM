# Risk Register – Pad Renting Management

## Sprint: 1

| # | Risk | Likelihood (1–5) | Impact (1–5) | Score | Mitigation | Owner |
| --- | ------ | :-----------------: | :-------------: | :-----: | ------------ | ------- |
| R01 | Team member becomes unavailable, leaving critical user stories (like Add Pad) unowned | 2 | 5 | 10 | Redistribute story ownership immediately; all members must understand the core Python logic | Tion (PM) |
| R02 | Authentication tokens or sessions are improperly managed, exposing landlord data | 2 | 5 | 10 | Enforce secure session handling and token expiry; conduct peer security review before merge | Galleros (Security) |
| R03 | Merge conflicts in GitHub due to uncoordinated parallel development on `main.py` | 4 | 4 | 16 | Enforce feature-branch workflow and PR reviews; absolutely no direct pushes to main | Cabot (DevOps) |
| R04 | Sprint velocity is underestimated and core pad management features aren't completed on time | 3 | 4 | 12 | Review story point estimates weekly; deprioritize low-priority dashboard stories if behind schedule | Tion (PM) |
| R05 | Landlord passwords are stored in plaintext or with weak hashing | 2 | 5 | 10 | Use hashlib (sha256) or bcrypt; reviewed by Security Lead before any auth PR is merged | Galleros (Security) |
| R06 | Unclear acceptance criteria cause rework after feature completion (e.g., negative prices allowed) | 3 | 3 | 9 | Define and confirm input validation criteria before development starts each sprint | Mesa (Docs) |
| R07 | QA testing is skipped due to time pressure, introducing broken endpoints to the main branch | 3 | 4 | 12 | Pytest execution is mandatory before any PR is merged; testing evidence required in PR template | Olaer (QA) |
| R08 | Scope creep from new requirements (like adding tenant tracking too early) disrupts sprint plan | 3 | 3 | 9 | New requirements go through formal change request; backlog updated before sprint plan changes | Tion (PM) |
| R09 | Development environment inconsistencies cause "works on my machine" server errors | 3 | 3 | 9 | Document setup steps (requirements.txt); use consistent Python 3.10+ versions across the team | Cabot (DevOps) |
| R10 | Poor or missing documentation makes onboarding and deployment difficult | 2 | 3 | 6 | Documentation Lead reviews and updates all markdown files in `/docs` at the end of each sprint | Mesa (Docs) |

## Security Risks (Added Sprint 1 - Security Hardening)

| # | Risk | Likelihood (1–5) | Impact (1–5) | Score | Mitigation | Owner |
| --- | ------ | :-----------------: | :-------------: | :-----: | ------------ | ------- |
| SEC-01 | XSS (Cross-Site Scripting) vulnerability through unsanitized user input | 3 | 4 | 12 | Input sanitization implemented using `html.escape()` and length limits; all user inputs validated | Galleros (Security) |
| SEC-02 | Weak password requirements allowing brute force attacks | 3 | 5 | 15 | Strong password policy enforced: 8+ chars, uppercase, lowercase, digit/special char required | Galleros (Security) |
| SEC-03 | Hardcoded secrets (API keys, session keys) in source code | 4 | 5 | 20 | Flask secret key moved to environment variables; never commit secrets to repository | Cabot (DevOps) |
| SEC-04 | Known vulnerabilities in dependencies (13 CVEs detected) | 3 | 4 | 12 | Dependency audit implemented; Flask 3.1.0→3.1.3, Setuptools 65.5.0→78.1.1 upgrades required | Cabot (DevOps) |
| SEC-05 | Improper session management leading to session hijacking | 2 | 5 | 10 | Session cookies hardened: SECURE flag, HTTPONLY flag, SAMESITE=Lax; must run on HTTPS in production | Galleros (Security) |
| SEC-06 | User enumeration attacks through differential error messages | 2 | 3 | 6 | Generic error messages implemented for login; cannot determine if email exists | Galleros (Security) |
| SEC-07 | SQL Injection (future risk when database added) | 2 | 5 | 10 | Parametrized queries/ORM must be used when migrating to database; no string concatenation in SQL | Cabot (DevOps) |
| SEC-08 | Insufficient logging/monitoring of security events | 2 | 3 | 6 | Implement security event logging (failed login attempts, unauthorized access) in next sprint | Galleros (Security) |
| SEC-09 | Missing rate limiting allowing brute force login attempts | 3 | 4 | 12 | Implement Flask-Limiter with rate limits on /login and /register endpoints before production | Cabot (DevOps) |
| SEC-10 | HTTPS not enforced in production environment | 3 | 5 | 15 | All traffic must use HTTPS in production; implement SSL certificate and HTTP→HTTPS redirect | Cabot (DevOps) |
