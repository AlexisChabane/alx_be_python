num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case operation if operation == "+":
        total = num1 + num2
        print("The result is",total,"." )
    case operation if operation == "-":
        total = num1 - num2
        print("The result is",total,".")
    case operation if operation == "*":
        total = num1 * num2
        print("The result is",total,".")
    case operation if operation == "/":
        total = num1 / num2
        print("The result is",total,".")