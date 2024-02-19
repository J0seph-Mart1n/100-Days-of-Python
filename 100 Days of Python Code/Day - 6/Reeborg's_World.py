def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def square():
    turn_left()
    move()
    turn_right()
    if front_is_clear():
        move()
    else:
        turn_left()
        move()
    turn_right()
    move()
    turn_left()
    
while at_goal() == False:
    if wall_on_right():
        turn_left()
    else:
        turn_right()
        move()