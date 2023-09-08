from art import main_logo, versus
from data import data
from replit import clear
import random

#Initialize vowels
vowels = 'aeiou'

def get_random_instagram_account():
    return random.choice(data)

def check_answer(guess, a_followers, b_followers):
    """Take the user guess and follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account['name']
    account_description = account['description']
    account_country = account['country']
    if account_description[0].lower() in vowels:
        string = 'an'
    else:
        string = 'a'

    return f"{account_name}, {string} {account_description}, from {account_country}"

def play_game():
    print(main_logo)
    game_should_continue = True
    score = 0
    
    #Initialize two accounts from the game data
    account_b = get_random_instagram_account()
    
    while game_should_continue:
        
        # Make account at postion B become the next account at position A
        account_a = account_b
        account_b = get_random_instagram_account()
        
        # Prevent duplicates
        while account_a == account_b:
            account_b = get_random_instagram_account()
        
        print(f"Compare A: {format_data(account_a)}")
        print(versus)
        print(f"Compare B: {format_data(account_b)}")

        # Ask user for a guess:
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        
        # Check if user is correct. 
        # Get Follower Count of each account
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        # Clear the screen between rounds.
        clear()
        print(main_logo)

        # Use if statement to check if user is correct
        if is_correct:
            score += 1
            print(f"You're right! Current Score: {score}")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final Score: {score}")
            while input("Do you want to play another game of higher lower? ") == 'y':
                clear()
                play_game() 


if __name__ == "__main__":
    play_game()