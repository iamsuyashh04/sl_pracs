def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    return None

def rsa_key_gen(p, q, e):
    n, phi = p * q, (p - 1) * (q - 1)
    if gcd(e, phi) != 1:
        raise ValueError("e must be coprime with (p-1)*(q-1).")
    d = mod_inverse(e, phi)
    if d is None:
        raise ValueError("No modular inverse for e.")
    return (e, n), (d, n)

def rsa_encrypt(message, public_key):
    e, n = public_key
    return [pow(ord(char), e, n) for char in message]

def rsa_decrypt(ciphertext, private_key):
    d, n = private_key
    return ''.join([chr(pow(char, d, n)) for char in ciphertext])

# Main code
p = int(input("Enter prime p: "))
q = int(input("Enter prime q: "))
e = int(input("Enter public exponent e: "))

public_key, private_key = rsa_key_gen(p, q, e)
print(f"Public Key: {public_key}, Private Key: {private_key}")

message = input("Enter message to encrypt: ")
ciphertext = rsa_encrypt(message, public_key)
print(f"Ciphertext: {ciphertext}")

print(f"Decrypted Message: {rsa_decrypt(ciphertext, private_key)}")
