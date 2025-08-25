# CTR Mode using simplified S-DES logic
# Test: Counter starts at 00000000, Key = 0111111101, Plaintext = 000000010000001000000100
# Expected Ciphertext = 001110000100111100110010

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

def xor_bits(a, b):
    return ''.join('1' if a[i] != b[i] else '0' for i in range(len(a)))

def int_to_bin(n):
    return format(n, '08b')

def ctr_mode_encrypt(plaintext_bits, key, initial_counter):
    blocks = [plaintext_bits[i:i+8] for i in range(0, len(plaintext_bits), 8)]
    ciphertext_blocks = []
    counter = initial_counter
    for block in blocks:
        keystream = sdes_encrypt(int_to_bin(counter), key)
        cipher_block = xor_bits(block, keystream)
        ciphertext_blocks.append(cipher_block)
        counter += 1
    return ''.join(ciphertext_blocks)

def ctr_mode_decrypt(ciphertext_bits, key, initial_counter):
    return ctr_mode_encrypt(ciphertext_bits, key, initial_counter)  # Same process for CTR

# --- Test Data ---
plaintext = '000000010000001000000100'  # 3 blocks of 8 bits
key = '0111111101'
initial_counter = 0  # starts at 00000000

# Encrypt
ciphertext = ctr_mode_encrypt(plaintext, key, initial_counter)
print("Ciphertext:", ciphertext)

# Decrypt
decrypted = ctr_mode_decrypt(ciphertext, key, initial_counter)
print("Decrypted:", decrypted)
