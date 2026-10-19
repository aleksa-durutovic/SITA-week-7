# Tasks: One measured M1 experiment

**Revision**: v1 | **Status**: Awaiting user approval; all execution tasks remain unchecked.
**Input**: `spec.md`, `plan.md`, `research.md`, `data-model.md`, `contracts/chunking.md`.
One user story, US1. Focused tests are explicitly required by FR-006.
Baseline measurement already exists; these tasks must not overwrite it.

## Phase 1: Setup and approval

- [x] T001 User reviews and explicitly approves v1 of `spec.md`, `plan.md`, and `tasks.md`; record the actual approval in `approval.md` before implementation (FR-003).
- [x] T002 Verify the initial `review-manifest.json` hashes and inspect `results/before.json` and `results/tests-before.txt`; retain the raw baseline unchanged (FR-001).

## Phase 2: Foundational evidence review

- [x] T003 Igor and user review the two separate diagnoses in `docs/baseline-findings.md` against `results/E04-before-cli.txt` and `results/E09-before-cli.txt`; record only real human review in `docs/before-after-report.md` (FR-002).
- [x] T004 Check original hashes in `docs/checkpoint-manifest.json` and the allowlist in `plan.md`; confirm no source, config or tests changed before approval (FR-003, FR-005, FR-006, FR-011, FR-012).

## Phase 3: US1 - Implement and measure one decision (Priority: P1)

Goal: exactly one implementation with a complete evidence bundle, regardless of hypothesis outcome.
Independent test: full tests, same 12 eval questions/hash, one behavior diff, comparison, and CLI evidence.

- [x] T005 [US1] Add `tests/test_sentence_chunking.py` covering validation including empty text, whitespace, `. ! ?` boundaries, exact-fit joining space, isolated overlong sentences, unpunctuated tail, no text loss/duplication, dispatch and metadata/ID determinism from `contracts/chunking.md` (FR-004, FR-006).
- [x] T006 [US1] Run the focused tests before implementing the hook and save the expected missing-function failures in `results/tests-sentences-red.txt`; do not change existing tests (FR-006).
- [x] T007 [US1] Implement only `split_text_by_sentences` and its required standard-library import/docstring in `src/chunking.py`: positive size; normalized text; greedy intact sentences; overlong sentence alone; no overlap; deterministic order (FR-004, FR-005, FR-011).
- [x] T008 [US1] Change only `CHUNK_STRATEGY` from `chars` to `sentences` in `src/config.py`; keep size 140, overlap 30 and all other settings (FR-004, FR-005).
- [x] T009 [US1] Run the full suite using `quickstart.md`; save passing output in `results/tests-after.txt`, correcting only defects within the approved contract (FR-006).
- [x] T010 [US1] Run the full unchanged eval command with `--out results/after.json` and save `results/after-table.txt`; preserve `results/before.json` (FR-007).
- [x] T011 [US1] Run the standard comparator into `results/comparison.txt`; verify matching fingerprint, all fixed/regressed/unchanged IDs and metric deltas, and only one changed setting (FR-007, FR-008).
- [x] T012 [US1] Run CLI for one changed question using `quickstart.md`, save `results/<ID>-after-cli.txt`, and have the user and Igor inspect the answer/cited text; if none changes, record that and inspect E04 (FR-009).
- [x] T013 [US1] Save `results/change-src.diff` and `results/change-tests.diff` against the untouched Desktop original; verify all protected hashes and no extra files/settings changed (FR-005, FR-006, FR-011, FR-012).

## Phase 4: Report and hand back to the humans

- [x] T014 Fill measured sections of `docs/before-after-report.md` from raw evidence, explaining every regression and at least one remaining limitation; record a rejected hypothesis honestly (FR-008, FR-010).
- [ ] T015 Have the humans supply actual contributions, external pair feedback and the official template; map `docs/before-after-report.md` to it when available, leaving missing inputs visibly pending (FR-010).
- [x] T016 Update `docs/ai-use.md` with actual assistance and verification, record the user's demo role in `docs/before-after-report.md`, and hand over the evidence bundle without submitting or starting advanced work (FR-010, FR-012).

## Dependencies and execution strategy

Execute in numeric order. T001 blocks every application/config/test edit. T002 verifies the
initial reviewed package before task markers start changing. T005-T006 precede T007-T008;
T009 precedes after-eval and comparison. Reporting depends on actual evidence.
The assistant may prepare outputs, but T003, the human part of T012, and T015 require real people.
Stop and request missing input when a human task is pending; do not simulate it.

US1 is the entire mandatory experiment. There are no additional feature stories or deployment tasks.
No tasks are marked parallel because one PC and one assistant session are in use.
Parallel review example: the user explains E04 while Igor checks E09's saved output;
neither starts a second implementation. Complete only this experiment, then stop.
