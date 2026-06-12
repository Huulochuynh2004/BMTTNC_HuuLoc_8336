from cipher.caesar.alphabet import ALPHABET

class CaesarCipher:
    def __init__(self):
        self.alphabet = ALPHABET
    def encrypt_text(self, text, key):
        result = []
        for c in text.upper():
            if c in self.alphabet:
                result.append(self.alphabet[(self.alphabet.index(c)+key)%26])
            else:
                result.append(c)
        return ''.join(result)
    def decrypt_text(self, text, key):
        result = []
        for c in text.upper():
            if c in self.alphabet:
                result.append(self.alphabet[(self.alphabet.index(c)-key)%26])
            else:
                result.append(c)
        return ''.join(result)
