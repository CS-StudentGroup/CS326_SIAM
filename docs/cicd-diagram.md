# CI/CD Pipeline Diagram — USTP Nexus

## Project: USTP Nexus
## Week: 10
## Platform: Render (render.com)
## Trigger: Push to `main`

---

## Pipeline Stages

```
┌─────────────────────────────────────────────┐
│           Trigger: push to main             │
└─────────────────────┬───────────────────────┘
                      │
                      ▼
         ┌────────────────────────┐
         │         TEST           │
         │  python -m pytest      │
         │  tests/ -v             │
         └────────────┬───────────┘
              │               │
           pass             fail
              │               │
              ▼               ▼
         ┌────────┐     Pipeline stops
         │ DEPLOY │     No deploy triggered
         │        │
         │ POST → Render
         │ deploy hook  │
         └────────┬─────┘
                  │
                  ▼
         ┌──────────────────┐
         │   SMOKE TEST     │
         │  GET / → 200?    │
         └────────┬─────────┘
              │          │
            pass        fail
              │          │
              ▼          ▼
         ✓ Verified   Exit 1 (alert)
```

---

## Stage Details

### 1. Trigger
- Fires on every `git push` to the `main` branch
- Defined in `.github/workflows/deploy.yml`

### 2. Test
- Runner: `ubuntu-latest`, Python 3.10
- Command: `python -m pytest tests/ -v`
- Covers: `test_register_valid_user`, `test_add_pad_valid`, `test_delete_existing_pad`, etc.
- If any test fails: pipeline stops, deploy is skipped

### 3. Deploy
- Sends a `POST` request to the Render deploy hook URL
- Render rebuilds and restarts the service automatically
- Secret used: `RENDER_DEPLOY_HOOK_URL`

### 4. Smoke Test
- Waits 30 seconds for Render to finish spinning up
- Sends `GET /` to the live app URL
- Expects HTTP `200` and response: `{"message": "USTP Nexus API is running."}`
- If non-200: exits with code 1 (marks the workflow as failed)
- Secret used: `APP_URL`

---

## Secrets Required

Set these in **GitHub → Settings → Secrets and variables → Actions → New repository secret**:

| Secret name              | Value                                      |
|--------------------------|--------------------------------------------|
| `RENDER_DEPLOY_HOOK_URL` | From Render → your service → Settings → Deploy Hook |
| `APP_URL`                | Your live Render URL, e.g. `https://ustp-nexus.onrender.com` |

---

## Week 10 Checklist

- [x] CI updated to auto-deploy on push to `main`
- [x] Pipeline runs: test → deploy → smoke test
- [x] Secrets added via GitHub Actions (not hardcoded)
- [x] Smoke test checks `GET /` returns HTTP 200
- [x] Deployment verified working
- [x] This diagram created at `docs/cicd-diagram.md`
- [ ] Screenshot of successful deploy run attached
