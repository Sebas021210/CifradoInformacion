def KSA(key):
    key_length = len(key)
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % key_length]) % 256
        S[i], S[j] = S[j], S[i]
    return S

def PRGA(S, length):
    i = 0
    j = 0
    key_stream = []
    for _ in range(length):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        key_stream.append(K)
    return key_stream

def rc4_decrypt_manual(ciphertext_hex, key_string):
    ciphertext = bytes.fromhex(ciphertext_hex)
    key = [ord(c) for c in key_string]
    S = KSA(key)
    keystream = PRGA(S, len(ciphertext))
    plaintext = bytes([c ^ k for c, k in zip(ciphertext, keystream)])
    return plaintext

flag = "b1e1389add4d7921dd4666630b6d9cef09f7534e570d96332a46574e0c762de103111f4539"
carne = "21826"

texto_descifrado = rc4_decrypt_manual(flag, carne)
print("Flag cifrada:", flag)
print("Carne:", carne)
print("Texto descifrado:", texto_descifrado.decode(errors="replace"))
