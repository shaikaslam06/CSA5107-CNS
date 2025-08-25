# rsa_private_key.py
import math

def factor_n(n):
    """Simple trial-division factoring (sufficient for small n)."""
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return i, n // i
    return None, None

def extended_gcd(a, b):
    """Return (x, y, g) such that a*x + b*y = g = gcd(a,b)."""
    if b == 0:
        return (1, 0, a)
    x1, y1, g = extended_gcd(b, a % b)
    return (y1, x1 - (a // b) * y1, g)

def modinv(a, m):
    """Modular inverse of a mod m using extended Euclid (returns None if no inverse)."""
    x, y, g = extended_gcd(a, m)
    if g != 1:
        return None
    return x % m

def main():
    e = 31
    n = 3599

    p, q = factor_n(n)
    if p is None:
        print("Failed to factor n")
        return

    phi = (p - 1) * (q - 1)
    d = modinv(e, phi)

    print("Factoring n:")
    print(" p =", p)
    print(" q =", q)
    print("phi(n) =", phi)
    print("Public key: (e, n) =", (e, n))
    print("Private key d =", d)
    # verification
    print("Check: (e * d) % phi == 1 ->", (e * d) % phi == 1)

    # optional small test: encrypt/decrypt an integer message m < n
    m = 42
    c = pow(m, e, n)
    m_recov = pow(c, d, n)
    print(f"Test: m={m}, ciphertext={c}, decrypted={m_recov}")

if __name__ == "__main__":
    main()
