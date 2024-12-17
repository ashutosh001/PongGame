from turtle import Turtle
FONT =  ("Courier", 24, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.up()
        self.divide()

    def divide(self):
        """Draws a line in the middle of the playground diving the screen"""
        self.goto(0,300)
        self.setheading(270)
        for x in range(20):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(10)

    def writescore(self,player_left,player_right):
        """Writes the score of the players in their side"""
        self.clear()
        self.divide()
        self.goto(-40,250)
        self.write(f"{player_left.score}",font=FONT)
        self.goto(25,250)
        self.write(f"{player_right.score}",font=FONT)
        
            
            