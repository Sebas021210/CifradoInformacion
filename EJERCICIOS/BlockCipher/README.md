# Ejercicio Block Cipher

## Generación una función cifrado y descifrado DES
```python
def encrypt(input_file):
    cipher = DES.new(key, DES.MODE_ECB)

    data = read_file(input_file)
    data = pad_text(data)
    encrypted_data = cipher.encrypt(data)

    return encrypted_data
```

```python
def decrypt(encrypted_data):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_data = cipher.decrypt(encrypted_data)
    decrypted_data = unpad_text(decrypted_data)

    return decrypted_data
```

## Generación una función cifrado y descifrado 3DES
```python
def encrypt(input_file):
    cipher = DES3.new(key, DES3.MODE_CBC, vector)

    data = read_file(input_file)
    padded_data = pad(data, DES3.block_size)
    encrypted_data = cipher.encrypt(padded_data)

    return encrypted_data
```

```python
def decrypt(encrypted_data):
    cipher = DES3.new(key, DES3.MODE_CBC, vector)
    decrypted_data = cipher.decrypt(encrypted_data)
    unpadded_data = unpad(decrypted_data, DES3.block_size)

    return unpadded_data
```

## Generación una función cifrado y descifrado AES con CBC Y ECB
```python
def encrypt_aes_ecb(input_file, output_file):
    cipher = AES.new(key, AES.MODE_ECB)

    data = read_file(input_file)
    padded_data = pad(data, AES.block_size)
    encrypted_data = cipher.encrypt(padded_data)

    write_file(output_file, encrypted_data)
```

```python
def decrypt_aes_ecb(input_file, output_file):
    cipher = AES.new(key, AES.MODE_ECB)

    encrypted_data = read_file(input_file)
    decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)

    write_file(output_file, decrypted_data)
```

```python
def encrypt_aes_cbc(input_file, output_file):
    iv = urandom(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)

    data = read_file(input_file)
    padded_data = pad(data, AES.block_size)
    encrypted_data = iv + cipher.encrypt(padded_data)

    write_file(output_file, encrypted_data)
```

```python
def decrypt_aes_cbc(input_file, output_file):
    encrypted_data = read_file(input_file)
    iv = encrypted_data[:16] 
    encrypted_data = encrypted_data[16:] 

    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)

    write_file(output_file, decrypted_data)
```

## Preguntas a Responder

¿Qué tamaño de clave se está usando para DES, 3DES y AES
- DES: Usa una clave de 56 bits
- 3DES: Usa una clave de 168 bits
- AES: Puede usar claves de 128, 192 o 256 bits

¿Qué modo de operación está implementado?
- Para DES: Se implementó ECB (Electronic Codebook)
- Para 3DES: Se implementó CBC (Cipher Block Chaining)
- Para AES: Se implementó ECB y CBC

¿Por qué no debemos usar ECB en datos sensibles?
- ECB cifra cada bloque de manera independiente y siempre produce el mismo cifrado para bloques idénticos, lo que permite patrones visibles.

¿Cual es la diferencia entre ECB vs CBC, se puede notar directamente en una imagen?
- ECB: Cada bloque se cifra de forma independiente. Se mantienen patrones visibles.
- CBC: Cada bloque depende del anterior, con un IV aleatorio. Se elimina la estructura visible.

¿Que es el IV?
- IV (Vector de Inicialización) es un bloque de datos aleatorio usado en modos de cifrado en bloque como CBC, CFB y OFB para evitar que el mismo texto cifrado se genere para mensajes idénticos.

¿Que es el PADDING?
- El Padding se usa cuando el tamaño de los datos no es múltiplo del tamaño del bloque del algoritmo de cifrado.

¿En qué situaciones se recomienda cada modo de operación?
- ECB: No recomendado para datos sensibles. Solo en situaciones donde el rendimiento es más importante que la seguridad.
- CBC: Recomendado para archivos, imágenes y datos sensibles donde se requiere aleatoriedad.
- CFB: Bueno para flujos de datos o cuando no se necesita padding.
- OFB: Útil para cifrado de transmisión de datos en tiempo real.
- GCM: Mejor para transmisión segura, ya que incluye autenticación.

¿Cómo elegir un modo seguro en cada lenguaje de programación?
- Evitar ECB en datos sensibles.
- Usar CBC o GCM para datos importantes.
- Usar IV aleatorio y diferente para cada cifrado.
- Utilizar librerías seguras y probadas.
- No reutilizar claves ni IVs en múltiples cifrados.
