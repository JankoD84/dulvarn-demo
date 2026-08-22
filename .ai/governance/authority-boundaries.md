# Authority Boundaries

## Repository authority

`dulvarn-demo` may own:

- Its own demo FastAPI behavior.
- Its own demo routes.
- Demo auth behavior.
- Demo JWT behavior.
- Demo mock releases.
- Demo validation behavior.
- Tests for the demo.
- Demo CI.

## Out of scope

`dulvarn-demo` does not own:

- `dulvarn-core` release decision logic.
- GO / CONDITIONAL_GO / NO_GO semantics.
- Dulvarn Evidence lifecycle.
- Dulvarn release policy.
- Dulvarn backtesting.
- Dulvarn cryptographic proof.
- Dulvarn production authentication.
- Dulvarn production authorization.
- Canonical Store/license data.
- Canonical infrastructure.
- Canonical production API architecture.

When describing Dulvarn production behavior, cite the appropriate canonical repository or current source of truth. Do not derive production behavior from this demo.
