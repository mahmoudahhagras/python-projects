from art import logo
print(logo)
print("Welcome to the calculator program!")
def calculate(n1, n2, operation):
    if operation == "+":
        return n1 + n2
    elif operation == "-":
        return n1 - n2
    elif operation == "*":
        return n1 * n2
    elif operation == "/":
        if n2 == 0:
            print("Division by zero is not allowed.")
            return None
        else:
            return n1 / n2
    else:
        print("Invalid operation")
        return None
restart = "yes"
more = "yes"
while restart.lower() == "yes":
    n1 = float(input("What is the first number?: "))
    operation = input("Pick an operation: ")
    n2 = float(input("What is the next number?: "))
    more = "yes"
    while more.lower() == "yes":
        result = calculate(n1, n2, operation)
        if result is None:
            break
        print(f"The results are {result}")
        n1 = result
        more = input("Do you want to perform another operation with the results as the first number? ")
        if more.lower() == "yes":
            print(f"The current results {n1} becomes the first number")
            operation = input("Pick another operation: ")
            n2 = float(input("What is the next number?: "))
    restart = input("Do you want to start a new calculation?")
print("Thank you for using the calculator program!")
exit()
