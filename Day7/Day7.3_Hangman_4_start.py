import random

stages= ['''
         
  +---+
  |   |
  0   |
/ | \ | 
 / \  |
      |
========
''', '''
         
  +---+
  |   |
  0   |
/ | \ | 
 /    |
      |
========
''', '''
         
  +---+
  |   |
  0   |
/ | \ | 
      |
      |
========
''', '''
         
  +---+
  |   |
  0   |
/ |   | 
      |
      |
========
''', '''
         
  +---+
  |   |
  0   |
  |   | 
      |
      |
========
''', '''
         
  +---+
  |   |
  0   |
      | 
      |
      |
========
''', '''
         
  +---+
  |   |
      |
      | 
      |
      |
========
''']

end_of_game = False

word_list = ['ardvark', 'baboon', 'camel']

word = random.choice(word_list)

#Testing code

print(f"Pssst, the solution is {word}. ")

#Todo-1: Create a variable called 'lives' to keep track of the number of lives left
#Set 'lives' to equal 6. 

lives = 6
display = []
for letter in word:
    display.append('_')
#print(display)

while not end_of_game:
    user_input = input("Guess a letter: ")
    user_input = user_input.lower()

    #check guessed letter
    for i in range(len(word)):
        if word[i] == user_input:
            display[i] = user_input
    print(display)

#Todo-2: If guess is not a letter in word, reduce lives by 1.
#If lives goes down to 0, then the game should stop and print "You lose"

    if user_input not in word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    if "_" not in display:
        end_of_game = True
        print("You Win. ")

    print(stages[lives])