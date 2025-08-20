import sys
import csv
from tabulate import tabulate

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pizza.py filename.csv")
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

    try:
        with open(sys.argv[1]) as file:
            reader = csv.reader(file)
            header = next(reader)
            menu = []
            for row in reader:
                menu.append(row)

        print(tabulate(menu, headers=header, tablefmt="grid"))

    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()
