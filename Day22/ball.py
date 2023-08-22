from turtle import Turtle

class Ball(Turtle):
    
    def __init__(self):
        """Inherits from Turtle class"""
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 3
        self.y_move = 3
        self.move_speed = 1.5

    def move(self):
        """Increase by 10 pixels in the x and y coordinates"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """To start moving in the opposite direction in the y direction, after the ball bounces off a surface"""
        self.y_move *= -1

    def bounce_x(self):
        """When in contact with paddle or wall, move the ball in the negative/opposite x direction"""
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()

