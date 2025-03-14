from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad, unpad
from os import urandom

key = DES3.adjust_key_parity(urandom(24))
vector = urandom(8)

def read_file(input_file):
    with open(input_file, 'rb') as f:
        return f.read()

def encrypt(input_file):
    cipher = DES3.new(key, DES3.MODE_CBC, vector)

    data = read_file(input_file)
    padded_data = pad(data, DES3.block_size)
    encrypted_data = cipher.encrypt(padded_data)

    return encrypted_data

def decrypt(encrypted_data):
    cipher = DES3.new(key, DES3.MODE_CBC, vector)
    decrypted_data = cipher.decrypt(encrypted_data)
    unpadded_data = unpad(decrypted_data, DES3.block_size)

    return unpadded_data

# Ejemplo de uso
encrypted_data = encrypt('./EJERCICIOS/BlockCipher/3des.txt')
print("Mensaje cifrado:", encrypted_data)

decrypted_data = decrypt(encrypted_data)
print("\nMensaje descifrado:", decrypted_data.decode("utf-8", errors="ignore"))
