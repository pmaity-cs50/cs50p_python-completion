import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    
    matches = re.search(r"^(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)$", s, re.IGNORECASE)
    if not matches:
        raise ValueError

    parts = matches.groups()
    start_time = convert_to_24h(parts[0], parts[1], parts[2])
    end_time = convert_to_24h(parts[3], parts[4], parts[5])

    return f"{start_time} to {end_time}"

def convert_to_24h(hour_str, minute_str, ampm):
    hour = int(hour_str)
    minute = int(minute_str) if minute_str else 0

    if not (1 <= hour <= 12 and 0 <= minute <= 59):
        raise ValueError

    if ampm.lower() == "pm" and hour != 12:
        hour += 12
    elif ampm.lower() == "am" and hour == 12:
        hour = 0

    return f"{hour:02d}:{minute:02d}"

if __name__ == "__main__":
    main()
