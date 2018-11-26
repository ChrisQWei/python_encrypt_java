# python_encrypt_java
使用pycrypto进行加密，加密方式为：AES/ECB/PKCS5Padding， 可与java进行交互！

环境要求:
python 3.x or python 2.x
pycrypto        2.6.1

如果通过 pip 安装pycrypto后， 无法 "from Crypto.Cipher import AES" , 您需要将pycrypto卸载，使用"easy_install pycrypto"
进行安装。

如何使用?
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
结果:
cipher: b99ff1b7b7bde7784e21e7c0f9a11723
plain: abcd123456dbca