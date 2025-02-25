# Stream Cipher

## Funciones

### Generación de Keystream
```python
def keystream(length, seed):
    random.seed(seed)
    return [random.randint(0, 255) for _ in range(length)]
```

### Cifrado
```python
def xor_encrypt(text, key):
    text = text.encode()
    return [t ^ k for t, k in zip(text, key)]
```


### Descifrado
```python
def xor_decrypt(ciphertext, key):
    return bytes([c ^ k for c, k in zip(ciphertext, key)]).decode()
```

## Ejemplo de uso 
```python
text = "Hola Mundo"
seed = 42
key = keystream(len(text), seed)
ciphertext = xor_encrypt(text, key)
decrypted = xor_decrypt(ciphertext, key)
```

```
-Stream Cipher
Texto a cifrar: Hola Mundo
KeyStream: [57, 12, 140, 125, 114, 71, 52, 44, 216, 16]
Texto cifrado: [113, 99, 224, 28, 82, 10, 65, 66, 188, 127]
Texto descifrado: Hola Mundo
```

## Pruebas Unitarias
```
...
----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
```

## Preguntas a Responder
¿Qué sucede cuando cambias la clave utilizada para generar el keystream?
- ... 

¿Qué riesgos de seguridad existen si reutilizas el mismo keystream para cifrar dos mensajes diferentes?
- ...

¿Cómo afecta la longitud del keystream a la seguridad del cifrado?
- ...

¿Qué consideraciones debes tener al generar un keystream en un entorno real?
- ...
