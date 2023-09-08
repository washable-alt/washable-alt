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
from food import Food
from scoreboard import Scoreboard


screen = Screen()

screen.setup(width=600, height=600)

screen.bgcolor("black")

screen.title("My Snake Game")

#Screen is not updated until the entire turtle movement is complete
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    # Update the screen
    screen.update()

    #pauses the program for 0.1 seconds
    time.sleep(0.1)
    
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()             

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail

    # Slice from first last element to 2nd element
    # Works for lists and tuples
    # Equivalent to for segment in snake.segments[1:]

    for segment in snake.segments[:1:-1]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()