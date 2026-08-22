# Acme API — Dulvarn Demo Repository

> This repository is a **demo/sandbox** used to demonstrate selected Dulvarn Release Decision & Intelligence System (RDIS) workflows against a small FastAPI application.

It is intentionally simplified and is **not** the canonical implementation of Dulvarn production release decisions, evidence lifecycle, release policy, authorization, backtesting, cryptographic proof, infrastructure, or production API architecture.

## Dulvarn authority boundary

- `dulvarn-core` is the authoritative owner of governed release evidence, release policy, and `GO` / `CONDITIONAL_GO` / `NO_GO` ReleaseDecision semantics.
- This repository owns only its Acme demo API, demo auth/release data, tests, and demo scenarios.
- Simplified demo patterns must not be copied into production Dulvarn services as architecture guidance.

## Stack

- Python 3.11
- FastAPI
- PostgreSQL-oriented production example / SQLite development configuration where supported by the demo
- pytest

## Setup

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Tests

```bash
pytest tests/ -v --tb=short
```

## Demo endpoints

| Method | Path | Description |
|---|---|---|
| GET | `/health` | Demo health check |
| POST | `/auth/login` | Demo authentication/token flow |
| GET | `/releases/` | List demo releases |
| GET | `/releases/{id}` | Get a demo release |
| POST | `/releases/{id}/validate` | Run the demo release-readiness validation |

Endpoint behavior is defined by current `app/` source and tests.

## Source of truth

1. current tracked source and tests in this repository
2. `.ai/repo/` and `.ai/governance/`
3. `AGENTS.md`
4. this README

Do not use this demo repository as evidence of current Dulvarn Core production behavior.