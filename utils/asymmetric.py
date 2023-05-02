import logging

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.serialization import load_pem_private_key

logging.getLogger().setLevel(logging.INFO)


class asymmetric:
    def __init__(self) -> None:
        '''Class for working with asymmetric encryption algorithm'''
        self.__private_key = None
        self.__public_key = None

    def keys_generated(self) -> None:
        '''The functiion generated a public and private keys'''
        keys = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        self.__private_key = keys
        self.__public_key = keys.public_key()
        logging.info(" Asymmetric keys successfully generated")

    def load_private_key(self, private_pem: str) -> None:
        '''
        The function loads a private key from .pem file

        :param private_pem - name of .pem file
        '''

        try:
            with open(private_pem, "rb") as pem_in:
                private_bytes = pem_in.read()
            self.__private_key = load_pem_private_key(private_bytes, password=None)
            logging.info(f" Private key successfully loaded from {private_pem}")

        except OSError as err:
            logging.warning(f" Private key was not loaded from file {private_pem}\n{err}")
    
    def save_asymmetric_keys(self, private_pem: str, public_pem: str) -> None:
        '''
        The function saves a private and public keys to .pem files
        
        :param private_pem - .pem file for private key
        :param public_pem - .pem file for public key
        '''

        try:
            with open(private_pem, 'wb') as private_out:
                private_out.write(self.__private_key.private_bytes(encoding=serialization.Encoding.PEM,
                                                                   format=serialization.PrivateFormat.TraditionalOpenSSL,
                                                                   encryption_algorithm=serialization.NoEncryption()))
                logging.info(f" Private key successfully saved to {private_pem}")

        except OSError as err:
            logging.warning(f" Private key wasn't saved to {private_pem}\n{err}")

        try:
            with open(public_pem, "wb") as public_out:
                public_out.write(self.__public_key.public_bytes(encoding=serialization.Encoding.PEM,
                                                                format=serialization.PublicFormat.SubjectPublicKeyInfo))
                logging.info(f" Public key successfully saved to {public_pem}")

        except OSError as err:
            logging.warning(f" Public key wasn't saved to {public_pem}\n{err}")

    def asymmetric_encrypt(self, sym_key: bytes) -> bytes:
        '''
        Encrypts an symmetrical key using public key
        
        :param sym_key - symmetrical key for encryption
        :return - encrypted symmetrical key
        '''
        
        cipher_key = self.__public_key.encrypt(sym_key,
                                               padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                            algorithm=hashes.SHA256(), label=None))
        logging.info(" Symmetrical key was encrypt successfully")
        return cipher_key
    
    def asymmetric_decrypt(self, sym_key: bytes) -> bytes:
        '''
        Decrypts an symmetrical key using private key
        
        :param sym_key - encryption symmetrical key
        :return - decrypted symmetrical key
        '''

        text = self.__private_key.decrypt(sym_key,
                                          padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                       algorithm=hashes.SHA256(), label=None))
        logging.info(" Symmetrical key was decrypt successfully")
        return text