# Secrets and Demo Credential Safety

## Protected data

Do not expose, copy, or normalize literal values for:

- Demo passwords.
- Secret keys.
- Tokens.
- Credentials.
- Authorization headers.
- Private values.

This applies even when those values are hard-coded placeholders in demo source.

## Preferred wording

Use generic descriptions such as:

- Placeholder demo credentials.
- Development-only secret defaults.
- Demo bearer token.
- Local-only `.env` values.

## Configuration guidance

- Do not edit `.env*` files without explicit user confirmation.
- Do not add real credentials to Standards, skills, Zed tasks, tests, examples, or docs.
- Do not create Zed tasks that generate tokens using real credentials.
- Do not present current demo credential patterns as acceptable production configuration.
