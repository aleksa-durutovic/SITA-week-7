# Week 7 working instructions

## Approval comes first

Current state: planning only. Read `specs/001-sentence-chunking/approval.md` before edits.
Do not edit application code, configuration, tests, or dependencies, or run
`$speckit-implement`, until the user explicitly approves the current spec, plan and tasks.
The user's baseline permission and Luna 6 choice are not implementation approval.
Never mark approval on the user's behalf without quoting an actual approval message.
Ask about scope changes; do not choose another improvement or tune an extra setting.

## Read only the relevant context

For implementation, read this file, `.specify/memory/constitution.md`, then the feature's
`approval.md`, `spec.md`, `plan.md`, `tasks.md`, and `contracts/chunking.md`.
Use `quickstart.md` for commands. Read `docs/baseline-findings.md` when interpreting evidence.
Do not regenerate these artifacts or read every installed skill/template during implementation.
The approved package is recorded in `review-manifest.json`; verify it before the first code
edit. Later task completion markers are permitted; material instruction changes need review.

## Boundaries

- Assignment source: `docs/weekly-assignment.md`; mandatory Granica rada only.
- Exactly one RAG intent, proposed M1. No new dependency or infrastructure.
- After approval, only `src/chunking.py`, the `CHUNK_STRATEGY` value in `src/config.py`,
  and new `tests/test_sentence_chunking.py` may change behavior/tests.
- Preserve every other original file, especially eval questions, evaluator/comparator,
  corpus, retrieval, answering, existing tests, requirements and ignore rules.
- Keep `results/before.json` and baseline logs immutable. Never invent after results.
- If outcomes disappoint, report them. Do not add another fix to improve the score.

Use PowerShell and `.venv\Scripts\python.exe` in this workspace. No paid API is part
of the application. Use one assistant session; do not launch other agents or workflows
that implement automatically. The user and Igor alternate driver/reviewer on this PC.
The user leads this week's demo. Do not fabricate contributions or peer feedback.
Do not commit, send messages, submit, or start advanced work without a later user request.
