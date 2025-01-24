# Scipts 
print("SCRIPTS DE CRIPTOGRAFÍA")
text = 'Sebastián'
print(f'Texto: {text}')

# Conversión de texto a binario
def text_to_binary(text):
    print("\nConversión de texto a binario")
    result = ''.join(format(ord(char), '08b') for char in text)
    return result

binary = text_to_binary(text)
print(f'Binario: {binary}')

# Conversión de binario a base64
def binary_to_base64(binary):
    print("\nConversión de binario a base64")
    result = ''
    for i in range(0, len(binary), 6):
        chunk = binary[i:i+6]
        while len(chunk) < 6:
            chunk += '0'
        result += 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'[int(chunk, 2)]
    return result

base64 = binary_to_base64(binary)
print(f'Base64: {base64}')

# Conversión de base64 a binario
def base64_to_binary(base64):
    print("\nConversión de base64 a binario")
    result = ''
    for char in base64:
        value = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'.index(char)
        result += format(value, '06b')
    return result

binary = base64_to_binary(base64)
print(f'Binario: {binary}')

# Conversión de binario a texto
def binary_to_text(binary):
    print("\nConversión de binario a texto")
    result = ''
    for i in range(0, len(binary), 8):
        chunk = binary[i:i+8]
        result += chr(int(chunk, 2))
    return result

text = binary_to_text(binary)
print(f'Texto: {text}')
