from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        super().__init__()
        self.all_cars = []

    def create_car(self):
        car = Turtle('square')
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.color(random.choice(COLORS))
        random_y = random.randint(-250, 250)
        car.penup()
        car.goto(300, random_y)
        self.all_cars.append(car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def level_up(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT