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
pc_wins= 0
user_wins = 0
game = ["rock", "paper", "scissors"]
go = input("Want to Play rock, paper, scissors?\n")
while go.lower() == "yes":
    user = input("What will you choose?\n").lower()
    console_play = random.randint(0, 2)
    user_play = int(game.index(user))
    if user_play == 0 and console_play == 0:
        print("console Play\n" + rock + "\nIt's a tie")
    elif user_play == 0 and console_play == 1:
        print("console Play\n" + paper + "\nYou Lose")
        pc_wins+=1
    elif user_play == 0 and console_play == 2:
        print("console Play\n" + scissors + "\nYou Win")
        user_wins+=1
    elif user_play == 1 and console_play == 0:
        print("console Play\n" + rock + "\nYou Win")
        user_wins+=1
    elif user_play == 1 and console_play == 1 :
        print("console Play\n" + paper + "\nIt's a tie")
    elif user_play == 1 and console_play == 2 :
        print("console Play\n" + scissors + "\nYou Lose")
        pc_wins+=1
    elif user_play == 2 and console_play == 0 :
        print("console Play\n" + rock + "\nYou Lose")
    elif user_play == 2 and console_play == 1:
        print("console Play\n" + paper + "\nYou Win")
        user_wins+=1
    elif user_play == 2 and console_play == 2:
        print("console Play\n" + scissors + "\nIt's a tie")
    print("Leaderboard\n" + "User has won " + str(user_wins) + " times\n" + "PC has won "+ str(pc_wins) + " times")
    go = input("Want to Play rock, paper, scissors again?\n")
else:
    print("ok, next time then")
    print("Leaderboard\n" + "User has won " + str(user_wins) + " times\n" + "PC has won "+ str(pc_wins) + " times")