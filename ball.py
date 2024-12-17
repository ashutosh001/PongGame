from turtle import Turtle

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.up()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

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
        self.move_speed *= 0.9

    def reset_position(self):
        """Resets the position of the ball after it goes out of bounds"""
        self.goto(0,0)
        self.bounce_paddle()
        self.move_speed = 0.1
