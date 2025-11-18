# Simple Calculator with History

history = []  # to store all calculations

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

def show_history():
    if len(history) == 0:
        print("\nNo history available!\n")
    else:
        print("\n---- Calculation History ----")
        for item in history:
            print(item)
        print("-----------------------------\n")

while True:
    print("------ SIMPLE CALCULATOR ------")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Show History")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '6':
        print("Exiting... Goodbye!")
        break

    elif choice == '5':
        show_history()
        continue

    # taking input for calculation
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        result = add(num1, num2)
        calc = f"{num1} + {num2} = {result}"

    elif choice == '2':
        result = subtract(num1, num2)
        calc = f"{num1} - {num2} = {result}"

    elif choice == '3':
        result = multiply(num1, num2)
        calc = f"{num1} * {num2} = {result}"

    elif choice == '4':
        result = divide(num1, num2)
        calc = f"{num1} / {num2} = {result}"

    else:
        print("Invalid choice! Try again.\n")
        continue

    print("\nResult:", result, "\n")
    history.append(calc)

