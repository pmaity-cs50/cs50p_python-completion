# import re
# import sys

# def main():
#     print(parse(input("HTML: ")))

# def parse(s):

#     matches = re.search(r"\"https?://(www\.)?youtube\.com/embed/([a-zA-Z0-9]+)\"", s)

#     if matches:

#         video_id = matches.group(2)

#         return f"https://youtu.be/{video_id}"
#     else:
#         return None

# if __name__ == "__main__":
#     main()


import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    # The regex now specifically looks for the iframe and src attribute
    if matches := re.search(r"<iframe.*?src=\"https?://(www\.)?youtube\.com/embed/([a-zA-Z0-9_]+)\".*?></iframe>", s):
        return f"https://youtu.be/{matches.group(2)}"
    else:
        return None

if __name__ == "__main__":
    main()
