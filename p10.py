# Playfair Cipher Encryption using a given matrix

# 5x5 Matrix given in the question
playfair_matrix = [
    ['M', 'F', 'H', 'I', 'K'],
    ['U', 'N', 'O', 'P', 'Q'],
    ['Z', 'V', 'W', 'X', 'Y'],
    ['E', 'L', 'A', 'R', 'G'],
    ['D', 'S', 'T', 'B', 'C']
]

SIZE = 5

def format_plaintext(text):
    # Remove non-alphabetic characters and convert to uppercase
    text = ''.join([ch.upper() for ch in text if ch.isalpha()])

    # Insert 'X' between duplicate letters and pad with X if odd length
    formatted = []
    i = 0
    while i < len(text):
        formatted.append(text[i])
        if i + 1 < len(text) and text[i] == text[i + 1]:
            formatted.append('X')
        i += 1
    if len(formatted) % 2 != 0:
        formatted.append('X')
    return ''.join(formatted)

def find_position(ch):
    if ch == 'J':  # Treat J as I
        ch = 'I'
    for i in range(SIZE):
        for j in range(SIZE):
            if playfair_matrix[i][j] == ch:
                return i, j
    return None

def encrypt_playfair(plaintext):
    ciphertext = ''
    for i in range(0, len(plaintext), 2):
        a = plaintext[i]
        b = plaintext[i + 1]
        row1, col1 = find_position(a)
        row2, col2 = find_position(b)

        if row1 == row2:
            ciphertext += playfair_matrix[row1][(col1 + 1) % SIZE]
            ciphertext += playfair_matrix[row2][(col2 + 1) % SIZE]
        elif col1 == col2:
            ciphertext += playfair_matrix[(row1 + 1) % SIZE][col1]
            ciphertext += playfair_matrix[(row2 + 1) % SIZE][col2]
        else:
            ciphertext += playfair_matrix[row1][col2]
            ciphertext += playfair_matrix[row2][col1]
    return ciphertext

# Main
message = "Must see you over Cadogan West. Coming at once."
formatted = format_plaintext(message)
ciphertext = encrypt_playfair(formatted)

print("Original Message:", message)
print("Formatted Message:", formatted)
print("Encrypted Ciphertext:", ciphertext)
