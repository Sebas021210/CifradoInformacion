# Cifrado Afines
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def modInverse(a, m) :
    for i in range(1, m) :
        if ((a * i) % m == 1) :
            return i
    raise ValueError(f"{a} no tiene inverso modular módulo {m}")

def afine_encrypt(text, a, b):
    result = ''
    for c in text:
        if c in alphabet:
            result += alphabet[(a * alphabet.index(c) + b) % len(alphabet)]
        else:
            result += c
    return result

def afine_decrypt(text, a, b):
    result = ''
    aInverse = modInverse(a, len(alphabet))
    for c in text:
        if c in alphabet:
            result += alphabet[(aInverse * (alphabet.index(c) - b)) % len(alphabet)]
        else:
            result += c
    return result

text = 'hola mundo'
a = 3
b = 8

print("Cifrado Afines")
encrypted = afine_encrypt(text, a, b)
print(f"Mensaje cifrado: {encrypted}")
descrypted = afine_decrypt(encrypted, a, b)
print(f"Mensaje descifrado: {descrypted}")
