from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os

image_path = 'imagenes/tux.ppm'
img = Image.open(image_path).convert('L')

image_data = np.array(img)
image_bytes = image_data.tobytes()

# Clave AES de 16 bytes
key = os.urandom(16)

# Longitud de los datos de la imagen sea múltiplo de 16
image_bytes_padded = pad(image_bytes, AES.block_size)

# Cifrado AES en modo ECB
cipher = AES.new(key, AES.MODE_ECB)
ciphertext = cipher.encrypt(image_bytes_padded)

cipher_image_data = np.frombuffer(ciphertext, dtype=np.uint8)
new_height = (img.height // 16) * 16
new_width = (img.width // 16) * 16
cipher_image_data = cipher_image_data[:new_height * new_width]
cipher_img = Image.fromarray(cipher_image_data.reshape((new_height, new_width)))

# Guardar la imagen cifrada
cipher_img.save('imagenes/tux_ecb.ppm')

# Mostrar la imagen original y la cifrada
original_img = Image.open("imagenes/tux.ppm").convert('L')
encrypted_img = Image.open("imagenes/tux_ecb.ppm")

fig, axs = plt.subplots(1, 2, figsize=(10, 5))
axs[0].imshow(original_img, cmap="gray")
axs[0].set_title("Imagen Original")
axs[0].axis("off")

axs[1].imshow(encrypted_img, cmap="gray")
axs[1].set_title("Imagen Cifrada (ECB)")
axs[1].axis("off")

plt.show()

# Guardar la comparación de las imágenes
fig.savefig("imagenes/comparison_ecb.png")
