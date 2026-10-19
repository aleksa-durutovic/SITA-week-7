# Proposed pair workflow on one PC

**User**: plan approver, implementation driver, and this week's demonstration lead.
**Igor Nenadovic**: evidence and regression-review lead.
Igor led last week's demonstration; the user leads this week to satisfy rotation.
These are proposed responsibilities, not completed contribution claims.

| Step | Driver at the keyboard | Reviewer/navigator | Concrete responsibility |
| --- | --- | --- | --- |
| Baseline review | Igor | User | Read the saved test/eval output; explain E04 and E09; reproduce if needed using separate filenames. |
| Plan review | User | Igor | Review spec, contract, file allowlist, risks and tasks. Only the user authorizes implementation. |
| Approved implementation | User, using Luna 6 in Codex | Igor | Supervise the scoped edit and inspect that it implements only M1. |
| Verification | Igor | User | Run/read tests, after eval and comparison; check every regression and immutable hashes. |
| Manual answer check | User | Igor | Inspect one changed question's CLI answer and citation against the source. |
| Shared report | Igor drafts evidence tables | User reviews conclusion | Include actual results, limitations and genuine external pair feedback. |
| Demonstration | User presents | Igor supports evidence/questions | Show failure, specification, diff, before/after, limitations and both contributions. |

Use one working directory and take turns. Do not create separate implementation branches,
copies, or simultaneous assistant runs. Each reviewer should be able to explain the other's
work. When a step is completed, record what each person actually did in the report.

The baseline run in this chat was executed by the assistant with permission. It is not
already Igor's or the user's completed manual measurement. Human review of that evidence
can be recorded once it occurs.

An external pair must still review the report; Igor's internal review does not substitute
for that requirement. Do not invent or send peer feedback on the pair's behalf.
The user's full submission name remains to be filled in by the user.
