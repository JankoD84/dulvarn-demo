# Acme API — Demo Repository

> This repository is used as a live demo environment for [Dulvarn](https://dulvarn.com) — a Release Control System that gives every pull request an explicit GO, CONDITIONAL GO, or NO-GO decision.

## Stack

- Python 3.11
- FastAPI
- PostgreSQL (production) / SQLite (dev)
- pytest

## Setup

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Tests

```bash
pytest tests/ -v
```

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/health` | Health check |
| POST | `/auth/login` | Authenticate and get token |
| GET | `/releases/` | List all releases |
| GET | `/releases/{id}` | Get release by ID |
| POST | `/releases/{id}/validate` | Validate release readiness |
