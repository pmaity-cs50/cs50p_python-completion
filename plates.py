# def main():
#     plate = input("Plate: ")
#     if is_valid(plate):
#         print("Valid")
#     else:
#         print("Invalid")

# def is_valid(s):
#     # Check length
#     if not 2 <= len(s) <= 6:
#         return False

#     # Check if first two characters are letters
#     if not s[0].isalpha() or not s[1].isalpha():
#         return False

#     # Check for numbers and their placement
#     has_number = False
#     for i, char in enumerate(s):
#         if char.isdigit():
#             has_number = True
#             if char == '0' and i > 1 and not s[i-1].isdigit():
#                 return False
#             if i > 1 and s[i-1].isalpha():
#                 pass
#         elif has_number:
#             return False

#     # Check for non-alphanumeric characters
#     if not s.isalnum():
#         return False

#     return True

# if __name__ == "__main__":
#     main()



def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Check length (2-6 chars)
    if not 2 <= len(s) <= 6:
        return False

    # First two must be letters
    if not s[:2].isalpha():
        return False

    # No punctuation/spaces
    if not s.isalnum():
        return False

    # Number rules:
    numbers = [c for c in s if c.isdigit()]
    if numbers:
        # Numbers can't start with 0
        if numbers[0] == '0':
            return False
        # Numbers must be at the end
        if not s[s.index(numbers[0]):].isdigit():
            return False

    return True

if __name__ == "__main__":
    main()
