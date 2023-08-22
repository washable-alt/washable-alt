from turtle import Screen
from ball import Ball
from paddle import Paddle
import time
from scoreboard import Scoreboard

## Creating a Pong Game

## Create the screen
screen = Screen()

screen.bgcolor("black")

screen.setup(width=800, height=600)

screen.tracer(0)

ball = Ball()

scoreboard = Scoreboard()


## Create and move a paddle
# A paddle object that takes in a tuple
r_paddle = Paddle((350, 0))

## Create another paddle
l_paddle = Paddle((-350, 0))

# Creates a listener for events
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True

while game_is_on:
    # Pause for 0.1 seconds
    time.sleep(0.1)
    # Update the screen because the tracer will not refresh the screen unless screen is updated.
    screen.update()
    ball.move()
    
## Create the ball and make it move

## Detect collision with wall and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
## Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()        
## Detect when paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    elif ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()