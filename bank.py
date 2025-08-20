def main():
    # Get user input and strip whitespace
    greeting = input("Greeting: ").strip().lower()

    # Check for "hello"
    if greeting.startswith("hello"):
        print("$0")
    # Check for "h"
    elif greeting.startswith("h"):
        print("$20")
    # Otherwise, print $100
    else:
        print("$100")

if __name__ == "__main__":
    main()

    
