
# def main():
#     months = [
#         "January", "February", "March", "April", "May", "June",
#         "July", "August", "September", "October", "November", "December"
#     ]

#     while True:
#         try:
#             date_str = input("Date: ").strip()


#             if '/' in date_str:
#                 month, day, year = date_str.split('/')
#                 month = int(month)
#                 day = int(day)
#                 year = int(year)
#                 if not (1 <= month <= 12 and 1 <= day <= 31):
#                     continue


#             elif ',' in date_str:
#                 parts = date_str.replace(',', '').split()
#                 if len(parts) != 3 or parts[0] not in months:
#                     continue
#                 month = months.index(parts[0]) + 1
#                 day = int(parts[1])
#                 year = int(parts[2])
#                 if not (1 <= month <= 12 and 1 <= day <= 31):
#                     continue


#             print(f"{year:04d}-{month:02d}-{day:02d}")
#             break

#         except (ValueError, IndexError):
#             continue

# if __name__ == "__main__":
#     main()



def main():
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    while True:
        try:
            date_str = input("Date: ").strip()

            
            if '/' in date_str:
                month, day, year = date_str.split('/')
                month = int(month)
                day = int(day)
                year = int(year)
                if not (1 <= month <= 12 and 1 <= day <= 31):
                    continue


            elif ',' in date_str:
                parts = date_str.replace(',', '').split()
                if len(parts) != 3 or parts[0] not in months:
                    continue
                month = months.index(parts[0]) + 1
                day = int(parts[1])
                year = int(parts[2])
                if not (1 <= month <= 12 and 1 <= day <= 31):
                    continue
            else:

                continue


            print(f"{year:04d}-{month:02d}-{day:02d}")
            break

        except (ValueError, IndexError):

            continue

if __name__ == "__main__":
    main()
