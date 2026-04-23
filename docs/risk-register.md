# Risk Register – USTP Nexus

## Project: USTP Nexus
## Sprint: 1

| # | Risk | Likelihood (1–5) | Impact (1–5) | Score | Mitigation | Owner |
|---|------|:-----------------:|:-------------:|:-----:|------------|-------|
| R01 | Team member becomes unavailable or drops the course, leaving user stories unowned | 2 | 5 | 10 | Redistribute story ownership immediately; all members must understand each feature at a high level | Tion (PM) |
| R02 | Authentication tokens or sessions are improperly managed, exposing user accounts | 2 | 5 | 10 | Enforce secure session handling and token expiry; conduct peer security review before merge | Galleros (Security) |
| R03 | Merge conflicts in GitHub due to uncoordinated parallel development | 4 | 4 | 16 | Enforce feature-branch workflow and PR reviews; no direct pushes to main | Cabot (DevOps) |
| R04 | Sprint velocity is underestimated and core features are not completed on time | 3 | 4 | 12 | Review story point estimates weekly; deprioritize low-priority stories if behind schedule | Tion (PM) |
| R05 | User passwords are stored in plaintext or with weak hashing | 2 | 5 | 10 | Use bcrypt or equivalent hashing library; reviewed by Security Lead before any auth merge | Galleros (Security) |
| R06 | Unclear or missing acceptance criteria cause rework after feature completion | 3 | 3 | 9 | Define and confirm acceptance criteria before development starts each sprint | Mesa (Docs) |
| R07 | QA testing is skipped due to time pressure, introducing bugs into the main branch | 3 | 4 | 12 | QA sign-off is mandatory before any PR is merged; testing evidence required in PR template | Olaer (QA) |
| R08 | Scope creep from new requirements disrupts sprint plan mid-sprint | 3 | 3 | 9 | New requirements go through formal change request process; backlog updated before sprint plan changes | Tion (PM) |
| R09 | Development environment inconsistencies cause "works on my machine" bugs | 3 | 3 | 9 | Document setup steps in README; use consistent Node/Python versions across the team | Cabot (DevOps) |
| R10 | Poor or missing documentation makes onboarding and handoff difficult in future sprints | 2 | 3 | 6 | Documentation Lead reviews and updates all docs at the end of each sprint | Mesa (Docs) |

---
