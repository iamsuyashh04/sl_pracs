def mod_inverse(e, phi):
    x, y = 0, 1
    while e:
        x, y = y - (phi // e) * x, x
        phi, e = e, phi % e
    return y % phi

def rsa_keygen(p, q, e):
    n, phi = p * q, (p - 1) * (q - 1)
    return (e, n), (mod_inverse(e, phi), n)

def rsa_sign(msg, d, n):
    return pow(msg, d, n)

def rsa_verify(msg, sig, e, n):
    return "Authenticated" if pow(sig, e, n) == msg else "Altered"

# Main code
p, q, e = (int(input(f"Enter {var}: ")) for var in ["p", "q", "e"])
pub_key, priv_key = rsa_keygen(p, q, e)
print(f"Public Key: {pub_key}, Private Key: {priv_key}")

msg = int(input("Enter message to sign: "))
sig = rsa_sign(msg, priv_key[0], priv_key[1])
print(f"Signature: {sig}")

# Verification
sig = int(input("Enter signature to verify: "))
print(rsa_verify(msg, sig, pub_key[0], pub_key[1]))
