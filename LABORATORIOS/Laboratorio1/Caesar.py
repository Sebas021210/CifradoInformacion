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
    print(f'Mensaje cifrado: {result}')
    return result

def cesar_decrypt(text, key):
    result = ''
    for c in text:
        if c in alphabet:
            result += alphabet[(alphabet.index(c) - key) % len(alphabet)]
        else:
            result += c
    print(f'Mensaje descifrado: {result}')
    return result
