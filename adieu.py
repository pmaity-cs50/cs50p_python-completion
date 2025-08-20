
import inflect
import sys

def main():
    p = inflect.engine()
    names = []

    while True:
        try:
            name = input("Name: ")
            names.append(name)
        except EOFError:
            print("\nAdieu, adieu, to", p.join(names))
            sys.exit(0)

if __name__ == "__main__":
    main()
