from art import logo
from replit import clear
from random import randint


EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

def check_answer(guess, answer, turns):
    """Checks answer against guess. Returns the number of turns remaining. """
    
    if guess > answer:
        print("Too High.")
        return turns - 1
    elif guess < answer:
        print("Too Low.")
        return turns - 1
    else: 
        print(f"You got it! The answer was {answer}.")

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS



def play_game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
     
    print(f"Pssst, the correct answer is {answer}")

    turns = set_difficulty()
    

    # let the user guess the number.
    guess = 0 
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number")

        guess = int(input("Make a guess: "))

    # Track the number of turns and reduce by 1 if they get it wrong. 
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return 
        elif guess != answer:
            print("Guess again.")
            

    while input("Do you want to play another game of number guessing?") == 'y':
        clear()
        play_game()



if __name__=="__main__":
    play_game()

