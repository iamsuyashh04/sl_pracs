def playfair_cipher(text, key, mode):
    alphabet = 'abcdefghiklmnopqrstuvwxyz'
    key = key.lower().replace(' ', '').replace('j', 'i')
    key_square = ''.join(sorted(set(key + alphabet), key=lambda x: (key + alphabet).index(x)))
    
    def display_key_matrix():
        for i in range(5):
            print(' '.join(key_square[i*5:(i+1)*5]))

    text = text.lower().replace(' ', '').replace('j', 'i')
    if len(text) % 2 == 1:
        text += 'x'
    digraphs = [text[i:i+2] for i in range(0, len(text), 2)]
    
    def process_digraph(digraph, direction):
        a, b = digraph
        row_a, col_a = divmod(key_square.index(a), 5)
        row_b, col_b = divmod(key_square.index(b), 5)
        if row_a == row_b:
            col_a = (col_a + direction) % 5
            col_b = (col_b + direction) % 5
        elif col_a == col_b:
            row_a = (row_a + direction) % 5
            row_b = (row_b + direction) % 5
        else:
            col_a, col_b = col_b, col_a
        return key_square[row_a * 5 + col_a] + key_square[row_b * 5 + col_b]
    
    display_key_matrix()
    direction = 1 if mode == 'encrypt' else -1
    return ''.join(process_digraph(dg, direction) for dg in digraphs)

plaintext = input("Message: ").strip()
key = input("Key: ").strip()
mode = input("Mode (encrypt/decrypt): ").strip().lower()

if mode in ['encrypt', 'decrypt']:
    result = playfair_cipher(plaintext, key, mode)
    print(f"Result: {result}")
