# Release Notes – USTP Nexus

## Version: v0.8
## Release Date: Week 5
## Sprint: 1



## Overview

This release covers the initial implementation of core authentication and task management logic, along with QA infrastructure, branch protection rules, and source control management practices established in Weeks 3–5.

---

## What's New

### Authentication (Story 1, 2, 4)
- User registration with email and password validation
- Login with credential verification and password hashing
- Logout with session clearing

### Task Management (Story 3, 5)
- Create tasks with title and due date
- Delete tasks by ID with not-found handling

### QA & Testing
- 14 unit tests written using Pytest covering all Sprint 1 stories
- Defect log created and BUG-001 identified, logged, and resolved

---

## Bug Fixes

| Bug ID | Description | Fix |
|--------|-------------|-----|
| BUG-001 | `validate_password()` rejected valid 8-character passwords due to `> 8` instead of `>= 8` | Changed operator to `>= 8` |

---

## Branch & PR Activity

| Branch | Type | Status |
|--------|------|--------|
| `feature/week3-risk-register` | Feature | Merged |
| `feature/week4-qa-setup` | Feature | Merged |
| `bug/bug-001` | Bug | Merged |
| `fix/bug-001` | Fix | Merged |
| `feature/week5-scm` | Feature | Merged |

---

## Known Limitations

- Authentication is logic-only (no database or web framework yet)
- Integration and system testing planned for future sprints
- UI not yet implemented

---

## Next Release

Version v1.0 will include a working web interface, database integration, and full Sprint 1 feature deployment.
