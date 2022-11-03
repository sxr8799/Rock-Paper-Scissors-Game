import random

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

RSP = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.  "))
if user_choice >= 3 or user_choice < 0:
  print("You typed an invalid number, you lose!")
else:
  user_choice_img = RSP[(user_choice)]
  print(f"\nYou chose:\n{user_choice_img}")
  PC_choice = random.randint(0,2)
  PC_choice_img = (RSP[PC_choice])
  print(f"\n*********************\n\nThe computer chose:\n{PC_choice_img}")

  if user_choice == 0 and PC_choice == 2:
    print("You win!")
  elif PC_choice == 0 and user_choice == 2:
    print("You lose")
  elif PC_choice > user_choice:
    print("You lose")
  elif user_choice > PC_choice:
    print("You win!")
  elif PC_choice == user_choice:
    print("It's a Tie")
