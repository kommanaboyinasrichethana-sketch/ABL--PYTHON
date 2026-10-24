# Case Study 31: String-Based Examination Answer Evaluation
# Correct answer: +2 marks; incorrect answer: -0.5 marks; unanswered: 0 marks.

answer_key = ["A", "C", "B", "D", "A"]
valid_answers = ["A", "B", "C", "D", "X"]

correct = 0
incorrect = 0
unanswered = 0

for i in range(len(answer_key)):
    answer = input(
        "Enter answer for question "
        + str(i + 1)
        + " (A/B/C/D, or X if blank): "
    ).strip().upper()

    while answer not in valid_answers:
        print("Invalid answer. Enter A, B, C, D, or X.")
        answer = input("Enter your answer again: ").strip().upper()

    if answer == "X":
        unanswered = unanswered + 1
    elif answer == answer_key[i]:
        correct = correct + 1
    else:
        incorrect = incorrect + 1

score = correct * 2 - incorrect * 0.5

print("\n----- Examination Result -----")
print("Correct answers:", correct)
print("Incorrect answers:", incorrect)
print("Unanswered questions:", unanswered)
print("Final score:", score, "out of", len(answer_key) * 2)
