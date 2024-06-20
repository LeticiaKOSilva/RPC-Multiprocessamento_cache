from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

'''
    Realiza a criptografia e descriptografia de mensagens usando
    AES(Advanced Encryption Standard) no modo CBC (Cipher Block Chaining)
'''
class CryptoHandler:
    
    # Criptografa uma mensagem usando a chave "key".
    @staticmethod
    def encrypt_message(message, key):
        '''
            Com o modo CBC cria-se um objeto de cifra AES com a chave "key" e um 
            vetor de incicialização "IV" com um valor fixo.
        '''
        cipher = AES.new(key, AES.MODE_CBC, IV=b'1234567890123456')
        
        '''
            A mensagem é convertida para bytes e então é preenchida para
            um cumprimento que seja múltiplo do tamanho do bloco AES e 
            realizar a criptografia da mensagem.
        '''
        ciphertext = cipher.encrypt(pad(message.encode('utf-8'), AES.block_size))

        # O resultado criptografado é convertido para a Base64 para facilitar o armazenamento e transporte seguro.
        return base64.b64encode(ciphertext).decode('utf-8')

    # Descriptografa uma texto cifrado "ciphertext" usando a chave "key" 
    @staticmethod
    def decrypt_message(ciphertext, key):
        if not ciphertext: 
            return ""

        cipher = AES.new(key, AES.MODE_CBC, IV=b'1234567890123456')
        # Bytes decodificados de base 64 para obter os bytes originais da mensagem criptografada
        decrypted = unpad(cipher.decrypt(base64.b64decode(ciphertext)), AES.block_size)
        return decrypted.decode('utf-8')
