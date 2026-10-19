# Prompt for the next Luna 6 session

Start the next session in this workspace and select Luna 6. Paste the following prompt.
This file is a handoff requested after v1 approval; it does not change the approved approach.

```text
Continue the approved Week 7 RAG assignment in:
C:\Users\AleksA\Documents\ChatGPT\week-7

I approved v1 in the previous chat and agreed with the E04/E09 diagnosis. Read AGENTS.md
and specs/001-sentence-chunking/approval.md first. My approval persists; do not ask for it
again. Implementation was intentionally deferred to this session using Luna 6.

Read the constitution and the feature's spec.md, plan.md, tasks.md, contracts/chunking.md
and quickstart.md. T001 and T002 are complete. Establish whether Igor has completed his
baseline review for T003; ask only for his missing confirmation if it is still unrecorded.
Do not attribute human work without confirmation.

Verify the original checkpoint and reviewed package hashes before editing. When verifying
tasks.md against the initial review manifest, normalize completed task checkboxes to unchecked;
completion markers are the only permitted difference. Do not rewrite the manifest to hide
other differences or regenerate approved plans.

Then implement exactly M1: sentence-aware chunking, following the approved tasks and contract.
Behavior/test edits are limited to src/chunking.py, only CHUNK_STRATEGY in src/config.py,
and new tests/test_sentence_chunking.py. Keep every other setting, existing test, corpus,
eval question, evaluator, dependency and infrastructure unchanged.

Use .venv\Scripts\python.exe. Preserve before.json and baseline logs. Run the focused tests
before implementing, then the full suite, all 12 eval questions, the standard comparison,
and diff/integrity checks using quickstart.md. Save actual evidence; report all regressions
and a rejected hypothesis honestly rather than adding another fix.

Prepare the measured report sections and pause for genuine human checks or missing inputs.
Roles: I approve/supervise and lead the demonstration; Igor leads evidence/regression review.
Do not invent peer feedback or contributions. Do not start advanced work, commit, submit,
send messages, or launch another assistant. Report changed files, tests, comparison results,
remaining limitations and pending human tasks.
```
