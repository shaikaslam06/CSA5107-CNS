def caesar_cipher_encrypt(text, k):
    result = ""
    for char in text:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift + k) % 26 + shift)
        else:
            result += char
    return result

def caesar_cipher_decrypt(cipher_text, k):
    return caesar_cipher_encrypt(cipher_text, -k)

# Example usage
text = input("Enter the text: ")
for k in range(1, 26):
    encrypted = caesar_cipher_encrypt(text, k)
    decrypted = caesar_cipher_decrypt(encrypted, k)
    print(f"\nShift: {k}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
