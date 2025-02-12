from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img1 = Image.open("./LABORATORIOS/Laboratorio2/imagen_decifrada.png").convert("RGB")
img2 = Image.open("./LABORATORIOS/Laboratorio2/key_xor.png").convert("RGB")

img2 = img2.resize(img1.size)
arr1 = np.array(img1)
arr2 = np.array(img2)

xor_result = np.bitwise_xor(arr1, arr2)

img_xor = Image.fromarray(xor_result)

img_xor.save("./LABORATORIOS/Laboratorio2/imagen_xor_resultado.png")

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

axes[0].imshow(img1)
axes[0].set_title("Imagen Original")
axes[0].axis("off")

axes[1].imshow(img2)
axes[1].set_title("Imagen Llave")
axes[1].axis("off")

axes[2].imshow(img_xor)
axes[2].set_title("Imagen XOR")
axes[2].axis("off")

plt.show()
