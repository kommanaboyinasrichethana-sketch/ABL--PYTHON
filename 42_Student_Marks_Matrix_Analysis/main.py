marks = [
    [85, 78, 92],
    [67, 88, 74],
    [90, 91, 89]
]

student_totals = []

for i in range(len(marks)):
    total = sum(marks[i])
    average = total / len(marks[i])
    student_totals.append(total)
    print(f"Student {i + 1}: Total = {total}, Average = {average:.2f}")

for j in range(len(marks[0])):
    subject_total = 0
    for i in range(len(marks)):
        subject_total += marks[i][j]
    subject_average = subject_total / len(marks)
    print(f"Subject {j + 1} average: {subject_average:.2f}")

top_index = student_totals.index(max(student_totals))
print("Top student: Student", top_index + 1)
print("Highest total:", student_totals[top_index])
