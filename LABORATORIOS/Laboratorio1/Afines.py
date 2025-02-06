# Cifrado Afines
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def modInverse(a, m) :
    for i in range(1, m) :
        if ((a * i) % m == 1) :
            return i
    raise ValueError(f"{a} no tiene inverso modular módulo {m}")

def afine_encrypt(text, a, b):
    result = ''
    text = ''.join([c.lower() for c in text if c.isalpha() or c == ' '])
    for c in text:
        if c in alphabet:
            result += alphabet[(a * alphabet.index(c) + b) % len(alphabet)]
        else:
            result += c
    #print(f'Mensaje cifrado: {result}')
    return result

def afine_decrypt(text, a, b):
    result = ''
    aInverse = modInverse(a, len(alphabet))
    for c in text:
        if c in alphabet:
            result += alphabet[(aInverse * (alphabet.index(c) - b)) % len(alphabet)]
        else:
            result += c
    #print(f'Mensaje descifrado: {result}')
    return result
