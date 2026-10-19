# Implementation approval

**Package revision**: v1
**State**: APPROVED
**Approved by**: User
**Approval message**: "i approve v1"
**Approval date**: 2026-10-19 (Europe/Budapest)

The user approved the v1 specification, plan and tasks in this chat. Initial review hashes
were checked successfully for all 16 artifacts before task completion markers were changed.
All 22 original checkpoint files still match their baseline hashes. T001 and T002 are complete.
The user confirmed the diagnosis with "i agree with the diagnostic" on 2026-10-19.
Igor's part of T003 has not been explicitly confirmed, so T003 remains unchecked.
Source, configuration and test implementation has not begun.

## Session boundary requested by the user

On 2026-10-19 the user instructed: "do not do any implementation here" and requested a
prompt to start the next session using Luna 6. This chat is limited to recording decisions
and preparing that handoff. Do not implement or launch another session from this chat.
The v1 approval persists for the next user-started session; do not request it again.
The next session should establish Igor's actual T003 review before code edits, then follow
the approved task sequence. The new handoff is `luna-6-next-session.md`.

The planning documents retain their original drafting status as part of the reviewed package;
this approval record is the current authorization state. Task completion markers may advance
without changing the approved task text. The scope and file allowlist remain v1.

The proposal is M1: sentence-aware chunking. Review `spec.md`, `plan.md`, `tasks.md`,
and the linked chunking contract. The original file allowlist is two source files and
one new test file; measurement/report artifacts are listed separately in the plan.

The user previously approved copying the checkpoint into this workspace, collecting baseline
evidence, English instructions, and a provisional report outline. The user selected Luna 6
for future implementation and confirmed Igor led last week. Those earlier permissions were
separate from the explicit v1 approval recorded above.

Only an explicit user message approving the current plan authorizes code/config/test edits.
For clarity, the user may say: "I approve v1 of the M1 specification, plan and tasks."
Record the actual message and date here when received; do not invent or pre-fill them.
Igor's review assists the decision; the user remains the implementation approver.

`review-manifest.json` captures the reviewed artifacts' initial hashes. Check it before
the first code edit. Expected task checkbox changes after execution begins do not change
the approved approach. Other material changes require a revised package and fresh approval.

The root instructions and constitution enforce this as an assistant workflow rule, not an
operating-system access control. The bundled workflow also has a review gate before
implementation; assistants must never auto-approve it.
