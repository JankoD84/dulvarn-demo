# CI and Validation Truthfulness

## Current CI

Current GitHub Actions CI runs:

```bash
pip install -r requirements.txt
pytest tests/ -v --tb=short
```

on Python 3.11 for pushes and pull requests targeting `main`.

## Do not claim absent checks

Do not claim CI currently runs:

- Ruff.
- mypy.
- Static type checking.
- Security scanning.
- Coverage gates.
- Docker builds.
- Migration validation.
- Production integration tests.
- Deployment checks.

unless the workflow is changed and current source proves it.

## Standards validation

For Standards/config changes, useful checks are:

```bash
python3 -m json.tool .zed/settings.json >/dev/null
python3 -m json.tool .zed/tasks.json >/dev/null
git diff --check
pytest tests/ -v --tb=short
python3 -m compileall -q app
```

Report exactly what was run and whether it passed.
