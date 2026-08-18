---
name: demo-auth-work
description: Use for dulvarn-demo login, placeholder auth, JWT helper behavior, token verification, or auth-related tests; high-risk because demo auth must not be described as production auth.
---

# Demo Auth Work

Use this skill for authentication/JWT work in `dulvarn-demo`.

## Required context

Read first:

- `AGENTS.md`
- `.ai/repo/repository-context.md`
- `.ai/repo/architecture.md`
- `.ai/governance/auth-and-demo-security.md`
- `.ai/governance/secrets-and-demo-credentials.md`
- `.ai/governance/demo-vs-production.md`
- `.ai/process/implementation-workflow.md`

## Rules

- This is demo auth, not Dulvarn production authentication or authorization.
- Do not reproduce literal demo credentials or signing defaults in docs, examples, tasks, or reports.
- Do not claim database-backed identity, RBAC, permissions, middleware, token refresh, revocation, or production signing-key management unless current source implements it.
- If endpoints are unauthenticated in current source, document that truthfully.
- Auth/JWT/security work is task class E and requires stronger review.

## Validation

Run targeted auth tests and then the CI-equivalent suite when auth behavior changes:

```bash
pytest tests/test_auth.py -v --tb=short
pytest tests/ -v --tb=short
```
