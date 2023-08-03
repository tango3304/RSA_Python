# Coding: UTF-8
# Crypto.Util.number: https://pycryptodome.readthedocs.io/en/latest/src/util/util.html

from Crypto.Util.number import getPrime
from Crypto.Util.number import bytes_to_long, long_to_bytes

class CreatePublicKeyAndPriveteKey:
    def __init__(self, bit):
        self.encryption_bit = bit

    def create_key(self):
        if (self.encryption_bit == 1024) or (self.encryption_bit == 2048)  or (self.encryption_bit == 4096):
    # Get random N-bit prime number
            p = getPrime(self.encryption_bit)
            q = getPrime(self.encryption_bit)
            encryption_key = getPrime(16)
    # Create PublicKey and PriveteKey
            public_key = p*q
            public_key_sub = (p-1)*(q-1)
            privete_key = pow(encryption_key, -1, public_key_sub)

            return public_key, encryption_key, privete_key
        else:
            print("\nNot Inappropriate Bit Value. Please see below for the details.")
            print("> Key Langht 1024-Bit: Low Strength Key")
            print("> Key Langht 2048-Bit: Medium Strength Key")
            print("> Key Langht 4096-Bit: High Strength Key")
            exit(1)
            

class RSA_Encryption:
    def __init__(self, value, public_key, encryption_key):
        self.plaintext = value
        self.encryption_key = encryption_key
        self.public_key = public_key

    def encryption(self):
    # plaintext Type str => Type int
        plaintext_int = bytes_to_long(self.plaintext.encode('UTF-8'))
    # Encryption
        encryption_value = pow(plaintext_int, self.encryption_key, self.public_key)

        return encryption_value

class RSA_Decryption:
    def __init__(self, encryption_value, privete_key, public_key):
        self.encryption_value = encryption_value
        self.privete_key = privete_key
        self.public_key = public_key

    def decryption(self):
    # Decryption
        plaintext = long_to_bytes(pow(self.encryption_value, self.privete_key, self.public_key)).decode('UTF-8')

        return plaintext