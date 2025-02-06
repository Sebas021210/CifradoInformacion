import Caesar
import Afines
import Vigenere
import Frecuencia
import string

def load_spanish_frequencies(filename):
    distribution = {}
    with open(filename, "r", encoding="utf-8") as file:
        next(file)
        for line in file:
            letter, freq = line.strip().split("\t")
            letter = letter.lower()
            freq = float(freq.strip('%')) / 100
            if letter in string.ascii_lowercase or letter == 'ñ':
                distribution[letter] = freq
    return distribution

def load_cipher_text(file_path):
    with open(file_path, 'r', encoding="utf-8") as file:
        return file.read().lower()
    
def clean_text(text):
    alphabet = "abcdefghijklmnñopqrstuvwxyz"
    return "".join([char for char in text if char in alphabet])

def brute_force_caesar(cipher_text, spanish_distribution, max_shift=30):
    best_shift = []

    for key in range(1, max_shift + 1):
        decrypted_text = Caesar.cesar_decrypt(cipher_text, key)
        cleaned_text = clean_text(decrypted_text)
        freq, _ = Frecuencia.frequency_analysis(cleaned_text)
        score = Frecuencia.compare_distribution(freq, spanish_distribution)
        best_shift.append((key, score, decrypted_text))
    
    best_shift.sort(key=lambda x: x[1])

    return best_shift[:3]

spanish_distribution = load_spanish_frequencies("LABORATORIOS/Laboratorio1/sp_frequencies.txt")
cipher_text = load_cipher_text("LABORATORIOS/Laboratorio1/Cifrados/ceasar.txt")
best_keys = brute_force_caesar(cipher_text, spanish_distribution)
print("\nMejores llaves encontradas: ")
for key, score, text in best_keys:
    print(f"Llave: {key}")
    print(f"Texto descifrado: {text}\n")
