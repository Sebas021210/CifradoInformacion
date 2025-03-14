from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from os import urandom

key = urandom(32)

def read_file(input_file):
    with open(input_file, 'rb') as f:
        return f.read()

def write_file(output_file, data):
    with open(output_file, 'wb') as f:
        f.write(data)

def encrypt_aes_ecb(input_file, output_file):
    cipher = AES.new(key, AES.MODE_ECB)

    data = read_file(input_file)
    padded_data = pad(data, AES.block_size)
    encrypted_data = cipher.encrypt(padded_data)

    write_file(output_file, encrypted_data)
    
def decrypt_aes_ecb(input_file, output_file):
    cipher = AES.new(key, AES.MODE_ECB)

    encrypted_data = read_file(input_file)
    decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)

    write_file(output_file, decrypted_data)

def encrypt_aes_cbc(input_file, output_file):
    iv = urandom(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)

    data = read_file(input_file)
    padded_data = pad(data, AES.block_size)
    encrypted_data = iv + cipher.encrypt(padded_data)

    write_file(output_file, encrypted_data)

def decrypt_aes_cbc(input_file, output_file):
    encrypted_data = read_file(input_file)
    iv = encrypted_data[:16] 
    encrypted_data = encrypted_data[16:] 

    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)

    write_file(output_file, decrypted_data)

# Ejemplo de uso
input_image = "./EJERCICIOS/BlockCipher/aes.png"

# Cifrar y descifrar con ECB
encrypt_aes_ecb(input_image, "./EJERCICIOS/BlockCipher/output/ecb_encrypted.png")
decrypt_aes_ecb("./EJERCICIOS/BlockCipher/output/ecb_encrypted.png", "./EJERCICIOS/BlockCipher/output/ecb_decrypted.png")

# Cifrar y descifrar con CBC
encrypt_aes_cbc(input_image, "./EJERCICIOS/BlockCipher/output/cbc_encrypted.png")
decrypt_aes_cbc("./EJERCICIOS/BlockCipher/output/cbc_encrypted.png", "./EJERCICIOS/BlockCipher/output/cbc_decrypted.png")
