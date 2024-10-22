def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(e, phi_n):
    for d in range(1, phi_n):
        if (e * d) % phi_n == 1:
            return d
    return None

def rsa_key_generation(p, q, e):
    if p == q:
        raise ValueError("p and q must be different.")
    
    n = p * q
    phi_n = (p - 1) * (q - 1)

    if gcd(e, phi_n) != 1:
        raise ValueError("e must be coprime with (p-1)*(q-1).")
    
    d = mod_inverse(e, phi_n)
    if d is None:
        raise ValueError("Cannot find modular inverse for e.")
    
    return (e, n), (d, n)

def rsa_encrypt(message, public_key):
    e, n = public_key
    return [pow(ord(char), e, n) for char in message]

def rsa_decrypt(ciphertext, private_key):
    d, n = private_key
    return ''.join([chr(pow(char, d, n)) for char in ciphertext])

def main():
    p = int(input("Enter prime number p: "))
    q = int(input("Enter prime number q: "))
    e = int(input("Enter public key e: "))
    
    public_key, private_key = rsa_key_generation(p, q, e)
    print(f"Public Key: {public_key}, Private Key: {private_key}")
    
    message = input("Enter message to encrypt: ")
    ciphertext = rsa_encrypt(message, public_key)
    print(f"Ciphertext: {ciphertext}")
    
    decrypted_message = rsa_decrypt(ciphertext, private_key)
    print(f"Decrypted Message: {decrypted_message}")

if __name__ == "__main__":
    main()
