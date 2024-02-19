rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
import sys

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
if player>=3:
  print("You typed an invalid number")
  sys.exit()
CPU = random.randint(0,2)

rps = [rock,paper,scissors]

player_choice = rps[player]
CPU_choice = rps[CPU]

print(player_choice)
print("\nComputer Chose: ")
print(CPU_choice)

if player == 0 and CPU == 1:
  print("You Lose")
elif player == 0 and CPU == 2:
  print("You Win!!")
elif player == 1 and CPU == 0:
  print("You Win!!")
elif player == 1 and CPU == 2:
  print("You Lose")
elif player == 2 and CPU == 0:
  print("You Lose")
elif player == 2 and CPU == 1:
  print("You Win!!")
elif player == CPU:
  print("Draw")
