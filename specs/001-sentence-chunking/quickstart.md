# Validation guide

Run PowerShell from `C:\Users\AleksA\Documents\ChatGPT\week-7`.
Use the existing `.venv\Scripts\python.exe` (Python 3.12.14, pytest 8.3.3).
The environment is already installed. No runtime network or API key is needed.

## Baseline already captured

These were the actual baseline commands. Do not rerun them over the preserved files:

```powershell
& '.\.venv\Scripts\python.exe' -m pytest
& '.\.venv\Scripts\python.exe' -m src.eval_runner --out results/before.json
```

Saved output: `results/tests-before.txt`, `results/before-table.txt`.
Result: 18 tests pass; 6/12 eval questions pass. Full values are in `results/before.json`.

## Before any implementation

Read `approval.md`. Without explicit user approval of v1, stop. A checked requirements
checklist or Spec Kit skill invocation is not approval. Check the reviewed artifact hashes:

```powershell
$taskReview = Get-Content -Raw -LiteralPath 'specs/001-sentence-chunking/review-manifest.json' | ConvertFrom-Json
foreach ($taskEntry in $taskReview.files.PSObject.Properties) {
    $taskHash = (Get-FileHash -Algorithm SHA256 -LiteralPath $taskEntry.Name).Hash.ToLowerInvariant()
    if ($taskHash -ne $taskEntry.Value) { throw "Review artifact changed: $($taskEntry.Name)" }
}
```

## After the approved change

Run these sequentially; check each native command's exit code. Preserve outputs on failure.

```powershell
& '.\.venv\Scripts\python.exe' -m pytest 2>&1 | Tee-Object -FilePath results/tests-after.txt
if ($LASTEXITCODE -ne 0) { throw 'Tests failed; stop and diagnose within the approved scope.' }
& '.\.venv\Scripts\python.exe' -m src.eval_runner --out results/after.json 2>&1 | Tee-Object -FilePath results/after-table.txt
if ($LASTEXITCODE -ne 0) { throw 'After evaluation failed.' }
& '.\.venv\Scripts\python.exe' -m src.eval_compare results/before.json results/after.json 2>&1 | Tee-Object -FilePath results/comparison.txt
if ($LASTEXITCODE -ne 0) { throw 'Comparison failed; do not modify the evaluator.' }
```

The eval command differs from baseline only in its output filename. Expected mechanical
result: all tests pass. Expected settings delta: only `CHUNK_STRATEGY`. An eval improvement
is not guaranteed. Explain every regression; ask before any proposed second adjustment.

## Human CLI check

Choose an ID reported as changed by the comparison, copy its exact question from the fixed
eval set, and run `src.cli --question '<exact question>' --show-retrieved`. Save output as
`results/<ID>-after-cli.txt`. Verify answer, cited text, title, version, and status with Igor.
If E04 changes, its command is:

```powershell
& '.\.venv\Scripts\python.exe' -m src.cli --question 'How many business days does a laptop replacement take?' --show-retrieved 2>&1 | Tee-Object -FilePath results/E04-after-cli.txt
```

If none changes, explicitly record that outcome and inspect E04. Record who actually
performed the human check; an assistant's CLI run alone is not a human sign-off.

## Preserve the behavior diff and immutable files

There is currently no Git commit in this workspace. `git diff` alone will not show
untracked source files. Compare against the untouched Desktop checkpoint instead:

```powershell
$taskOriginal = 'C:/Users/AleksA/Desktop/rag-week-7-weak-checkpoint/rag-week-7-weak-checkpoint'
git diff --no-index --no-ext-diff --no-color --output=results/change-src.diff -- "$taskOriginal/src" src
if ($LASTEXITCODE -gt 1) { throw 'Source diff failed.' }
git diff --no-index --no-ext-diff --no-color --output=results/change-tests.diff -- "$taskOriginal/tests" tests
if ($LASTEXITCODE -gt 1) { throw 'Test diff failed.' }
```

Exit code 1 means differences were found. Review these two diffs separately from Spec Kit
setup. Expected behavior edits: `src/chunking.py`, `src/config.py`; one new test file.
Use `docs/checkpoint-manifest.json` to check hashes of all protected original files,
especially eval/metrics, corpus, retrieval, answering, requirements, and existing tests.

`results/*.json` is ignored by the original `.gitignore`. Include both JSON files explicitly
in the eventual submission attachment; if the user later requests a commit, they need
explicit inclusion. Do not change ignore rules or commit as part of implementation.
