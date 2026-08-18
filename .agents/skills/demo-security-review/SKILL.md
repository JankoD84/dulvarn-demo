---
name: demo-security-review
description: Use when reviewing dulvarn-demo auth/security wording, secret handling, JWT behavior, or changes that could make demo security look production-safe.
---

# Demo Security Review

Use this skill for security-sensitive reviews in `dulvarn-demo`.

## Required context

Read first:

- `AGENTS.md`
- `.ai/governance/auth-and-demo-security.md`
- `.ai/governance/secrets-and-demo-credentials.md`
- `.ai/governance/demo-vs-production.md`
- `.ai/process/review-workflow.md`

## Review focus

Block changes that:

- Reproduce literal demo credentials, secret keys, tokens, authorization headers, or private values.
- Present placeholder/demo auth as production-safe.
- Claim RBAC, permissions, database-backed identity, middleware, token refresh, revocation, or production signing-key management without current source evidence.
- Copy demo shortcuts into production guidance.
- Add tasks or docs that require real secrets.

Security/auth work is high-risk even in a demo repository.
