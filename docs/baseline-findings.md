# Measured baseline and failure diagnosis

**Measured**: 2026-10-19, unchanged checkpoint, Python 3.12.14, pytest 8.3.3.
The assistant ran these commands with the user's permission. Human reproduction/review
is planned; it has not been attributed to either learner.

| Measurement | Actual result | Evidence |
| --- | --- | --- |
| Mechanical tests | 18 passed | `results/tests-before.txt` |
| Eval passed | 6/12 | `results/before.json`, `results/before-table.txt` |
| Behaviour accuracy | 0.8333 | Raw baseline summary |
| Retrieval hit rate | 0.7778 | Raw baseline summary |
| Mean citation precision | 0.4545 | Raw baseline summary |

Eval SHA-256: `afe46db1e75a0b85bb5c9a93b6763e3b96e5cd7b289e12da6d2671e4d8650064`.
Passing IDs: E01, E02, E03, E07, E08, E12.
Failing IDs: E04, E05, E06, E09, E10, E11.

## Failure 1: E04

- Question: `How many business days does a laptop replacement take?`
- Expected: answer from `hb-01` with the complete fact `5 business days`.
- Actual: answers and cites `hb-01-chunk-0` and `hb-01-chunk-2`. Retrieval hit is true,
  citation precision is 1.0, but fact-in-citations is false and the question fails.
- CLI evidence: `results/E04-before-cli.txt`. Chunk 0 stops at `with`; chunk 2 starts
  `iness days.`. The intact duration fact is absent from the selected citations.
- Type: chunking/retrieval interaction resulting in an incomplete answer. The expected
  document is found, but the needed fact-bearing chunk is not among the selected two.
- Hypothesis: sentence boundaries could preserve the fact together with its context.

## Failure 2: E09

- Question: `Where do I request a replacement laptop and how long does it take?`
- Expected: answer from `hb-01`, request through IT portal under Hardware, and the
  complete duration fact `5 business days` (the fixed evaluator checks that duration).
- Actual: the same two citations; the portal location is visible, but the complete duration
  is missing. Retrieval hit true, citation precision 1.0, fact-in-citations false, FAIL.
- CLI evidence: `results/E09-before-cli.txt`, including the retrieved scores and fragments.
- Type: chunking/retrieval interaction and incomplete answer.
- Hypothesis: keeping the duration sentence intact could make it retrievable with context.

These are two distinct eval questions with the same plausible cause. No after result
exists, so this diagnosis does not establish that the proposed M1 change will fix them.

## Other observed failures to retain in the report

E05 retrieves unrelated documents for a paraphrase. E06 cites superseded `hb-02`, not the
expected current `hb-03`. E10 and E11 answer questions that should be refused. These are
baseline facts, not guaranteed post-change outcomes. Do not add fixes for them to M1.

The evaluator checks facts in cited chunks and document-based citation precision. A pass
does not establish general language understanding or exhaustive answer correctness.
