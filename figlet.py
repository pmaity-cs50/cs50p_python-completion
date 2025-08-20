
import sys
import random
from pyfiglet import Figlet

def main():
    figlet = Figlet()

    # Get a list of all available fonts
    fonts = figlet.getFonts()

    # Check for command-line arguments
    if len(sys.argv) == 1:
        # If no arguments, use a random font
        font = random.choice(fonts)
    elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
        # If font is specified, use it
        font = sys.argv[2]
        if font not in fonts:
            sys.exit("Invalid font")
    else:
        # Invalid command-line arguments
        sys.exit("Invalid usage")

    # Set the font
    figlet.setFont(font=font)

    # Prompt user for text and print in the chosen font
    text = input("Input: ")
    print(figlet.renderText(text))

if __name__ == "__main__":
    main()
