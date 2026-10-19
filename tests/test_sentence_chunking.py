import pytest

from src import chunking, config
from src.corpus import Document


@pytest.mark.parametrize("chunk_size", [0, -1])
@pytest.mark.parametrize("text", ["", "   \t\n"])
def test_sentence_split_rejects_nonpositive_size_even_for_empty_text(
    text: str, chunk_size: int
) -> None:
    with pytest.raises(ValueError, match="chunk_size must be > 0"):
        chunking.split_text_by_sentences(text, chunk_size=chunk_size)


@pytest.mark.parametrize("text", ["", " \t\n  "])
def test_sentence_split_returns_no_chunks_for_empty_text(text: str) -> None:
    assert chunking.split_text_by_sentences(text, chunk_size=10) == []


def test_sentence_split_normalizes_whitespace_and_retains_punctuation() -> None:
    text = "  First\t sentence.\nSecond sentence!  Third?  Final words  "

    chunks = chunking.split_text_by_sentences(text, chunk_size=100)

    assert chunks == ["First sentence. Second sentence! Third? Final words"]
    assert " ".join(chunks) == "First sentence. Second sentence! Third? Final words"


def test_sentence_split_packs_exact_fit_including_joining_space() -> None:
    assert chunking.split_text_by_sentences("A. BB.", chunk_size=6) == ["A. BB."]
    assert chunking.split_text_by_sentences("A. BB.", chunk_size=5) == ["A.", "BB."]


def test_sentence_split_keeps_overlong_sentence_alone_and_in_order() -> None:
    text = "Short. This sentence is longer than ten. End."

    chunks = chunking.split_text_by_sentences(text, chunk_size=10)

    assert chunks == ["Short.", "This sentence is longer than ten.", "End."]
    assert " ".join(chunks) == text


def test_sentence_split_preserves_unpunctuated_tail_without_duplication() -> None:
    text = "First sentence. Final words without punctuation"

    chunks = chunking.split_text_by_sentences(text, chunk_size=18)

    assert chunks == ["First sentence.", "Final words without punctuation"]
    assert " ".join(chunks) == text


def test_split_text_dispatches_to_both_strategies(monkeypatch: pytest.MonkeyPatch) -> None:
    char_calls: list[tuple[str, int, int]] = []
    sentence_calls: list[tuple[str, int]] = []

    def fake_chars(text: str, chunk_size: int, overlap: int) -> list[str]:
        char_calls.append((text, chunk_size, overlap))
        return ["chars"]

    def fake_sentences(text: str, chunk_size: int) -> list[str]:
        sentence_calls.append((text, chunk_size))
        return ["sentences"]

    monkeypatch.setattr(chunking, "split_text_with_overlap", fake_chars)
    monkeypatch.setattr(chunking, "split_text_by_sentences", fake_sentences)
    monkeypatch.setattr(config, "CHUNK_SIZE", 17)
    monkeypatch.setattr(config, "CHUNK_OVERLAP", 4)

    monkeypatch.setattr(config, "CHUNK_STRATEGY", "chars")
    assert chunking.split_text("sample") == ["chars"]
    monkeypatch.setattr(config, "CHUNK_STRATEGY", "sentences")
    assert chunking.split_text("sample") == ["sentences"]

    assert char_calls == [("sample", 17, 4)]
    assert sentence_calls == [("sample", 17)]


def test_sentence_strategy_builds_deterministic_chunks_with_metadata(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    document = Document(
        doc_id="hb-test",
        title="Test handbook",
        section="Testing",
        version="2026",
        status="current",
        text="First. Second sentence.",
    )
    monkeypatch.setattr(config, "CHUNK_STRATEGY", "sentences")
    monkeypatch.setattr(config, "CHUNK_SIZE", 8)

    first_run = chunking.build_chunks([document])
    second_run = chunking.build_chunks([document])

    assert first_run == second_run
    assert [chunk.chunk_id for chunk in first_run] == [
        "hb-test-chunk-0",
        "hb-test-chunk-1",
    ]
    assert [chunk.text for chunk in first_run] == ["First.", "Second sentence."]
    assert all(
        (chunk.doc_id, chunk.title, chunk.version, chunk.status)
        == ("hb-test", "Test handbook", "2026", "current")
        for chunk in first_run
    )
