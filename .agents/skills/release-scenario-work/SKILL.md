---
name: release-scenario-work
description: Use for dulvarn-demo mock release records, release routes, validation response behavior, or demo scenario outcomes; high-risk for demo stability.
---

# Release Scenario Work

Use this skill for release mock-data and validation scenario work in `dulvarn-demo`.

## Required context

Read first:

- `AGENTS.md`
- `.ai/repo/repository-context.md`
- `.ai/repo/architecture.md`
- `.ai/governance/release-demo-boundaries.md`
- `.ai/governance/mock-data-safety.md`
- `.ai/governance/demo-scenario-stability.md`
- `.ai/process/implementation-workflow.md`

## Rules

- Current release records are demo mock data, not persistent release evidence or production customer data.
- The demo validator returns `valid` and `errors`; do not map that response to Dulvarn canonical release-decision semantics.
- Do not claim GO / CONDITIONAL_GO / NO_GO behavior unless current source literally implements it.
- Preserve deterministic scenario behavior unless the task explicitly requests a scenario change.
- Mock-data and validation behavior changes require explicit demo-impact review.

## Validation

Run release tests and then the CI-equivalent suite when release behavior changes:

```bash
pytest tests/test_releases.py -v --tb=short
pytest tests/ -v --tb=short
```
