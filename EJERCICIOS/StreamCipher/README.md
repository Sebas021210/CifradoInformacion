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
- Cuando se cambia la clave utilizada para generar el keystream, provoca una alteración en el generador de números pseudoaleatorios y este generará un keystream completamente diferente. Al cifrar el mismo mensaje con una clave diferente, el texto cifrado también será diferente.

¿Qué riesgos de seguridad existen si reutilizas el mismo keystream para cifrar dos mensajes diferentes?
- Si se reutiliza el mismo keystream para cifrar dos mensajes diferentes, se tiene un grave riesgo de seguridad. Uno de los principales riegos es la Revelación de Patrones, ya que si un atacante tiene acceso a ambos mensajes cifrados y sabe que comparten el mismo keystream, puede realizar una operación XOR entre ambos para obtener el contenido de los mensajes.

¿Cómo afecta la longitud del keystream a la seguridad del cifrado?
- La longitud del keystream es importante para la seguridad del cifrado, ya que si el keystream es más corto que el mensaje, se repetirían valores del keystream, lo que comprometerá la seguridad. 

¿Qué consideraciones debes tener al generar un keystream en un entorno real?
- El keystream debe ser generado de manera aleatoria para que no haya patrones predecibles.
- No se debe de reutilizar el keystream para cifrar diferentes mensajes. Cada mensaje debería tener su propio keystream único basado en una clave única.
- Se tiene que asegurar que el keystream tenga la longitud suficiente para el mensaje a cifrar. 
- El PRNG debe ser rápido y no debe afectar el rendimiento del sistema, especialmente si se necesita generar keystreams para mensajes grandes o de forma continua.
