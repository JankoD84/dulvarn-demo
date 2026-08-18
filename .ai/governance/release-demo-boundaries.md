# Release Demo Boundaries

## Current demo validator

The current release validator exists to provide deterministic demo behavior and integration surface.

It returns:

```text
valid: boolean
errors: list
```

It currently checks a small set of fields/statuses in mock release records.

## Boundary to Dulvarn canonical decisions

Do not describe the demo validator as:

- Dulvarn's canonical release-decision engine.
- A policy engine.
- Evidence lifecycle processing.
- Backtesting.
- Cryptographic proof.
- GO / CONDITIONAL_GO / NO_GO semantics.

Canonical Dulvarn release-decision semantics live outside this repository.

## Demo scenario stability

Validation behavior can affect demo outcomes and integration showcases. A change that alters `valid`/`errors` outcomes is a demo release scenario change and requires explicit demo-impact review.
