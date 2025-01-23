# Cifrado de Cesar
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(text, key):
    result = ''
    for c in text:
        if c in alphabet:
            result += alphabet[(alphabet.index(c) + key) % len(alphabet)]
        else:
            result += c
    return result

def decrypt(text, key):
    result = ''
    for c in text:
        if c in alphabet:
            result += alphabet[(alphabet.index(c) - key) % len(alphabet)]
        else:
            result += c
    return result

text = 'hola mundo'
key = 3

print('Cifrado de Cesar')
print(f'Mensaje original: {text}')

encrypted = encrypt(text, key)
print(f'Mensaje cifrado: {encrypted}')

decrypted = decrypt(encrypted, key)
print(f'Mensaje descifrado: {decrypted}')
