# # def main():
# #     while True:
# #         fraction = input("Fraction: ")
# #         try:
# #             x, y = convert(fraction)
# #             print(gauge(x, y))
# #             break
# #         except (ValueError, ZeroDivisionError):
# #             pass

# # def convert(fraction):
# #     x, y = fraction.split('/')
# #     x = int(x)
# #     y = int(y)
# #     if y == 0:
# #         raise ZeroDivisionError
# #     if x > y:
# #         raise ValueError
# #     return x, y

# # def gauge(x, y):
# #     percentage = round((x / y) * 100)
# #     if percentage <= 1:
# #         return "E"
# #     elif percentage >= 99:
# #         return "F"
# #     else:
# #         return f"{percentage}%"

# # if __name__ == "__main__":
# #     main()



# def main():
#     while True:
#         fraction = input("Fraction: ")
#         try:
#             x, y = convert(fraction)
#             print(gauge(x, y))
#             break
#         except (ValueError, ZeroDivisionError):
#             pass

# def convert(fraction):
#     try:
#         x, y = fraction.split('/')
#         x = int(x)
#         y = int(y)
#     except (ValueError, IndexError):
#         raise ValueError

#     if x < 0 or y < 0:
#         raise ValueError
#     if y == 0:
#         raise ZeroDivisionError
#     if x > y:
#         raise ValueError

#     return x, y

# def gauge(x, y):
#     percentage = round((x / y) * 100)
#     if percentage <= 1:
#         return "E"
#     elif percentage >= 99:
#         return "F"
#     else:
#         return f"{percentage}%"

# if __name__ == "__main__":
#     main()


def main():
    while True:
        try:
            fraction = input("Fraction: ").strip()
            percentage = convert(fraction)
            print(gauge(percentage))
            break
        except (ValueError, ZeroDivisionError):
            pass

def convert(fraction):
    try:
        x, y = map(int, fraction.split('/'))

        if y == 0:
            raise ZeroDivisionError
        if x > y:
            raise ValueError
        if x < 0 or y < 0:
            raise ValueError

        return round((x / y) * 100)

    except (ValueError, ZeroDivisionError):
        raise

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
