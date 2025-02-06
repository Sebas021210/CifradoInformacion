# Cifrado Vigenère
alphabet = 'abcdefghijklmnñopqrstuvwxyz'

def vigenere_encrypt(text, key):
    result = ''
    text = ''.join([c.lower() for c in text if c.isalpha() or c == ' '])
    for c in range(len(text)):
        if text[c] in alphabet:
            result += alphabet[(alphabet.index(text[c]) + alphabet.index(key[c % len(key)])) % len(alphabet)]
        else:
            result += text[c]
    #print(f'Mensaje cifrado: {result}')
    return result

def vigenere_decrypt(text, key):
    alphabet = 'abcdefghijklmnñopqrstuvwxyz'
    result = ''
    
    text = text.lower()
    key = key.lower()
    
    for c in range(len(text)):
        if text[c] in alphabet and key[c % len(key)] in alphabet:
            result += alphabet[(alphabet.index(text[c]) - alphabet.index(key[c % len(key)]) + len(alphabet)) % len(alphabet)]
        else:
            result += text[c] 
    
    #print(f'Mensaje cifrado: {result}')
    return result
