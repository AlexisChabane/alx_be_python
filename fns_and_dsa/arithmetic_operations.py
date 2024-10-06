def perform_operation(num1,num2,operation):
    match operation:
        case operation if operation == "add":
            add = lambda num1, num2: num1 + num2
        case operation if operation == "subtract":
            subtract = lambda num1, num2: num1 - num2
        case operation if operation == "multiply":
            mutiply = lambda num1, num2: num1 * num2
        case operation if operation == "divide":
            divide = lambda num1, num2: num1 / num2

        