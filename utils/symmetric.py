import logging
import os

from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

logging.getLogger().setLevel(logging.INFO)


class symmetric:
    def __init__(self) -> None:
        '''Class for working with symmetric encryption algorithm'''
        self.__symmetric_key = None
        self.__extra_parameter = None
        
    def key_generated(self) -> None:
        '''The functiion generated a symmetric key and extra parameter'''
        self.__symmetric_key = os.urandom(32)
        self.__extra_parameter = os.urandom(16)
        logging.info(" Symmetric key and extra parameter of ChaCha20 algorithm successfully generated")

    def get_key(self) -> bytes:
        '''Getter for symmetric key'''
        return self.__symmetric_key
    
    def set_key(self, new_key: bytes) -> None:
        '''Setter for symmetric key'''
        self.__symmetric_key = new_key

    sym_key = property(get_key, set_key)

    def load_symmetric_key(self, symmetric_txt: str, extra_pam_txt: str) -> None:
        '''
        The function loads a symmetric key and extra parameter from txt file

        :param symmetric_txt - name of .txt file
        :param extra_pam_txt - name of .txt file for extra parameter
        '''

        try:
            with open(symmetric_txt, "rb") as key_file:
                self.__symmetric_key = key_file.read()
            logging.info(f" Symmetric key successfully loaded from {symmetric_txt}")

        except OSError as err:
            logging.warning(f" Symmetric key was not loaded from file {symmetric_txt}\n{err}")

        try:
            with open(extra_pam_txt, "rb") as extra_file:
                self.__extra_parameter = extra_file.read()
            logging.info(f" Extra parameter successfully loaded from {extra_pam_txt}")

        except OSError as err:
            logging.warning(f" Symmetric key was not loaded from file {extra_pam_txt}\n{err}")
    
    def save_symmetric_key(self, symmetric_txt: str, extra_pam_txt: str) -> None:
        '''
        The functiion saves a symmetric key and extra parameter to .txt

        :param symmetric_txt - name of .txt file for symmetric key
        :param extra_pam_txt - name of .txt file for extra parameter
        '''

        try:
            with open(symmetric_txt, "wb") as key_file:
                key_file.write(self.__symmetric_key)
            logging.info(f" Symmetric key successfully saved to {symmetric_txt}")
        
        except OSError as err:
            logging.warning(f" Symmetric key wasn't saved to {symmetric_txt}\n{err}")

        try:
            with open(extra_pam_txt, "wb") as extra_file:
                extra_file.write(self.__extra_parameter)
            logging.info(f" Extra parameter successfully saved to {extra_pam_txt}")

        except OSError as err:
            logging.warning(f" Extra parameter wasn't saved to {extra_pam_txt}\n{err}")

    def symmetric_encrypt(self, txt: bytes) -> bytes:
        '''
        The function encrypts an input text using symmetric key

        :param text - text for encryption
        :return - encrypted text
        '''
        
        padder = padding.ANSIX923(32).padder()
        padder_text = padder.update(txt) + padder.finalize()
        iv = os.urandom(32)
        cipher = Cipher(algorithms.ChaCha20(self.__symmetric_key, self.__extra_parameter),
                        modes.CBC(iv))
        encryptor = cipher.encryptor()
        cipher_text = encryptor.update(padder_text) + encryptor.finalize()
        logging.info(" Text encryption was successful")
        return iv + cipher_text
    
    
        