from Day6 import turn_left, move, RUR

#look at Reeborg's keyboard

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

def at_goal():  #py:at_goal
    """
    Indicates if Reeborg has reached the desired location.

    Returns:
        True if Reeborg has reached its goal, False otherwise.
    """
    return RUR._at_goal_()

number_of_hurdles = 6
while number_of_hurdles > 0: 
    jump()
    number_of_hurdles -= 1
    print(number_of_hurdles)

# while something_is_true:
# Do this
# Then do this
# Then do this

#while not at goal, perform the jump hurdle action

while not at_goal():
    jump()
