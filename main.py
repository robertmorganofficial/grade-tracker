print("Welcome to the Grade Tracker!")
user_name = input("What is your name? ")
grade_bracket = []

quiz_number = 0

while quiz_number < 5:
    quiz_score = int(input("Enter quiz score: "))
    quiz_number += 1
    grade_bracket.append(quiz_score)

print(f"Quiz bracket is: {grade_bracket}")