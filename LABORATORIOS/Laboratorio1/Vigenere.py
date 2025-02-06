# Cifrado Vigenère
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def vigenere_encrypt(text, key):
    result = ''
    text = ''.join([c.lower() for c in text if c.isalpha() or c == ' '])
    for c in range(len(text)):
        if text[c] in alphabet:
            result += alphabet[(alphabet.index(text[c]) + alphabet.index(key[c % len(key)])) % len(alphabet)]
        else:
            result += text[c]
    #print(f'Mensaje cifrado: {result}')
    return result

def vigenere_decrypt(text, key):
    result = ''
    for c in range(len(text)):
        if text[c] in alphabet:
            result += alphabet[(alphabet.index(text[c]) - alphabet.index(key[c % len(key)]) + len(alphabet) ) % len(alphabet)]
        else:
            result += text[c]
    #print(f'Mensaje descifrado: {result}')
    return result
