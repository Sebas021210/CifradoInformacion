import socket
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

HOST = "0.0.0.0"  
PUERTO = 4444  

clave = b"1234567890123456" 
iv = b"1234567890123456"  # 16 bytes

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((HOST, PUERTO))
servidor.listen(1)

print(f" Servidor esperando conexiones en {HOST}:{PUERTO}...")

conn, addr = servidor.accept()
print(f"Conexión establecida con {addr}")

while True:
    datos_cifrados = conn.recv(1024)
    if not datos_cifrados:
        break

    cipher = AES.new(clave, AES.MODE_CBC, iv)
    mensaje_descifrado = unpad(cipher.decrypt(datos_cifrados), AES.block_size)
    
    print(f" Mensaje recibido: {mensaje_descifrado.decode()}")

conn.close()
servidor.close()
