student_scores = {
    "Harry": 81,
    "Roy": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

#Todo-1: Create an empty dictionary called student_grades
student_grades = {}

#Todo-2 : Write code below to add the grades 
for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80 and score <= 90:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70 and score <= 80:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

#Don't change the code below
print(student_grades)