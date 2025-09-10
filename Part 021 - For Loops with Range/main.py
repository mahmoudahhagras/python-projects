# Work out the total of the numbers between 1 and 100, inclusive of both 1 and 100.
list = [0]
for num in range(1,101):
        list.append(num)
print(sum(list))