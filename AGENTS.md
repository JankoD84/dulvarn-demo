# Dulvarn Demo Agent Instructions

Repository: `dulvarn-demo`
Canonical path: `/home/qaengineer/Dokumenty/Wildcode Studio/Dulvarn/dulvarn-demo`

This repository is a **demo / sandbox** for Dulvarn Release Control System integration and release-related workflows using a small Acme FastAPI API. It is not the canonical implementation of Dulvarn production internals.

## Required starting point

Before implementation or review work, confirm:

```bash
git status -sb
git branch --show-current
git log -1 --oneline
git diff --stat
```

Expected Standards V2 branch: `chore/demo-standards-v2` at `31770f7 feat: initial project setup — FastAPI auth and releases`.

If unexpected modified or untracked work exists, stop and report it.

## Source of truth

Use this order:

1. Current tracked source and tests in this repository
2. `.ai/repo/*`
3. `.ai/governance/*`
4. `.ai/process/*`
5. Relevant `.agents/skills/*`
6. README, clearly separated as documented claims when not implemented

Do not treat unmerged feature branches as current repository truth.

## Authority boundary

`dulvarn-demo` may own its own demo FastAPI routes, demo auth/JWT behavior, mock releases, validation response, tests, and demo CI.

It does **not** own Dulvarn production release decision logic, evidence lifecycle, release policy, backtesting, cryptographic proof, production auth/authorization, canonical Store/license data, infrastructure, or production API architecture.

When describing Dulvarn production behavior, reference the appropriate canonical repository rather than deriving it from this demo.

## Demo implementation != production pattern

Simplified demo constructs in this repository must not be copied into production repositories such as `dulvarn-core`, `wildcode-api`, `license-service`, or other production services.

This includes placeholder authentication, development-only defaults, simplified JWT/session behavior, mock release data, intentionally small validation rules, SQLite/dev-oriented configuration, and simple CI.

## Protected scope

Do not modify these paths for Standards work:

- `app/**`
- `tests/**`
- `.github/**`
- `README.md`
- `requirements.txt`

Allowed Standards/config paths:

- `AGENTS.md`
- `CLAUDE.md`
- `.ai/**`
- `.agents/**`
- `.zed/**`

## Task classes

Use `.ai/repo/repository-context.md` and `.ai/process/implementation-workflow.md` to classify work before editing.

Higher-risk classes include authentication/JWT/security, demo release scenario/mock-data, Dulvarn integration/demo-contract, dependency/CI/runtime configuration, and any change that alters demo scenario signals.

## Validation baseline

Use only tooling present in this repository unless the task explicitly adds more tooling.

Current CI-equivalent command:

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

Do not claim Ruff, mypy, coverage gates, Docker builds, security scans, deployment checks, or production integration tests unless the repository actually adds them.
