########################################################
#            # Snake game                              #                 
#            # 3 steps - Part 1                        # 
#                                                      #
#            # Create the Snake body part              #
#                                                      #
#            # Move the Snake                          #
#                                                      #
#            # Control the snake                       #
#                                                      #
#            # Part 2                                  #
#            # Detect Collision with food              #
#                                                      #
#            # Create a scoreboard                     #
#                                                      #
#            # Detect collision with wall              # 
#                                                      #
#            # Detect collision with tail              #
########################################################

from turtle import Turtle, Screen
import random
import time
from snake import Snake

screen = Screen()

screen.setup(width=1000, height=1000)

screen.bgcolor("black")

screen.title("My Snake Game")

#Screen is not updated until the entire turtle movement is complete
screen.tracer(0)

snake = Snake()


game_is_on = True

while game_is_on:
    # Update the screen
    screen.update()

    #pauses the program for 0.1 seconds
    time.sleep(0.1)
    
    snake.move()

screen.exitonclick()