def playfair_cipher(text, key, mode):
    alphabet = 'abcdefghiklmnopqrstuvwxyz'
    key = ''.join(dict.fromkeys(key.lower().replace(' ', '').replace('j', 'i') + alphabet))
    text = text.lower().replace(' ', '').replace('j', 'i')
    text += 'x' * (len(text) % 2)  # Padding if necessary
    digraphs = [text[i:i+2] for i in range(0, len(text), 2)]

    def process_digraph(digraph, direction):
        a, b = digraph
        row_a, col_a = divmod(key.index(a), 5)
        row_b, col_b = divmod(key.index(b), 5)
        if row_a == row_b:
            col_a, col_b = (col_a + direction) % 5, (col_b + direction) % 5
        elif col_a == col_b:
            row_a, row_b = (row_a + direction) % 5, (row_b + direction) % 5
        else:
            col_a, col_b = col_b, col_a
        return key[row_a * 5 + col_a] + key[row_b * 5 + col_b]

    direction = 1 if mode == 'encrypt' else -1
    return ''.join(process_digraph(dg, direction) for dg in digraphs)

# Main code
plaintext = input("Message: ").strip()
key = input("Key: ").strip()
mode = input("Mode (encrypt/decrypt): ").strip().lower()

if mode in ['encrypt', 'decrypt']:
    print("Result:", playfair_cipher(plaintext, key, mode))
