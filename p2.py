import string

def generate_cipher_alphabet():
    # You can define your own mapping or shuffle letters randomly
    # Here we use a fixed example mapping
    return "QWERTYUIOPASDFGHJKLZXCVBNM"  # Example cipher alphabet

def encrypt(plaintext, cipher_alphabet):
    alphabet = string.ascii_uppercase
    mapping = {alphabet[i]: cipher_alphabet[i] for i in range(26)}
    
    ciphertext = ""
    for char in plaintext.upper():
        if char in mapping:
            ciphertext += mapping[char]
        else:
            ciphertext += char
    return ciphertext

def decrypt(ciphertext, cipher_alphabet):
    alphabet = string.ascii_uppercase
    reverse_mapping = {cipher_alphabet[i]: alphabet[i] for i in range(26)}
    
    plaintext = ""
    for char in ciphertext.upper():
        if char in reverse_mapping:
            plaintext += reverse_mapping[char]
        else:
            plaintext += char
    return plaintext

# Example usage
cipher_alphabet = generate_cipher_alphabet()
print("Cipher Alphabet:", cipher_alphabet)

plaintext = input("Enter the text to encrypt: ")
ciphertext = encrypt(plaintext, cipher_alphabet)
print("Encrypted text:", ciphertext)

decrypted_text = decrypt(ciphertext, cipher_alphabet)
print("Decrypted text:", decrypted_text)
