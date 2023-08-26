# For loop
# List Comprehension

import random

numbers = [1,2,3]

new_numbers = [n + 1 for n in numbers]

name = "Angela"

letters_list = [letter for letter in name]

range_list = [num*2 for num in range(1,5)]

names = ["Alex", "Beth", "Caroline", "Dave","Elanor","Freddie"]

short_names = [name for name in names if len(name) < 5]

long_names = [name.upper() for name in names if len(name) > 5]



# Dict Comprehension

student_scores = {}
student_scores = {student:random.randint(1,100) for student in names}

print(student_scores)

#names = {"Alex": '1', "Beth": '2', "Caroline": '3', "Dave": '4',"Elanor": '5',"Freddie": '6' }
#for student, value in names.items():
#    student_scores[student] = random.randint(1,100)
#print(student_scores)

# Conditional Dictionary Comprehension

#passed_students = {student:score for student, score in student_scores.items() if score >= 60}
#print(passed_students)

passed_students = {}
for student, score in student_scores.items():
    if score>=60:
        passed_students[student] = score

print(passed_students)