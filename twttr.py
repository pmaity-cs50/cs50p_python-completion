
def main():
    # Get user input
    text = input("Input: ")

    
    vowels = "aeiouAEIOU"


    new_text = ""
    for char in text:
        if char not in vowels:
            new_text += char


    print("Output:", new_text)

if __name__ == "__main__":
    main()
