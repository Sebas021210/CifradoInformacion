# Cifrado de César

El **Cifrado de César** es una de las técnicas de cifrado más antiguas y conocidas, Julio César usaba este cifrado para sus
mensajes militares. El cifrado consistía en correr todas las letras del alfabeto un número fijo de posiciones a la derecha.
---

## ¿Por qué se eligió el Cifrado César?

Para cifrar una palabra, solo es necesario desplazar los caracteres del alfabeto un número fijo de posiciones según la clave que se proporcione. E(x) = x + k (mod 26) y D(x) = x - k (mod 26)

---

## Ventajas

- **Fácil de implementar**: El cifrado puede realizarse con operaciones simples como sumas y restas. 
- **Rápido**: Incluso para cadenas largas, este cifrado puede ejecutarse en cuestión de milisegundos, ya que recorre cada letra una sola vez.

---

## Vulnerabilidades

- **Ataques de fuerza bruta**: Con solo 25 claves posibles, un atacante puede descifrar el mensaje rápidamente probando todas las combinaciones.
- **Análisis de frecuencias**: Las letras más comunes en un idioma pueden revelar el mensaje cifrado.
- **Clave estática**: Si un atacante intercepta la clave, puede descifrar todos los mensajes protegidos con este método.

---

## Ejemplos de Aplicación

### Ejemplo 1: Cifrar un mensaje
Se quiere cifrar el mensaje **"hola mundo"** con una clave de desplazamiento de **3**:

Resultado cifrado: **"krod pxqgr"**

### Ejemplo 2: Descifrar un mensaje
Si conocemos la clave de desplazamiento, podemos revertir el proceso. Por ejemplo, descifrar **"krod pxqgr"** con una clave de **3**:

Resultado descifrado: **"hola mundo"**
