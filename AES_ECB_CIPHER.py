from Crypto.Cipher import AES
import codecs
BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s : s[:-ord(s[len(s)-1:])]


class AESCipher:
    def __init__(self, key):
        """
        Requires hex encoded param as a key
        """
        self.key = key

    def encrypt(self, raw):
        """
        Returns hex encoded encrypted value!
        """
        raw = pad(raw)
        cipher = AES.new(self.key, AES.MODE_ECB)
        return codecs.encode(cipher.encrypt(raw), 'hex').decode('utf-8')

    def decrypt(self, enc):
        """
        Requires hex encoded param to decrypt
        """
        enc = codecs.decode(enc,"hex")
        cipher = AES.new(self.key, AES.MODE_ECB)
        return unpad(cipher.decrypt(enc)).decode('utf-8')


if __name__ == "__main__":
    from AES_ECB_CIPHER import AESCipher
    key = "asdfas12313aer43"
    plaintext = 'abcd123456dbca'
    encryptor = AESCipher(key)
    ciphertext = encryptor.encrypt(plaintext)
    print('cipher:{}'.format(ciphertext))
    plain = encryptor.decrypt(ciphertext)
    print('plain:{}'.format(plaintext))
