# QA Plan – Pad Renting Management

## Sprint: 1

## QA Lead: Olaer

---

## 1. Test Levels

### Unit Testing

Tests individual Python functions in isolation. No database or UI involved.

- **Tool:** Pytest
- **Scope:** Auth logic (registration, login, logout), Pad logic (add_pad, delete_pad)
- **Owner:** Each developer tests their own story

### Integration Testing

Tests how multiple components work together (e.g., passing the in-memory array between auth and pad creation).

- **Tool:** Pytest
- **Scope:** Auth flows, Pad management flows
- **Owner:** QA Lead (Olaer)

### System Testing

End-to-end testing of the full application from the user's perspective.

- **Tool:** Manual testing via API/Swagger UI
- **Scope:** Full flow: register -> login -> add pad -> delete pad -> logout
- **Owner:** QA Lead (Olaer)

---

## 2. Entry Criteria

Testing begins only when:

- [ ] Feature branch has been pushed to GitHub
- [ ] Unit tests have been written for the feature in `tests/tests.py`
- [ ] PR has been opened and linked to the user story

---

## 3. Exit Criteria

A feature is considered done when:

- [ ] All unit tests pass with no failures
- [ ] Acceptance criteria from the backlog are verified
- [ ] QA Lead has signed off on the PR

---

## 4. Severity Levels

| Level | Name | Description | Example |
| ------- | ------ | ------------- | --------- |
| S1 | Critical | System is unusable; core feature is broken | Login returns 500 error for all landlords |
| S2 | High | Major feature is broken but workaround exists | Duplicate email allowed during registration |
| S3 | Medium | Feature partially works; minor data issue | Pad added but price saves as a string instead of float |
| S4 | Low | Cosmetic or trivial issue | Typo in error message |

---

## 5. Test Coverage Goals (Sprint 1)

| Feature | Unit Tests | Integration | Manual |
| --------- | ----------- | ------------- | -------- |
| Registration | ✅ | Planned | Planned |
| Login | ✅ | Planned | Planned |
| Add Pad | ✅ | Planned | Planned |
| Delete Pad | ✅ | Planned | Planned |
