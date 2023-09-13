student_heights = input("Input a list of student heights ").split()

# Do not use the len() and sum() function
#for n in range(0, len(student_heights)):
#    student_heights[n] = int(student_heights[n])
#print(student_heights)

total_height = 0
number_of_students = 0 

for height in student_heights:
    total_height += int(height)
    number_of_students += 1

average_height = round(total_height / number_of_students)

print(f"There are a total of {number_of_students} in student_heights. \n")
print(f"Average height rounded to the nearest whole number = {average_height}")
