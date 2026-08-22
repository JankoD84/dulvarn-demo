# Review Workflow

## Review posture

Review against current tracked source and tests. Do not treat README-only claims, old summaries, or unmerged branch code as authoritative.

## 1. Confirm state

Run:

```bash
git status -sb
git branch --show-current
git log -1 --oneline
git diff --stat
```

Identify unexpected user work before reviewing or suggesting changes.

## 2. Classify the change

Use the task classes from `.ai/process/implementation-workflow.md` and apply stricter review to higher-risk classes:

- Auth/JWT/security.
- Release scenario/mock-data.
- Dulvarn integration/demo contract.
- Dependency/CI/runtime config.
- API contract changes.

## 3. Check boundaries

For every review, verify relevant boundaries:

- `.ai/governance/authority-boundaries.md`
- `.ai/governance/demo-vs-production.md`
- `.ai/governance/canonical-vs-feature-branch.md`
- `.ai/governance/api-contract-safety.md`

For auth/security changes, also verify:

- `.ai/governance/auth-and-demo-security.md`
- `.ai/governance/secrets-and-demo-credentials.md`

For release changes, also verify:

- `.ai/governance/release-demo-boundaries.md`
- `.ai/governance/mock-data-safety.md`
- `.ai/governance/demo-scenario-stability.md`

## 4. Review checklist

- Does the change stay within requested scope?
- Does it preserve protected files when required?
- Does it describe implemented behavior truthfully?
- Does it avoid leaking literal demo credentials/secrets?
- Does it avoid presenting demo shortcuts as production patterns?
- Does it avoid importing feature-branch behavior into current-main docs?
- Does it keep API route/method/status/response behavior explicit when changed?
- Does it include tests or validation appropriate to the task class?
- Does it avoid claiming Ruff, mypy, coverage, Docker, security scanning, deployment, or database persistence unless implemented and run?

## 5. Review output

Report findings by severity:

- Blocker: unsafe, incorrect, or out-of-scope behavior.
- Major: high-risk ambiguity or missing validation.
- Minor: clarity or maintainability issue.
- Note: non-blocking observation.

If no issues are found, still state the validation evidence reviewed.
