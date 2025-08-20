def convert(text):
    # Replace :) with a happy emoji
    text = text.replace(":)", "🙂")
    # Replace :( with a sad emoji
    text = text.replace(":(", "🙁")
    return text

def main():
    # Prompt the user for input
    user_input = input()
    # Call the convert function and print the result
    print(convert(user_input))

# Call the main function to run the program
if __name__ == "__main__":
    main()


