# Demo Implementation != Production Pattern

This repository intentionally contains simplified demo constructs. They are acceptable only as demo behavior when intentional and documented.

Examples confirmed by current source inspection:

- Placeholder authentication.
- Development-oriented configuration defaults.
- Simplified JWT/session behavior.
- In-memory/mock release data.
- Intentionally small validation rules.
- SQLite/dev-oriented database URL configuration that is not currently used for runtime persistence.
- Simple CI focused on pytest.

These constructs must not automatically become implementation patterns for:

- `dulvarn-core`
- `wildcode-api`
- `license-service`
- Other production services

If production behavior is needed, inspect the canonical production repository and its tests. Do not copy demo shortcuts into production code or documentation.
