from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.car_speed = 0.1

    def up(self):
        self.setheading(90)
        self.forward(MOVE_DISTANCE)

    def down(self):
        self.setheading(270)
        self.forward(MOVE_DISTANCE)

    def player_left(self):
        self.setheading(180)
        self.forward(MOVE_DISTANCE)

    def player_right(self):
        self.setheading(0)
        self.forward(MOVE_DISTANCE)

    def reset(self):
        self.shape('turtle')
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def increase_speed(self):
        self.car_speed *= 0.7

