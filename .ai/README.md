# dulvarn-demo AI Context

`.ai/` is the repository-local AI navigation and governance layer.

It must not become a second copy of product documentation or an IDE-specific configuration directory.

Structure:

- `repo/` — repository identity, boundaries, commands and architecture pointers
- `governance/` — source-of-truth, safety, quality and documentation rules
- `process/` — reusable engineering workflows
- `templates/` — compact output and handoff templates

Authority model:

- `AGENTS.md` = universal AI entrypoint for Devin, Windsurf/Cascade, Cursor, VS Code + Roo Code, and Zed.
- `.ai/` = IDE-neutral repository context and governance.
- `.agents/skills/` = task-specific operational knowledge, when this repository has repeatable workflows worth encoding.
- IDE-specific directories such as `.zed/`, `.cursor/`, `.roo/`, `.windsurf/`, and `.vscode/` are execution adapters only.

Application/product truth remains in code, tests, schemas, current runtime state, and canonical repository documentation.
