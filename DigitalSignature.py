def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    raise ValueError("No modular inverse found")

def rsa_keygen(p, q, e):
    n = p * q
    phi = (p - 1) * (q - 1)
    d = mod_inverse(e, phi)
    return (e, n), (d, n)

def rsa_sign(message, d, n):
    return pow(message, d, n)

def rsa_verify(message, signature, e, n):
    return "Authenticated" if pow(signature, e, n) == message else "Altered"

# Main code
# Main code
p = int(input("Enter prime p: "))
q = int(input("Enter prime q: "))
e = int(input("Enter public exponent e: "))

# Generate keys
public_key, private_key = rsa_keygen(p, q, e)
print("Public Key:", public_key)
print("Private Key:", private_key)

# Sign message
message = int(input("Enter message (as an integer): "))
signature = rsa_sign(message, private_key[0], private_key[1])
print("Signature:", signature)

# Verify signature
signature_to_verify = int(input("Enter signature to verify: "))
print(rsa_verify(message, signature_to_verify, public_key[0], public_key[1]))

