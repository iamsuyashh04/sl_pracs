def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    x, y = 0, 1
    while e:
        x, y = y - (phi // e) * x, x
        phi, e = e, phi % e
    return y % phi

def rsa_keygen(p, q, e):
    n, phi = p * q, (p - 1) * (q - 1)
    d = mod_inverse(e, phi)
    return (e, n), (d, n)

def rsa_sign(message, d, n):
    return pow(message, d, n)

def rsa_verify(message, signature, e, n):
    return "Authenticated" if pow(signature, e, n) == message else "Altered"

# Main code
p, q, e = (int(input(f"Enter {var}: ")) for var in ["p", "q", "e"])
public_key, private_key = rsa_keygen(p, q, e)
print(f"Public Key: {public_key}, Private Key: {private_key}")

message = int(input("Enter message: "))
signature = rsa_sign(message, private_key[0], private_key[1])
print(f"Signature: {signature}")

# Verification
signature = int(input("Enter signature to verify: "))
print(rsa_verify(message, signature, public_key[0], public_key[1]))
