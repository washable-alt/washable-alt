import random

# Generate a random word and use a word list

words_list = ["ardvark", "baboon", "camel"]

word = random.choice(words_list)

#Testing code

print(f"Pssst, the solution is {word}. ")


display = []
for letter in word:
    display.append('_')
#print(display)


#Todo-1 - Use a while loop to let the user guess again. The loop should only stop once the user 
#guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can 
#tell the user they've won.
end_of_game = False

while not end_of_game:
    user_input = input("Guess a letter: ")
    user_input = user_input.lower()

    for i in range(len(word)):
        if word[i] == user_input:
            display[i] = user_input
    print(display)

    if "_" not in display:
        end_of_game = True
        print("You Win. ")