# SCM Notes – USTP Nexus

## Project: USTP Nexus
## Sprint: 1
## Author: Mesa (Documentation Lead)
## Last Updated: Week 5

---

## Branch Naming Rules

| Type | Format | Example |
|------|--------|---------|
| New feature | `feature/<name>` | `feature/week5-scm` |
| Bug report | `bug/<name>` | `bug/bug-001` |
| Bug fix | `fix/<name>` | `fix/bug-001` |
| Hotfix (urgent) | `hotfix/<name>` | `hotfix/login-crash` |

**Rule:** No direct pushes to `main`. All changes go through a Pull Request.

---

## Merge Conflict – Week 5

### What Happened
A merge conflict occurred when merging `feature/week5-scm` into `dev`. Both branches had a function called `new_function()` in `src/main.py` but with different print statements.

- `dev` branch had: `print("Hello World")`
- `feature/week5-scm` had: `print("World Hello")`

Git could not automatically decide which version to keep, so it flagged it as a conflict:

```
<<<<<<< feature/week5-scm
def new_function():
    print("World Hello")
=======
def new_function():
    print("Hello World")
>>>>>>> dev
```

### How We Resolved It
Resolved the conflict directly in the GitHub conflict editor. Removed the conflict markers and kept the `dev` version `print("Hello World")`. Clicked **Mark as resolved** then **Commit merge**.

### What We Learned
- Merge conflicts happen when two branches edit the same line differently
- Git marks both versions and requires a developer to manually choose
- Always resolve conflicts carefully and re-test after merging

---

## Release Tagging

| Tag | Version | Description |
|-----|---------|-------------|
| `v0.5` | 0.5 | First tagged release — core auth + task logic + QA setup |
