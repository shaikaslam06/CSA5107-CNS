# CBC Mode using simplified S-DES logic
# Test: IV = 10101010 (0xAA), Key = 0111111101 (0x1FD), Plaintext = 00000001 00100011

IP = [2, 6, 3, 1, 4, 8, 5, 7]
IP_INV = [4, 1, 3, 5, 7, 2, 8, 6]

def permute(bits, permutation):
    return ''.join(bits[i - 1] for i in permutation)

def initial_permutation(bits):
    return permute(bits, IP)

def inverse_initial_permutation(bits):
    return permute(bits, IP_INV)

# Simplified fk function for demo (XOR with key)
def fk(bits, key):
    return ''.join('1' if bits[i] != key[i % len(key)] else '0' for i in range(len(bits)))

def sdes_encrypt(block, key):
    block = initial_permutation(block)
    left, right = block[:4], block[4:]
    right_new = ''.join('1' if left[i] != fk(right, key)[i] else '0' for i in range(4))
    block = right + right_new
    return inverse_initial_permutation(block)

def sdes_decrypt(block, key):
    return sdes_encrypt(block, key)  # Symmetric

def xor_bits(a, b):
    return ''.join('1' if a[i] != b[i] else '0' for i in range(len(a)))

def cbc_encrypt(plaintext_blocks, key, iv):
    ciphertext_blocks = []
    prev = iv
    for block in plaintext_blocks:
        xored = xor_bits(block, prev)
        encrypted = sdes_encrypt(xored, key)
        ciphertext_blocks.append(encrypted)
        prev = encrypted
    return ciphertext_blocks

def cbc_decrypt(ciphertext_blocks, key, iv):
    plaintext_blocks = []
    prev = iv
    for block in ciphertext_blocks:
        decrypted = sdes_decrypt(block, key)
        original = xor_bits(decrypted, prev)
        plaintext_blocks.append(original)
        prev = block
    return plaintext_blocks

# Convert integer to 8-bit binary string
def int_to_bin(n):
    return format(n, '08b')

# --- Test Data ---
plaintext_blocks = [int_to_bin(0x01), int_to_bin(0x23)]
key = '0111111101'
iv = '10101010'

# Encrypt
ciphertext_blocks = cbc_encrypt(plaintext_blocks, key, iv)
print("Ciphertext Blocks:", ciphertext_blocks)

# Decrypt
decrypted_blocks = cbc_decrypt(ciphertext_blocks, key, iv)
print("Decrypted Blocks:", decrypted_blocks)
