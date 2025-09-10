from hangman_words import word_list
from hangman_art import logo, stages
import random
print(logo)
chosen_word = random.choice(word_list)
place_holder = []
letters = len(chosen_word)
while len(place_holder) < letters:
    place_holder.append("_")
print("Rules:\nyour current HP is 3\nevery wrong answer will take off 1 hp.")
correct = 0
hp = 3
no = 0
display = ""
while hp > 0 and display != chosen_word:
    guess = input("take a guess?\n")
    for letter in chosen_word :
        if letter == guess.lower() :
            correct = 1
            place_holder[no] = letter
            no+=1
        else:
            no+=1
    if correct > 0 :
        print("Correct")
        correct = 0
        no = 0
        display = "".join(place_holder)
        print(display)
        print("Your Current HP is " + str(hp))
        print(stages[hp])
    else:
        hp -= 1
        no = 0
        print("Incorrect\n-1 HP")
        if hp == 0:
            print("Your Current HP is 0\nYou Lose")
            print(stages[0])
            exit()
        elif hp != 0:
            print("Your Current HP is " + str(hp))
            print(stages[hp])
else:
    print("You Win")
    print("Your Current HP is " + str(hp) + "\nThe word was " + display.capitalize())