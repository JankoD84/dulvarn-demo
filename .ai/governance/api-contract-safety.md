# API Contract Safety

## Current implemented API contract

| Method | Path | Current auth status | Key responses |
| --- | --- | --- | --- |
| `GET` | `/health` | Unauthenticated | `200` with status payload. |
| `POST` | `/auth/login` | Unauthenticated | `200` token payload for accepted placeholder demo credentials; `401` invalid credentials; `422` validation error for malformed/missing fields. |
| `GET` | `/releases/` | Unauthenticated | `200` mock release list. |
| `GET` | `/releases/{release_id}` | Unauthenticated | `200` matching mock release; `404` when missing. |
| `POST` | `/releases/{release_id}/validate` | Unauthenticated | `200` demo validation response for matching release; `404` when missing. |

## Change safety

API contract changes may affect:

- Demo scripts and screenshots.
- Customer-facing walkthroughs.
- CI expectations.
- Dulvarn integration demonstrations.

Before changing routes, methods, status codes, response shapes, or auth requirements:

1. Classify the task in `.ai/process/implementation-workflow.md`.
2. Inspect current tests.
3. Add or update tests when behavior intentionally changes.
4. State demo impact explicitly in review.

Do not invent or document future endpoints from unmerged branches, including token refresh, unless current source implements them.
