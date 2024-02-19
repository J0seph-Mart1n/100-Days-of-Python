# ###This code will not work in repl.it as there is no access to the colorgram package here.###
# ##We talk about this in the video tutorials##
# import colorgram
#
# rgb_colors = []
# rgb_values = []
# #Extracts 30 colors from the image
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     rgb_colors.append(color.rgb)
# for color in rgb_colors:
#     r = color.r
#     g = color.g
#     b = color.b
#     rgb_values.append((r,g,b))
#
# print(rgb_colors)
# print(rgb_values)
import turtle
from turtle import Turtle, Screen
import random

final_colors = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
dot_turtle = Turtle()
screen = Screen()
turtle.colormode(255)

dot_turtle.hideturtle()
def damien_hirst():
    y = -225
    dot_turtle.speed(0)
    for _ in range(10):
        dot_turtle.penup()
        dot_turtle.goto(-230,y)
        dot_turtle.pendown()
        for _ in range(10):
            dot_turtle.dot(20,random.choice(final_colors))
            dot_turtle.penup()
            dot_turtle.forward(50)
            dot_turtle.pendown()
        dot_turtle.penup()
        y+=50

damien_hirst()
screen.exitonclick()