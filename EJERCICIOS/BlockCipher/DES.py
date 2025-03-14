from Crypto.Cipher import DES
from os import urandom

key = urandom(8)

def read_file(input_file):
    with open(input_file, 'rb') as f:
        return f.read()

def pad_text(text):
    padding_len = 8 - (len(text) % 8)
    padding = b'x\00' * (padding_len // 2)
    if padding_len % 2 == 1:
        padding += b'x'
    return text + padding

def unpad_text(text):
    while text[-2:] == b'x\00' or text[-1:] == b'x':
        text = text[:-2] if text[-2:] == b'x\00' else text[:-1]
    return text

def encrypt(input_file):
    cipher = DES.new(key, DES.MODE_ECB)

    data = read_file(input_file)
    data = pad_text(data)
    encrypted_data = cipher.encrypt(data)

    return encrypted_data

def decrypt(encrypted_data):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_data = cipher.decrypt(encrypted_data)
    decrypted_data = unpad_text(decrypted_data)

    return decrypted_data

# Ejemplo de uso
encrypted_data = encrypt('./EJERCICIOS/BlockCipher/des.txt')
print("Mensaje cifrado:", encrypted_data)

decrypted_data = decrypt(encrypted_data)
print("\nMensaje descifrado:", decrypted_data.decode("utf-8", errors="ignore"))
