# Scipts 
print("SCRIPTS DE CRIPTOGRAFÍA")
text = 'Sebastián'
print(f'Texto: {text}')

# --------------------------------------------------- Funciones Adicionales --------------------------------------------------

# Conversión de decimal a binario
def decimal_to_binary(decimal):
    binary = ''
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2
    return binary.zfill(8)

# --------------------------------------------------- Funciones Principales --------------------------------------------------

# Conversión de texto a binario
def text_to_binary(text):
    print("\nConversión de texto a binario")
    result = ''.join(decimal_to_binary(ord(char)) for char in text)
    return result

# Conversión de binario a base64
def binary_to_base64(binary):
    print("\nConversión de binario a base64")
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
    return result

# Conversión de base64 a binario
def base64_to_binary(base64):
    print("\nConversión de base64 a binario")
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
    return result

# Conversión de binario a texto
def binary_to_text(binary):
    print("\nConversión de binario a texto")
    result = ''
    for i in range(0, len(binary), 8):
        chunk = binary[i:i+8]
        decimal = 0
        for j, bit in enumerate(reversed(chunk)):
            if bit == '1':
                decimal += 2 ** j
        result += chr(decimal)
    return result

# --------------------------------------------------- Ejecución -----------------------------------------------------------

binary = text_to_binary(text)
print(f'Texto a binario: {binary}')

base64 = binary_to_base64(binary)
print(f'Binario a base64: {base64}')

binary = base64_to_binary(base64)
print(f'Base64 a binario: {binary}')

text = binary_to_text(binary)
print(f'Binario a texto: {text}')
