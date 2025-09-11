# Work out the total of the numbers between 1 and 100, inclusive of both 1 and 100.
list = [0]
for num in range(1,101):
        list.append(num)
print(sum(list))

# FizzBuzz Game

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num%5 == 0:
        print("Buzz")
    elif num % 3 == 0:
        print("Fizz")
    else:
        print(str(num))