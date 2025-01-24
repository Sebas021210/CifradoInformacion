# Cifrado de César

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

## Referencias
Stallings, W. (2016). Cryptography and Network Security: Principles and Practice (7ª ed.). Pearson.
