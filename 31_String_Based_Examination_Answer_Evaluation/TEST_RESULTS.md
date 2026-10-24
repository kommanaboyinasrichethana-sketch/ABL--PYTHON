# Executed Test Results — Case Study 31

The program logic was executed with Python using six input sets. All six completed with exit code 0 and produced the expected results below.

| Test | Input answers | Expected score | Observed score | Status |
|---|---|---:|---:|---|
| TC-01 All correct | A, C, B, D, A | 10.0 | 10.0 | PASS |
| TC-02 Mixed answers | A, B, X, D, C | 3.0 | 3.0 | PASS |
| TC-03 All unanswered | X, X, X, X, X | 0.0 | 0.0 | PASS |
| TC-04 All incorrect | B, A, D, C, B | -2.5 | -2.5 | PASS |
| TC-05 Lowercase answers | a, c, b, d, a | 10.0 | 10.0 | PASS |
| TC-06 Invalid input followed by valid answers | ?, A, C, B, D, A | 10.0 | 10.0 | PASS |

## Evidence

See [test_output_evidence.svg](./test_output_evidence.svg) for a readable image of the observed result lines.

**Browser-run note:** TinyFish opened the online Python editor and captured the page, but it could not enter code into the editor because it uses a custom Ace editor. Therefore, the PASS results above are from local Python execution, not from a successful TinyFish browser run. No browser-run screenshot is claimed as proof of execution.
