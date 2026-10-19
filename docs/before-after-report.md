# Week 7: One controlled RAG improvement

**State**: M1 implemented and measured; the approved scope and evidence checks are complete.
External pair feedback, the official template, and individual learner report details remain pending.
**Pair**: User (full submission name to be supplied) and Igor Nenadovic.
**Demonstration lead**: User; Igor led last week.
**Template**: The official before/after template has not been supplied. Map this content
to it later. This shared experiment report accompanies each learner's own weekly report.

## 1. Scope and starting state

Mandatory assignment only. Measured experiment: M1 sentence-aware chunking.
Spec Kit setup and planning are separate artifacts. The user approved v1 with "i approve v1"
and accepted the diagnosis with "i agree with the diagnostic" on 2026-10-19. On 2026-10-19,
the user confirmed Igor reviewed the baseline diagnoses and evidence.
Python 3.12.14, pytest 8.3.3; local handbook CLI, no runtime API or new infrastructure.

## 2. Baseline evidence

Commands actually run by the assistant with user permission:

```powershell
& '.\.venv\Scripts\python.exe' -m pytest
& '.\.venv\Scripts\python.exe' -m src.eval_runner --out results/before.json
```

18 tests passed. The eval passed 6/12. Behaviour accuracy: 0.8333; supported retrieval
hit rate: 0.7778; mean citation precision over answered questions: 0.4545.
Raw files: [before.json](../results/before.json), [eval table](../results/before-table.txt),
[test output](../results/tests-before.txt).

Eval fingerprint: `afe46db1e75a0b85bb5c9a93b6763e3b96e5cd7b289e12da6d2671e4d8650064`.

## 3. Two documented failures

| ID | Expected | Observed before | Type and evidence |
| --- | --- | --- | --- |
| E04 | Equipment duration `5 business days` from `hb-01` | Answer cites chunks 0 and 2 from the correct document; complete duration absent; fact=false; FAIL | Chunking/retrieval interaction; [CLI output](../results/E04-before-cli.txt). |
| E09 | IT portal under Hardware and duration `5 business days` from `hb-01` | Portal location appears, duration is incomplete; same two chunks; fact=false; FAIL | Chunking/retrieval interaction; [CLI output](../results/E09-before-cli.txt). |

The exact questions, scores and diagnosis are in [baseline findings](baseline-findings.md).
Human review: the user agreed with the diagnosis after the walkthrough on 2026-10-19.
On 2026-10-19, the user confirmed Igor reviewed both E04 and E09 against their saved CLI
evidence. No separate baseline review comment was supplied, so none is attributed here.

## 4. Specification written before the change

Approved v1: [specification](../specs/001-sentence-chunking/spec.md),
[plan](../specs/001-sentence-chunking/plan.md), [tasks](../specs/001-sentence-chunking/tasks.md).

The hypothesis was that whole sentences would keep the duration fact with its context. Only
M1 was approved. The measured result fixed E04 and E09, while the full comparison showed no
regressions. The remaining risk is that chunk lengths can alter rankings, citations and
refusals across the full set; E05, E10 and E11 remain failures.

User approval: "i approve v1", 2026-10-19 (Europe/Budapest), recorded in
[approval record](../specs/001-sentence-chunking/approval.md).

## 5. Applied change and diff

Implemented only the M1 sentence-aware splitter and selected `sentences` in `CHUNK_STRATEGY`.
The behavior diff is in `results/change-src.diff`; focused tests are in
`results/change-tests.diff`. No other config setting changed. The comparator reported no
settings warning.

## 6. After measurement and comparison

Attach `results/after.json`, `results/after-table.txt`, `results/tests-after.txt`, and the
unedited `results/comparison.txt`. The eval fingerprint matches the baseline.

| Metric | Before | After | Delta |
| --- | --- | --- | --- |
| Passed | 6/12 | 9/12 | +3 |
| Behaviour accuracy | 0.8333 | 0.8333 | +0.0000 |
| Retrieval hit rate | 0.7778 | 0.8889 | +0.1111 |
| Mean citation precision | 0.4545 | 0.5455 | +0.0910 |

Fixed: E04, E06, E09. Regressed: none. Unchanged: E01, E02, E03, E05, E07, E08, E10,
E11, E12. Changed setting: `CHUNK_STRATEGY` (`chars` to `sentences`) only. Comparator
warning: none. The eval fingerprint matched exactly:
`afe46db1e75a0b85bb5c9a93b6763e3b96e5cd7b289e12da6d2671e4d8650064`.

The hypothesis was supported for E04 and E09: citations now contain `5 business days`.
E06 also changed from fail to pass. No previously passing question regressed. E05 still
misses the expected document for the paraphrase; E10 and E11 still answer questions that
should be refused.

## 7. Manual answer and citation check

Question checked: E04. Command:
`& '.\.venv\Scripts\python.exe' -m src.cli --question 'How many business days does a laptop replacement take?' --show-retrieved`.
Output: [E04 after CLI evidence](../results/E04-after-cli.txt). The output cites the complete
duration sentence from `hb-01-chunk-1` and shows the source title, version and current status.
On 2026-10-19, the user confirmed both the user and Igor inspected the answer and citation
and found them correct.

## 8. Remaining limitations

E05 still fails because the lexical retriever misses the expected handbook document for a
paraphrased question. E10 and E11 still answer unsupported questions. Sentence splitting
uses a simple `.`, `!`, `?` boundary rule and does not parse abbreviations or quoted
punctuation. These limits remain outside M1's approved scope.

## 9. External pair review

Reviewer pair, actual comment, and date: pending. Ask the assigned pair to address:

1. Is the change one intent and consistent with the specification?
2. Does the before/after evidence support the conclusion?
3. Is any regression or limitation omitted?

Do not substitute internal team review or an AI-generated comment for this feedback.

## 10. AI use and actual contributions

Assistance and verification are recorded in [AI-use note](ai-use.md).

| Person | Planned role | Actual contribution and verification |
| --- | --- | --- |
| User | Approve plan, supervise implementation, inspect CLI, lead demonstration | Approved v1, agreed with the diagnosis, confirmed Igor's baseline review, and confirmed both user and Igor checked E04's answer and citation. Leads the demonstration. |
| Igor Nenadovic | Review failures, verify measurements/regressions, draft evidence tables | User confirmed Igor reviewed E04/E09 baseline evidence and joined the E04 answer/citation check. Further contribution detail is pending confirmation. |

Use [team workflow](team-workflow.md) for the planned allocation. Each learner still supplies
their own reflection and individual weekly-report content. Do not infer it from this outline.

## 11. Submission evidence and demonstration

Attach both raw eval JSON files (they are Git-ignored), comparison output, behavior/test
diffs, final shared report, actual peer comment, AI-use note, and both contributions.
The user demonstrates failure -> spec -> diff -> same-set comparison -> limitation/regression
-> pair contributions. Submission is a separate human action.

Assignment dates (Europe/Budapest): external pair comment 19 October 2026 at 20:00;
individual reports 20 October at 12:00; Session 2 demonstration 21 October.
No comment, report, or email has been sent by this assistant.
