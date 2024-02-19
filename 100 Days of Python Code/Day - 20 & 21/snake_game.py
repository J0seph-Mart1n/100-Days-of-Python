from turtle import Screen
from food import Food
from scoreboard import ScoreBoard
import time
from snake import Snake

screen = Screen()
food = Food()
scoreboard = ScoreBoard()

screen.setup(width=600, height=600)
screen.bgcolor("green")
screen.title("Snake Game")
level = screen.textinput(title='Snake Game', prompt='Enter Level (1,2,3)')
levels = {"1":0.2, "2":0.1, "3":0.05}
screen.tracer(0)
snake = Snake()
game_is_on = True

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')


score = 0
with open('high_score.txt') as file:
    high_score = file.read()

scoreboard.score(score,high_score)
while game_is_on:
    screen.update()
    time.sleep(levels[level])
    snake.move()

    # Detecting tail collision
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            #game_is_on = False
            if score > int(high_score):
                high_score = score
            score = 0
            with open('high_score.txt', mode='w') as file:
                 file.write(str(high_score))

            scoreboard.score(score,high_score)
            snake.reset()
    else:
        pass

    # Detecting collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        #game_is_on = False
        if score > int(high_score):
            high_score = score
        score = 0
        with open('high_score.txt', mode='w') as file:
            file.write(str(high_score))
        snake.reset()
        scoreboard.score(score,high_score)


    #Detecting collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score+=1
        snake.extend()
        scoreboard.score(score,high_score)

screen.exitonclick()
