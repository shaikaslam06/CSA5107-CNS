def generate_key(text, key):
    key = key.upper()
    if len(key) >= len(text):
        return key[:len(text)]
    else:
        return (key * (len(text) // len(key) + 1))[:len(text)]

def encrypt(plaintext, key):
    plaintext = plaintext.upper()
    key = generate_key(plaintext, key)
    ciphertext = ""
    
    for p, k in zip(plaintext, key):
        if p.isalpha():
            shift = ord(k) - ord('A')
            ciphertext += chr((ord(p) - ord('A') + shift) % 26 + ord('A'))
        else:
            ciphertext += p
    return ciphertext

def decrypt(ciphertext, key):
    ciphertext = ciphertext.upper()
    key = generate_key(ciphertext, key)
    plaintext = ""
    
    for c, k in zip(ciphertext, key):
        if c.isalpha():
            shift = ord(k) - ord('A')
            plaintext += chr((ord(c) - ord('A') - shift + 26) % 26 + ord('A'))
        else:
            plaintext += c
    return plaintext

# Example usage
plaintext = input("Enter plaintext: ")
key = input("Enter key: ")

ciphertext = encrypt(plaintext, key)
print("\nEncrypted Text:", ciphertext)

decrypted_text = decrypt(ciphertext, key)
print("Decrypted Text:", decrypted_text)
