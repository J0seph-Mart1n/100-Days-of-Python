import random
from art import logo,vs
from game_data import data
#from replit import clear

def take_person():
  person = random.choice(data)
  return person
  
play_game = True
score = 0
A = take_person()
B = take_person()
print(logo)
while play_game:
  print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}")
  print(vs)
  print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}")

  guess = input("Who has more followers. Type 'A' or 'B': ")
  if guess == 'A':
    if A['follower_count'] > B['follower_count']:
      score+=1
      #clear()
      print(logo)
      print(f"Your score is {score}")
      A = B
      B = take_person()
    else:
      print(f"Sorry, Wrong guess your final score {score}")
      play_game = False
  elif guess == 'B':
    if B['follower_count'] > A['follower_count']:
      score+=1
      #clear()
      print(logo)
      print(f"Your score is {score}")
      A = B
      B = take_person()
    else:
      #clear()
      print(f"Sorry, wrong guess your final score {score}")
      play_game = False

  