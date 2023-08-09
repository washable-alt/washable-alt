import random

# Generate a random word and use a word list

words_list = ["ardvark", "baboon", "camel"]

word = random.choice(words_list)

#user input - guess the number of letters, string data type
while True:
    user_input = input("Please guess a letter in the word: ")

    if len(user_input) == 1:
        print(f"Your single letter input was: {user_input}")
        break
    print("Please enter a single letter to continue")


user_input = user_input.lower()

for letter in word:
    if letter == user_input:
        print("Right")
    else:
        print("Wrong")