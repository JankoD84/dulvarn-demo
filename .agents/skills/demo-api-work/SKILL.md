---
name: demo-api-work
description: Use when changing or inspecting dulvarn-demo FastAPI routes, request/response behavior, status codes, or demo API contracts.
---

# Demo API Work

Use this skill for route-level work in `dulvarn-demo`.

## Required context

Read first:

- `AGENTS.md`
- `.ai/repo/repository-context.md`
- `.ai/repo/architecture.md`
- `.ai/governance/api-contract-safety.md`
- `.ai/governance/demo-scenario-stability.md`
- `.ai/process/implementation-workflow.md`

## Rules

- Treat this repository as a demo/sandbox, not production Dulvarn API architecture.
- Verify current routes in source before describing or changing API behavior.
- Do not invent endpoints from unmerged branches.
- Do not add auth requirements, token refresh, or production behavior unless explicitly requested.
- Preserve deterministic demo behavior unless the task asks to change it.

## Validation

Run the current CI-equivalent tests when API behavior changes:

```bash
pytest tests/ -v --tb=short
```
