from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

class PongGame:
    def __init__(self):
        pass

    def start_game(self):
        """Creates the playground for the pong game"""
        my_screen = Screen()
        my_screen.title("Pong")
        my_screen.bgcolor("Black")
        my_screen.setup(width=800,height=600)
        my_screen.tracer(0)

        my_screen.listen()
        player2 = Paddle(350,0)
        player1 = Paddle(-350,0)
        ball = Ball()
        scoreboard = ScoreBoard()
        scoreboard.writescore(player1,player2)
        game_is_on = True

        my_screen.onkey(key="i",fun=player2.move_up)
        my_screen.onkey(key="k",fun=player2.move_down)
        my_screen.onkey(key="w",fun=player1.move_up)
        my_screen.onkey(key="s",fun=player1.move_down)

        while game_is_on: 
            time.sleep(0.1)
            my_screen.update()

            ball.move()
            if ball.ycor() > 280 or ball.ycor() < -280:
                #Detect collision with the top or bottom wall
                ball.bounce_wall()

            if player1.detect_collision(ball) or player2.detect_collision(ball) :
                #Detect if ball is hit by the paddle
                ball.bounce_paddle()

            if ball.xcor() > 380:
                #Detect if R paddle misses the ball
                player1.score += 1
                ball.reset_position()
                scoreboard.writescore(player1,player2)

            if ball.xcor() < -380:
                #Detect if L paddle misses the ball
                player2.score += 1
                ball.reset_position()
                scoreboard.writescore(player1,player2)

        my_screen.exitonclick()

if __name__ == "__main__":
    play = PongGame()
    play.start_game()
