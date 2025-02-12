# ----------------------------------------------------- Funciones -------------------------------------------------------------

# Función de cadena de texto a binario
def decimal_to_binary(decimal):
    binary = ''
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2
    return binary.zfill(8)

def text_to_binary(text):
    print('\n-Conversión de texto a binario')
    #print(f'Texto: {text}')
    result = ''
    for char in text:
        binary_char = decimal_to_binary(ord(char))
        #print(f'{char} -> {binary_char}')
        result += binary_char
    print(f'Texto a binario: {result}')
    return result

# Función de cadena binaria a texto
def binary_to_text(binary):
    print('\n-Conversión de binario a texto')
    #print(f'Binario: {binary}')
    result = ''
    for i in range(0, len(binary), 8):
        chunk = binary[i:i+8]
        decimal = 0
        for j, bit in enumerate(reversed(chunk)):
            if bit == '1':
                decimal += 2 ** j
        char = chr(decimal)
        #print(f'{chunk} -> {char}')
        result += char
    print(f'Binario a texto: {result}')
    return result

# Función de cadena binaria a base64
def binary_to_base64(binary):
    print('\n-Conversión de binario a base64')
    #print(f'Binario: {binary}')
    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    result = ''
    for i in range(0, len(binary), 6):
        chunk = binary[i:i+6]
        while len(chunk) < 6:
            chunk += '0'
        value = 0
        for j, bit in enumerate(reversed(chunk)):
            if bit == '1':
                value += 2 ** j
        base64_char = base64_chars[value]
        #print(f'{chunk} -> {value} -> {base64_char}')
        result += base64_char
    print(f'Binario a base64: {result}')
    return result

# Función de cadena base64 a binaria
def base64_to_binary(base64):
    print("\n-Conversión de base64 a binario")
    #print(f'Base64: {base64}')
    base64_value = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    result = ''
    for char in base64:
        value = 0
        for i, letter in enumerate(base64_value):
            if letter == char:
                value = i
                break
        binary = ''
        while value > 0:
            binary = str(value % 2) + binary
            value = value // 2
        #print(f'{char} -> {value} -> {binary.zfill(6)}')
        result += binary.zfill(6)
    print(f'Base64 a binario: {result}')
    return result

# Función de cadena de texto a base64
def text_to_base64(text):
    print('\nConversión de texto a base64')
    print(f'Texto: {text}')
    binary = text_to_binary(text)
    base64 = binary_to_base64(binary)
    print(f'Texto a base64: {base64}')
    return base64

# Función de cadena base64 a texto
def base64_to_text(base64):
    print('\nConversión de base64 a texto')
    print(f'Base64: {base64}')
    binary = base64_to_binary(base64)
    text = binary_to_text(binary)
    print(f'Base64 a texto: {text}')
    return text

# Función operación XOR
def xor(binary, key):
    print('\n-Operación XOR')
    #print(f'Binario: {binary}')
    #print(f'Key: {key}')
    key = (key * (len(binary) // len(key) + 1))[:len(binary)]
    #print(f'Key expandida: {key}')

    result = ''.join(str(int(b) ^ int(k)) for b, k in zip(binary, key))
    print(f'Resultado XOR: {result}')
    return result

#----------------------------------------------------- Ejemplos -------------------------------------------------------------

'''
text = 'Hola Mundo'

Text_to_Binary = text_to_binary(text)
Binary_to_Text = binary_to_text(Text_to_Binary)
Text_to_Base64 = text_to_base64(text)
Base64_to_Text = base64_to_text(Text_to_Base64)

binary = '01001000011011110110110001100001001000000100110101110101011011100110010001101111'
key = '0110001101101100011000010111011001100101'

XOR = xor(binary, key)
'''
