
def main():
    # Get the camel case string from the user
    camel_case_string = input("camelCase: ")

    # Initialize an empty string for the snake case
    snake_case_string = ""

    # Iterate through each character of the input string
    for char in camel_case_string:
        # If the character is an uppercase letter, prepend an underscore and convert to lowercase
        if char.isupper():
            snake_case_string += "_" + char.lower()
        else:
            # Otherwise, just append the character as is
            snake_case_string += char

    # Print the final snake case string
    print("snake_case:", snake_case_string)

if __name__ == "__main__":
    main()
