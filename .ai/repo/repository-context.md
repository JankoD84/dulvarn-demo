# Repository Context — dulvarn-demo

## Identity

- Repository: `dulvarn-demo`
- Canonical path: `/home/qaengineer/Dokumenty/Wildcode Studio/Dulvarn/dulvarn-demo`
- Standards V2 branch: `chore/demo-standards-v2`
- Standards V2 base/HEAD: `31770f7 feat: initial project setup — FastAPI auth and releases`

## Role

This is a **demo / sandbox** repository for Dulvarn Release Control System integration and release-related workflows using a small Acme FastAPI API.

It is not the canonical implementation of Dulvarn production internals.

## Current implemented stack

IMPLEMENTED in tracked source:

- Python FastAPI application in `app/main.py`
- JWT creation and verification helpers using PyJWT in `app/auth/service.py`
- Pydantic settings in `app/core/config.py`
- In-memory release data in `app/releases/service.py`
- Pytest tests under `tests/`
- GitHub Actions CI running Python 3.11 and pytest

DOCUMENTED in `README.md` but not implemented as runtime persistence in current source:

- PostgreSQL production / SQLite dev stack statement. `database_url` exists in settings, but current release/auth runtime does not use a database connection or persistence layer.

## Current API surface

Implemented routes from current source:

| Method | Path | Auth required by current source | Behavior |
| --- | --- | --- | --- |
| `GET` | `/health` | No | Returns `{"status": "ok"}`. |
| `POST` | `/auth/login` | No | Accepts username/password JSON. Returns a bearer access token on accepted placeholder demo credentials. Returns `401` for invalid credentials and FastAPI/Pydantic `422` for missing required fields. |
| `GET` | `/releases/` | No | Returns the current in-memory mock release list. |
| `GET` | `/releases/{release_id}` | No | Returns a matching mock release or `404` with `Release not found`. |
| `POST` | `/releases/{release_id}/validate` | No | Returns a deterministic demo validation result for a matching mock release or `404` with `Release not found`. |

No token refresh endpoint is implemented on current main. No release endpoint authentication dependency or auth middleware is implemented on current main.

## Current auth/JWT behavior

Current main includes:

- A simple `/auth/login` endpoint.
- Placeholder demo credential checking.
- Access token creation with an `exp` claim.
- HS256 JWT encode/decode helpers.
- Token verification returns payload for valid tokens and `None` for expired or invalid tokens.

Current main does not implement:

- Database-backed identity.
- RBAC or permissions.
- Auth middleware protecting routes.
- Token refresh.
- Production-grade credential storage or signing-key management.

Do not reproduce literal credential or signing defaults in Standards docs. Refer to them generically as placeholder demo credentials and development-only secret defaults.

## Current release behavior

Current release behavior is implemented as in-memory mock data with three records. Validation is intentionally small and deterministic:

- A blocked status creates an error.
- Missing version creates an error.
- Response shape is `{"valid": boolean, "errors": list}`.

This demo validation result is not Dulvarn's canonical release decision system and must not be described as GO, CONDITIONAL_GO, or NO_GO semantics.

## Current tests

Current tests verify:

- Login success returns an access token and bearer token type.
- Invalid login returns `401`.
- Missing login field returns `422`.
- Listing releases returns a list of length 3.
- Release ID 1 returns version `1.0.0`.
- Unknown release returns `404`.
- Blocked release validation returns `valid: false` with errors.
- Released release validation returns `valid: true`.

Tests use `fastapi.testclient.TestClient` and do not require external services.

## Current CI

`.github/workflows/ci.yml` currently:

- Runs on pushes and pull requests targeting `main`.
- Uses `ubuntu-latest`.
- Sets up Python `3.11`.
- Installs `requirements.txt`.
- Runs `pytest tests/ -v --tb=short`.

CI does not currently run Ruff, mypy, coverage gates, Docker builds, security scans, migrations, deployment checks, or production integration tests.

## README-vs-code findings

- README endpoint list matches implemented routes.
- README test command is close but CI uses `pytest tests/ -v --tb=short`.
- README stack mentions PostgreSQL production / SQLite dev. Current code has a database URL setting but no implemented database persistence or connection usage.
- README describes Dulvarn as producing GO / CONDITIONAL GO / NO-GO decisions. Current demo validator returns only `valid` and `errors`; do not map it to Dulvarn decision semantics.
