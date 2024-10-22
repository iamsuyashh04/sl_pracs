def vigenere_cipher(text, keyword, mode='encrypt'):
    keyword = keyword.upper()  # Ensure keyword is uppercase
    text = text.upper()        # Ensure text is uppercase
    result = ""                # Store result (encrypted or decrypted text)
    keyword_index = 0          # Track position in the keyword

    for char in text:
        if char.isalpha():  # Process alphabetic characters only
            shift = ord(keyword[keyword_index]) - ord('A')  # Calculate the shift value from keyword
            if mode == 'decrypt':
                shift = -shift  # Reverse the shift for decryption

            # Encrypt or decrypt the character
            new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            result += new_char

            # Move to the next character in the keyword
            keyword_index = (keyword_index + 1) % len(keyword)
        else:
            result += char  # Add non-alphabet characters as-is

    return result


def main():
    while True:
        choice = input("Encrypt, decrypt, or quit (e/d/q)? ").lower()
        if choice == 'q':
            break
        if choice not in ('e', 'd'):
            continue

        text = input("Enter text: ")
        keyword = input("Enter keyword: ")
        mode = 'encrypt' if choice == 'e' else 'decrypt'

        # Perform encryption or decryption
        result = vigenere_cipher(text, keyword, mode)
        print(f"Result: {result}")


if __name__ == "__main__":
    main()
