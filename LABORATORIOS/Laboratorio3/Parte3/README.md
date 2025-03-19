# 🔐 Laboratorio 3 - Cifrados Simetricos

## Parte No. 3

### ChaCha20
```python
# Generar una clave de 256 bits y un nonce de 12 bytes
clave = get_random_bytes(32)
nonce = get_random_bytes(12)

# Cifrar con ChaCha20
cipher = ChaCha20.new(key=clave, nonce=nonce)
ciphertext = cipher.encrypt(text)

# Descifrar
cipher_dec = ChaCha20.new(key=clave, nonce=nonce)
text_descifrado = cipher_dec.decrypt(ciphertext)
```

```
Mensaje original:  Mensaje a cifrar con ChaCha20
Cifrado ChaCha20:  1a1f9056955f5ae2d7626f4a55849fe08aa1caa374573507bd1307d114
Descifrado:  Mensaje a cifrar con ChaCha20
```

### Comparación ChaCha20 - AES
```python
# Claves y configuración
key_aes = os.urandom(16)
key_chacha = get_random_bytes(32)
nonce_chacha = get_random_bytes(12)
iv_aes = get_random_bytes(AES.block_size)

# Prueba de ChaCha20
inicio = time.time()
cipher_chacha = ChaCha20.new(key=key_chacha, nonce=nonce_chacha)
ciphertext_chacha = cipher_chacha.encrypt(text)
tiempo_chacha = time.time() - inicio

# Prueba de AES en modo CBC
inicio = time.time()
cipher_aes = AES.new(key_aes, AES.MODE_CBC, iv_aes)
ciphertext_aes = cipher_aes.encrypt(pad(text, AES.block_size))
tiempo_aes = time.time() - inicio
```

```
Tiempo de cifrado ChaCha20: 0.004112 segundos
Tiempo de cifrado AES (CBC): 0.002908 segundos
```

### Preguntas
- ¿Analizar que cifrado es mas rápido ChaCha20 o AES?
  - En las pruebas AES tuvo un mejor tiempo que ChaCha20. Esto puede deberse a que la prueba se ejecutó en un entorno donde el procesador tiene soporte que optimiza el rendimiento del cifrado AES. Sin embargo, en dispositivos sin esta optimización, ChaCha20 suele ser más rápido, ya que usa solo operaciones aritméticas simples, mientras que AES requiere múltiples accesos a tablas en memoria y puede ser más costoso en software puro.

- ¿En qué casos debería usarse en vez de AES?
  - Se usa en dispositivos móviles o embebidos sin aceleración AES.
  - Se necesita seguridad comparable a AES pero con mayor velocidad en software puro.
  - Se requiere evitar ataques de side-channel, ya que AES puede ser vulnerable en implementaciones mal optimizadas.
