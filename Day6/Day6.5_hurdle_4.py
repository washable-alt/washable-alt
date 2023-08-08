from Day6 import turn_left, move, RUR

#look at Reeborg's keyboard
#Hurdle 4 world

def wall_on_right():  #py:wall_on_right
    """
    Indicates if an wall is on the immediate right of Reeborg.

    Returns:
       True if a wall is on Reeborg's right, False otherwise.
    """
    return RUR._wall_on_right_()


def front_is_clear(self):  #py:UR.front_is_clear
        """
        Indicates if an obstacle (wall, fence, water, etc.) blocks the path.

        Returns:
           True if the path is clear (not blocked), False otherwise.
        """
        return RUR._UR.front_is_clear_(self.body)

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    # after turning left, check whether there is a wall
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

def wall_in_front(self):  #py:UR.wall_in_front
        """
        Indicates if a wall blocks the way.

        Returns:
           True if the path blocked by a wall, False otherwise.
        """
        return RUR._UR.wall_in_front_(self.body)

def at_goal():  #py:at_goal
    """
    Indicates if Reeborg has reached the desired location.

    Returns:
        True if Reeborg has reached its goal, False otherwise.
    """
    return RUR._at_goal_()

while not at_goal():
    if wall_in_front():
        jump()
    else: 
        move()
