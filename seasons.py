# # import sys
# # import re
# # from datetime import date
# # import inflect

# # def main():
# #     try:
# #         birth_date_str = input("Date of Birth: ")

# #         if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", birth_date_str):
# #             raise ValueError


# #         minutes = calculate_minutes(birth_date_str)


# #         p = inflect.engine()
# #         minutes_words = p.number_to_words(minutes, andword="")
# #         print(f"{minutes_words.capitalize()} minutes")
# #     except ValueError:
# #         sys.exit("Invalid Date")

# # def calculate_minutes(birth_date_str):
# #     birth_date = date.fromisoformat(birth_date_str)
# #     today = date.today()

# #     if birth_date > today:
# #         raise ValueError

# #     delta = today - birth_date
# #     return int(delta.total_seconds() / 60)

# # if __name__ == "__main__":
# #     main()




# # import sys
# # import re
# # from datetime import date
# # import inflect

# # def main():
# #     try:
# #         birth_date_str = input("Date of Birth: ")
# #         # This regex will catch invalid formats like "February 6th, 1998"
# #         if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", birth_date_str):
# #             sys.exit("Invalid Date")

# #         # Calculate age in minutes
# #         minutes = calculate_minutes(birth_date_str)

# #         # Convert minutes to words and print
# #         p = inflect.engine()
# #         minutes_words = p.number_to_words(minutes, andword="")
# #         print(f"{minutes_words.capitalize()} minutes")
# #     except ValueError:
# #         sys.exit("Invalid Date")

# # def calculate_minutes(birth_date_str):
# #     birth_date = date.fromisoformat(birth_date_str)
# #     today = date.today()

# #     if birth_date > today:
# #         raise ValueError

# #     delta = today - birth_date
# #     return int(delta.total_seconds() / 60)

# # if __name__ == "__main__":
# #     main()


# from datetime import date
# import sys

# def get_minutes_lived(birthdate):
#     """
#     Calculate the number of minutes lived since the birthdate.
#     """
#     today = date.today()
#     delta = today - birthdate
#     minutes_lived = delta.days * 24 * 60
#     return minutes_lived

# def number_to_words(number):
#     """
#     Convert a number to its English word representation.
#     """
#     # This is a simplified implementation for demonstration purposes.
#     # A full implementation would be more complex.
#     if number == 0:
#         return "zero"
#     elif number == 1:
#         return "one"
#     elif number == 525600:
#         return "five hundred twenty-five thousand, six hundred"
#     else:
#         return str(number)  # Fallback to string representation

# def main():
#     try:
#         # Prompt the user for their birthdate
#         birthdate_str = input("Date of Birth (YYYY-MM-DD): ")
#         birthdate = date.fromisoformat(birthdate_str)

#         # Calculate minutes lived
#         minutes_lived = get_minutes_lived(birthdate)

#         # Convert minutes to words
#         minutes_in_words = number_to_words(minutes_lived)

#         # Print the result
#         print(f"{minutes_in_words} minutes")

#     except ValueError:
#         sys.exit("Invalid date")

# if __name__ == "__main__":
#     main()




from datetime import date
import sys
import inflect

def main():
    try:
        birth_date = get_date(input("Date of Birth: "))
        today = date.today()
        minutes = calculate_minutes(birth_date, today)
        print(convert_to_words(minutes))
    except (ValueError, SystemExit):
        sys.exit("Invalid date")

def get_date(date_str):
    try:
        year, month, day = map(int, date_str.split('-'))
        return date(year, month, day)
    except (ValueError, AttributeError):
        raise ValueError

def calculate_minutes(birth_date, today):
    if birth_date > today:
        raise ValueError
    delta = today - birth_date
    return round(delta.total_seconds() / 60)

def convert_to_words(number):
    p = inflect.engine()
    words = p.number_to_words(number, andword="").capitalize()
    return f"{words} minutes"

if __name__ == "__main__":
    main()
