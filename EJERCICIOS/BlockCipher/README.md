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
