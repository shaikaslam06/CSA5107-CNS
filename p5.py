import math
import string

# Compute modular inverse of 'a' under mod 26
def mod_inverse(a):
    a = a % 26
    for x in range(1, 26):
        if (a * x) % 26 == 1:
            return x
    return None  # No inverse means invalid 'a'

def affine_encrypt(text, a, b):
    if math.gcd(a, 26) != 1:
        raise ValueError("Invalid key: 'a' must be coprime to 26")
    
    result = ""
    for char in text.upper():
        if char.isalpha():
            p = ord(char) - ord('A')
            c = (a * p + b) % 26
            result += chr(c + ord('A'))
        else:
            result += char
    return result

def affine_decrypt(ciphertext, a, b):
    if math.gcd(a, 26) != 1:
        raise ValueError("Invalid key: 'a' must be coprime to 26")
    
    a_inv = mod_inverse(a)
    if a_inv is None:
        raise ValueError("No modular inverse found for 'a'")
    
    result = ""
    for char in ciphertext.upper():
        if char.isalpha():
            c = ord(char) - ord('A')
            p = (a_inv * (c - b + 26)) % 26
            result += chr(p + ord('A'))
        else:
            result += char
    return result

# Example usage
plaintext = input("Enter plaintext: ")
a = int(input("Enter value of a (must be coprime with 26): "))
b = int(input("Enter value of b: "))

ciphertext = affine_encrypt(plaintext, a, b)
print("\nEncrypted text:", ciphertext)

decrypted_text = affine_decrypt(ciphertext, a, b)
print("Decrypted text:", decrypted_text)
