---
name: test-validation
description: Use when validating dulvarn-demo changes with pytest, compile checks, Zed JSON checks, git diff whitespace checks, or cleanup of generated validation artifacts.
---

# Test Validation

Use this skill for validation and cleanup in `dulvarn-demo`.

## Required context

Read first:

- `AGENTS.md`
- `.ai/repo/testing.md`
- `.ai/governance/ci-and-validation-truthfulness.md`
- `.ai/process/implementation-workflow.md`

## Current real tooling

CI-equivalent tests:

```bash
pytest tests/ -v --tb=short
```

Useful local checks:

```bash
python3 -m compileall -q app
python3 -m json.tool .zed/settings.json >/dev/null
python3 -m json.tool .zed/tasks.json >/dev/null
git diff --check
```

Do not invent Ruff, mypy, coverage, Docker, security scanning, deployment, or migration validation unless the repository adds those tools.

## Cleanup

Remove only generated artifacts created by validation:

- `.pytest_cache/`
- `__pycache__/`
- `*.pyc`
- temporary validation virtualenv

Do not use broad `git clean` without explicit user approval.
