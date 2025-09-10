print("Welcome to Python Pizza Deliveries!")
bill = 0
size = input("What size pizza do you want? S, M or L: ")
if size.lower() == "s":
    bill+=15
    print("ok, a Small pizza")
elif size.lower() == "m":
    bill+=20
    print("ok, a medium pizza")
elif size.lower() == "l":
    bill+=25
    print("ok, a Large pizza")
else:
    print("You entered an invalid pizza size, please try again!")
    exit()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
if pepperoni.lower() == "y":
    if size.lower() == "s":
        bill+=2
    else:
        bill+=3
    print("Added pepperoni")
elif pepperoni.lower() == "n":
    print("Didn't add pepperoni")
else:
    print("You entered an invalid entry, please try again!")
    exit()
extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese.lower() == "y":
    bill+=1
    print("Added extra cheese")
elif extra_cheese.lower() == "n":
    print("Didn't add extra cheese")
else:
    print("You entered an invalid entry, please try again!")
    exit()
print(f"Your final bill is: ${bill}.")