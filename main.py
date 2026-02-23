print("Welcome to the Grade Tracker!")
user_name = input("What is your name? ")
print()
grade_bracket = []

quiz_number = 0

while quiz_number < 5:
    quiz_score = int(input("Enter quiz score: "))
    if quiz_score < 0 or quiz_score > 100:
        print("Invalid score. Please enter a score between 0 and 100.")
        continue
    quiz_number += 1
    grade_bracket.append(quiz_score)

print(f"""
------------------------------
📊 Grade Report for {user_name}
------------------------------""")
print(f"Your quiz scores are: {grade_bracket}")
print(f"Highest score: {max(grade_bracket)}")
print(f"Lowest score: {min(grade_bracket)}")
print(f"Your average quiz score is: {sum(grade_bracket) / len(grade_bracket)}")