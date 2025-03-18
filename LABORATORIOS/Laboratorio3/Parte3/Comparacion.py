import time
from Crypto.Cipher import AES
from Crypto.Cipher import ChaCha20
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import os

text = get_random_bytes(1024 * 1024)

# Claves y configuración
key_aes = os.urandom(16)
key_chacha = get_random_bytes(32)
nonce_chacha = get_random_bytes(12)
iv_aes = get_random_bytes(AES.block_size)

# Prueba de ChaCha20
inicio = time.time()
cipher_chacha = ChaCha20.new(key=key_chacha, nonce=nonce_chacha)
ciphertext_chacha = cipher_chacha.encrypt(text)
tiempo_chacha = time.time() - inicio

# Prueba de AES en modo CBC
inicio = time.time()
cipher_aes = AES.new(key_aes, AES.MODE_CBC, iv_aes)
ciphertext_aes = cipher_aes.encrypt(pad(text, AES.block_size))
tiempo_aes = time.time() - inicio

print(f"Tiempo de cifrado ChaCha20: {tiempo_chacha:.6f} segundos")
print(f"Tiempo de cifrado AES (CBC): {tiempo_aes:.6f} segundos")
