# Decision research: M1 proposal

**Status**: Proposed, v1; no candidate implementation or after-eval has been run.

## Decision

Propose menu item M1, using the existing sentence-chunking hook and standard library.
Keep `CHUNK_SIZE=140`, `CHUNK_OVERLAP=30`, and every retrieval/answering setting unchanged.
The overlap setting remains recorded but is unused by the sentence strategy, as the menu requires.

## Rationale

`results/before.json` records E04 and E09 as retrieval hits but without the fact in citations.
Their saved CLI runs show `hb-01-chunk-0` and `hb-01-chunk-2`; the latter starts with
`iness days.`. This supports investigating boundaries and retrieval together. It does not prove
that keeping sentences intact will make the sentence rank in the top two.

`src/chunking.py` already dispatches `sentences` to an unimplemented function.
`docs/improvement-menu.md` defines intact sentences, greedy packing, overlong single chunks,
and no overlap. There is no technology or dependency selection left to research externally.

## Alternatives considered

| Option | Evidence fit | Effort | Reason not included in this experiment |
| --- | --- | --- | --- |
| M1: sentence chunks | E04 and E09 | Small function, one setting, focused tests | Recommended proposal; effect unmeasured. |
| M5: current versions | E06 cites superseded `hb-02` | Small filter and one setting | A different intent; keep for a later user decision. |
| M6: top-k | More candidates might include a missing fact | One setting | Also changes citation noise; not combined with M1. |

## Limits

A simple punctuation-and-whitespace rule is sufficient for this handbook experiment, not a
general sentence parser. Changing chunk lengths changes lexical scores for all documents.
Do not experiment with alternatives or tune a second setting to force an improvement.

## Sources

- `docs/weekly-assignment.md`: required result, acceptance, verification, and Granica rada.
- `docs/improvement-menu.md`: M1 contract and one-intent rule.
- `src/chunking.py`, `src/config.py`, `src/retrieval.py`: current interfaces and scoring.
- `docs/baseline-findings.md` and its raw evidence links.
- Lesson slides 9, 15, 21, 23-26, 30: fixed questions, one change, risks, and reporting.
