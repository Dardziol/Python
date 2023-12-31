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

# Write your code below this line 👇
rps = [rock, paper, scissors]
user = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors.\n"))
if user >= 3 or user < 0:
    print("You can't use anything else, you lose!")
else:
    print("You chose:")
    print(rps[user])
    computer = random.randint(0, 2)
    print("Computer chose:")
    print(rps[computer])
    if user == computer:
        print("It's a draw!")
    elif user == 0 and computer == 2:
        print("You win!")
    elif computer == 0 and user == 2:
        print("You lose!")
    elif user > computer:
        print("You win!")
    elif computer > user:
        print("You lose!")
