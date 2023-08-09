import random
from Day7_hangman_wordlist import wordlist
from Day7_hangman_art import logo, stages

# ToDo-1: Update the wordlist to use the 'wordlist from Day7_hangman_wordlist.py
word = random.choice(wordlist)

end_of_game = False
lives = 6

print(logo)

print(f"Pssst, the solution is {word}. ")

display = []
for letter in word:
    display.append('_')
#print(display)

while not end_of_game:
    user_input = input("Guess a letter: ")
    user_input = user_input.lower()
    #Creating a while loop to check if the user input is equal to 1
    while len(user_input) != 1:
        user_input = input("Guess a letter: ").lower()

    #check guessed letter
    for i in range(len(word)):
        if word[i] == user_input:
            display[i] = user_input
    print(display)


    if user_input not in word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    if "_" not in display:
        end_of_game = True
        print("You win. ")

    print(stages[lives])