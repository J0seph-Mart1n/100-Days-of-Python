import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, 'Up')
screen.onkey(player.down, 'Down')
screen.onkey(player.player_left, 'Left')
screen.onkey(player.player_right, 'Right')

count = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # When turtle reaches at top
    if player.ycor() == 280:
        player.reset()
        car_manager.level_up()
        scoreboard.add_score()

    # Check if turtle hits the car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    # Generates a new car every 6th iteration of while loop
    if count == 6:
        car_manager.create_car()
        count = 0

    # Moves the car
    car_manager.move_car()
    count += 1

screen.exitonclick()