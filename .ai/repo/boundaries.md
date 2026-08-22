# Repository Boundaries

## Architecture boundaries

Owned here is the implementation and documentation present in this repository, especially: `.agents/`, `app/`, `tests/`, `.ai/`, `.zed/`, `.github/`.

Do not move responsibilities into or out of this repository without an explicit architecture task and evidence from current code/docs.

## Ownership boundaries

- Changes must stay within this repository's documented purpose and current implementation boundaries.
- Do not duplicate business logic into prompts, adapters or generated governance files.
- Do not silently change external API, schema, billing, auth, deployment or persistence behavior.

## High-risk integration boundaries

- .env*
- secrets, credentials and private keys
- CI/CD workflows

Never expose secret values.
