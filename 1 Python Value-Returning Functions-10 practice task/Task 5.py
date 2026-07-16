#1
def average_score(score1, score2, score3):
    return (score1 + score2 + score3) / 3
average = average_score(80, 90, 100)
print("Average:", average)
#2
def average_five_scores(s1, s2, s3, s4, s5):
    return (s1 + s2 + s3 + s4 + s5) / 5
score1 = float(input("Enter score for Subject 1: "))
score2 = float(input("Enter score for Subject 2: "))
score3 = float(input("Enter score for Subject 3: "))
score4 = float(input("Enter score for Subject 4: "))
score5 = float(input("Enter score for Subject 5: "))
average = average_five_scores(score1, score2, score3, score4, score5)
print(f"Average = {average}")
#3
def get_letter_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"
average_value = 87
grade = get_letter_grade(average_value)
print(f"Average = {average_value}")
print(f"Grade = {grade}")