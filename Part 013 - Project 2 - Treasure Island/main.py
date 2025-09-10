print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/@mahmoudahhagras/_____/_____ /_____/
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input("You're at a crossroad which way will you go?\nType 'left' to go left or 'right' to go right.")
if choice1.lower() == "left":
    choice2 = input("You find your self at a lake,\nType 'swim' to swim past the lake or 'wait' to wait for the ferry?")
    if choice2.lower() == "wait":
        choice3 = input("you arrive at a forest with three huts, which one will you enter? red, yellow or green?")
        if choice3 == "yellow":
            print("Congratulations!! You found the treasure")
            exit()
        elif choice3.lower() == "green":
            print("GAME OVER!! You have been eaten by an orc.")
            exit()
        elif choice3.lower() == "red":
            print("GAME OVER!! You have been burned alive by fire.")
            exit()
        else:
            print("GAME OVER!! A Snake killed you.")
            exit()
    else:
        print("GAME OVER!! You Drowned.")
        exit()
else:
    print("GAME OVER!! you fall into a hole.")
    exit()