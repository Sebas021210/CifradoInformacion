from PIL import Image
import piexif
from luffy_xor import xor_cipher

def extraer_texto_metadata(imagen_path):
    img = Image.open(imagen_path)
    exif_dict = piexif.load(img.info.get('exif', b''))
    texto = exif_dict['0th'].get(piexif.ImageIFD.Artist)
    if texto:
        return texto.decode('utf-8')
    return None

image_path = "PROYECTOS/Proyecto1/images/poneglyph_nami.jpeg"
student_id = input("Introduce tu carné para descifrar el mensaje: ")
texto_cifrado = extraer_texto_metadata(image_path)
decrypted_text = xor_cipher(texto_cifrado, student_id)
print(decrypted_text)
