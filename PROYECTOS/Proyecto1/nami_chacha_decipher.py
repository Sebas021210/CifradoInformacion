from Crypto.Cipher import ChaCha20

def generate_key_nonce(user_id):
    key = (user_id.encode() * 32)[:32]
    nonce = (user_id.encode() * 8)[:8]
    return key, nonce

def chacha20_decrypt(ciphertext_hex, user_id):
    key, nonce = generate_key_nonce(user_id=user_id)
    cipher = ChaCha20.new(key=key, nonce=nonce)
    ciphertext = bytes.fromhex(ciphertext_hex)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext.decode(errors="replace")

flag = "e0f51dd075c06ca667ffb66f73b0b0fce0d16e7470a9a538d7533b562d2cd6151a49bd7e0e"
carne = "21826"

texto_descifrado = chacha20_decrypt(flag, carne)
print("Flag cifrada:", flag)
print("Carne:", carne)
print("Texto descifrado:", texto_descifrado)
