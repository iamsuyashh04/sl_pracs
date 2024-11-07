def rsa_sign(p, q, e, message):
    n = p * q
    phi = (p - 1) * (q - 1)
    d = pow(e, -1, phi)  # Find the private key 'd'
    signature = pow(message, d, n)  # Sign the integer message
    return signature, (e, n), (d, n)  # Return signature, public key, and private key
def rsa_verify(signature, message, e, n):
    verified_message = pow(signature, e, n)  # Verify the signature
    return verified_message == message  # Return True if verified
p = int(input("Enter prime p: "))
q = int(input("Enter prime q: "))
e = int(input("Enter public key exponent e: "))
message = int(input("Enter message to sign (as an integer): "))
signature, public_key, private_key = rsa_sign(p, q, e, message)
print("Public Key (e, n):", public_key)
print("Private Key (d, n):", private_key)
print("Digital Signature (S):", signature)
print("Verification:", rsa_verify(signature, message, public_key[0], public_key[1]))
