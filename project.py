# # import csv
# # from datetime import datetime

# # def main():
# #     """Main function to run the finance tracker"""
# #     print("Welcome to Finance Tracker!")
# #     while True:
# #         choice = input("\n1. Add transaction\n2. View summary\n3. Exit\n> ")
# #         if choice == "1":
# #             add_transaction()
# #         elif choice == "2":
# #             view_summary()
# #         elif choice == "3":
# #             break
# #         else:
# #             print("Invalid choice")

# # def add_transaction():
# #     """Add a new financial transaction"""
# #     try:
# #         amount = float(input("Amount: "))
# #         category = input("Category: ")
# #         date = input("Date (YYYY-MM-DD, today if empty): ") or datetime.now().strftime("%Y-%m-%d")

# #         with open("transactions.csv", "a", newline="") as file:
# #             writer = csv.writer(file)
# #             writer.writerow([date, amount, category])
# #         print("Transaction added!")
# #     except ValueError:
# #         print("Invalid input")

# # def view_summary():
# #     """Display summary of transactions"""
# #     try:
# #         with open("transactions.csv", "r") as file:
# #             transactions = list(csv.reader(file))

# #         total = sum(float(t[1]) for t in transactions)
# #         print(f"\nTotal transactions: {len(transactions)}")
# #         print(f"Total amount: ${total:.2f}")

# #         categories = {}
# #         for t in transactions:
# #             categories[t[2]] = categories.get(t[2], 0) + float(t[1])
# #         print("\nBy category:")
# #         for cat, amt in categories.items():
# #             print(f"- {cat}: ${amt:.2f}")

# #     except FileNotFoundError:
# #         print("No transactions yet")

# # def calculate_balance(transactions):
# #     """Calculate current balance from transactions"""
# #     return sum(float(t[1]) for t in transactions)

# # if __name__ == "__main__":
# #     main()


# import csv
# from datetime import datetime

# def main():
#     """Main function to run the finance tracker"""
#     print("Welcome to Finance Tracker!")
#     while True:
#         choice = input("\n1. Add transaction\n2. View summary\n3. Exit\n> ")
#         if choice == "1":
#             add_transaction()
#         elif choice == "2":
#             view_summary()  # Uses default filename
#         elif choice == "3":
#             break
#         else:
#             print("Invalid choice")

# def add_transaction(filename="transactions.csv"):
#     """Add a new financial transaction"""
#     try:
#         amount = float(input("Amount: "))
#         category = input("Category: ")
#         date = input("Date (YYYY-MM-DD, today if empty): ") or datetime.now().strftime("%Y-%m-%d")

#         with open(filename, "a", newline="") as file:
#             writer = csv.writer(file)
#             writer.writerow([date, amount, category])
#         print("Transaction added!")
#     except ValueError:
#         print("Invalid input")

# def view_summary(filename="transactions.csv"):
#     """Display summary of transactions"""
#     try:
#         with open(filename, "r") as file:
#             transactions = list(csv.reader(file))

#         total = sum(float(t[1]) for t in transactions)
#         print(f"\nTotal transactions: {len(transactions)}")
#         print(f"Total amount: ${total:.2f}")

#         categories = {}
#         for t in transactions:
#             categories[t[2]] = categories.get(t[2], 0) + float(t[1])
#         print("\nBy category:")
#         for cat, amt in categories.items():
#             print(f"- {cat}: ${amt:.2f}")

#     except FileNotFoundError:
#         print("No transactions yet")

# def calculate_balance(transactions):
#     """Calculate current balance from transactions"""
#     return sum(float(t[1]) for t in transactions)

# if __name__ == "__main__":
#     main()



import csv
from datetime import datetime

def main():
    """Main function to run the finance tracker"""
    print("Welcome to Finance Tracker!")
    while True:
        choice = input("\n1. Add transaction\n2. View summary\n3. Exit\n> ")
        if choice == "1":
            add_transaction()
        elif choice == "2":
            view_summary()
        elif choice == "3":
            break
        else:
            print("Invalid choice")

def add_transaction(amount=None, category=None, date=None, filename="transactions.csv"):
    """Add a new financial transaction (parameters for testing)"""
    try:
        if amount is None:  # Normal execution
            amount = float(input("Amount: "))
            category = input("Category: ")
            date = input("Date (YYYY-MM-DD, today if empty): ") or datetime.now().strftime("%Y-%m-%d")

        with open(filename, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([date, amount, category])
        return True
    except ValueError:
        print("Invalid input")
        return False

def view_summary(filename="transactions.csv"):
    """Display summary of transactions"""
    try:
        with open(filename, "r") as file:
            transactions = list(csv.reader(file))

        total = sum(float(t[1]) for t in transactions)
        print(f"\nTotal transactions: {len(transactions)}")
        print(f"Total amount: ${total:.2f}")

        categories = {}
        for t in transactions:
            categories[t[2]] = categories.get(t[2], 0) + float(t[1])
        print("\nBy category:")
        for cat, amt in categories.items():
            print(f"- {cat}: ${amt:.2f}")

    except FileNotFoundError:
        print("No transactions yet")

def calculate_balance(transactions):
    """Calculate current balance from transactions"""
    return sum(float(t[1]) for t in transactions)

if __name__ == "__main__":
    main()
