def main():
    # Get mass from the user and convert to an integer
    m_str = input("m: ")
    m = int(m_str)

    # Define the speed of light squared
    c = 300000000
    c_squared = c * c

    # Calculate energy using E = mc^2
    E = m * c_squared

    # Print the result
    print(f"E: {E}")

if __name__ == "__main__":
    main()
