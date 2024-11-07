# Modular inverse using a simple loop
def mod_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    return None

# RSA Key Generation
def rsa_key_gen(p, q, e):
    n = p * q
    phi = (p - 1) * (q - 1)
    d = mod_inverse(e, phi)
    return (e, n), (d, n)

# RSA Encryption
def rsa_encrypt(message, public_key):
    e, n = public_key
    return [pow(ord(char), e, n) for char in message]

# RSA Decryption
def rsa_decrypt(ciphertext, private_key):
    d, n = private_key
    return ''.join(chr(pow(char, d, n)) for char in ciphertext)

# Main code
p = int(input("Enter prime p: "))
q = int(input("Enter prime q: "))
e = int(input("Enter public exponent e: "))

public_key, private_key = rsa_key_gen(p, q, e)
print(f"Public Key: {public_key}, Private Key: {private_key}")

message = input("Enter message to encrypt: ")
ciphertext = rsa_encrypt(message, public_key)
print(f"Ciphertext: {ciphertext}")

decrypted_message = rsa_decrypt(ciphertext, private_key)
print(f"Decrypted Message: {decrypted_message}")
