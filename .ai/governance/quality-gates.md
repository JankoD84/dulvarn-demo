# Quality Gates

Use targeted validation appropriate to the change.

## Repository validation

- `python -m pytest`

## Governance-only validation

```bash
git diff --check
git status --short
```

Before completion, inspect the diff and confirm:

- `AGENTS.md` remains the universal AI entrypoint.
- `.ai/` remains IDE-neutral.
- IDE-specific files are adapters only and do not redefine repository standards.
- No secrets, provider credentials, production configuration, migrations or deployment behavior were changed.
- Repository-specific safety and architecture rules are preserved.
