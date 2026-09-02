# Shravan Calculator
# A simple command-line calculator inspired by the uploaded web calculator.


def calculator():
    print("=" * 35)
    print("       SHRAVAN CALCULATOR")
    print("=" * 35)

    name = input("Enter your name: ").strip()
    if not name:
        name = "User"

    print(f"\nWelcome, {name}!")

    while True:
        print("\nChoose an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Show all results")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "6":
            print(f"\nThanks for using Shravan Calculator, {name}!")
            break

        if choice not in {"1", "2", "3", "4", "5"}:
            print("Invalid choice. Please choose 1-6.")
            continue

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except ValueError:
            print("Please enter valid numbers.")
            continue

        if choice == "1":
            print(f"Result: {a:g} + {b:g} = {a + b:g}")
        elif choice == "2":
            print(f"Result: {a:g} - {b:g} = {a - b:g}")
        elif choice == "3":
            print(f"Result: {a:g} * {b:g} = {a * b:g}")
        elif choice == "4":
            if b == 0:
                print("Cannot divide by zero.")
            else:
                print(f"Result: {a:g} / {b:g} = {a / b:g}")
        elif choice == "5":
            print("\n--- RESULTS ---")
            print(f"Addition:       {a + b:g}")
            print(f"Subtraction:    {a - b:g}")
            print(f"Multiplication: {a * b:g}")
            if b == 0:
                print("Division:        undefined (division by zero)")
            else:
                print(f"Division:        {a / b:g}")


if __name__ == "__main__":
    calculator()
