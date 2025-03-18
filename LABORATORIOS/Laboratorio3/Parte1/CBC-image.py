from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
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

# IV aleatorio para CBC
iv = get_random_bytes(AES.block_size)

# Longitud de los datos de la imagen sea múltiplo de 16
image_bytes_padded = pad(image_bytes, AES.block_size)

# Cifrar con AES en modo CBC
cipher_cbc = AES.new(key, AES.MODE_CBC, iv)
ciphertext_cbc = cipher_cbc.encrypt(image_bytes_padded)

cipher_image_data_cbc = np.frombuffer(ciphertext_cbc, dtype=np.uint8)
new_height = (img.height // 16) * 16
new_width = (img.width // 16) * 16
cipher_image_data_cbc = cipher_image_data_cbc[:new_height * new_width]
cipher_img_cbc = Image.fromarray(cipher_image_data_cbc.reshape((new_height, new_width)))

# Guardar la imagen cifrada
cipher_img_cbc.save('imagenes/tux_cbc.ppm')

# Mostrar la imagen original y la cifrada
original_img = Image.open("imagenes/tux.ppm").convert('L')
encrypted_img = Image.open("imagenes/tux_cbc.ppm")

fig, axs = plt.subplots(1, 2, figsize=(10, 5))
axs[0].imshow(original_img, cmap="gray")
axs[0].set_title("Imagen Original")
axs[0].axis("off")

axs[1].imshow(encrypted_img, cmap="gray")
axs[1].set_title("Imagen Cifrada (CBC)")
axs[1].axis("off")

plt.show()

# Guardar la comparación de las imágenes
fig.savefig("imagenes/comparison_cbc.png")
