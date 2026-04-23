# Defect Log – USTP Nexus

## Project: USTP Nexus
## Sprint: 1
## QA Lead: Olaer
## Last Updated: Week 4

---

| Bug ID | Description | Severity | Status |
|--------|-------------|----------|--------|
| BUG-001 | `validate_password()` uses `> 8` instead of `>= 8`, causing valid 8-character passwords to be rejected during registration | S2 – High | Open |

---

## BUG-001 – Password Validation Off-By-One Error

**File:** `src/main.py`
**Function:** `validate_password()`
**Reported by:** Olaer (QA Lead)
**Severity:** S2 – High

**Steps to Reproduce:**
1. Call `register_user()` with a password of exactly 8 characters (e.g. `pass1234`)
2. Check the result

**Expected:** `success: True` — registration should succeed

**Actual:** `success: False` — "Password must be at least 8 characters."

**Root Cause:**
```python
# Buggy
return isinstance(password, str) and len(password) > 8

# Fixed
return isinstance(password, str) and len(password) >= 8
```

**Test that caught it:** `test_register_exactly_8_char_password` in `tests/tests.py`