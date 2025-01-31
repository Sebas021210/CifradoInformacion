# Análisis de frecuencia de un texto plano
import Caesar
import Afines
import Vigenere

alphabet = "abcdefghijklmnopqrstuvwxyz"

def frequency_analysis(text):
    text = text.lower()
    counter = {}
    total_chars = 0

    for char in text:
        if char in alphabet:
            if char in counter:
                counter[char] += 1
            else:
                counter[char] = 1
            total_chars += 1

    frecuencies = {letter: (counter[letter] / total_chars if letter in counter else 0) for letter in alphabet}
    ordered_frecuencies = sorted(frecuencies.items(), key=lambda x: x[1], reverse=True)
    return ordered_frecuencies

text = "Este es un ejemplo de análisis de frecuencia de caracteres."
key = 3

result = Caesar.cesar_encrypt(text, key)
#result = Afines.afine_encrypt(text, 5, 8)
#result = Vigenere.vigenere_encrypt(text, "cripto")
frequency = frequency_analysis(result)

for letter, freq in frequency:
    print(f"{letter}: {freq:.2f}")
