Day 26
# List Comprehension 

e.g. 
list = [item for item in first_list]
equivalent to 
list = []

for item in first_list:
    list.append(item)


# Conditional List Comprehension

Shorten the for loop in a list into a line

e.g. list = [item for item in first list if condition]
equivalent to 
list = []
for item in first list:
    if condition == True:
        list.append(item)


# Dictionary Comprehension

e.g. student scores = {new_key:new_value for student in names}

equivalent to 

student_scores = {}
names = {"Alex": 1, "Beth": 2, "Caroline": 3, "Dave": 4,"Elanor": 5,"Freddie": 6}

for student, value, in names.items():
    student_scores[student] = random.randint(1,100)
print(student_scores)

for key, value in dict.items():
    second_dict[key] = function

# Conditional List Comprehension

e.g. passed_students = {new_key:new_value for key,value in dict.items() if condition}
equivalent to 
    passed_students = {}
    for student, score in student_scores.items():
        if score>=60:
            passed_students[student] = score

# Nato Alphabet Project

Create a list of the phonetic code words from a word that the user inputs

i.e. Hello -> Hotel Echo Lima Lima Oscar