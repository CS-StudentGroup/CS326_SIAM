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
