import math

def extended_gcd(a, b):
    """Return (x, y, gcd) for a*x + b*y = gcd(a, b)."""
    if b == 0:
        return (1, 0, a)
    x1, y1, g = extended_gcd(b, a % b)
    return (y1, x1 - (a // b) * y1, g)

def modinv(a, m):
    """Find modular inverse of a mod m."""
    x, y, g = extended_gcd(a, m)
    if g != 1:
        return None
    return x % m

def rsa_attack_with_common_factor(n, e, m_block):
    # Step 1: Compute gcd
    g = math.gcd(m_block, n)
    if g == 1:
        print("No common factor found. Attack fails.")
        return
    p = g
    q = n // g
    print(f"Found factor: p = {p}, q = {q}")
    
    # Step 2: Compute phi(n)
    phi = (p - 1) * (q - 1)
    
    # Step 3: Compute private key d
    d = modinv(e, phi)
    print(f"Private key d = {d}")
    
    return p, q, d

# Example:
n = 3599        # RSA modulus (p * q)
e = 31          # Public exponent
m_block = 59    # Assume one plaintext block shares a factor with n

rsa_attack_with_common_factor(n, e, m_block)
