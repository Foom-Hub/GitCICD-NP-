import calculator

try:
    num1 = int(input("Enter the first number (1 digit only): "))
    num2 = int(input("Enter the second number (1 digit only): "))

    if num1 > 9 or num2 > 9:
        print("Invalid input. Please enter numbers between 0 and 9.")
    else:
        print("\nSelect your calculator operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        select = int(input("Enter your choice (1-4): "))

        if select == 1:
            result = calculator.add(num1, num2)
            if result > 99:
                print("Result:", "99+")
            else:
                print("Result:", result)
        elif select == 2:
            result = calculator.subtract(num1, num2)
            if result < -99:
                print("Result:", "-99-")
            else:
                print("Result:", result)
        elif select == 3:
            result = calculator.multiply(num1, num2)
            if result > 99:
                print("Result:", "99+")
            else:
                print("Result:", result)
        elif select == 4:
            result = calculator.divide(num1, num2)
            if result is not None:
                if result > 99:
                    print("Result:", "99+")
                else:
                    print("Result:", result)
        else:
            print("Invalid choice.")
except ValueError:
    print("Invalid input. Please enter a number between 0 and 9.")
