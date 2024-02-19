import turtle
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
turtle.tracer(False)
screen.setup(width=800, height=500)
screen.title("Pong Game")
screen.bgcolor("black")

l_paddle = Paddle((-350,0))
r_paddle = Paddle((350,0))
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(l_paddle.up,"w")
screen.onkey(l_paddle.down,"s")
screen.onkey(r_paddle.up,"Up")
screen.onkey(r_paddle.down,"Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.increase_speed)
    ball.move_ball()
    screen.update()

    #Detect collision with wall
    if ball.ycor() > 230 or ball.ycor() < -230:
        ball.bounce_y()


    #Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Reset the ball if the right player misses the ball
    if ball.xcor() > 380:
        ball.goto(0, 0)
        ball.bounce_x()
        ball.increase_speed = 0.1
        scoreboard.add_l_score()


    #Reset the ball if the left player misses the ball
    if ball.xcor() < -380:
        ball.goto(0,0)
        ball.bounce_x()
        ball.increase_speed = 0.1
        scoreboard.add_r_score()


screen.exitonclick()