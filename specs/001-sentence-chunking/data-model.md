# Existing data model

No new schema, storage, service, or data file format is proposed.

| Entity | Existing fields and constraints | Proposed effect |
| --- | --- | --- |
| `Document` | `doc_id`, `title`, `section`, `version`, `status`, `text` | None; handbook content and metadata remain fixed. |
| `Chunk` | Frozen object: `chunk_id`, `doc_id`, `title`, `version`, `status`, `text` | Only text boundaries and therefore positional IDs can differ between strategies. |
| Chunk identifier | `doc_id` + `-chunk-` + zero-based position within that document | Preserve generation format and deterministic ordering. IDs need not stay identical across strategies. |
| Retrieval result | `chunk`, `score` | Same scoring and sorting rules; values can change with the new chunks. |
| Eval run | `created_at`, `eval_set_sha256`, `config`, `summary`, `results` | Existing schema; preserve both raw runs. |

All chunk texts are nonempty. Whitespace is normalized before sentence segmentation.
The only intended config snapshot difference is `CHUNK_STRATEGY: chars -> sentences`.
