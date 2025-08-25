def generate_matrix(key):
    key = key.upper().replace("J", "I")
    matrix = []
    used = set()

    for ch in key:
        if ch.isalpha() and ch not in used:
            matrix.append(ch)
            used.add(ch)

    for ch in "ABCDEFGHIKLMNOPQRSTUVWXYZ":  # J is merged with I
        if ch not in used:
            matrix.append(ch)

    return [matrix[i:i+5] for i in range(0, 25, 5)]


def find_position(matrix, ch):
    if ch == 'J':
        ch = 'I'
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == ch:
                return i, j
    return None, None


def decrypt_playfair(ciphertext, key):
    matrix = generate_matrix(key)
    ciphertext = ciphertext.replace(" ", "").upper()
    plaintext = ""

    # Process in pairs
    for i in range(0, len(ciphertext), 2):
        a, b = ciphertext[i], ciphertext[i+1]
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)

        if row1 == row2:  # Same row
            plaintext += matrix[row1][(col1 - 1) % 5]
            plaintext += matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:  # Same column
            plaintext += matrix[(row1 - 1) % 5][col1]
            plaintext += matrix[(row2 - 1) % 5][col2]
        else:  # Rectangle swap
            plaintext += matrix[row1][col2]
            plaintext += matrix[row2][col1]

    return plaintext


# --- Main ---
ciphertext = """KXJEY UREBE ZWEHE WRYTU HEYFS
KREHE GOYFI WTTTU OLKSY CAJPO
BOTEI ZONTX BYBNT GONEY CUZWR
GDSON SXBOU YWRHE BAAHY USEDQ"""

key = "PLAYFAIR"  # Common keyword for Playfair
ciphertext = ciphertext.replace("\n", "").replace(" ", "")
decrypted_text = decrypt_playfair(ciphertext, key)

print("Decrypted Text:", decrypted_text)
