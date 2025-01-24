import random
import string

# --------------------------------------------------- Funciones Adicionales --------------------------------------------------

# Conversión de decimal a binario
def decimal_to_binary(decimal):
    binary = ''
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2
    return binary.zfill(8)

# Generación de clave dinámica
def dynamic_key(length):
    #print("\nGeneración de clave dinámica")
    key = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))
    print(f'Clave generada: {key}')
    return key

# --------------------------------------------------- Funciones Principales --------------------------------------------------

# Conversión de texto a binario
def text_to_binary(text):
    #print("\nConversión de texto a binario")
    result = ''.join(decimal_to_binary(ord(char)) for char in text)
    print(f'Texto a binario: {result}')
    return result

# Conversión de binario a base64
def binary_to_base64(binary):
    #print("\nConversión de binario a base64")
    result = ''
    for i in range(0, len(binary), 6):
        chunk = binary[i:i+6]
        while len(chunk) < 6:
            chunk += '0'
        value = 0
        for j, bit in enumerate(reversed(chunk)):
            if bit == '1':
                value += 2 ** j
        result += 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'[value]
    print(f'Binario a base64: {result}')
    return result

# Conversión de base64 a binario
def base64_to_binary(base64):
    #print("\nConversión de base64 a binario")
    result = ''
    for char in base64:
        base64_value = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
        value = 0
        for i, letter in enumerate(base64_value):
            if letter == char:
                value = i
                break
        binary = ''
        while value > 0:
            binary = str(value % 2) + binary
            value = value // 2
        result += binary.zfill(6)
    print(f'Base64 a binario: {result}')
    return result

# Conversión de binario a texto
def binary_to_text(binary):
    #print("\nConversión de binario a texto")
    result = ''
    for i in range(0, len(binary), 8):
        chunk = binary[i:i+8]
        decimal = 0
        for j, bit in enumerate(reversed(chunk)):
            if bit == '1':
                decimal += 2 ** j
        result += chr(decimal)
    print(f'Binario a texto: {result}')
    return result

# Conversión de texto a base64
def text_to_base64(text):
    #print("\nConversión de texto a base64")
    binary = text_to_binary(text)
    base64 = binary_to_base64(binary)
    return base64

# Conversión de base64 a texto
def base64_to_text(base64):
    #print("\nConversión de base64 a texto")
    binary = base64_to_binary(base64)
    text = binary_to_text(binary)
    return text

# XOR de dos cadenas de binarios
def xor(binary, key):
    #print("\nXOR de dos cadenas de binarios")
    key = (key * (len(binary) // len(key) + 1))[:len(binary)]
    print(f'Key expandida: {key}')

    result = ''.join(str(int(b) ^ int(k)) for b, k in zip(binary, key))
    print(f'Resultado XOR: {result}')
    return result

# --------------------------------------------------- Cifrado -----------------------------------------------------------

# Cifrado con una llave fija
def encryption_fixed_key(text, key):
    print("\n-Cifrado con una llave fija-")
    binary_text = text_to_binary(text)
    binary_key = text_to_binary(key)

    cypher_binary = xor(binary_text, binary_key)
    #cypher_base64 = binary_to_base64(cypher_binary)
    #cypher_binary = base64_to_binary(cypher_base64)
    cypher_text = binary_to_text(cypher_binary)

    print(f'Texto cifrado: {cypher_text}')
    return cypher_text

# Cifrado con una llave dinámica
def encryption_dynamic_key(text):
    print("\n-Cifrado con una llave dinámica-")
    key = dynamic_key(len(text))
    binary_text = text_to_binary(text)
    binary_key = text_to_binary(key)

    cypher_binary = xor(binary_text, binary_key)
    #cypher_base64 = binary_to_base64(cypher_binary)
    #cypher_binary = base64_to_binary(cypher_base64)
    cypher_text = binary_to_text(cypher_binary)

    print(f'Texto cifrado: {cypher_text}')
    return cypher_text, key

# --------------------------------------------------- Descifrado -----------------------------------------------------------

# Descifrado con una llave fija
def decryption_fixed_key(cypher_text, key):
    print("\n-Descifrado con una llave fija-")
    binary_cypher = text_to_binary(cypher_text)
    binary_key = text_to_binary(key)

    text_binary = xor(binary_cypher, binary_key)
    text = binary_to_text(text_binary)

    print(f'Texto descifrado: {text}')
    return text

# Descifrado con una llave dinámica
def decryption_dynamic_key(cypher_text, key):
    print("\n-Descifrado con una llave dinámica-")
    binary_cypher = text_to_binary(cypher_text)
    binary_key = text_to_binary(key)

    text_binary = xor(binary_cypher, binary_key)
    text = binary_to_text(text_binary)

    print(f'Texto descifrado: {text}')
    return text

# --------------------------------------------------- Ejecución -----------------------------------------------------------

# Texto a cifrar
text = 'Hola Mundo!'

# Cifrado de texto
cypher_fixed = encryption_fixed_key(text, 'key')
cypher_dynamic, key = encryption_dynamic_key(text)

# Descifrado de texto
decryption_fixed_key(cypher_fixed, 'key')
decryption_dynamic_key(cypher_dynamic, key)
