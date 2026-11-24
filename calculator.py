
# Simple Calculator
# CodeOrbit Tech - Python Internship

# Display calculator title
print("===== SIMPLE CALCULATOR =====")

try:
    # Get numbers from the user
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Display available operations
    print("\nSelect an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    choice = input("Enter your choice (1-4): ")

    # Perform calculation
    if choice == "1":
        result = num1 + num2
        print("Result:", result)

    elif choice == "2":
        result = num1 - num2
        print("Result:", result)

    elif choice == "3":
        result = num1 * num2
        print("Result:", result)

    elif choice == "4":
        # Handle division by zero
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print("Result:", result)

    else:
        print("Invalid choice! Please select 1 to 4.")

except ValueError:
    # Handle invalid number inputs
    print("Error: Please enter valid numbers.")
