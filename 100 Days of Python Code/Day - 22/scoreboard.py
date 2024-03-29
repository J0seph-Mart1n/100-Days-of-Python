from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(-100, 150)
        self.write(self.l_score, align='center', font=("Courier", 70, "normal"))
        self.goto(100,150)
        self.write(self.r_score, align='center', font=("Courier", 70, "normal"))

    def add_l_score(self):
        self.l_score+=1
        self.clear()
        self.goto(-100, 150)
        self.write(self.l_score, align='center', font=("Courier", 70, "normal"))
        self.goto(100, 150)
        self.write(self.r_score, align='center', font=("Courier", 70, "normal"))

    def add_r_score(self):
        self.r_score+=1
        self.clear()
        self.goto(-100, 150)
        self.write(self.l_score, align='center', font=("Courier", 70, "normal"))
        self.goto(100, 150)
        self.write(self.r_score, align='center', font=("Courier", 70, "normal"))