# Support Plan – USTP Nexus

## Project: USTP Nexus
## Version: v0.5
## Last Updated: Week 7

---

## 1. Support Process

When a bug or issue is found:

1. **Report it** - open a GitHub Issue using the Bug Report template
2. **Log it** - add the bug to `docs/defect-log.md` with a Bug ID, description, and severity
3. **Assign it** - Project Manager (Tion) assigns the bug to the responsible developer
4. **Fix it** - developer creates a `fix/<bug-id>` branch and submits a PR
5. **Verify it** - QA Lead (Olaer) confirms the fix before the PR is merged
6. **Close it** - update the defect log status to ✅ Closed

---

## 2. Issue Reporting

All issues must be reported through GitHub Issues using the provided templates:

- **Bug Report** - for broken features or unexpected behavior
- **Feature Request** - for new requirements or enhancements

**Do not** report issues through chat or verbal communication only - everything must be tracked on GitHub.

---

## 3. Severity & Response Times

| Severity | Level | Description | Response Time | Resolution Target |
|----------|-------|-------------|---------------|-------------------|
| S1 | Critical | System is completely down or unusable | Within 2 hours | Within 24 hours |
| S2 | High | Major feature broken, no workaround | Within 4 hours | Within 48 hours |
| S3 | Medium | Feature partially works | Within 1 day | Within 1 week |
| S4 | Low | Cosmetic or minor issue | Within 1 week | Next sprint |

---

## 4. Escalation Path

| Step | Who | When |
|------|-----|------|
| 1st | Assigned Developer | Bug is first reported |
| 2nd | DevOps Lead (Cabot) | If fix requires repo or environment changes |
| 3rd | Security Lead (Galleros) | If bug involves auth or user data |
| 4th | Project Manager (Tion) | If unresolved after response time |

---

## 5. Common Issues & Fixes

| Issue | Likely Cause | Fix |
|-------|-------------|-----|
| App not loading on Render | Failed deployment | Check Render build logs; rollback if needed |
| Login not working | Wrong credentials or session issue | Clear browser cookies and retry |
| Registration rejected | Duplicate email or weak password | Use a unique email and 8+ character password |
| Task not saving | Empty title or due date | Ensure both fields are filled in |

---

## 6. Contacts

| Role | Name | Responsibility |
|------|------|---------------|
| Project Manager | Tion | Overall coordination and escalation |
| QA Lead | Olaer | Bug verification and test sign-off |
| DevOps Lead | Cabot | Deployment and repository issues |
| Documentation Lead | Mesa | Keeping support docs updated |
| Security Lead | Galleros | Auth and security-related bugs |
