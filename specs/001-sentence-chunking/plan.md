# Implementation Plan: M1 sentence-aware chunking

**Revision**: v1 | **Date**: 2026-10-19 | **Status**: Awaiting user approval
**Spec**: [spec.md](spec.md) | **Feature**: `001-sentence-chunking`
**Git**: Existing workspace has no commits; no branch or commit was created by this setup.

## Summary

Propose implementing the existing sentence-chunking hook and selecting that strategy.
The measured targets are E04 and E09. Their expected duration fact is missing from selected
character fragments. The effect on those questions and the other ten must be measured,
not assumed. A negative result is acceptable without adding another improvement.

## Technical Context

- Language/platform: Python 3.12.14, Windows PowerShell, local CLI.
- Dependencies: standard library plus existing `pytest==8.3.3`; no dependency changes.
- Environment: `.venv\Scripts\python.exe`; baseline already saved.
- Scale: 10 handbook documents; fixed 12-question evaluation.
- Storage: existing source and JSON evidence files; no new service or schema.
- Performance: retain the local batch/CLI workflow; no new performance target is required.
- Coding tool: Codex, with the user's selected Luna 6 for implementation after approval.

## Constitution Check

| Rule | Design check |
| --- | --- |
| One intent | Only M1; function implementation and strategy selection are one decision. |
| Fixed measurement | Eval questions, metric/comparison code and existing tests are protected. |
| Human approval | `approval.md` stays pending; no application/config/test edits until user approval. |
| Local simplicity | Standard library only; original dependency file stays unchanged. |
| Honest evidence | Report regressions and rejected hypotheses; human contribution fields stay pending until confirmed. |

Pre-design and post-design checks pass for this proposal. This means it is reviewable,
not approved for execution. No constitution exception is requested.

## Project Structure

```text
src/chunking.py                   existing function hook and dispatcher
src/config.py                     active CHUNK_STRATEGY only
src/retrieval.py, src/rag.py        read-only context
src/eval_runner.py                 protected evaluation and metrics
src/eval_compare.py                protected comparison tool
src/cli.py                         existing CLI; no interface changes
specs/001-sentence-chunking/        spec, plan, tasks, contract and approval
results/                          before/after JSON, logs, CLI evidence and diffs
tests/test_sentence_chunking.py    proposed focused new tests
```

The data structures remain those described in [data-model.md](data-model.md).
The normative splitter behavior and test cases are in [contracts/chunking.md](contracts/chunking.md).

## Implementation approach (after approval only)

1. Add focused tests in `tests/test_sentence_chunking.py` for the contract: validation,
   empty input, punctuation and whitespace, exact-fit packing, overlong sentences, tail
   preservation, dispatch, and metadata/ID integration. Use synthetic text and monkeypatch.
2. Implement only `split_text_by_sentences` in `src/chunking.py`, with a standard-library
   punctuation/whitespace rule and greedy packing. Preserve the character splitter and
   dispatcher interfaces. Do not hard-code question IDs, handbook facts, or expected metrics.
3. In `src/config.py`, change only `CHUNK_STRATEGY` from `chars` to `sentences`.
   Keep `CHUNK_SIZE=140` and `CHUNK_OVERLAP=30`; the sentence function does not use overlap.
4. Run the full test suite and fixed eval, compare, inspect CLI output with the humans,
   and document the result. Follow [quickstart.md](quickstart.md) for exact commands.

## File allowlist

Behavior/test edits after approval are limited to:

- `src/chunking.py`: the new function body and required standard-library import/docstring.
- `src/config.py`: only the `CHUNK_STRATEGY` value.
- `tests/test_sentence_chunking.py`: focused new tests.

Evidence/report updates are limited to `results/`, `docs/before-after-report.md`,
`docs/ai-use.md`, and completion markers in `tasks.md`. Recording the user's real approval
in `approval.md` is permitted only after that approval is actually received.

Keep all other original files byte-for-byte unchanged, including corpus, retrieval,
answering, CLI, eval set, eval tools, existing tests, requirements and ignore rules.
Do not rewrite planning artifacts to fit an unexpected result. Propose material changes
and obtain renewed user approval instead.

## Execution phases

- **Phase 0: Evidence** — complete: 18 tests pass; baseline 6/12; E04/E09 CLI evidence saved.
  Human review of the saved evidence remains part of the pair's work.
- **Phase 1: Review** — current: user and Igor review v1; user explicitly authorizes it.
- **Phase 2: One implementation** — execute only the allowed changes, test, and save after.
- **Phase 3: Explain** — compare all 12, disclose regressions/limitations, inspect one changed
  answer/citation, preserve the behavior diff, prepare the shared report and real peer review.
  Stop at the mandatory minimum. Final submission and advanced work require later instructions.

## Measurement and interpretation

Baseline config is preserved in `results/before.json`. The only expected changed setting
is `CHUNK_STRATEGY`. An extra setting or file change is a scope violation to investigate,
not a reason to change the comparison tool. Eval fingerprints must match exactly.

Chunk lengths alter lexical score denominators, which can change every ranking and citation.
Track all previously passing IDs (E01, E02, E03, E07, E08, E12) for regressions and all
other IDs for side effects. Do not promise that E04/E09 will pass. Do not tune size, top-k,
thresholds, stopwords or current-version filtering if the result disappoints.

## Completion and rollback

Technical completion requires the approved diff, full passing tests, raw after/comparison,
matching immutable hashes, and the report's measured conclusions. Human CLI verification,
contributions, external peer feedback and the official-template mapping must be honest;
leave them visibly pending when not yet supplied.

If the approved implementation has a coding defect, correct it within the contract. If it
has only an unfavorable eval outcome, retain that outcome and explain it. A different
behavior approach needs renewed approval. Preserve all measurements before any later revert;
restore only the approved edited files from the Desktop reference if the user asks.

## Complexity Tracking

No new abstraction, dependency, infrastructure, or constitution exception is proposed.
