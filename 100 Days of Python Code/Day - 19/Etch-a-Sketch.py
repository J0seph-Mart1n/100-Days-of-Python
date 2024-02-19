from turtle import Turtle, Screen

draw_turtle = Turtle()
screen = Screen()

def forward():
    draw_turtle.forward(10)

def left():
    draw_turtle.left(10)

def right():
    draw_turtle.right(10)

def backward():
    draw_turtle.back(10)

def clear():
    draw_turtle.reset()

screen.listen()
screen.onkey(key='w', fun=forward)
screen.onkey(key='a', fun=left)
screen.onkey(key='s', fun=backward)
screen.onkey(key='d', fun=right)
screen.onkey(key='c', fun=clear)

screen.exitonclick()