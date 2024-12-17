from turtle import Turtle
FONT =  ("Courier", 24, "normal")
ALIGN = "center"
class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.up()

    def writescore(self,player_left,player_right):
        """Writes the score of the players in their side"""
        self.clear()
        self.goto(-100,200)
        self.write(f"{player_left.score}",font=FONT,align=ALIGN)
        self.goto(100,200)
        self.write(f"{player_right.score}",font=FONT,align=ALIGN)
        
            
            