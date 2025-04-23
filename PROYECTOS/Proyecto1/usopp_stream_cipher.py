import random

def generate_keystream(seed, length):
    random.seed(seed)
    return bytes([random.randint(0, 255) for _ in range(length)])

def decrypt(ciphertext):
    cipherbytes = bytes.fromhex(ciphertext)
    for seed in range(100000):
        keystream = generate_keystream(seed, len(cipherbytes))
        plaintext = bytes([c ^ k for c, k in zip(cipherbytes, keystream)])
        if plaintext.startswith(b"FLAG_"):
            print(f"Semilla encontrada: {seed}")
            print(f"Texto descifrado: {plaintext.decode()}")
            break

ciphertext = "a77742694e4e0a84416d3e3a86cfde281f690e64c14f19d9164927b346adcf80be4c55dd6d"
decrypt(ciphertext)
