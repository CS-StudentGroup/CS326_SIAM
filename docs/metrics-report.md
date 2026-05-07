# Metrics Report - USTP Nexus

## Project: USTP Nexus
## Version: v0.8
## Last Updated: Week 13
## Author: Mesa (Documentation Lead)

---

## Overview

This report presents current measurements for each KPI defined in docs/kpis.md. Data is drawn from the defect log, GitHub Actions run history, performance benchmarks, and pytest output from CI.

---

## KPI-01 - Defect Rate

Current: 1 defect (BUG-001) identified and logged in Sprint 1.

Target: 1 or fewer defects per sprint.

Status: On target.

Interpretation: One bug was caught during Sprint 1 testing - an off-by-one error in validate_password() that rejected valid 8-character passwords. It was identified by the test suite (test_register_exactly_8_char_password), logged in docs/defect-log.md, and fixed in the bug/bug-001 branch. No new defects were introduced in subsequent weeks.

Action plan: Maintain current test coverage. Once BUG-001 is fully resolved in CI (the >= 8 fix is merged), re-enable the skipped test to prevent regression.

---

## KPI-02 - Deployment Frequency

Current: Approximately 3 to 5 deployments per week during Weeks 10 to 13 based on merged PRs to main triggering the GitHub Actions CI/CD pipeline.

Target: At least 2 successful deployments per week.

Status: On target.

Interpretation: The automated pipeline (test - deploy - smoke test) established in Week 10 has been running on every merge to main. PRs merged during Week 13 include the CI path fix, the syntax fix, and the skip-failing-tests fix - each triggering a deployment. The smoke test confirms the live URL at https://cs326-siam.onrender.com returns HTTP 200 after each deploy.

Action plan: Continue merging through PRs rather than direct pushes to main to keep deployment frequency measurable through GitHub Actions history.

---

## KPI-03 - API Response Time

Current measurements (from docs/performance.md, Python timeit, 10,000 runs):

- register_user(): 0.0030 ms per call
- login_user(): 0.0010 ms per call
- create_task(): 0.0004 ms per call
- delete_task(): 0.0002 ms per call

Target: All core functions under 1 ms per call.

Status: On target. All functions are well within the 1 ms threshold.

Interpretation: Performance was measured before and after the Week 8 docstring refactor (TD-05). Results were identical, confirming the refactor introduced no regression. All four core functions execute in under 0.004 ms per call, leaving significant headroom before the 1 ms target is approached.

Action plan: Re-run benchmarks when a persistent database (TD-01) is introduced in a future sprint, as database I/O will significantly increase response times and may require optimization.

---

## KPI-04 - Test Pass Rate

Current: 4 out of 6 tests passing in CI (66%).

Target: 100% of non-known-bug tests passing.

Status: Partially on target.

Interpretation: 6 tests are collected by pytest. 4 pass cleanly (test_add_pad_valid, test_add_pad_negative_price, test_add_pad_empty_name, test_delete_existing_pad). 2 are currently skipped in CI via the -k flag to unblock the pipeline. Of those 2, test_register_exactly_8_char_password is the documented BUG-001 (intentional failure). test_register_valid_user fails because the current password validator requires uppercase, which the test does not provide - this is an unresolved functional mismatch between the test expectation and the implementation.

Action plan:
- Fix the >= 8 operator in validate_password() to resolve BUG-001 and re-enable test_register_exactly_8_char_password.
- Update either the test or the password policy for test_register_valid_user to align with the current validation rules.
- Target: 6 out of 6 passing in CI with no skips.

---

## KPI-05 - Lead Time for Changes

Current: Estimated 10 to 30 minutes per fix branch during Week 10 to 13 based on commit timestamps visible in the GitHub commit history.

Target: Under 48 hours from branch creation to merge.

Status: On target.

Interpretation: Fix branches created during Week 10 to 13 (fix/skip-failing-tests, feature/week10-cicd, and related patches) were opened and merged within the same session. This is well within the 48-hour target. The team follows the SCM rules defined in docs/scm-notes.md - no direct pushes to main, all changes go through a named branch and PR.

Action plan: Continue following SCM policy. As the project grows, document branch open and merge times more formally to track this KPI accurately over multiple sprints.

---

## Summary Table

KPI | Current | Target | Status
Defect Rate | 1 bug in Sprint 1 | 1 or fewer per sprint | On target
Deployment Frequency | 3 to 5 per week | 2 or more per week | On target
API Response Time | 0.0002 to 0.0030 ms | Under 1 ms | On target
Test Pass Rate | 4 of 6 (66%) | 100% non-known-bug | Needs improvement
Lead Time for Changes | Under 30 minutes | Under 48 hours | On target
