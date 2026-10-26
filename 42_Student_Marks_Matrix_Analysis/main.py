
marks = [
    [85, 78, 92],
    [67, 88, 74],
    [90, 91, 89]
]
student_totals = []

for i in range(3):
    total = marks[i][0] + marks[i][1] + marks[i][2]
    average = total / 3

    student_totals.append(total)

    print(f"Student {i + 1}: Total = {total}, Average = {average:.2f}")

for j in range(3):
    subject_total = 0

    for i in range(3):
        subject_total = subject_total + marks[i][j]

    subject_average = subject_total / 3
    print(f"Subject {j + 1} average: {subject_average:.2f}")

top_index=0

for i in range(3):
     if student_totals[i] > student_totals[top_index]:
         top_index = i

print("Top student:student",top_index +1)
print("Highest total:", student_totals[top_index])
