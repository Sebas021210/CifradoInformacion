# 🔐 Laboratorio 3 - Cifrados Simetricos
Este laboratorio explora diferentes técnicas de cifrado y sus aplicaciones prácticas en seguridad informática.

## 📂 Estructura del Proyecto
```
📦 CifradosInformacion
├── 📂 Laboratorio3
│   ├── 📂 Parte1
│   │   ├── 📂 imagenes
│   │   ├── 📄 CBC-image.py
│   │   ├── 📄 EBC-image.py
│   ├── 📂 Parte2
│   │   ├── 📄 cliente.py
│   │   ├── 📄 servidor.py
│   ├── 📂 Parte3
│   │   ├── 📄 ChaCha20.py
│   │   ├── 📄 Comparacion.py
│   ├── 📂 Parte4
│   │   ├── 📂 archivos
│   │   ├── 📄 Ransomware.py
│   │   ├── 📄 Desencriptar.py
│   ├── 📄 Dockerfile
```

## 🚀 Cómo ejecutar

### 1️⃣ Construir el contenedor Docker  
Antes de ejecutar los scripts, asegúrate de tener Docker instalado. Luego, crea la imagen del contenedor con:  

```sh
docker build -t laboratorio-cripto .
```

### 2️⃣ Ejecutar el contenedor interactivo
Para acceder al contenedor y ejecutar los scripts dentro de él, usa:

```sh
docker run -it --rm -v $(pwd):/app laboratorio-cripto bash
```
Esto montará el directorio actual en /app dentro del contenedor.

### 3️⃣ Ejecutar cada parte
Una vez dentro del contenedor, puedes ejecutar los scripts según la parte correspondiente:

🔹 Parte 1: Cifrado en ECB y CBC
```sh
python3 Parte1/EBC-image.py
python3 Parte1/CBC-image.py
```

🔹 Parte 2: Capturando Cifrado en Red con Wireshark
```sh
python3 Parte2/cliente.py
python3 Parte2/servidor.py
```

🔹 Parte 3: Cifrado con ChaCha20
```sh
python3 Parte3/ChaCha20.py
python3 Parte3/Comparacion.py
```

🔹 Parte 4: Simulación de Ransomware
Cifrar archivos en la carpeta archivos/:
```sh
python3 Parte4/Ransomware.py
```

Descifrar archivos:
```sh
python3 Parte4/Desencriptar.py
```

Ahora con esto ya tienes todo listo para correr las pruebas en Docker. 🚀🔥