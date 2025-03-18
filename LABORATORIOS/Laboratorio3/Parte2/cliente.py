import socket
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

HOST = "192.168.68.68"  
PUERTO = 4444 

clave = b"1234567890123456" 
iv = b"1234567890123456" 

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((HOST, PUERTO))

while True:
    mensaje = input("Escribe un mensaje para cifrar y enviar: ")
    if mensaje.lower() == "salir":
        break

    cipher = AES.new(clave, AES.MODE_CBC, iv)
    mensaje_cifrado = cipher.encrypt(pad(mensaje.encode(), AES.block_size))
    
    cliente.send(mensaje_cifrado)
    print(f" Mensaje cifrado enviado: {mensaje_cifrado.hex()}")

cliente.close()
