
import random
import sys

def main():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                break
        except ValueError:
            pass

    secret_number = random.randint(1, level)

    while True:
        try:
            guess = int(input("Guess: "))
            if guess > 0:
                if guess < secret_number:
                    print("Too small!")
                elif guess > secret_number:
                    print("Too large!")
                else:
                    print("Just right!")
                    sys.exit(0)
        except ValueError:
            pass

if __name__ == "__main__":
    main()
