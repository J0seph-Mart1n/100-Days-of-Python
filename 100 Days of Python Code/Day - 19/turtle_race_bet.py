import random
from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=500,height=400)
guess_bet = screen.textinput(title='Guess your bet', prompt='Which turtle will win: Enter color')
colors = ['red','orange','yellow','green','blue','purple']
distance = [-100,-60,-20,20,60,100]
all_turtles = []

for i in range(0,6):
    race_turtle = Turtle(shape='turtle')
    race_turtle.color(colors[i])
    race_turtle.penup()
    race_turtle.goto(-230, distance[i])
    all_turtles.append(race_turtle)

game_on = False
if guess_bet in colors:
    game_on = True

while game_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            game_on = False
            winning_color = turtle.pencolor()
            if guess_bet == winning_color:
                print(f"You won!!. The {winning_color} turtle is the winner")
            else:
                print(f"You lost. The {winning_color} turtle is the winner")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()