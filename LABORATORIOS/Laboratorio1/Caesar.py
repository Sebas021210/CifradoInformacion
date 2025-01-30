# Cifrado César
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def cesar_encrypt(text, key):
    result = ''
    text = ''.join([c.lower() for c in text if c.isalpha() or c == ' '])
    for c in text:
        if c in alphabet:
            result += alphabet[(alphabet.index(c) + key) % len(alphabet)]
        else:
            result += c
    return result

def cesar_decrypt(text, key):
    result = ''
    for c in text:
        if c in alphabet:
            result += alphabet[(alphabet.index(c) - key) % len(alphabet)]
        else:
            result += c
    return result

text = 'hola mundo'
key = 3

print("Cifrado César")
encrypted = cesar_encrypt(text, key)
print(f"Mensaje cifrado: {encrypted}")
descrypted = cesar_decrypt(encrypted, key)
print(f"Mensaje descifrado: {descrypted}")
