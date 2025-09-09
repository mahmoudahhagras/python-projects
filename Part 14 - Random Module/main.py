import random
times = input("how many time do you want to flip the coin?")
num_times = int(times)
if num_times > 10:
    print("Number too high, Max output is set to 10")
    num_times = 10
else:
    print("Flipping the coin " + str(num_times) + " times")
while num_times > 0:
    flip = random.randint(1, 2)
    if flip == 1:
        coin_face = "Heads"
        num_times-=1
        print(coin_face)
    else:
        coin_face = "Tails"
        num_times-=1
        print(coin_face)
else:
    print("Flipped Successfully")