from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def score(self, score_num,high_score_num):
        self.clear()
        self.goto(-10,260)
        self.write(f"Score: {score_num} Highscore: {high_score_num}", True, align="center", font=('Arial', 20, 'normal'))

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over", True, align="center", font=('Arial', 20, 'normal'))