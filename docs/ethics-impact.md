# Ethics Impact Assessment — USTP Nexus

## Project: USTP Nexus
## Version: v0.8
## Last Updated: Week 12
## Author: Mesa (Documentation Lead)

---

## 1. Purpose

This document identifies the stakeholders affected by USTP Nexus, the potential ethical risks the system introduces, and the mitigations put in place to address them.

---

## 2. Stakeholders

| Stakeholder | Role | How They Are Affected |
|-------------|------|-----------------------|
| Landlords | Primary users | Register, manage pads and tasks through the API |
| Tenants / Boarders | Indirect users | Their rental information may be stored or referenced |
| USTP Students | Potential users | May use the system to find or manage boarding arrangements |
| Development Team | Builders | Responsible for secure and ethical implementation |
| Course Instructor | Evaluator | Reviews system for compliance with course requirements |

---

## 3. Potential Ethical Risks

| # | Risk | Who Is Affected | Severity |
|---|------|-----------------|----------|
| E-01 | User credentials stored insecurely (weak hashing) | Landlords, tenants | High |
| E-02 | Unauthorized access to task or pad data | Landlords | High |
| E-03 | No data deletion mechanism — users cannot remove their accounts | All users | Medium |
| E-04 | Lack of transparency about what data is collected | All users | Medium |
| E-05 | Session tokens not expiring, leading to prolonged unauthorized access | Landlords | Medium |
| E-06 | System used to collect tenant data without tenant consent | Tenants | High |
| E-07 | No rate limiting — system vulnerable to brute force login attacks | All users | Medium |
| E-08 | Error messages could leak system internals in future versions | Developers | Low |

---

## 4. Mitigations

| # | Risk | Mitigation Implemented |
|---|------|------------------------|
| E-01 | Weak password hashing | SHA-256 hashing implemented in `src/main.py::hash_password()`; bcrypt recommended for production |
| E-02 | Unauthorized access | `@require_login` decorator protects all sensitive endpoints |
| E-03 | No data deletion | Noted as a future enhancement; currently a demo system with no persistent database |
| E-04 | Lack of transparency | `docs/privacy-note.md` created to document data handling |
| E-05 | Sessions not expiring | Session hardened with `SECURE`, `HTTPONLY`, and `SAMESITE=Lax` flags |
| E-06 | Tenant data without consent | System is currently demo-only; no real tenant data is collected or stored |
| E-07 | No rate limiting | Identified in risk register (SEC-09); Flask-Limiter planned for production |
| E-08 | Error message leakage | Generic 404/500 handlers implemented in `app.py` |

---

## 5. Overall Ethical Assessment

USTP Nexus is a demonstration system built for academic purposes. It does not currently store data persistently and does not process real user data. The team has implemented foundational secure coding practices to prepare the system for responsible production use. Remaining risks are documented in `docs/risk-register.md` and are targeted for resolution before any real-world deployment.

---

## References

- [ACM Code of Ethics](https://www.acm.org/code-of-ethics)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- `docs/risk-register.md` — SEC-01 through SEC-10
- `docs/security-checklist.md`
