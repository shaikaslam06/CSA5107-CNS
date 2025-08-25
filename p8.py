import string

def generate_cipher_alphabet(keyword):
    keyword = keyword.upper()
    seen = set()
    cipher = ""

    # Add keyword letters first
    for ch in keyword:
        if ch.isalpha() and ch not in seen:
            cipher += ch
            seen.add(ch)

    # Add remaining letters
    for ch in string.ascii_uppercase:
        if ch not in seen:
            cipher += ch

    return cipher

def encrypt(plaintext, cipher):
    alphabet = string.ascii_uppercase
    mapping = {alphabet[i]: cipher[i] for i in range(26)}
    
    encrypted = ""
    for ch in plaintext:
        if ch.isalpha():
            enc = mapping[ch.upper()]
            encrypted += enc.lower() if ch.islower() else enc
        else:
            encrypted += ch
    return encrypted

def decrypt(ciphertext, cipher):
    alphabet = string.ascii_uppercase
    reverse_mapping = {cipher[i]: alphabet[i] for i in range(26)}
    
    decrypted = ""
    for ch in ciphertext:
        if ch.isalpha():
            dec = reverse_mapping[ch.upper()]
            decrypted += dec.lower() if ch.islower() else dec
        else:
            decrypted += ch
    return decrypted

# Example usage
keyword = input("Enter keyword: ")
cipher_alphabet = generate_cipher_alphabet(keyword)
print("Cipher Alphabet:", cipher_alphabet)

plaintext = input("Enter plaintext: ")
encrypted_text = encrypt(plaintext, cipher_alphabet)
print("Encrypted text:", encrypted_text)

ciphertext = input("Enter ciphertext to decrypt: ")
decrypted_text = decrypt(ciphertext, cipher_alphabet)
print("Decrypted text:", decrypted_text)
