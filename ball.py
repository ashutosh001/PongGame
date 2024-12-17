from turtle import Turtle

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.up()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        """Moves the ball in a zig zag way"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def bounce_wall(self):
        """Changes the direction of the ball if it collides the top or the bottom wall"""
        self.y_move *= -1

    def bounce_paddle(self):
        """Changes the direction of the ball if it collides the either of the two paddle"""
        self.x_move *= -1
