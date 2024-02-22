import turtle
import pandas as pd

screen = turtle.Screen()
image = "blank_states_img.gif"
screen.setup(width=800, height=600)
screen.addshape(image)
screen.title('U.S State Game')
turtle.shape(image)
state_name = turtle.Turtle('turtle')
state_name.hideturtle()


us_states = pd.read_csv('50_states.csv')
states = us_states.state.to_list()
score = 0
total_score = 50
guessed_state = []

while score<=total_score:
    answer_state = screen.textinput(title=f'{score}/{total_score} Score', prompt='Enter the state').title().strip()
    if answer_state == "Exit":
        break
    if answer_state in states:
        if answer_state not in guessed_state:
            state_name.penup()
            state_data = us_states[us_states.state == answer_state]
            state_name.goto(int(state_data.x),int(state_data.y))
            state_name.write(f'{answer_state}',True,align='center',font=('Arial',10,'normal'))
            guessed_state.append(answer_state)
            score+=1

#learn.csv

missing_states = [state for state in states if state not in guessed_state]
df = pd.DataFrame(missing_states)
df.to_csv('learn.csv')
