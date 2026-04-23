# QA Plan – USTP Nexus

## Project: USTP Nexus
## Sprint: 1
## QA Lead: Olaer
## Last Updated: Week 4

---

## 1. Test Levels

### Unit Testing
Tests individual functions or methods in isolation. No database or UI involved.
- **Tool:** Pytest
- **Scope:** Auth logic (registration, login, logout), task logic (create, delete)
- **Owner:** Each developer tests their own story

### Integration Testing
Tests how multiple components work together (e.g., a route calling a function that writes to the database).
- **Tool:** Pytest
- **Scope:** Auth endpoints, task endpoints
- **Owner:** QA Lead (Olaer)

### System Testing
End-to-end testing of the full application from the user's perspective.
- **Tool:** Manual testing / browser walkthrough
- **Scope:** Full user flows: register → login → create task → delete task → logout
- **Owner:** QA Lead (Olaer)

---

## 2. Entry Criteria

Testing begins only when:
- [ ] Feature branch has been pushed to GitHub
- [ ] Unit tests have been written for the feature
- [ ] PR has been opened and linked to the user story
- [ ] Code passes a basic code review from the DevOps lead

---

## 3. Exit Criteria

A feature is considered done when:
- [ ] All unit tests pass with no failures
- [ ] Acceptance criteria from the backlog are verified manually
- [ ] No open S1 or S2 bugs remain
- [ ] QA Lead has signed off on the PR

---

## 4. Severity Levels

| Level | Name | Description | Example |
|-------|------|-------------|---------|
| S1 | Critical | System is unusable; core feature is broken | Login returns 500 error for all users |
| S2 | High | Major feature is broken but workaround exists | Duplicate email allowed during registration |
| S3 | Medium | Feature partially works; minor data issue | Due date not saved with task |
| S4 | Low | Cosmetic or trivial issue | Button label has a typo |

---

## 5. Test Coverage Goals (Sprint 1)

| Feature | Unit Tests | Integration | Manual |
|---------|-----------|-------------|--------|
| Registration | ✅ | Planned | Planned |
| Login | ✅ | Planned | Planned |
| Logout | ✅ | Planned | Planned |
| Create Task | ✅ | Planned | Planned |
| Delete Task | ✅ | Planned | Planned |

---

## 6. Tools & Setup

- **Language:** Python
- **Framework:** Pytest
- **Test location:** `/tests/tests.py `
- **Run command:** `python -m pytest tests/tests.py -v`
