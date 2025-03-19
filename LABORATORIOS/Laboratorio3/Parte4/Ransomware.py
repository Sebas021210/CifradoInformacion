from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import os

folder = "archivos"
key = get_random_bytes(16)
iv = get_random_bytes(16)

# Guardar la clave en un archivo
with open("clave.bin", "wb") as key_file:
    key_file.write(key)
    key_file.write(iv)

def encrypt_file(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted_data = cipher.encrypt(pad(data, AES.block_size))
    
    with open(file_path + ".enc", "wb") as f:
        f.write(encrypted_data)
    
    os.remove(file_path)

# Recorrer la carpeta y cifrar cada archivo
for file in os.listdir(folder):
    file_path = os.path.join(folder, file)
    if os.path.isfile(file_path):
        encrypt_file(file_path)

print(f"Se han cifrado los archivos en la carpeta {folder}")
