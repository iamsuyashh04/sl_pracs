def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(e, phi_n):
    x, y, gcd = 0, 1, phi_n
    while e:
        x, y = y - (phi_n // e) * x, x
        phi_n, e = e, phi_n % e
    return y % gcd

def rsa_keygen(p, q, e):
    n, phi_n = p * q, (p - 1) * (q - 1)
    d = mod_inverse(e, phi_n)
    return (e, n), (d, n)

def rsa_sign(message, d, n):
    return pow(message, d, n)

def rsa_verify(message, S, e, n):
    return "Authenticated" if pow(S, e, n) == message else "Altered"

def main():
    p, q, e = int(input("Enter p: ")), int(input("Enter q: ")), int(input("Enter e: "))
    public_key, private_key = rsa_keygen(p, q, e)
    print(f"Public Key: {public_key}, Private Key: {private_key}")
    
    message = int(input("Enter message: "))
    S = rsa_sign(message, private_key[0], private_key[1])
    print(f"Signature: {S}")

    S = int(input("Enter signature: "))
    print(rsa_verify(message, S, public_key[0], public_key[1]))

if __name__ == "__main__":
    main()
