# DevOps Practices - USTP Nexus

## Project: USTP Nexus
## Version: v1.0
## Last Updated: Week 15
## Author: Cabot (DevOps Lead)

---

## 1. Automation

### CI/CD Pipeline
- Tool: GitHub Actions
- Trigger: every push to main branch
- Pipeline stages: Run Tests - Deploy to Render - Smoke Test
- Workflow file: .github/workflows/deploy.yml
- Deployment method: Render deploy hook via POST request
- Smoke test: curl GET / and assert HTTP 200 response

### Automated Testing
- Tool: pytest
- Command: python -m pytest tests/tests.py -v
- Runs on every CI trigger before deployment
- Deployment is blocked if any test fails
- 4 of 6 tests currently passing; 2 skipped pending BUG-001 fix

### Dependency Auditing
- Tool: pip-audit
- Run manually before major releases
- Results saved to docs/audit-results.txt
- 13 vulnerabilities identified in Week 11 across Flask, Pillow, and Setuptools

---

## 2. Collaboration

### Branching Strategy
- Main branch: main (production)
- Working branch: dev (integration)
- Feature branches: feature/description
- Bug fix branches: fix/description
- Defined in docs/scm-notes.md

### Pull Request Workflow
- No direct pushes to main
- All changes go through a named branch and PR
- PR template enforces: summary, type of change, screenshots, and testing checklist
- At least one team member reviews before merge

### Commit Message Convention
- feat: new feature
- fix: bug fix
- docs: documentation update
- refactor: code change with no functional impact
- chore: maintenance task

---

## 3. Monitoring and Logging

### Request Logging
- Implemented in app.py using Python logging module
- Logs every incoming request: method, path, IP address
- Logs every outgoing response: method, path, status code
- Per-endpoint logs for register, login, logout, and tasks
- Warning logs for unauthorized access attempts
- Error logs on 500 responses with exception detail

### Render Logs
- Accessible via Render dashboard - Logs tab
- Shows Gunicorn startup, request logs, and deploy output
- Used as evidence of live monitoring in Week 13

### Uptime
- Smoke test runs after every deploy to confirm availability
- Render free tier may spin down after inactivity (50+ second cold start)
- Upgrade to paid tier recommended for production use

---

## 4. Cloud and DevOps Improvement - Pipeline Optimization

### Improvement Added: workflow_dispatch trigger

Added manual trigger support to the CI/CD pipeline to allow the team to run the workflow on any branch without requiring a merge to main. This speeds up testing and debugging during development.

Added to .github/workflows/deploy.yml:

on:
  push:
    branches: [main]
  workflow_dispatch:

### Why This Was Chosen
- Low effort, high value - one line addition
- Allows the team to test the pipeline on fix branches before merging
- Reduces the number of merges needed just to verify pipeline behavior
- No additional cost or infrastructure required

### Alternatives Considered
- Dockerize the app: higher value but requires significant setup time
- Add staging environment: planned for Sprint 2 when database is added
- Add monitoring alert: requires paid Render tier or third-party service

---

## 5. Feedback Loop

### Development to Deployment
1. Developer creates feature or fix branch from dev
2. Code is committed and pushed
3. Pull request opened with description and checklist
4. Team member reviews and approves
5. PR merged into main
6. GitHub Actions runs automatically: test - deploy - smoke test
7. Green checkmark confirms successful deployment
8. Render logs confirm live requests are being served

### Issue Tracking
- Defects logged in docs/defect-log.md with severity and status
- Tech debt tracked in docs/tech-debt.md with target sprint
- Security risks tracked in docs/risk-register.md
- KPIs reviewed in docs/metrics-report.md each sprint

---

## 6. Release Process

### v1.0 Release Checklist
- CI green on main branch
- All non-known-bug tests passing
- Smoke test confirmed live on https://cs326-siam.onrender.com
- docs/architecture.md created
- docs/devops-practices.md created
- Git tag v1.0 applied to final commit on main
- Demo script prepared
