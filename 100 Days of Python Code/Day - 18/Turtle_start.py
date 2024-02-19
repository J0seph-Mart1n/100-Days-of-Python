import turtle
from turtle import Turtle, Screen
import random

tiny_turtle = Turtle()
tiny_turtle.shape('turtle')

i = 100
def square():
    for _ in range(4):
        tiny_turtle.forward(i)
        tiny_turtle.right(90)

def dashed_line():
    for _ in range(10):
        tiny_turtle.forward(10)
        tiny_turtle.penup()
        tiny_turtle.forward(10)
        tiny_turtle.pendown()

def triangle():
    for _ in range(3):
        tiny_turtle.forward(i)
        tiny_turtle.right(120)

def pentagon():
    for _ in range(5):
        tiny_turtle.forward(i)
        tiny_turtle.right(72)

def hexagon():
    for _ in range(6):
        tiny_turtle.forward(i)
        tiny_turtle.right(60)

def heptagon():
    for _ in range(7):
        tiny_turtle.forward(i)
        tiny_turtle.right(51.43)

def octagon():
    for _ in range(8):
        tiny_turtle.forward(i)
        tiny_turtle.right(45)

def nonagon():
    for _ in range(9):
        tiny_turtle.forward(i)
        tiny_turtle.right(40)

def decagon():
    for _ in range(10):
        tiny_turtle.forward(i)
        tiny_turtle.right(36)

turtle.colormode(255)
def random_walk():
    tiny_turtle.forward(20)
    path = random.choice([tiny_turtle.right, tiny_turtle.left])
    path(random.choice([0,90,180,270]))
    color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    tiny_turtle.color(color)

# tiny_turtle.pensize(5)
tiny_turtle.speed(0)
# for _ in range(200):
#     random_walk()

def random_color():
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    tiny_turtle.color(color)

def spirograph(gap_in_circle):
    for _ in range(int(360/gap_in_circle)):
        random_color()
        tiny_turtle.circle(100)
        tiny_turtle.setheading(tiny_turtle.heading()+5)

spirograph(5)
screen = Screen()
screen.exitonclick()