---
name: api-contract-review
description: Use when reviewing dulvarn-demo API route, method, status-code, response-shape, or authentication-contract changes.
---

# API Contract Review

Use this skill for API contract reviews in `dulvarn-demo`.

## Required context

Read first:

- `AGENTS.md`
- `.ai/repo/repository-context.md`
- `.ai/governance/api-contract-safety.md`
- `.ai/process/review-workflow.md`

## Review focus

Check that changes:

- Match current source or explicitly update behavior and tests.
- Do not document unmerged branch endpoints as current behavior.
- Preserve or intentionally change route methods, paths, status codes, response shape, and auth status.
- Call out demo impact for customer demos, screenshots, walkthroughs, and CI.
- Avoid production Dulvarn architecture claims.

## Validation evidence

Prefer test evidence from:

```bash
pytest tests/ -v --tb=short
```
