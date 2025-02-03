# Análisis de frecuencia de un texto plano
import Caesar
import Afines
import Vigenere
import matplotlib.pyplot as plt

alphabet = "abcdefghijklmnñopqrstuvwxyz"

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
    return frecuencies, ordered_frecuencies

def compare_distribution(frequency):
    distribution = {
        'a': 12.53 / 100, 'b': 1.42 / 100, 'c': 4.68 / 100, 'd': 5.86 / 100, 'e': 13.68 / 100,
        'f': 0.69 / 100, 'g': 1.01 / 100, 'h': 0.70 / 100, 'i': 6.25 / 100, 'j': 0.44 / 100,
        'k': 0.02 / 100, 'l': 4.97 / 100, 'm': 3.15 / 100, 'n': 6.71 / 100, 'ñ': 0.31 / 100,
        'o': 8.68 / 100, 'p': 2.51 / 100, 'q': 0.88 / 100, 'r': 6.87 / 100, 's': 7.98 / 100,
        't': 4.63 / 100, 'u': 3.93 / 100, 'v': 0.90 / 100, 'w': 0.01 / 100, 'x': 0.22 / 100,
        'y': 0.90 / 100, 'z': 0.52 / 100
    }

    observed_dict = dict(frequency)
    differences = {letter: abs(observed_dict.get(letter, 0) - distribution[letter]) for letter in distribution}
    sorted_differences = sorted(differences.items(), key=lambda x: x[1], reverse=True)

    return distribution, sorted_differences, differences

text = "Este es un ejemplo de análisis de frecuencia de caracteres"
key = 3

result = Caesar.cesar_encrypt(text, key)
#result = Afines.afine_encrypt(text, 5, 8)
#result = Vigenere.vigenere_encrypt(text, "cripto")

frequency, ordered_frecuencies = frequency_analysis(result)
print(f"Frecuencia de caracteres en el texto cifrado: ")
for letter, freq in ordered_frecuencies:
    print(f"{letter}: {freq:.2f}")

expected_distribution, sorted_differences, differences = compare_distribution(frequency)
print("\nDiferencia de frecuencia con el idioma español: ")
for letter, diff in sorted_differences:
    print(f"{letter}: {diff:.2f}")

plt.figure(figsize=(12, 6))
plt.bar(frequency.keys(), frequency.values(), alpha=0.6, label="Texto cifrado")
plt.plot(expected_distribution.keys(), expected_distribution.values(), color='red', marker='o', linestyle='dashed', label="Distribución en español")

plt.xlabel("Letras")
plt.ylabel("Frecuencia")
plt.title("Análisis de frecuencia: Texto cifrado vs Español")
plt.legend()
plt.show()
