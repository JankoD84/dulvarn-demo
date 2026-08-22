# Mock Data Safety

## Current state

Current release data is in-memory mock data in `app/releases/service.py`.

It is:

- Demo state.
- Deterministic fixture-like application data.
- Not persistent release evidence.
- Not production customer data.
- Not backed by a database in current runtime source.

## Change safety

Changing mock records can affect:

- Demo behavior.
- Expected validation outcomes.
- Screenshots and walkthroughs.
- CI tests.
- Dulvarn integration demonstrations.

Treat mock release changes as demo scenario changes. Preserve deterministic behavior unless the task explicitly requests a scenario update.

Do not invent a database persistence model because configuration mentions a database URL. Current code must prove persistence before Standards or reviews claim it.
