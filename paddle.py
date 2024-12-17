from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,x_axis,y_axis):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.up()
        self.shapesize(stretch_len=1,stretch_wid=5)
        self.goto(x=x_axis,y=y_axis)
        self.score = 0

    def move_up(self):
        """Move the paddle up based on user input"""
        new_y = self.ycor() + 50
        if self.ycor() < 250:
            self.goto(self.xcor(),new_y)

    def move_down(self):
        """Move the paddle down based on user input"""
        new_y = self.ycor() - 50
        if self.ycor() > -250:
            self.goto(self.xcor(),new_y)

    def detect_collision(self,ball):
        """Detects if the ball is hit by the paddle"""
        if (ball.xcor() > 325 or ball.xcor() < -325) and self.distance(ball) < 50:
            return True
        return False
    