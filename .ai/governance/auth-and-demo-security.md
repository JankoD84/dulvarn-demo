# Auth and Demo Security Boundary

## Current implemented auth behavior

Current main implements:

- `POST /auth/login` with a simple JSON username/password request.
- Placeholder demo credential checking.
- JWT access-token creation with an expiry claim.
- JWT verification helper that returns decoded payload for valid tokens.
- `None` for expired or invalid tokens.

Current main does not implement:

- Database-backed identity.
- Production credential storage.
- RBAC or permission checks.
- Auth middleware protecting release routes.
- Token refresh.
- Session revocation or rotation.
- Production signing-key management.

## Documentation rules

- Never describe placeholder/demo credentials as production-safe.
- Never reproduce literal demo credentials or development signing defaults in Standards docs.
- Do not claim real users, RBAC, permissions, refresh tokens, or auth middleware unless implemented in current source and validated by tests.
- If release endpoints remain unauthenticated, document that truthfully.
- Do not silently upgrade the documented security level.

This repository may demonstrate an auth surface, but it is not Dulvarn production authentication or authorization.
