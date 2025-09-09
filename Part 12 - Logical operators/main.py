# A and B #Both conditions need to be true
# C or D #Only one condition needs to be true
# not E #The condition must be false

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
group1 = 5
group2 = 7
group3 = 12
group4 = 0
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        price = group1
    elif age <= 18:
        price = group2
    elif age > 45 or age < 55:
        price = group4
    else:
        price = group3
    photo = input("Do you want a photo with the ride? Type 'yes' or if not press enter to skip.")
    if photo.lower() == "yes":
        final_price = price+3
        print("Please Pay $ " + str(final_price))
    else:
        final_price = price
        print("Please Pay $ " + str(final_price))
else:
    print("Sorry you have to grow taller before you can ride.")
