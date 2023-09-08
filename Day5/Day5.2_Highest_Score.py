# To write a program that calculates the highest score from a list of scores

student_scores = input("Input a list of student scores from a list of scores: ").split()

max = 0

for score in student_scores:
    score = int(score)
    if score > max:
      max = score
      
print(f"The highest score in the class is: {max} ")