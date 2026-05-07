# IP and Attribution — USTP Nexus

## Project: USTP Nexus
## Version: v0.8
## Last Updated: Week 12
## Author: Mesa (Documentation Lead)

---

## 1. License

This project is released under the **MIT License**. See `LICENSE` in the root of the repository for the full license text.

The MIT License was chosen because:
- It is simple and permissive
- It allows academic use, modification, and redistribution
- It requires attribution (copyright notice must be kept)
- It is appropriate for a student project that may be shared or reviewed publicly

---

## 2. Third-Party Libraries

All libraries used in this project and their respective licenses:

| Library | Version | License | Purpose |
|---------|---------|---------|---------|
| Flask | 3.1.0 | BSD 3-Clause | Web framework and routing |
| Gunicorn | 23.0.0 | MIT | WSGI HTTP server for production (Render) |
| Pytest | 8.3.5 | MIT | Unit testing framework |

All libraries are listed in `requirements.txt` and are installed via `pip`.

---

## 3. Assets Used

No external images, icons, fonts, or media assets are used in this version. USTP Nexus is a REST API with no frontend UI.

---

## 4. Code Attribution

All application code was written by the CS326 SIAM development team:

| Author | Role | Contribution |
|--------|------|--------------|
| Tion | Project Manager | Sprint planning, coordination, task management logic |
| Olaer | QA Lead | Test cases in `tests/tests.py`, acceptance criteria verification |
| Cabot | DevOps | GitHub repository setup, CI/CD pipeline, deployment to Render |
| Mesa | Documentation Lead | All files in `docs/`, PR templates, branch naming standards |
| Galleros | Security Lead | Auth logic, input validation, session hardening, security checklist |

---

## 5. External References and Resources

The following resources were referenced during development:

| Resource | URL | Used For |
|----------|-----|----------|
| Flask Documentation | https://flask.palletsprojects.com | API routing and session management |
| OWASP Secure Coding Practices | https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/ | Security implementation guidance |
| Python hashlib Documentation | https://docs.python.org/3/library/hashlib.html | Password hashing |
| Render Documentation | https://render.com/docs | Deployment configuration |
| GitHub Actions Documentation | https://docs.github.com/en/actions | CI/CD pipeline setup |
| pip-audit | https://pypi.org/project/pip-audit/ | Dependency vulnerability scanning |

---

