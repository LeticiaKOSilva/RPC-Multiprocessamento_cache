from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

class CryptoHandler:
    @staticmethod
    def encrypt_message(message, key):
        cipher = AES.new(key, AES.MODE_CBC, IV=b'1234567890123456')
        ciphertext = cipher.encrypt(pad(message.encode('utf-8'), AES.block_size))
        return base64.b64encode(ciphertext).decode('utf-8')

    @staticmethod
    def decrypt_message(ciphertext, key):
        if not ciphertext:  # Adicione esta verificação
            return ""

        cipher = AES.new(key, AES.MODE_CBC, IV=b'1234567890123456')
        decrypted = unpad(cipher.decrypt(base64.b64decode(ciphertext)), AES.block_size)
        return decrypted.decode('utf-8')
