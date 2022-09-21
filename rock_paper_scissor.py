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

random_number = random.randint(0,2)
userchoice = int(input("Enter your choice 0 for rock, 1 for paper and 2 for scissors: "))
choice = [rock, paper, scissors]
print(choice[userchoice]+"\n")
print("Computer choose:\n")
print(choice[random_number])
if random_number==userchoice:
  print("Draw")

elif (userchoice==0 and random_number==1) or (userchoice==1 and random_number==2) or (userchoice==2 and random_number==0):
  print("You lose")

else:
  print("You win")