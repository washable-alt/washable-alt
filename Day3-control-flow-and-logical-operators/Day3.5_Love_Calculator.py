print("Welcome to the Love Calculator!")
user_name=input("What is your name? ")
lover_name=input("What is his/her name? ")


first_word = 'TRUE'
second_word = 'LOVE'

combined_string = user_name + lover_name

love_scores_1 = 0
love_scores_2 = 0

for letter in combined_string:
    letter = letter.upper()
    for match in first_word:
        if letter == match:
            love_scores_1 += 1
    for match in second_word:
        if letter == match:
            love_scores_2 += 1
            
final_love_score= int(str(love_scores_1) + str(love_scores_2))

if (final_love_score < 10) or (final_love_score > 90):
    print(f"Your score is {final_love_score}, you go together like coke and mentos. ")

elif (final_love_score) >= 40 and (final_love_score) <= 50:
    print(f"Your score is {final_love_score}, you are alright together. ")
else:
    print(f"Your score is {final_love_score}. ")