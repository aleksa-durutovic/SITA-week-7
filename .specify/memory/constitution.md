<!--
Sync Impact Report (remove before a future commit):
Version: unfilled scaffold -> 1.0.0 (initial rules from the user and assignment).
Principles: one change; fixed measurement; human approval; offline simplicity; honest evidence.
Added sections: Scope and environment; Pair workflow and review.
Removed sections: none. Deferred governance fields: none.
-->
# Week 7 RAG Constitution

## Core Principles

### I. Exactly one change of intent

The mandatory assignment MUST contain exactly one RAG behavior change between the baseline
and the after measurement. Supporting tests and evidence belong to that change. Spec Kit setup
and planning documents MUST be distinguishable from the behavior diff. Unrelated refactoring,
parameter tuning, and additional menu items MUST NOT be bundled into the experiment.

### II. Fixed, reproducible measurement

The team MUST preserve `eval/eval_set.json`, `src/eval_runner.py`, `src/eval_compare.py`,
and the existing evaluation tests. The baseline MUST precede the behavior edit. Both runs MUST
use all 12 questions and the same eval command, with only the output filename differing.
The eval hash MUST match; every regression and metric delta MUST be reported.

### III. User approval before implementation

Plans and instructions may be drafted now. Application code, configuration, and test edits
MUST wait for the user's explicit approval of the current specification, plan, and tasks.
Baseline permission, a model choice, and completed checklists do not grant that approval.
An assistant MUST NOT approve its own work. A material change to the approved approach or
file allowlist MUST return to the user before editing. Record approval in the feature's
`approval.md` using the user's actual words; do not invent consent.

### IV. Keep the existing local system

The mandatory work MUST use the existing Python CLI and standard library, with the current
`pytest==8.3.3` dependency. It MUST NOT introduce a vector database, embedding service, paid
API, web UI, new service, or new infrastructure. A coding assistant is a development tool;
it MUST NOT become a runtime dependency of this RAG system.

### V. Evidence and authorship must be truthful

AI suggestions MUST remain hypotheses until measured. The report MUST document at least two
question-specific failures, the change specification, actual before/after evidence, all
regressions, and at least one remaining limitation. A rejected hypothesis is an acceptable
outcome. Contributions and peer comments MUST describe real human work; assistants MUST NOT
invent reflection, human checks, reviewer feedback, or successful results.

## Scope and environment

`docs/weekly-assignment.md` is the assignment source of truth. The initial scope is the
mandatory work under "Granica rada". The advanced goal requires a later explicit request
after the mandatory submission. Instructions are in English. Work takes place on this PC
in `C:\Users\AleksA\Documents\ChatGPT\week-7`, using `.venv\Scripts\python.exe`
(Python 3.12.14). Keep the Desktop checkpoint as the original reference.

## Pair workflow and review

The user and Igor Nenadovic work as a pair, alternating driver and reviewer on the same PC.
The user approves plans and leads this week's demonstration because Igor led last week.
`docs/team-workflow.md` owns the proposed task allocation; its entries are planned work until
the people confirm completion. Review by another pair is separate from Igor's internal
review. The missing official before/after template may be mapped from a provisional outline
when supplied; it MUST NOT be represented as already available.

## Governance

The assignment and explicit user instructions govern these rules. Any amendment that expands
scope or changes implementation permission MUST be raised with the user. Use semantic
versioning for later amendments: major for incompatible rules, minor for added rules, patch
for clarifications. Planning review MUST check scope, immutable evaluation, the file allowlist,
approval state, and evidence requirements. Do not commit, publish, or submit on the pair's
behalf without a separate user instruction.

**Version**: 1.0.0 | **Ratified**: 2026-10-19 | **Last Amended**: 2026-10-19
