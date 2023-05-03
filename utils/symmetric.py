import logging
import os

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms

logging.getLogger().setLevel(logging.INFO)


class Symmetric:
    """Class for working with symmetric encryption algorithm"""

    def __init__(self) -> None:
        """Constructor"""
        self.__key = None
        self.__nonce = None

    def key_generated(self) -> None:
        """The functiion generated a symmetric key and extra parameter"""
        self.__key = os.urandom(32)
        self.__nonce = os.urandom(16)
        logging.info(
            "Symmetric key and extra parameter of ChaCha20 algorithm successfully generated")

    def get_key(self) -> bytes:
        """Getter for symmetric key"""
        return self.__key

    def set_key(self, new_key: bytes) -> None:
        """Setter for symmetric key"""
        self.__key = new_key

    sym_key = property(get_key, set_key)

    def load_symmetric_key(self, key_txt: str, nonce_txt: str) -> None:
        """
        The function loads a symmetric key and extra parameter from .txt file

        :param symmetric_txt - name of .txt file
        :param extra_pam_txt - name of .txt file for extra parameter
        """
        try:
            with open(key_txt, "rb") as key_file:
                self.__key = key_file.read()
            logging.info(f"Symmetric key successfully loaded from {key_txt}")
        except OSError as err:
            logging.warning(
                f"Symmetric key was not loaded from file {key_txt}\n{err}")
        try:
            with open(nonce_txt, "rb") as nonce_file:
                self.__nonce = nonce_file.read()
            logging.info(
                f"Extra parameter successfully loaded from {nonce_txt}")
        except OSError as err:
            logging.warning(
                f"Symmetric key was not loaded from file {nonce_txt}\n{err}")

    def save_symmetric_key(self, key_txt: str, nonce_txt: str) -> None:
        """
        The functiion saves a symmetric key and extra parameter to .txt

        :param symmetric_txt - name of .txt file for symmetric key
        :param extra_pam_txt - name of .txt file for extra parameter
        """
        try:
            with open(key_txt, "wb") as key_file:
                key_file.write(self.__key)
            logging.info(f"Symmetric key successfully saved to {key_txt}")
        except OSError as err:
            logging.warning(f"Symmetric key wasn't saved to {key_txt}\n{err}")
        try:
            with open(nonce_txt, "wb") as nonce_file:
                nonce_file.write(self.__nonce)
            logging.info(f"Extra parameter successfully saved to {nonce_txt}")
        except OSError as err:
            logging.warning(
                f"Extra parameter wasn't saved to {nonce_txt}\n{err}")

    def symmetric_encrypt(self, txt: bytes) -> bytes:
        """
        The function encrypts an input text using symmetric key

        :param txt - text for encryption
        :return - encrypted text
        """
        algorithm = algorithms.ChaCha20(self.__key, self.__nonce)
        cipher = Cipher(algorithm, mode=None)
        encryptor = cipher.encryptor()
        cipher_text = encryptor.update(txt)
        logging.info("Text was successfully encrypted")
        return cipher_text
