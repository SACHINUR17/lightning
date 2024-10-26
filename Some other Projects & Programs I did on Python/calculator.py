def calculator():
    while True:
        print("Choose an operation (+, -, *, /):")
        operation = input()

        if operation not in ['+', '-', '*', '/']:
            print("Invalid operation. Please choose +, -, *, or /.")
            continue

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                continue
            result = num1 / num2

        print(f"{num1} {operation} {num2} = {result}")

if __name__ == "__main__":
    calculator()