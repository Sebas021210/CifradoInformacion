# Cifrado Vigenère
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def vigenere_encrypt(text, key):
    result = ''
    for c in range(len(text)):
        if text[c] in alphabet:
            result += alphabet[(alphabet.index(text[c]) + alphabet.index(key[c % len(key)])) % len(alphabet)]
        else:
            result += text[c]
    return result

def vigenere_decrypt(text, key):
    result = ''
    for c in range(len(text)):
        if text[c] in alphabet:
            result += alphabet[(alphabet.index(text[c]) - alphabet.index(key[c % len(key)]) + len(alphabet) ) % len(alphabet)]
        else:
            result += text[c]
    return result

text = 'hola mundo'
key = 'crypto'

print("Cifrado Vigenère")
encrypted = vigenere_encrypt(text, key)
print(f"Mensaje cifrado: {encrypted}")
descrypted = vigenere_decrypt(encrypted, key)
print(f"Mensaje descifrado: {descrypted}")
