from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,x_axis,y_axis):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.up()
        self.shapesize(stretch_len=1,stretch_wid=5)
        self.goto(x=x_axis,y=y_axis)

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
        ball_x = ball.xcor()
        ball_y = ball.ycor()

        paddle_left = self.xcor() -10
        paddle_right = self.xcor() + 10
        paddle_top = self.ycor() + 50
        paddle_bottom = self.ycor() - 50

        if ball_x > 340 or ball_x < -340:
            if (paddle_left <= ball_x <= paddle_right) or (paddle_bottom <= ball_y <= paddle_top):
                return True
        return False
    