# import re

# def main():
#     print(validate(input("IPv4 Address: ")))

# def validate(ip_address):
#     # Split the IP address by the dot
#     parts = ip_address.split('.')

#     # Check if there are exactly 4 parts
#     if len(parts) != 4:
#         return False

#     # Check each part
#     for part in parts:
#         # Check if the part is an integer between 0 and 255
#         if not part.isdigit() or not 0 <= int(part) <= 255:
#             return False

#     return True

# if __name__ == "__main__":
#     main()



# import re
# import sys

# def main():
#     print(validate(input("IPv4 Address: ")))

# def validate(ip):
#     if re.search(r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$", ip):
#         parts = ip.split('.')
#         for part in parts:
#             if not 0 <= int(part) <= 255:
#                 return False
#         return True
#     else:
#         return False

# if __name__ == "__main__":
#     main()


import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip_address):
    parts = ip_address.split('.')

    if len(parts) != 4:
        return False

    for part in parts:
        if not part.isdigit():
            return False

        # Check for leading zeros, except for "0" itself
        if len(part) > 1 and part.startswith('0'):
            return False

        if not 0 <= int(part) <= 255:
            return False

    return True

if __name__ == "__main__":
    main()
