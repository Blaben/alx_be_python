num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
Operation = input("Choose the operation (+, -, *, /): ")
result = 0

match Operation:
    case "+" :
        result = num1 + num2
        print(f"The result is {result}")

    case"-" :
        result = num1 - num2
        print(f"The result is {result}")

    case "*":
        result = num1 * num2
        print(f"The result is {result}")

    case "/" :
        if num2 == 0 :
            print("You Cannot divide by zero.")
        else :
            result = num1 / num2
        print(f"The result is {result}")

    case _:
        print("Invalid input")