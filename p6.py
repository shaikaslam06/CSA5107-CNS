import math

# Modular inverse
def mod_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

# Affine decrypt
def affine_decrypt(ciphertext, a, b):
    a_inv = mod_inverse(a, 26)
    if a_inv is None:
        raise ValueError("No modular inverse for a")
    plaintext = ""
    for char in ciphertext.upper():
        if char.isalpha():
            c = ord(char) - ord('A')
            p = (a_inv * (c - b + 26)) % 26
            plaintext += chr(p + ord('A'))
        else:
            plaintext += char
    return plaintext

# Given info
cipher_most_freq = 'B'
second_freq = 'U'
plain_guess_e = 'E'
plain_guess_t = 'T'

# Numeric values
c1, p1 = ord(cipher_most_freq) - 65, ord(plain_guess_e) - 65
c2, p2 = ord(second_freq) - 65, ord(plain_guess_t) - 65

# Solve equations:
# (a * p1 + b) % 26 = c1
# (a * p2 + b) % 26 = c2
a = ((c1 - c2) * mod_inverse((p1 - p2) % 26, 26)) % 26
b = (c1 - a * p1) % 26

print(f"Calculated keys: a = {a}, b = {b}")

ciphertext = input("Enter the ciphertext: ")
plaintext = affine_decrypt(ciphertext, a, b)
print("Decrypted text:", plaintext)
