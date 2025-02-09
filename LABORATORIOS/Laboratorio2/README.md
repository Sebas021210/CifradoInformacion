# Laboratorio No. 2 – Base 64 y XOR

## Funciones Necesarias 

### Función de cadena de texto a binario
```python
def decimal_to_binary(decimal):
    binary = ''
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2
    return binary.zfill(8)

def text_to_binary(text):
    print('\n-Conversión de texto a binario')
    print(f'Texto: {text}')
    result = ''
    for char in text:
        binary_char = decimal_to_binary(ord(char))
        print(f'{char} -> {binary_char}')
        result += binary_char
    print(f'Texto a binario: {result}')
    return result
```

```
Texto: sebas
s -> 01110011
e -> 01100101
b -> 01100010
a -> 01100001
s -> 01110011
Texto a binario: 0111001101100101011000100110000101110011
```

```
Texto: Hola Mundo
H -> 01001000    
o -> 01101111    
l -> 01101100    
a -> 01100001    
  -> 00100000    
M -> 01001101    
u -> 01110101
n -> 01101110
d -> 01100100
o -> 01101111
Texto a binario: 01001000011011110110110001100001001000000100110101110101011011100110010001101111
```

### Función de cadena binaria a texto
```python
def binary_to_text(binary):
    print('\n-Conversión de binario a texto')
    print(f'Binario: {binary}')
    result = ''
    for i in range(0, len(binary), 8):
        chunk = binary[i:i+8]
        decimal = 0
        for j, bit in enumerate(reversed(chunk)):
            if bit == '1':
                decimal += 2 ** j
        char = chr(decimal)
        print(f'{chunk} -> {char}')
        result += char
    print(f'Binario a texto: {result}')
    return result
```

```
Binario: 0111001101100101011000100110000101110011
01110011 -> s
01100101 -> e
01100010 -> b
01100001 -> a
01110011 -> s
Binario a texto: sebas
```

```
Binario: 01001000011011110110110001100001001000000100110101110101011011100110010001101111
01001000 -> H
01101111 -> o
01101100 -> l
01100001 -> a
00100000 ->
01001101 -> M
01110101 -> u
01101110 -> n
01100100 -> d
01101111 -> o
Binario a texto: Hola Mundo
```

### Función de cadena binaria a base64
```python
def binary_to_base64(binary):
    print('\n-Conversión de binario a base64')
    print(f'Binario: {binary}')
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
        print(f'{chunk} -> {value} -> {base64_char}')
        result += base64_char
    print(f'Binario a base64: {result}')
    return result
```

```
Binario: 0111001101100101011000100110000101110011
011100 -> 28 -> c
110110 -> 54 -> 2
010101 -> 21 -> V
100010 -> 34 -> i
011000 -> 24 -> Y
010111 -> 23 -> X
001100 -> 12 -> M
Binario a base64: c2ViYXM
```

```
Binario: 01001000011011110110110001100001001000000100110101110101011011100110010001101111
010010 -> 18 -> S
000110 -> 6 -> G
111101 -> 61 -> 9
101100 -> 44 -> s
011000 -> 24 -> Y
010010 -> 18 -> S
000001 -> 1 -> B
001101 -> 13 -> N
011101 -> 29 -> d
010110 -> 22 -> W
111001 -> 57 -> 5
100100 -> 36 -> k
011011 -> 27 -> b
110000 -> 48 -> w
Binario a base64: SG9sYSBNdW5kbw
```

### Función de cadena base64 a binaria
```python
def base64_to_binary(base64):
    print("\n-Conversión de base64 a binario")
    print(f'Base64: {base64}')
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
        print(f'{char} -> {value} -> {binary.zfill(6)}')
        result += binary.zfill(6)
    print(f'Base64 a binario: {result}')
    return result
```

```
Base64: c2ViYXM
c -> 0 -> 011100
2 -> 0 -> 110110
V -> 0 -> 010101
i -> 0 -> 100010
Y -> 0 -> 011000
X -> 0 -> 010111
M -> 0 -> 001100
Base64 a binario: 011100110110010101100010011000010111001100
```

```
Base64: SG9sYSBNdW5kbw
S -> 0 -> 010010
G -> 0 -> 000110
9 -> 0 -> 111101
s -> 0 -> 101100
Y -> 0 -> 011000
S -> 0 -> 010010
B -> 0 -> 000001
N -> 0 -> 001101
d -> 0 -> 011101
W -> 0 -> 010110
5 -> 0 -> 111001
k -> 0 -> 100100
b -> 0 -> 011011
w -> 0 -> 110000
Base64 a binario: 010010000110111101101100011000010010000001001101011101010110111001100100011011110000
```

### Función de cadena de texto a base64
```python
def text_to_base64(text):
    print('\nConversión de texto a base64')
    print(f'Texto: {text}')
    binary = text_to_binary(text)
    base64 = binary_to_base64(binary)
    print(f'Texto a base64: {base64}')
    return base64
```

### Función de cadena base64 a texto
```python
def base64_to_text(base64):
    print('\nConversión de base64 a texto')
    print(f'Base64: {base64}')
    binary = base64_to_binary(base64)
    text = binary_to_text(binary)
    print(f'Base64 a texto: {text}')
    return text
```

### Función operación XOR
```python
def xor(binary, key):
    print('\n-Operación XOR')
    print(f'Binario: {binary}')
    print(f'Key: {key}')
    key = (key * (len(binary) // len(key) + 1))[:len(binary)]
    print(f'Key expandida: {key}')

    result = ''.join(str(int(b) ^ int(k)) for b, k in zip(binary, key))
    print(f'Resultado XOR: {result}')
    return result
```

```
Binario: 0101001101100101011000100110000101110011
Key: 0110001101101100011000010111011001100101
Key expandida: 0110001101101100011000010111011001100101
Resultado XOR: 0011000000001001000000110001011100010110
```

```
Binario: 01001000011011110110110001100001001000000100110101110101011011100110010001101111
Key: 0110001101101100011000010111011001100101
Key expandida: 01100011011011000110000101110110011001010110001101101100011000010111011001100101
Resultado XOR: 00101011000000110000110100010111010001010010111000011001000011110001001000001010
```
