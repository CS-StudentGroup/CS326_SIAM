# KPIs - USTP Nexus

## Project: USTP Nexus
## Version: v0.8
## Last Updated: Week 13
## Author: Mesa (Documentation Lead)

---

## Overview

This document defines the five Key Performance Indicators (KPIs) used to measure the quality, reliability, and delivery performance of USTP Nexus.

---

## KPI-01 - Defect Rate

Definition: The number of bugs found per sprint relative to the features delivered.

Why it matters: A high defect rate indicates insufficient testing or rushed development. Tracking it helps the team improve code quality over time.

Target: 1 or fewer defects per sprint.

Measurement: Count of entries in docs/defect-log.md per sprint.

---

## KPI-02 - Deployment Frequency

Definition: How often a successful deployment reaches the live environment (Render).

Why it matters: Higher deployment frequency indicates a healthy CI/CD pipeline and short feedback loops.

Target: At least 2 successful deployments per week during active sprints.

Measurement: Count of successful GitHub Actions workflow runs on main per week.

---

## KPI-03 - API Response Time

Definition: The average time in milliseconds for core API functions to execute.

Why it matters: Slow response times degrade user experience. Baseline measurements allow the team to detect regressions after changes.

Target: All core functions under 1 ms per call.

Measurement: Python timeit module, 10,000 runs per function, recorded in docs/performance.md.

---

## KPI-04 - Test Pass Rate

Definition: The percentage of automated tests that pass in CI on a given run.

Why it matters: A low pass rate means the codebase is unstable or broken. A high pass rate gives confidence that new changes do not break existing features.

Target: 100% of non-known-bug tests passing in CI.

Measurement: pytest output in GitHub Actions - passed vs total collected.

---

## KPI-05 - Lead Time for Changes

Definition: The average time from opening a feature branch to merging it into main.

Why it matters: Long lead times indicate bottlenecks in review, testing, or integration. Shorter lead times mean faster delivery.

Target: Under 48 hours from branch creation to merge.

Measurement: Timestamps of branch creation vs PR merge on GitHub.
