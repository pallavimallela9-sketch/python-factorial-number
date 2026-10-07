# Program: Factorial of a Number
# Author: M.Pallavi


def calculate_factorial(number):
    factorial = 1

    for i in range(1, number + 1):
        factorial = factorial * i

    return factorial


def main():
    print("================================")
    print("      FACTORIAL OF A NUMBER")
    print("================================")

    try:
        number = int(input("Enter a non-negative integer: "))

        if number < 0:
            print("\nFactorial is not defined for negative numbers.")
            return

        result = calculate_factorial(number)

        print("\nNumber    :", number)
        print("Factorial :", result)

        # Display the calculation steps
        if number == 0:
            print("\nCalculation: 0! = 1")
        else:
            expression = " × ".join(str(i) for i in range(1, number + 1))
            print("\nCalculation:")
            print(f"{number}! = {expression} = {result}")

    except ValueError:
        print("\nInvalid input!")
        print("Please enter a valid integer.")


if __name__ == "__main__":
    main()
