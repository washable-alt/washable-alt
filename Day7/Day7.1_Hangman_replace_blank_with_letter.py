import random

# Generate a random word and use a word list

words_list = ["ardvark", "baboon", "camel"]

word = random.choice(words_list)

#Testing code

print(f"Pssst, the solution is {word}. ")

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

#Todo1: Create an empty list called display
#For each letter in the chosen_word, add a "_" to 'display'

# My attempt
display = []
for letter in word:
    display.append('_')
#print(display)


#Angela Yu's course attempt, _ means that we do not care about the iterator value, only it should run some specific number of times
#display = []
#for _ in range(len(word)):
#    display += '_'
#print(display)

#Todo-2: Loop through each position in the word:
# my attempt
for i in range(len(word)):
    if word[i] == user_input:
        display[i] = user_input
print(display)

# Angela's yu course attempt

#for position in range(len(word)):
#   letter = word[position]
#   if letter == user_input:
#       display[position] = letter
#print(display)