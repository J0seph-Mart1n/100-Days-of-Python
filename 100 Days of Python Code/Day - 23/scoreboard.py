from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.goto(-230, 250)
        self.write(f"Level: {self.score}", align='center', font=("Courier", 20, "normal"))

    def add_score(self):
        self.score += 1
        self.clear()
        self.goto(-230, 250)
        self.write(f"Level: {self.score}", align='center', font=("Courier", 20, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align='center', font=("Courier", 20, "normal"))