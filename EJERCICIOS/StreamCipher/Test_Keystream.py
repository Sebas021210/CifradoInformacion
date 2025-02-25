import unittest
from Keystream import keystream, xor_encrypt, xor_decrypt

class TestStreamCipher(unittest.TestCase):

    # Test para la longitud del keystream
    def test_keystream_length(self):
        key = keystream(5, 42)
        self.assertEqual(len(key), 5)

    # Test para los valores del keystream
    def test_keystream_values(self):
        key = keystream(10, 42)
        for k in key:
            self.assertTrue(0 <= k <= 255)

    # Test para cifrar y descifrar con XOR
    def test_xor_encrypt_decrypt(self):
        text = "Hola Mundo"
        seed = 42
        key = keystream(len(text), seed)

        # Cifrado
        ciphertext = xor_encrypt(text, key)
        self.assertIsInstance(ciphertext, list)

        # Descifrado
        decrypted = xor_decrypt(ciphertext, key)
        self.assertEqual(decrypted, text)

if __name__ == "__main__":
    unittest.main()
