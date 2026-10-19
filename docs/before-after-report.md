# Week 7: One controlled RAG improvement — before/after report

**Pair**: Aleksa Durutovic and Igor Nenadovic.
**Report updated**: 2026-10-20 (Europe/Budapest).
**State**: The mandatory technical experiment is complete; external pair feedback is pending.
**Demonstration lead**: Aleksa Durutovic; Igor led last week.
**Format check**: This report covers the required content in the weekly assignment. The
separate official "Šablon za izveštaj pre/posle" has not been supplied, so alignment with
that template remains unverified. This is the pair's shared report; each learner submits
their own individual weekly report alongside it.

**Repository**: [SITA-week-7](https://github.com/aleksa-durutovic/SITA-week-7).
**Implementation commit**: [57d7aca](https://github.com/aleksa-durutovic/SITA-week-7/commit/57d7aca42a84782be28b8fcaa4c83167a1ed5d7c).

## 1. Scope and starting state

Mandatory assignment only. Measured experiment: M1 sentence-aware chunking.
Spec Kit setup and planning are separate artifacts. Aleksa approved v1 with "i approve v1"
and accepted the diagnosis with "i agree with the diagnostic" on 2026-10-19. On 2026-10-19,
Aleksa confirmed Igor reviewed the baseline diagnoses and evidence. Both members later
confirmed, through Aleksa, that they reviewed the code and diff and manually ran commands.
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
Human review: Aleksa agreed with the diagnosis after the walkthrough on 2026-10-19.
On 2026-10-19, Aleksa confirmed Igor reviewed both E04 and E09 against their saved CLI
evidence. No separate baseline review comment was supplied, so none is attributed here.

## 4. Specification written before the change

Approved v1: [specification](../specs/001-sentence-chunking/spec.md),
[plan](../specs/001-sentence-chunking/plan.md), [tasks](../specs/001-sentence-chunking/tasks.md).

The specification was written and approved before the behavior edit:

| Specification field | Decision recorded before implementation |
| --- | --- |
| Failure | E04 and E09 retrieve the equipment document but omit the complete duration fact from the selected citations. |
| Hypothesis | Whole sentences keep the duration fact together with the context needed for retrieval. |
| One change | M1: implement sentence-aware chunking and select that strategy; preserve all other RAG settings. |
| Expected effect | E04 and E09 gain the cited fact `5 business days`, ideally changing from FAIL to PASS. |
| Regression risk | Changed chunk lengths alter lexical scores, rankings, citations and potentially refusals across all 12 questions. |
| Verification | Full tests, full unchanged eval set before/after, standard comparison, matching fingerprint, and a manual CLI answer/citation check. |

The actual results are reported in section 6. No second improvement was added to obtain
those results.

Aleksa's approval: "i approve v1", 2026-10-19 (Europe/Budapest), recorded in
[approval record](../specs/001-sentence-chunking/approval.md).

## 5. Applied change and diff

Implemented only the M1 sentence-aware splitter and selected `sentences` in `CHUNK_STRATEGY`.
The behavior diff is in [change-src.diff](../results/change-src.diff); focused tests are in
[change-tests.diff](../results/change-tests.diff). Implementing the splitter and selecting
it are one intent. Spec Kit, documentation and Git packaging accompany the experiment;
the behavior-only diff isolates the RAG change. No other RAG config setting changed.
The comparator reported no settings warning.

## 6. After measurement and comparison

The full after measurement uses the same eval command as the baseline, differing only
in its output filename:

```powershell
& '.\.venv\Scripts\python.exe' -m src.eval_runner --out results/after.json
& '.\.venv\Scripts\python.exe' -m src.eval_compare results/before.json results/after.json
& '.\.venv\Scripts\python.exe' -m pytest
```

Saved evidence: [after.json](../results/after.json), [after table](../results/after-table.txt),
[test output](../results/tests-after.txt), and the unedited
[comparison output](../results/comparison.txt). All 30 tests passed. The eval fingerprint
matches the baseline, and the fixed questions, evaluator and comparison code are unchanged.

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
E06 also changed from fail to pass as an effect of the same chunking change; no current-version
filter or second improvement was introduced. No previously passing question regressed. E05 still
misses the expected document for the paraphrase; E10 and E11 still answer questions that
should be refused.

## 7. Manual answer and citation check

Question checked: E04. Command:
`& '.\.venv\Scripts\python.exe' -m src.cli --question 'How many business days does a laptop replacement take?' --show-retrieved`.
Output: [E04 after CLI evidence](../results/E04-after-cli.txt). The output cites the complete
duration sentence from `hb-01-chunk-1` and shows the source title, version and current status.
On 2026-10-19, Aleksa confirmed both he and Igor inspected the answer and citation
and found them correct.

## 8. Remaining limitations

E05 still fails because the lexical retriever misses the expected handbook document for a
paraphrased question. E10 and E11 still answer unsupported questions. Sentence splitting
uses a simple `.`, `!`, `?` boundary rule and does not parse abbreviations or quoted
punctuation. These limits remain outside M1's approved scope.

## 9. External pair review

The actual review has not been supplied for inclusion in this report.

- Reviewer pair: pending.
- Review date: pending.
- Received comment: pending.
- The pair's reciprocal review of the assigned other pair: not recorded in the supplied evidence.

The assigned reviewers must address:

1. Is the change one intent and consistent with the specification?
2. Does the before/after evidence support the conclusion?
3. Is any regression or limitation omitted?

Do not substitute internal team review or an AI-generated comment for this feedback.

## 10. AI use and actual contributions

AI assisted with understanding the checkpoint, preparing the specification and plan,
and implementing the approved change. Aleksa confirmed that implementation used Luna 6.
Aleksa and Igor reviewed the code and diff, manually ran commands, and checked the E04
answer and citation. The measured evidence supports the conclusion about improvement.
Additional assistance and verification details are recorded in [AI-use note](ai-use.md).

| Person | Confirmed contribution | Planned role in Session 2 |
| --- | --- | --- |
| Aleksa Durutovic | Approved v1 before implementation and agreed with the diagnosis; reviewed code and diff with Igor; participated in manual command execution and the E04 answer/citation check. | Leads the demonstration. |
| Igor Nenadovic | Reviewed the E04/E09 baseline diagnoses and saved CLI evidence; reviewed code and diff with Aleksa; participated in manual command execution and the E04 answer/citation check. | Supports the evidence review and questions. |

These contributions are based on Aleksa's confirmations in the project conversations;
they do not claim that either learner independently authored the AI-generated implementation.
The [team workflow](team-workflow.md) records the planned allocation. Each learner supplies
their own reflection and individual weekly-report content separately.

## 11. Submission evidence and demonstration

The repository includes both raw eval JSON files despite the original ignore pattern,
comparison output, test results, behavior/test diffs, the shared report and the AI-use note.
The actual external peer comment must still be added. Both members attach the same shared
report or repository link to their individual weekly submissions.

Aleksa demonstrates failure -> specification -> diff -> same-set comparison -> remaining
limitation/regression -> pair contributions. Igor supports the evidence discussion.
Submission and reciprocal peer review are human actions; this report does not claim they
have been completed.

Assignment dates (Europe/Budapest): external pair comment 19 October 2026 at 20:00;
individual reports 20 October at 12:00; Session 2 demonstration 21 October.
No comment, report, or email has been sent by this assistant.
