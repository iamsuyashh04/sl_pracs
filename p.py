def encrypt(text,shift):
    result = ""
    
    for char in text:
        if char.isupper():
            new_char = chr((ord(char) - 65 + shift) % 26 + 65)
            result+=new_char
        elif char.islower():
            new_char = chr((ord(char) - 97 + shift) % 26 + 97)
            result+=new_char
        else:
            result+=char
    return result

def decrypt(text,shift):
    result = ""
            