"""
Simple Python Calculator Program

This module provides basic arithmetic operations: add, subtract, multiply, and divide.
"""


def add(a, b):
    """Add two numbers.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        The sum of a and b
    """
    return a + b


def subtract(a, b):
    """Subtract two numbers.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        The difference of a and b
    """
    return a - b


def multiply(a, b):
    """Multiply two numbers.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        The product of a and b
    """
    return a * b


def divide(a, b):
    """Divide two numbers.
    
    Args:
        a: Dividend (first number)
        b: Divisor (second number)
        
    Returns:
        The quotient of a divided by b
        
    Raises:
        ValueError: If b is zero
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def main():
    """Main calculator interface."""
    print("Simple Python Calculator")
    print("-" * 40)
    
    while True:
        try:
            # Get user input
            print("\nOptions:")
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")
            print("5. Exit")
            
            choice = input("\nEnter operation (1/2/3/4/5): ").strip()
            
            if choice == "5":
                print("Thank you for using the calculator. Goodbye!")
                break
            
            if choice not in ["1", "2", "3", "4"]:
                print("Invalid choice. Please try again.")
                continue
            
            # Get numbers from user
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            # Perform operation
            if choice == "1":
                result = add(num1, num2)
                operation = "+"
            elif choice == "2":
                result = subtract(num1, num2)
                operation = "-"
            elif choice == "3":
                result = multiply(num1, num2)
                operation = "*"
            else:  # choice == "4"
                result = divide(num1, num2)
                operation = "/"
            
            print(f"\n{num1} {operation} {num2} = {result}")
            
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
