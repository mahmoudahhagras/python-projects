# a hangman game in progress
import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print("Rules:\nyour current hp is \nevery wrong answer will take your hp.")
correct = 0
hp = 1
while hp > 0:
    guess = input("take a guess?")
    for letter in chosen_word:
        if letter == guess.lower():
            
            correct = 1
    if correct > 0:
        print("You Win")
        correct = 0
    else:
        hp-= 1
else:
    print("You lose")