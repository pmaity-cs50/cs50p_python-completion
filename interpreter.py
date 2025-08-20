
def main():
    # Get the expression from the user
    expression = input("Expression: ")
    # Call the calculate function to get the result
    result = calculate(expression)
    # Print the result formatted to one decimal place
    print(f"{result:.1f}")

def calculate(expression):
    # Split the expression into x, y, and z
    x, y, z = expression.split()
    # Convert x and z to integers
    x = int(x)
    z = int(z)

    # Perform the calculation based on the operator y
    if y == '+':
        return float(x + z)
    elif y == '-':
        return float(x - z)
    elif y == '*':
        return float(x * z)
    elif y == '/':
        return float(x / z)
    else:
        # Handle invalid operators
        return "Invalid operator"

if __name__ == "__main__":
    main()