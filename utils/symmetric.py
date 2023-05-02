from typing import List

import logging
import os
import uuid

logging.getLogger().setLevel(logging.INFO)


class symmetric:
    def __init__(self) -> None:
        '''Class for working with symmetric encryption algorithm'''
        self.__symmetric_key = os.urandom(32)
        self.__extra_parameter = os.urandom(16)
        logging.info("Summetric key and additional parameter of ChaCha20 algorithm successfully generated")

    def get_key(self) -> bytes:
        '''Getter'''
        return self.__symmetric_key
    
    def set_key(self, new_key: bytes) -> None:
        '''Setter'''
        self.__symmetric_key = new_key

    sym_key = property(get_key, set_key)
    
    def save_symmetric_key(self, symmetric_txt: str, extra_pam_txt: str) -> None:
        '''
        The functiion saves a symmetric key and extra parameter to .txt

        :param symmetric_txt - name of .txt file for symmetric key
        :param extra_pam_txt - name of .txt file for extra parameter
        '''

        try:
            with open(symmetric_txt, "wb") as key_file:
                key_file.write(self.__symmetric_key)
            logging.info(f"Symmetric key successfully saved to {symmetric_txt}")
        
        except OSError as err:
            logging.warning(f"Symmetric key wasn't saved to {symmetric_txt}\n{err}")

        
        try:
            with open(extra_pam_txt, "wb") as extra_file:
                extra_file.write(self.__extra_parameter)
            logging.info(f"Extra parameter successfully saved to {extra_pam_txt}")

        except OSError as err:
            logging.warning(f"Extra parameter wasn't saved to {extra_pam_txt}\n{err}")
