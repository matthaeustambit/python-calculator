import math

def calculator():
    print("- calculator")
    print("Type 'exit' to quit anytime.")

    while True:
        operation = input("Enter (+, -, *, /, sqrt): ")

        if operation == 'exit':
            print("Exiting calculator. See you, lil bro!")
            break

        if operation == 'sqrt':
            num = float(input("Enter number for square root: "))
            if num >= 0:
                print(f"√{num} = {math.sqrt(num)}")
            else:
                print("Error: Cannot take square root of a negative number.")
        elif operation in ('+', '-', '*', '/'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if operation == '+':
                print(f"{num1} + {num2} = {num1 + num2}")
            elif operation == '-':
                print(f"{num1} - {num2} = {num1 - num2}")
            elif operation == '*':
                print(f"{num1} * {num2} = {num1 * num2}")
            elif operation == '/':
                if num2 != 0:
                    print(f"{num1} / {num2} = {num1 / num2}")
                else:
                    print("Error: Division by zero is not allowed.")
        else:
            print("Invalid operation. Please enter +, -, *, /, sqrt, or exit.")

# Run it
calculator()
