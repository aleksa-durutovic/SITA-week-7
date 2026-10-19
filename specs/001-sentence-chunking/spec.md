# Feature Specification: One measured sentence-chunking change

**Feature directory**: `specs/001-sentence-chunking`
**Created**: 2026-10-19
**Revision**: v1
**Status**: Proposed; awaiting user approval before implementation
**Input**: Mandatory Week 7 assignment only; English instructions; Luna 6 implementation;
user and Igor Nenadovic working on the same PC.

## User Scenarios & Testing

### User Story 1 - Explain one controlled RAG experiment (Priority: P1)

As the learner pair, we want to diagnose concrete failures, propose one change, approve its
plan, and measure its effects on the same questions so we can explain the result honestly.

**Independent test**: The evidence bundle contains baseline, two diagnosed question IDs,
a specification written before the edit, one behavior diff, a full after run, comparison,
and a manual answer/citation check. A negative result is a valid measured outcome.

**Acceptance scenarios**:

1. Given the unchanged checkpoint, when the baseline is measured, all 12 questions and
   the eval fingerprint are recorded; at least two failures have expected/actual evidence.
2. Given this proposed change, when the user has not approved v1, code and test edits stop.
3. Given approval, when whole-sentence chunks replace character cuts, no sentence is split
   solely to meet the chunk-size target; other RAG decisions remain fixed.
4. Given the after measurement, when compared with baseline, every fixed and regressed
   question and every metric delta is retained, even if the hypothesis is rejected.

### Edge Cases

- Empty or whitespace-only text produces no chunks; nonpositive size is rejected.
- Adjacent short sentences fit together up to the size target, including the joining space.
- A sentence longer than the target remains intact in its own chunk.
- Final text without terminal punctuation is retained; repeated whitespace is normalized.
- Changed boundaries may change chunk IDs, rankings, citations, and refusal decisions.
- The simple sentence rule is for this English handbook; abbreviations and quoted punctuation
  are not a general natural-language parsing requirement.

## Requirements

### Functional Requirements

- **FR-001**: Preserve the measured baseline and record all 12 question results and settings.
- **FR-002**: Document E04 and E09 separately with expected answer, actual citations,
  failure type, and evidence links.
- **FR-003**: Before edits, specify failure, hypothesis, one change, expected effect,
  regression risk, and verification; obtain the user's approval of spec, plan, and tasks.
- **FR-004**: Apply only menu item M1: whole-sentence chunking, greedily packed to the
  existing size target; keep overlong sentences intact and introduce no overlap.
- **FR-005**: Keep all other settings, handbook content, retrieval, and answering behavior
  unchanged; preserve the existing character-chunking option.
- **FR-006**: Preserve the eval questions, metric/comparison code, and existing tests;
  add focused tests for the new chunking contract without changing measured expectations.
- **FR-007**: Rerun all 12 questions with the same eval command, differing only in output
  filename; compare the saved runs with an identical eval fingerprint.
- **FR-008**: Record fixed IDs, regression IDs, unchanged IDs, all metric deltas, changed
  settings, and any warning; explain all regressions and remaining limitations.
- **FR-009**: Manually inspect the CLI answer and citation for one changed question.
  If no question changes, record that fact and inspect E04 as the unchanged target.
- **FR-010**: Prepare a before/after report, evidence files, behavior diff, AI-use note,
  actual contributions of both people, and the user's demonstration role; include real
  external pair feedback when available and map to the official template when supplied.
- **FR-011**: Keep runtime local and offline after setup, with no new runtime dependency,
  vector database, embedding service, paid API, or infrastructure.
- **FR-012**: Stop after the mandatory experiment; any advanced goal needs a later request.

### Key Entities

- **Change specification**: one proposed decision, its risks, approval, and revision.
- **Evidence bundle**: immutable baseline, after run, comparison, CLI check, and diff.
- **Pair contribution**: real activity attributed to the user or Igor; planned work is labeled.

## Success Criteria

- **SC-001**: At least two failures are explained with concrete question IDs and evidence.
- **SC-002**: Exactly one approved behavior change is visible in the experiment diff.
- **SC-003**: Both measurements cover the same 12 questions and fingerprint; the full
  mechanical test suite passes after the change.
- **SC-004**: Every regression is disclosed, at least one limitation remains documented,
  and a human checks one CLI answer and its cited source.
- **SC-005**: Both people can explain their actual contribution and the user can lead
  the demonstration from the saved evidence.

## Proposed change specification

| Field | Proposal |
| --- | --- |
| Failure | E04 and E09 cite equipment fragments without the complete duration fact. |
| Hypothesis | Keeping sentences intact will put the duration and its context in a retrievable unit. |
| Change | M1: replace active character cuts with sentence-aware chunks; retain size target. |
| Expected effect | E04 and E09 gain the cited fact `5 business days`, ideally changing FAIL to PASS. This is unmeasured. |
| Regression risk | Different lengths change lexical score denominators, rankings and citations across all questions; some current passes can fail. |
| Verification | Full unchanged eval before/after, standard comparison, full tests, and a human CLI check. |

## Assumptions and deferred inputs

M1 is a recommendation for review, not a user-selected or approved implementation yet.
The official report template is missing; a provisional outline is authorized.
The user's full submission name and external reviewer's feedback will be supplied by people.
Neither is needed to review the technical plan. Improvement is a hypothesis, not a pass condition
that authorizes extra tuning when results disappoint.
