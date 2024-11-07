def vigenere_cipher(text, keyword, mode='encrypt'):
    keyword = keyword.upper()
    text = text.upper()
    result = ""
    keyword_index = 0

    for char in text:
        if char.isalpha():
            shift = ord(keyword[keyword_index]) - ord('A')
            shift = shift if mode == 'encrypt' else -shift
            new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            result += new_char
            keyword_index = (keyword_index + 1) % len(keyword)
        else:
            result += char

    return result

# Get user inputs
choice = input("Enter 'e' to encrypt or 'd' to decrypt: ").lower()
text = input("Enter text: ")
keyword = input("Enter keyword: ")

mode = 'encrypt' if choice == 'e' else 'decrypt'
result = vigenere_cipher(text, keyword, mode)
print(f"Result: {result}")
