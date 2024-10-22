def encrypt(text, shift):
    result = ""
    
    for char in text:
        if char.isupper():
            new_char = chr((ord(char) - 65 + shift) % 26 + 65)
            result += new_char
            
        elif char.islower():
            new_char = chr((ord(char) - 97 + shift) % 26 + 97)
            result += new_char
        else:
            result += char
    return result 

def decrypt(text, shift):
    result = ""
    
    for char in text:
        if char.isupper():
            new_char = chr((ord(char) - shift - 65) % 26 + 65)
            result += new_char
            
        elif char.islower():
            new_char = chr((ord(char) - shift - 97) % 26 + 97)
            result += new_char
        else:
            result += char
    return result 

text = "SUYASH"
shift = 4

# Encrypt the original text
encrypted_text = encrypt(text, shift)

# Decrypt the encrypted text
decrypted_text = decrypt(encrypted_text, shift)

print("Original Text :", text)
print("Shift Value   :", shift)
print("Encrypted Text:", encrypted_text)
print("Decrypted Text:", decrypted_text)
