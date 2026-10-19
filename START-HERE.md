# Week 7: Review before implementation

**Current state**: Spec Kit installed, baseline collected, M1 plan v1 proposed.
**Implementation permission**: pending. No RAG source/configuration/test changes.

## Review these first

1. [Measured failures](docs/baseline-findings.md): 18 tests pass; baseline 6/12; E04 and E09
   lack the duration fact in cited fragments.
2. [Specification](specs/001-sentence-chunking/spec.md): one hypothesis and measurable outcome.
3. [Plan](specs/001-sentence-chunking/plan.md): exact files, risks, fixed settings and verification.
4. [Tasks](specs/001-sentence-chunking/tasks.md): 16 ordered tasks, including human checks.
5. [Pair roles](docs/team-workflow.md): user approves and demonstrates; Igor leads evidence review.

The proposal is **M1: sentence-aware chunking**, not an approved choice yet. Whole sentences
may retain the missing fact and may also change rankings elsewhere. No other improvement
or advanced work is included. Review the linked contract if you want the exact edge cases.

## Tool and model

Recommendation: keep using Codex for this local project and select the user's chosen
Luna 6 for implementation after approval. Codex supports repository instructions through
`AGENTS.md` ([OpenAI workflow guidance](https://developers.openai.com/cookbook/examples/codex/iterating-development-workflows-with-codex)); the narrowly scoped handoff is in
[implementation-prompt.md](specs/001-sentence-chunking/implementation-prompt.md).
Luna is described by [OpenAI's model documentation](https://developers.openai.com/api/docs/models/gpt-6-luna)
as efficient for focused tasks. Suitability for this particular change is a recommendation;
tests and measurements still determine whether its output is correct.

Spec Kit 1.0.9 is configured for Codex skills and PowerShell. Its commands are chat skills
such as `$speckit-plan`, `$speckit-tasks`, and `$speckit-implement`, not terminal commands.
See the [official integration guide](https://github.github.io/spec-kit/reference/integrations.html).
The first two stages are drafted; do not regenerate approved plans just to start coding.
No additional model, global configuration, external repository, or service was installed.

## Approval and handoff

Read [approval.md](specs/001-sentence-chunking/approval.md). If the proposal is acceptable,
explicitly approve v1 of the specification, plan and tasks in this chat. Requested revisions
are welcome before that approval. Then select Luna 6 and use the bounded handoff prompt.
The approval rule is an assistant instruction, not an operating-system permission lock.

[AGENTS.md](AGENTS.md), the constitution, the approval record, and an added review gate in
the bundled workflow all require human approval before implementation. Automatic approval
flags or workflow gates must not be used to bypass the user's review.

## Remaining human inputs

- User/Igor review of the proposed change and roles, followed by the user's decision.
- Official before/after report template, when supplied; [provisional outline](docs/before-after-report.md) is ready.
- User's full submission name, actual contributions and external pair feedback before final report.

The original Desktop checkpoint is preserved. All 22 original files can be checked against
[checkpoint-manifest.json](docs/checkpoint-manifest.json). [Quickstart](specs/001-sentence-chunking/quickstart.md)
includes exact commands and a diff method that works despite the workspace having no commits.
