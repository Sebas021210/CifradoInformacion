import random

# Función para generar el keystream
def keystream(length, seed):
    random.seed(seed)
    return [random.randint(0, 255) for _ in range(length)]

# Función para cifrar con XOR
def xor_encrypt(text, key):
    text = text.encode()
    return [t ^ k for t, k in zip(text, key)]

# Función para descifrar con XOR
def xor_decrypt(ciphertext, key):
    return bytes([c ^ k for c, k in zip(ciphertext, key)]).decode()

# Ejejmplo de uso
text = "Hola Mundo"
seed = 42
key = keystream(len(text), seed)

print("-Stream Cipher")
print("Texto a cifrar:", text)
print("KeyStream:", key)

ciphertext = xor_encrypt(text, key)
print("Texto cifrado:", ciphertext)

decrypted = xor_decrypt(ciphertext, key)
print("Texto descifrado:", decrypted)
