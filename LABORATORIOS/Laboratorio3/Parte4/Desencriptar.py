from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import os

folder = "archivos"

# Leer la clave almacenada
with open("clave.bin", "rb") as key_file:
    key = key_file.read(16)
    iv = key_file.read(16)

def decrypt_file(file_path):
    with open(file_path, "rb") as f:
        encrypted_data = f.read()

    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)

    # Restaurar el nombre original
    original_file = file_path.replace(".enc", "")
    with open(original_file, "wb") as f:
        f.write(decrypted_data)
    
    os.remove(file_path)

# Recorrer la carpeta y descifrar cada archivo
for file in os.listdir(folder):
    file_path = os.path.join(folder, file)
    if file.endswith(".enc") and os.path.isfile(file_path):
        decrypt_file(file_path)

print(f"Se han descifrado los archivos en la carpeta {folder}")
