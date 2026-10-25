# Case Study 42: Student Marks Matrix Analysis

## Problem statement
Store marks for multiple students and subjects in a nested list. Calculate student totals and averages, subject averages, and the top student's total.

## Objectives
- Represent table data with nested lists.
- Calculate row-wise and column-wise statistics.
- Find the highest total using list operations.

## Assumptions
- The example contains 3 students and 3 subjects.
- Marks are integers from 0 to 100.
- If totals tie, the first student with the highest total is selected.

## Algorithm
1. Create a nested list of marks.
2. For each student row, calculate total and average.
3. For each subject column, calculate the average.
4. Find the highest student total.
5. Display all summaries.

## Flowchart
```mermaid
flowchart TD
 A([Start]) --> B[Create marks nested list]
 B --> C[Loop through students: total and average]
 C --> D[Loop through subjects: average]
 D --> E[Find maximum student total]
 E --> F[Display statistics]
 F --> G([Stop])
```

## Pseudocode
```text
BEGIN
marks = nested list of student marks
FOR each student row
    calculate total and average
    store total
FOR each subject column
    add marks for all students
    calculate and print subject average
find index of maximum total
print top student and highest total
END
```

## Test cases
| Test input / condition | Expected result |
|---|---|
| Included matrix | Totals: 255, 229, 270; top student is Student 3 |
| A student's marks are 100, 100, 100 | Total 300; average 100.00 |
| A student's marks are 0, 0, 0 | Total 0; average 0.00 |

## Output screenshot
Run `main.py`; capture the displayed student and subject summaries.

## Conclusion
This program practises nested lists, nested loops, arithmetic, and finding maximum values.
