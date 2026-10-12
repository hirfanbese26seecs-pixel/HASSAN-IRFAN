
def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b


def even_odd(number):
    if number % 2 == 0:
        return f"{number} is Even."
    return f"{number} is Odd."


def percentage(a, b):
    if b == 0:
        return "Error: Cannot calculate percentage with zero as the second number."
    return (a / b) * 100


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def main():
    while True:
        print("\n===== PYTHON CALCULATOR =====")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Check Even/Odd")
        print("6. Calculate Percentage")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "7":
            print("Thank you for using the calculator!")
            break

        elif choice in ("1", "2", "3", "4", "6"):
            a = get_number("Enter the first number: ")
            b = get_number("Enter the second number: ")

            if choice == "1":
                result = addition(a, b)
                print("Result:", result)

            elif choice == "2":
                result = subtraction(a, b)
                print("Result:", result)

            elif choice == "3":
                result = multiplication(a, b)
                print("Result:", result)

            elif choice == "4":
                result = division(a, b)
                print("Result:", result)

            elif choice == "6":
                result = percentage(a, b)
                if isinstance(result, str):
                    print(result)
                else:
                    print(f"Percentage: {result:.2f}%")

        elif choice == "5":
            number = get_number("Enter a whole number: ")
            if not number.is_integer():
                print("Please enter a whole number.")
            else:
                print(even_odd(int(number)))

        else:
            print("Invalid choice! Please select 1-7.")


if __name__ == "__main__":
    main()
