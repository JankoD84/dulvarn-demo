# Canonical Main vs Feature Branches

Standards V2 describes current canonical main behavior only.

Known unmerged candidate branches may include:

- `feat/token-refresh`
- `fix/null-check-release-validator`
- `refactor/extract-auth-middleware`

These branches are not current repository truth unless merged into main and visible in the current tracked source.

## Rules

- Do not merge feature branches during Standards work.
- Do not cherry-pick from feature branches during Standards work.
- Do not copy architecture from feature branches.
- Do not describe unmerged middleware, token refresh, tests, or refactors as current architecture.
- Do not use unmerged branch tests as main acceptance criteria.
- If feature branch work is mentioned, label it as unmerged candidate work.

Main behavior != feature branch behavior.
