fruits = ["Cherry", "Apple", "Pear"]
names = ["Alice", "Bob", "Adam", "Charlie", "David", "Emanuel", "Hannah", "Jack", "Joe", "Alya", "Samuel", "Adam", "George", "Peter"]
all = [fruits, names]
print(all)
fruits.extend(["Mango", "Orange", "Pineapple"])
num_fruits = len(fruits)
num_names = len(names)
adamcount = names.count("Adam")
print(fruits)
print(str(adamcount))
print(str(num_fruits))
print(str(num_names))