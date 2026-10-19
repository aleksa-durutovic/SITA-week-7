# Luna 6 handoff

Use Codex with Luna 6, selected by the user. No coding model has been launched or changed
automatically. After plan approval, give it this prompt:

```text
Work in C:\Users\AleksA\Documents\ChatGPT\week-7.
Read AGENTS.md and specs/001-sentence-chunking/approval.md first.
If the user has not explicitly approved the current v1 spec, plan and tasks, stop.
Read the constitution, spec.md, plan.md, tasks.md and contracts/chunking.md.
Follow quickstart.md for verification and check the initial review-manifest hashes.
Implement only the approved M1 change, using the exact file allowlist.
Execute tasks in order, preserving all baseline and protected files.
Do not regenerate plans, tune extra settings, add dependencies, or start advanced work.
Use the saved eval before/after and comparator as evidence, even if M1 disappoints.
Pause for the human-review tasks; do not invent contributions or peer feedback.
Report the actual files changed, tests, fixed/regressed IDs, limitations and pending inputs.
Do not commit, submit, message another pair, or start a second assistant run.
```

The Spec Kit skill form for Codex is `$speckit-implement`; it is an alternative entry point
after approval, with the same scope and human-task requirements. These are chat instructions,
not PowerShell commands. The explicit handoff above gives the smaller model the bounded task
without repeating repository discovery or regenerating approved planning files.
