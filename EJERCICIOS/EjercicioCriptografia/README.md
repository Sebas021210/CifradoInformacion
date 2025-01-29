# Ejercicio Criptografía

# Ejercicio No. 1

El Cifrado César es una de las técnicas de cifrado más antiguas y reconocidas, utilizada históricamente por Julio César para proteger sus mensajes militares. Este método consiste en desplazar cada letra del texto original un número fijo de posiciones hacia la derecha en el alfabeto, utilizando una clave compartida entre el emisor y el receptor. Por ejemplo, con un desplazamiento de 3, la letra "A" se convierte en "D".

Como señala Stallings (2016), el Cifrado César es un ejemplo de cifrado por sustitución monoalfabética, lo que lo hace vulnerable a ataques de fuerza bruta o análisis de frecuencias debido a su simplicidad. Sin embargo, sigue siendo un punto de partida clave para comprender los principios básicos de la criptografía.

## ¿Por qué se eligió el Cifrado César?

Para cifrar una palabra, solo es necesario desplazar los caracteres del alfabeto un número fijo de posiciones según la clave que se proporcione. E(x) = x + k (mod 26) y D(x) = x - k (mod 26)

## Ventajas

- **Fácil de implementar**: El cifrado puede realizarse con operaciones simples como sumas y restas. 
- **Rápido**: Incluso para cadenas largas, este cifrado puede ejecutarse en cuestión de milisegundos, ya que recorre cada letra una sola vez.

## Vulnerabilidades

- **Ataques de fuerza bruta**: Con solo 25 claves posibles, un atacante puede descifrar el mensaje rápidamente probando todas las combinaciones.
- **Análisis de frecuencias**: Las letras más comunes en un idioma pueden revelar el mensaje cifrado.
- **Clave estática**: Si un atacante intercepta la clave, puede descifrar todos los mensajes protegidos con este método.

## Ejemplos de Aplicación

### Ejemplo 1: Cifrar un mensaje
Se quiere cifrar el mensaje **"hola mundo"** con una clave de desplazamiento de **3**:

Resultado cifrado: **"krod pxqgr"**

### Ejemplo 2: Descifrar un mensaje
Si conocemos la clave de desplazamiento, podemos revertir el proceso. Por ejemplo, descifrar **"krod pxqgr"** con una clave de **3**:

Resultado descifrado: **"hola mundo"**

## Demostración
```
Cifrado de Cesar
Mensaje original: hola mundo
Mensaje cifrado: krod pxqgr
Mensaje descifrado: hola mundo
```

## Referencias
Stallings, W. (2016). Cryptography and Network Security: Principles and Practice (7ª ed.). Pearson.

# Ejercicio No. 2

## Demostración Cifrado con Llave Fija
```
-Cifrado con una llave fija-
Texto a binario: 0100100001101111011011000110000100100000010011010111010101101110011001000110111100100001
Texto a binario: 011010110110010101111001
Key expandida: 0110101101100101011110010110101101100101011110010110101101100101011110010110101101100101  
Resultado XOR: 0010001100001010000101010000101001000101001101000001111000001011000111010000010001000100  
Binario a texto: #§E4▲♂↔♦D
Texto cifrado: #§E4▲♂↔♦D
```

## Demostración Cifrado con Llave Dinámica
```
-Cifrado con una llave dinámica-
Clave generada: S^9}>{e.wr_
Texto a binario: 0100100001101111011011000110000100100000010011010111010101101110011001000110111100100001
Texto a binario: 0101001101011110001110010111110100111110011110110110010100101110011101110111001001011111
Key expandida: 0101001101011110001110010111110100111110011110110110010100101110011101110111001001011111
Resultado XOR: 0001101100110001010101010001110000011110001101100001000001000000000100110001110101111110
Binario a texto: U∟▲6►@‼↔~
Texto cifrado: U∟▲6►@‼↔~
```
