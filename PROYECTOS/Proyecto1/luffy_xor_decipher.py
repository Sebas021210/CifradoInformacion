flag = "747d79756951555b0b04535408035753085953040b075e0654545700015203010c51005005"
carne = "21826"

def xor_decipher(flag, key):
    cipher_bytes = bytes.fromhex(flag)
    key_bytes = key.encode()
    plain_bytes = bytes([cipher_bytes[i] ^ key_bytes[i % len(key_bytes)] for i in range(len(cipher_bytes))])
    
    return plain_bytes.decode(errors="replace")

texto_descifrado = xor_decipher(flag, carne)
print("Flag:", flag)
print("Carne:", carne)
print("Texto descifrado:", texto_descifrado)
