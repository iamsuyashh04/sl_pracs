def rsa_encrypt(message, p, q, e):
    n = p * q
    phi = (p - 1) * (q - 1)
    d = pow(e, -1, phi)  # Calculate private key 'd'
    encrypted = pow(message, e, n)  # Encrypt the integer message
    return encrypted, (e, n), (d, n)  # Return encrypted message, public key, and private key

def rsa_decrypt(ciphertext, p, q, e):
    n = p * q
    phi = (p - 1) * (q - 1)
    d = pow(e, -1, phi)  # Calculate private key 'd'
    decrypted = pow(ciphertext, d, n)  # Decrypt the integer ciphertext
    return decrypted

# Main code
p = int(input("Enter prime p: "))
q = int(input("Enter prime q: "))
e = int(input("Enter public key exponent e: "))

message = int(input("Enter message to encrypt (as an integer): "))

# Encryption
encrypted_message, public_key, private_key = rsa_encrypt(message, p, q, e)
print("Public Key (e, n):", public_key)
print("Private Key (d, n):", private_key)
print("Encrypted message:", encrypted_message)

# Decryption
decrypted_message = rsa_decrypt(encrypted_message, p, q, e)
print("Decrypted message:", decrypted_message)
