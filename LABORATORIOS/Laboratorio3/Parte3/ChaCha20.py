from Crypto.Cipher import ChaCha20
from Crypto.Random import get_random_bytes

# Mensaje a cifrar
text = b"Mensaje a cifrar con ChaCha20"

# Generar una clave de 256 bits y un nonce de 12 bytes
clave = get_random_bytes(32)
nonce = get_random_bytes(12)

# Cifrar con ChaCha20
cipher = ChaCha20.new(key=clave, nonce=nonce)
ciphertext = cipher.encrypt(text)

# Descifrar
cipher_dec = ChaCha20.new(key=clave, nonce=nonce)
text_descifrado = cipher_dec.decrypt(ciphertext)

print("Mensaje original: ", text.decode())
print("Cifrado ChaCha20: ", ciphertext.hex())
print("Descifrado: ", text_descifrado.decode())
