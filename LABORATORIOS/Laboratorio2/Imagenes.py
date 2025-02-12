import base64
import Base64_XOR

key = "cifrados_2025"

with open("./LABORATORIOS/Laboratorio2/imagen_xor.png", "rb") as img_file:
    image_bytes = img_file.read()

base64_encoded = base64.b64encode(image_bytes).decode()
image_bytes = Base64_XOR.base64_to_binary(base64_encoded)

key_bytes = Base64_XOR.text_to_binary(key)

xor_result = Base64_XOR.xor(image_bytes, key_bytes)

base64_decoded = Base64_XOR.binary_to_base64(xor_result)
image_bytes_decoded = base64.b64decode(base64_decoded)

with open("./LABORATORIOS/Laboratorio2/imagen_decifrada.png", "wb") as img_file:
    img_file.write(image_bytes_decoded)
