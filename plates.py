
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    
    if not 2 <= len(s) <= 6:
        return False


    if not s[0].isalpha() or not s[1].isalpha():
        return False


    has_number = False
    for i, char in enumerate(s):
        if char.isdigit():
            has_number = True
            if char == '0' and i > 1 and not s[i-1].isdigit():
                return False
            if i > 1 and s[i-1].isalpha():
                pass
        elif has_number:
            return False


    if not s.isalnum():
        return False

    return True

if __name__ == "__main__":
    main()
