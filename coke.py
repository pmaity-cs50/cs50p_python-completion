
def main():
    # Set the cost of the Coke
    cost = 50

    # Initialize the amount paid
    paid = 0

    
    while paid < cost:
        # Calculate the amount due
        due = cost - paid
        print(f"Amount Due: {due}")


        coin = int(input("Insert Coin: "))

        # Check if the coin is a valid denomination
        if coin in [25, 10, 5]:
            paid += coin


    change = paid - cost
    print(f"Change Owed: {change}")

if __name__ == "__main__":
    main()
