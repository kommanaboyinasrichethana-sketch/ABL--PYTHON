# Case Study 42: Student Marks Matrix Analysis

## Problem statement
to analyze the marks of three students in three subjects. This program is calculateing the total marks and average marks of each student, calculate the average marks obtained in each subject, and identify the student who scored the highest total marks. Display all the results clearly using appropriate loops, lists, and conditional statements.

## Objectives
1.To calculate the total marks and average marks obtained by each student in three subjects.

2.To calculate the average marks obtained by all three students in each subject.

3.To identify the student who scored the highest total marks.

4.To understand the use of lists, nested lists, for loops, conditional statements, and the append() method in Python.


5.To display the results clearly using formatted output.

## Assumptions
1. The program considers marks of three students in three subjects.
2. The marks of each student are already given in the program.
3. All marks are valid numerical values between 0 and 100.
4. Each subject carries equal importance while calculating the average marks.
5. The total marks are calculated by adding the marks obtained in all three subjects.
6. The average marks are calculated by dividing the total marks by 3.
7. The student with the highest total marks is considered the top student.
8. If two or more students have the same highest total, the program displays the student who appears first in the list.

## Algorithm
1. Start the program.

2. Store the marks of three students in three subjects in a list.

3. Create an empty list to store the total marks of each student.

4. Calculate the total marks and average marks of each student.

5.Store each student's total marks in the list and display the total and average.

6. Calculate the average marks of each subject and display the results.

7. Assume the first student is the top student.

8. Compare the total marks of all students to find the highest total.

9. Display the top student's number and highest total marks.

10. Stop the program.

## Flowchat

<img width="1024" height="1536" alt="image" src="https://github.com/user-attachments/assets/cd5d9e1d-cade-4565-aa9a-64ae32065383" />


## Pseudocode
BEGIN

    Store marks of 3 students in 3 subjects
    Create an empty list student_totals

    FOR i = 0 TO 2
        total = marks[i][0] + marks[i][1] + marks[i][2]
        average = total / 3

        Add total to student_totals

        DISPLAY student number, total, average
    END FOR

    FOR j = 0 TO 2
        subject_total = 0

        FOR i = 0 TO 2
            subject_total = subject_total + marks[i][j]
        END FOR

        subject_average = subject_total / 3
        DISPLAY subject number, subject_average
    END FOR

    top_index = 0

    FOR i = 0 TO 2
        IF student_totals[i] > student_totals[top_index] THEN
            top_index = i
        END IF
    END FOR

    DISPLAY top student number (top_index + 1)
    DISPLAY highest total (student_totals[top_index])

END

## Test cases
| Test input / condition | Expected result |
|---|---|
| Included matrix | Totals: 255, 229, 270; top student is Student 3 |
| A student's marks are 100, 100, 100 | Total 300; average 100.00 |
| A student's marks are 0, 0, 0 | Total 0; average 0.00 |

## Output screenshot
Run `main.py`; capture the displayed student and subject summaries.
<img width="1105" height="305" alt="image" src="https://github.com/user-attachments/assets/f3a4e4ec-6ebb-4142-b7ae-82bf125e02fe" />

<img width="1105" height="312" alt="image" src="https://github.com/user-attachments/assets/8551076f-ceaf-4d00-b8f6-8d78bb30618b" />

<img width="1106" height="302" alt="image" src="https://github.com/user-attachments/assets/55c0727c-00a1-40e1-8ac5-49e27f82b095" />





## Conclusion
This program practises nested lists, nested loops, arithmetic, and finding maximum values.
