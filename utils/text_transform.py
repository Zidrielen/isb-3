import logging
import sys


class TextTransform:
    """Class for working with encrypted and decrypted text"""

    def __init__(self) -> None:
        """Conctructor"""
        self.__text = None

    def get(self) -> bytes:
        """Getter"""
        return self.__text

    def set(self, new_text: bytes) -> None:
        """Setter"""
        self.__text = new_text

    def byte_read_text(self, initial_txt: str) -> None:
        """
        The function reads text in byte form from .txt file

        :param initial_txt - name of .txt file.
        """
        try:
            with open(initial_txt, "rb") as text_file:
                self.__text = text_file.read()
            logging.info(f"Text was successfully read from file {initial_txt}")
        except OSError as err:
            logging.warning(f"Text wasn't read from file {initial_txt}")
            sys.exit(err)

    def byte_write_text(self, encryption_txt: str) -> None:
        """
        The function writes text in byte form to .txt file

        :param encryption_txt - name of txt file
        """
        try:
            with open(encryption_txt, "wb") as text_file:
                text_file.write(self.__text)
            logging.info(
                f"Text was successfully written to file {encryption_txt}")
        except OSError as err:
            logging.warning(f"Text wasn't written to file {encryption_txt}")
            sys.exit(err)

    txt = property(get, set)