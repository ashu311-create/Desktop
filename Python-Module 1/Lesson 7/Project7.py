def get_ascii_values():
    """
    Prompts the user for a string and prints the ASCII value of each character.
    """
    user_input = input("Enter a string of alphabets: ")

    print("\nASCII values for each character:")
    for char in user_input:
        # Check if the character is an alphabet (case-insensitive)
        if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
            print(f"Character: '{char}', ASCII Value: {ord(char)}")
        else:
            print(f"Character: '{char}' is not an alphabet. Skipping.")

if __name__ == "__main__":
    get_ascii_values()