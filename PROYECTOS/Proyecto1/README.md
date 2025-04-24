# Proyecto 1: Cifrados de Flujo

Este proyecto es una introducción práctica al mundo de los retos CTF, enfocados en el uso y ruptura de cifrados clásicos y modernos. A través de cuatro retos ambientados en el universo de One Piece, se aprenderá a explorar sistemas de archivos, extraer información oculta en metadatos e imágenes, y descifrar textos cifrados utilizando distintos algoritmos como XOR, RC4, stream cipher y ChaCha20.

## Requisitos
- Python 3
- Docker y Docker Compose
- pip para gestión de paquetes

## Instrucciones de instalación y ejecución

### 1. Clonar el repositorio e instalar los requisitos
```bash
git clone https://github.com/locano-uvg/ctf_onepice_symmetric_cipher
pip3 install -r resources/requirements.txt
```

### 2. Generar los retos con Python
```bash
python generate_challenges.py
```

### 3. Levantar los contenedores Docker
```bash
sudo docker compose up -d
docker ps
```

## Ingresar al primer reto
```bash
docker exec -it luffy_challenge bash
```

### 1. Cambiar a usuario del reto
```bash
su luffy
password: onepiece
```

### 2. Acceder al directorio del reto
```bash
cd ONEPIECE/
```

3. Crear el script de búsqueda de rutas
```bash
nano buscar_rutas.py
```

Escribir el siguiente contenido en el archivo:
```python
from pathlib import Path

def explorar_sistema(directorio_inicial):    
    for ruta in Path(directorio_inicial).rglob('*'):
        try:
            if ruta.is_file():
                print(f"Ruta encontrada: {str(ruta.absolute())}")
                print(f"Nombre del archivo: {ruta.name}")
                print("-" * 50)
        except Exception:
            pass
    
if __name__ == "__main__":
    directorio = "./"
    explorar_sistema(directorio)
```

Guardar con Ctrl + X, luego presionar Y y Enter.

### 4. Ejecutar el script
```bash
python3 buscar_rutas.py
```

### 5. Buscar la ruta de la flag y el archivo poneglyph
Para ver la flag:
```bash
cat flag.txt
```

Para acceder al poneglyph en una nueva terminal:
```bash
python -m http.server 8080
```

Luego en tu navegador accede a:
```bash
http://localhost:8080
```

Navega hasta el archivo .zip y descárgalo. El password para el primer archivo es:
```bash
onepiece
```

## Descripción de los retos
En cada reto se deberán repetir los pasos anteriores con cada usuario:
1. Extraer texto oculto de la imagen con extract_text_images.py.
2. Descifrar la flag cifrada con el script correspondiente.
3. Usar esa flag como contraseña para el siguiente reto.

|**Reto**|**Script para imagen**|**Script para flag**|**Flag se usa como contraseña de**|
|-------------|-----------------------|-----------|---------------------------------------------------------------------------------------|
| Reto 1 | extract_text_images.py | luffy_xor_decipher.py | Reto 2 |
| Reto 2 | extract_text_images.py | zoro_rc4_decipher.py | Reto 3 |
| Reto 3 | extract_text_images.py  | usopp_stream_cipher.py | Reto 4 |
| Reto 4 | extract_text_images.py   | nami_chacha_decipher.py | - |
