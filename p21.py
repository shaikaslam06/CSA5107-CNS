from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# --- Padding function ---
def pad(message, block_size=16):
    bitstring = ''.join(format(ord(c), '08b') for c in message)
    bitstring += '1'  # Add a single '1' bit
    while len(bitstring) % (block_size * 8) != 0:
        bitstring += '0'  # Add zero bits to complete block
    
    # Convert bitstring back to bytes
    padded_bytes = int(bitstring, 2).to_bytes(len(bitstring) // 8, 'big')
    return padded_bytes

# --- Unpad function ---
def unpad(data):
    bitstring = ''.join(format(byte, '08b') for byte in data)
    bitstring = bitstring.rstrip('0')  # Remove trailing zeros
    if bitstring[-1] == '1':
        bitstring = bitstring[:-1]  # Remove the last '1' bit
    # Convert back to original message
    chars = [bitstring[i:i+8] for i in range(0, len(bitstring), 8)]
    return ''.join(chr(int(c, 2)) for c in chars)

# --- AES ECB Mode ---
def aes_ecb_encrypt(plaintext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(plaintext)

def aes_ecb_decrypt(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.decrypt(ciphertext)

# --- AES CBC Mode ---
def aes_cbc_encrypt(plaintext, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return cipher.encrypt(plaintext)

def aes_cbc_decrypt(ciphertext, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return cipher.decrypt(ciphertext)

# --- AES CFB Mode ---
def aes_cfb_encrypt(plaintext, key, iv):
    cipher = AES.new(key, AES.MODE_CFB, iv, segment_size=128)
    return cipher.encrypt(plaintext)

def aes_cfb_decrypt(ciphertext, key, iv):
    cipher = AES.new(key, AES.MODE_CFB, iv, segment_size=128)
    return cipher.decrypt(ciphertext)

# --- Main Program ---
message = "HelloAESDemo"
key = get_random_bytes(16)  # 128-bit AES key
iv = get_random_bytes(16)   # Initialization vector

print("Original Message:", message)

# Padding the message
padded_message = pad(message)
print("Padded Length:", len(padded_message), "bytes")

# ECB
ecb_cipher = aes_ecb_encrypt(padded_message, key)
print("\nECB Encrypted:", ecb_cipher.hex())
ecb_plain = aes_ecb_decrypt(ecb_cipher, key)
print("ECB Decrypted:", unpad(ecb_plain))

# CBC
cbc_cipher = aes_cbc_encrypt(padded_message, key, iv)
print("\nCBC Encrypted:", cbc_cipher.hex())
cbc_plain = aes_cbc_decrypt(cbc_cipher, key, iv)
print("CBC Decrypted:", unpad(cbc_plain))

# CFB
cfb_cipher = aes_cfb_encrypt(padded_message, key, iv)
print("\nCFB Encrypted:", cfb_cipher.hex())
cfb_plain = aes_cfb_decrypt(cfb_cipher, key, iv)
print("CFB Decrypted:", unpad(cfb_plain))
