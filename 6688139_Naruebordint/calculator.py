def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

def calculate_velocity(distance: float, time: float) -> float:
    if time <= 0:
        raise ValueError("Time must be greater than zero")
    return distance / time

def main():
    print("Basic Calculator")
    print("Operations: +, -, *, /, v (velocity)")

    while True:
        operation = input("Enter operation (+, -, *, /, v): ")
        if operation in ['+', '-', '*', '/']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                if operation == '+':
                    result = add(num1, num2)
                elif operation == '-':
                    result = subtract(num1, num2)
                elif operation == '*':
                    result = multiply(num1, num2)
                elif operation == '/':
                    result = divide(num1, num2)
                print(f"Result: {result}")
            except ValueError:
                print("Invalid input. Please enter numbers.")
        elif operation == 'v':
            try:
                distance = float(input("Enter distance: "))
                time = float(input("Enter time: "))
                result = calculate_velocity(distance, time)
                print(f"Velocity: {result}")
            except ValueError as e:
                print(e)
        else:
            print("Invalid operation")

        again = input("Do another calculation? (y/n): ").lower()
        if again != 'y':
            break

if __name__ == "__main__":
    main()
