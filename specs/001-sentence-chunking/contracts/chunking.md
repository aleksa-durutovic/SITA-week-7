# M1 chunking contract

**Revision**: v1, proposed. This defines behavior, not implementation code.

`split_text_by_sentences(text: str, chunk_size: int = 140) -> list[str]`
must satisfy:

1. Reject `chunk_size <= 0` with `ValueError`, including when text is empty.
2. Normalize whitespace as the existing character splitter does: whitespace-separated
   tokens joined by one space, with no leading/trailing whitespace.
3. For nonempty normalized text, recognize a boundary at whitespace immediately following
   `.`, `!`, or `?`. Retain the punctuation and any final unpunctuated text.
4. Greedily pack adjacent sentences in original order, joining them with one space, while
   the combined length, including that space, is at most `chunk_size`.
5. A sentence longer than `chunk_size` is one chunk on its own; never split it or attach
   another sentence to it. Flush any preceding pending chunk first.
6. Do not introduce overlap or duplicate sentence text. Joining output chunks with one
   space reproduces the normalized input exactly.
7. Empty/whitespace-only input returns `[]`. Output is deterministic.

`split_text()` must continue dispatching both strategies. The `chars` branch, validation,
unknown-strategy error, `Chunk` metadata, and ID format retain existing behavior.
There is no CLI argument or output-schema change.

## Focused test scenarios

New tests go only in `tests/test_sentence_chunking.py`, after approval.

| Scenario | Observable assertion |
| --- | --- |
| Zero/negative size | `ValueError`, including for empty text. |
| Empty/whitespace | Empty list with a valid size. |
| Mixed whitespace and `. ! ?` | Normalized content, retained punctuation, correct sentence boundaries. |
| Exact fit and one character beyond | Packing includes the joining space and respects the limit. |
| Long sentence between shorter ones | Long sentence is intact and isolated; order is preserved. |
| Unpunctuated final text | Tail survives; no text loss or duplication. |
| Strategy dispatch | Use pytest monkeypatch to select each strategy; retain character results. |
| Chunk integration | Sentence strategy preserves per-document ID format, metadata, and deterministic output. |

Use small synthetic texts rather than changing eval questions or hard-coding handbook answers.
No NLP dependency, abbreviation dictionary, or quotation parser is required.
