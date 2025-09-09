print("Welcome to Simple Calculator!")

first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))
operation = input("Choose operation (+, -, *, /)")
if operation == "+":
    print("Result:", first_number + second_number)
elif operation == "-":
    print("Result:", first_number - second_number)
elif operation == "*":
    print("Result:", first_number * second_number)
elif operation == "/":
    if second_number != 0:
        print("Result:", first_number / second_number)
    else:
        print("Error: Cannot divide by zero.")

else:
    print("Please enter a valid operation (+, -, *, /")
