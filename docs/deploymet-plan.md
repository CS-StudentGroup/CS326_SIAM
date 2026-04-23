# Deployment Plan – USTP Nexus

## Project: USTP Nexus
## Version: v0.8
## Environment: Development
## Platform: Render
## Last Updated: Week 7

---

## 1. Target Environment

| Property | Details |
|----------|---------|
| Platform | Render (render.com) |
| Type | Web Service |
| Runtime | Python 3.10 |
| Branch | `dev` |
| Region | Singapore (closest to PH) |

---

## 2. Rollout Strategy

**Strategy: Direct Deployment**

Since this is a development environment with no real users yet, we deploy directly from the `dev` branch to Render on every merge. No staged rollout is needed at this phase.

Steps:
1. Merge feature branch into `dev` via Pull Request
2. Render automatically detects the push and redeploys
3. Verify the deployment succeeded in the Render dashboard
4. Confirm the live URL is responding correctly

---

## 3. Pre-Deployment Checklist

- [ ] All unit tests pass locally (`python -m pytest tests/ -v`)
- [ ] No open S1 or S2 bugs in the defect log
- [ ] Code has been reviewed and PR merged to `dev`
- [ ] `requirements.txt` is up to date
- [ ] Environment variables are set in Render dashboard

---

## 4. Deployment Steps

1. Push code to `dev` branch on GitHub
2. Log in to [render.com](https://render.com)
3. Go to your Web Service → Render will auto-deploy on push
4. Monitor the build log for errors
5. Once deploy is complete, open the live URL
6. Verify the app is running correctly

---

## 5. Rollback Steps

If the deployment breaks the system:

1. Go to Render dashboard → your Web Service
2. Click **Deploys** tab
3. Find the last working deployment
4. Click **Rollback to this deploy**
5. Confirm rollback, Render will restore the previous version
6. Verify the live URL is working again
7. Log the incident in `docs/defect-log.md`

---

## 6. Environment Variables

| Variable | Description |
|----------|-------------|
| `SECRET_KEY` | App secret key for session management |
| `DEBUG` | Set to `False` in production |

Set these in Render → your service → **Environment** tab. Never hardcode them in the source code.
