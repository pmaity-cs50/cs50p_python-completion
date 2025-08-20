def main():
    text = input("Input: ")
    print(shorten(text))

def shorten(word):
    vowels = "aeiouAEIOU"
    new_word = ""
    for char in word:
        if char not in vowels:
            new_word += char
    return new_word

if __name__ == "__main__":
    main()
