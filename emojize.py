
# import emoji

# def main():

#     text = input("Input: ")


#     emojized_text = emoji.emojize(text)


#     print("Output:", emojized_text)

# if __name__ == "__main__":
#     main()

# import emoji

# def main():
#     # Prompt the user for input without an explicit prompt label
#     text = input()

#     # Convert emoji shortcodes to emojis
#     emojized_text = emoji.emojize(text)

#     # Print only the final emojized output
#     print(emojized_text)

# if __name__ == "__main__":
#     main()



# import emoji

# def main():
#     text = input()
#     emojized_text = emoji.emojize(text)
#     print(emojized_text)

# if __name__ == "__main__":
#     main()


# import emoji

# def main():
#     try:
#         # Prompt the user for input
#         text = input()

#         # Convert emoji shortcodes to emojis
#         emojized_text = emoji.emojize(text)

#         # Print the output
#         print(emojized_text)
#     except EOFError:
#         # Exit gracefully if no more input is available
#         pass

# if __name__ == "__main__":
#     main()



import emoji

def main():
    # Prompt user for input
    user_input = input("Input: ")

    # Convert any emoji codes/aliases to emojis
    emojized_text = emoji.emojize(user_input, language='alias')

    # Output the result
    print("Output:", emojized_text)

if __name__ == "__main__":
    main()
