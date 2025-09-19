from art import logo
print(logo)
import random
print("welcome to the Black Jack game!!")
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
console_cards = []
con = True
repeat = "yes"
move_user = ""
def calcu(move_user , cards, user_cards, console_cards, con, repeat):
    console_score = sum(console_cards)
    user_score = sum(user_cards)
    if user_score > 21:
        if 11 in user_cards and user_score > 21:
            while 11 in user_cards and user_score > 21:
                user_cards[user_cards.index(11)] = 1
                user_score = sum(user_cards)
        else:
            print(f"User Loses Your score is {sum(user_cards)}\nand Console score = {sum(console_cards)}")
            repeat = input("Do you want to try again?")
            return repeat
    elif user_score == 21:
        print(f"User Wins Your score is {sum(user_cards)}\nand Console score = {sum(console_cards)}")
        repeat = input("Do you want to try again?")
        return repeat
    elif console_score == 21:
        print(f"Console Wins Your score is {sum(user_cards)}\nand Console score = {sum(console_cards)}")
        repeat = input("Do you want to try again?")
        return repeat
    elif console_score > 21:
        print(f"User Wins Your score is {sum(user_cards)}\nand Console score = {sum(console_cards)}")
        repeat = input("Do you want to try again?")
        return repeat
def deal_cards(move_user , cards, user_cards, console_cards, con, repeat):
    user_cards.append(random.choice(cards))
    user_cards.append(random.choice(cards))
    user_score = sum(user_cards)
    console_cards.append(random.choice(cards))
    console_cards.append(random.choice(cards))
    console_score = sum(console_cards)
    while con == True:
            print(f"Your Cards are {user_cards}")
            print(f"the Console is first card is {console_cards[0]}")
            move_user = input(f"if you want to draw a card. Type 'hit' or if you want to stand. type 'stand'\n")
            if move_user.lower() == "hit":
                user_cards.append(random.choice(cards))
                print(f"Your cards are {user_cards}")
                user_score = sum(user_cards)
                repeat = calcu(move_user , cards, user_cards, console_cards, con, repeat)
                if sum(user_cards) >= 21:
                    break
            if console_score >= 18:
                print(f"the console has chosen to stand")
            elif console_score < 18:
                console_cards.append(random.choice(cards))
                console_score = sum(console_cards)
                repeat = calcu(move_user , cards, user_cards, console_cards, con, repeat)
                if console_score >= 21:
                    break
            if move_user.lower() == "stand":
                user_score = sum(user_cards)
                repeat = calcu(move_user , cards, user_cards, console_cards, con, repeat)
                if user_score > console_score and user_score <= 21:
                    print(f"User Wins Your score is {sum(user_cards)}\nand Console score = {sum(console_cards)}")
                    repeat = input("Do you want to try again?")
                    return repeat
                else:  
                    print(f"Console Wins Your score is {sum(user_cards)}\nand Console score = {sum(console_cards)}")
                    repeat = input("Do you want to try again?")
                    return repeat
start = input("Type 'start' to start\n")
while start == "start" and repeat == "yes":
    console_score = 0
    user_score = 0
    user_cards = []
    console_cards = []
    con = True
    repeat = "yes"
    move_user = ""
    repeat = deal_cards(move_user , cards, user_cards, console_cards, con, repeat)
else:
    print("Thank you for playing until we meet again.")
    exit()