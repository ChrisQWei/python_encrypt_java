# python_encrypt_java
Encryption using pycrypto, AES/ECB/PKCS5Padding. Interact with JAVA, if use same encrypt method.
Envir require:
python 3.x or python 2.x
pycrypto        2.6.1
If you can't "from Crypto.Cipher import AES" in python after you have installed the "pycrypto" via pip, then you should
use "easy_install pycrypto" by the way.
How to use it?
------------------------------------------------
from AES_ECB_CIPHER import AESCipher
key = "asdfas12313aer43"
plaintext = 'abcd123456dbca'
encryptor = AESCipher(key)
ciphertext = encryptor.encrypt(plaintext)
print('cipher:{}'.format(ciphertext))
plain = encryptor.decrypt(ciphertext)
print('plain:{}'.format(plaintext))
------------------------------------------------
here is result:
cipher: b99ff1b7b7bde7784e21e7c0f9a11723
plain: abcd123456dbca