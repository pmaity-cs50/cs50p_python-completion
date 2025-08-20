import sys
from PIL import Image, ImageOps

def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python shirt.py [input_file] [output_file]")

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    
    if not (input_path.lower().endswith(('.jpg', '.jpeg', '.png')) and output_path.lower().endswith(('.jpg', '.jpeg', '.png'))):
        sys.exit("Invalid file format")
    if input_path.split('.')[-1].lower() != output_path.split('.')[-1].lower():
        sys.exit("Input and output files must have the same extension")

    try:

        input_image = Image.open(input_path)
        shirt_image = Image.open("shirt.png")


        input_image = ImageOps.fit(input_image, shirt_image.size)


        input_image.paste(shirt_image, shirt_image)


        input_image.save(output_path)

    except FileNotFoundError:
        sys.exit("Input file does not exist")

if __name__ == "__main__":
    main()
