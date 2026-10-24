# Test Cases — Case Study 31: String-Based Examination Answer Evaluation

**Scoring rule:** Correct = +2 marks, incorrect = -0.5 marks, unanswered (X) = 0 marks.
**Answer key:** A, C, B, D, A

| Test | Answers entered (Q1–Q5) | Expected correct | Expected incorrect | Expected unanswered | Expected score |
|---|---|---:|---:|---:|---:|
| TC-01: All correct | A, C, B, D, A | 5 | 0 | 0 | 10.0 |
| TC-02: Mixed answers | A, B, X, D, C | 2 | 2 | 1 | 3.0 |
| TC-03: All unanswered | X, X, X, X, X | 0 | 0 | 5 | 0.0 |
| TC-04: All incorrect | B, A, D, C, B | 0 | 5 | 0 | -2.5 |
| TC-05: Lowercase input | a, c, b, d, a | 5 | 0 | 0 | 10.0 |
| TC-06: Invalid input then valid | ?, A, C, B, D, A | 5 | 0 | 0 | 10.0 |

## How to run
Run `python main.py`, enter the five answers in order, and compare the displayed counts and final score with the expected values above.

## Test evidence
Add screenshots of the actual program output after running the test cases. Do not label a test as passed until the observed output matches the expected result.
