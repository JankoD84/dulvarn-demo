# Architecture — Current Main

## Scope

This file documents only the current tracked implementation on `chore/demo-standards-v2` / current main-equivalent HEAD. Do not import architecture from unmerged feature branches.

## Application layout

```text
app/
  main.py              FastAPI app construction and route inclusion
  core/config.py       Pydantic settings with development-oriented defaults
  auth/routes.py       Login request/response models and login route
  auth/service.py      Placeholder credential check and JWT helper functions
  releases/routes.py   Release listing, lookup, and validation routes
  releases/service.py  In-memory mock release records and demo validator
```

## Request flow

```mermaid
flowchart TD
    Client[Client] --> App[FastAPI app]
    App --> Health[GET /health]
    App --> AuthRouter[/auth router]
    App --> ReleaseRouter[/releases router]
    AuthRouter --> Login[POST /auth/login]
    Login --> AuthService[auth service]
    AuthService --> Token[JWT access token]
    ReleaseRouter --> List[GET /releases/]
    ReleaseRouter --> Get[GET /releases/{id}]
    ReleaseRouter --> Validate[POST /releases/{id}/validate]
    List --> MockData[In-memory mock releases]
    Get --> MockData
    Validate --> DemoValidator[Simple demo validator]
    DemoValidator --> ValidationShape[valid + errors]
```

## Auth architecture boundary

Current source has auth helper functions and a login route, but no route protection middleware or dependency is applied to release endpoints.

Do not claim auth middleware, RBAC, permissions, database-backed users, refresh tokens, session rotation, or production signing-key handling exists unless current source is changed and tests verify it.

## Release architecture boundary

Current release data is a module-level in-memory list. It is useful demo state, not persisted release evidence and not production customer data.

The validator exists to provide deterministic demo behavior and integration surface. Canonical Dulvarn release-decision semantics live outside this repository.

## Configuration boundary

`app/core/config.py` defines Pydantic settings and reads `.env`, including a database URL setting and development-only secret defaults. Current runtime code does not use the database URL for persistence.

Do not copy development defaults or placeholder credentials into production guidance or Standards examples.

## Non-goals for this repository

This repository does not implement:

- Dulvarn production release policy.
- Evidence lifecycle or cryptographic proof.
- Backtesting.
- Canonical Store/license data.
- Production API architecture.
- Production authentication or authorization.
- Infrastructure deployment.
