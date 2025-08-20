import sys
import csv

def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python scourgify.py before.csv after.csv")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        students = []
        with open(input_file) as csv_in:
            reader = csv.DictReader(csv_in)
            for row in reader:
                last, first = row['name'].split(', ')
                students.append({'first': first, 'last': last, 'house': row['house']})

        with open(output_file, 'w') as csv_out:
            writer = csv.DictWriter(csv_out, fieldnames=['first', 'last', 'house'])
            writer.writeheader()
            for student in students:
                writer.writerow(student)

    except FileNotFoundError:
        sys.exit(f"Could not read {input_file}")

if __name__ == "__main__":
    main()
    