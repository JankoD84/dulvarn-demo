# Implementation Workflow

## 1. Precheck

Before editing, run:

```bash
git status -sb
git branch --show-current
git log -1 --oneline
git diff --stat
```

Expected Standards V2 branch: `chore/demo-standards-v2` at `31770f7 feat: initial project setup — FastAPI auth and releases`.

If unexpected modified or untracked work exists, stop and report it.

## 2. Classify the task

Use the highest applicable class:

| Class | Description | Risk |
| --- | --- | --- |
| A | Standards/docs/editor change | Low, if protected scope is respected |
| B | Test-only demo change | Medium |
| C | Demo API behavior change | Medium/high |
| D | Demo release scenario/mock-data change | High for demos |
| E | Authentication/JWT/security change | High |
| F | Dulvarn integration/demo-contract change | High |
| G | Dependency/CI/runtime configuration change | High |

Higher classes require stronger source inspection, explicit demo-impact notes, and targeted tests.

## 3. Load relevant context

Always prefer current tracked source and tests over README or old summaries.

Read as needed:

- `.ai/repo/repository-context.md`
- `.ai/repo/architecture.md`
- `.ai/repo/testing.md`
- Relevant `.ai/governance/*`
- Relevant `.agents/skills/*/SKILL.md`

## 4. Protected scope

For Standards V2 work, modify only:

- `AGENTS.md`
- `CLAUDE.md`
- `.ai/**`
- `.agents/**`
- `.zed/**`

Do not modify:

- `app/**`
- `tests/**`
- `.github/**`
- `README.md`
- `requirements.txt`

For non-Standards tasks, inspect scope and ask before touching protected or sensitive files such as `.env*`, CI, dependencies, migrations, production config, or secrets.

## 5. Implementation rules

- Make the smallest correct change.
- Preserve current public API contracts unless explicitly changing them.
- Do not import behavior from unmerged feature branches.
- Do not upgrade dependencies unless explicitly requested.
- Do not redesign auth during unrelated work.
- Do not implement Dulvarn production RCS features in this demo repository.
- Do not reproduce literal demo credentials or secret-looking values in docs/config.

## 6. Validation

Choose validation based on task class.

For Standards/config changes:

```bash
python3 -m json.tool .zed/settings.json >/dev/null
python3 -m json.tool .zed/tasks.json >/dev/null
git diff --check
pytest tests/ -v --tb=short
python3 -m compileall -q app
```

For app behavior changes, run the CI-equivalent test command at minimum and add targeted tests when behavior changes.

### Zed task safety: `run demo locally`

The `run demo locally` Zed task is for local development only. It must bind only to `127.0.0.1` / `localhost`, is not production or deployment validation, and must not be changed to `0.0.0.0` without an explicit task requiring that behavior. Application startup loads local `.env` configuration through Pydantic settings, so do not use this task with a local `.env` containing real production credentials or secrets.

## 7. Cleanup and report

Remove only generated local artifacts created by validation, such as `.pytest_cache/`, `__pycache__/`, `*.pyc`, or a temporary validation virtualenv.

Final report should include:

- Repository, canonical path, branch, HEAD.
- Files changed.
- Validation run.
- Protected-scope check.
- Remaining risks.
- Recommended commit message.

Do not commit or push unless explicitly requested.
