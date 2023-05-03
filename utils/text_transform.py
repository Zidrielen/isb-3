import logging


class Text_transform:
    """Class for working with encrypted and decrypted text"""

    def __init__(self) -> None:
        """Conctructor"""
        self.text = None

    def get(self) -> bytes:
        """Getter"""
        return self.text

    def set(self, new_text: bytes) -> None:
        """Setter"""
        self.text = new_text

    def byte_read_text(self, initial_txt: str) -> None:
        """
        The function reads text in byte form from .txt file

        :param file_name - name of .txt file.
        """
        try:
            with open(initial_txt, "rb") as text_file:
                self.text = text_file.read()
            logging.info(f"Text was successfully read from file {initial_txt}")
        except OSError as err:
            logging.warning(
                f"Text was not read from file {initial_txt}\n{err}")

    def byte_write_text(self, encryption_txt: str) -> None:
        """
        The function writes text in byte form to .txt file

        :param encryption_txt - name of txt file
        """
        try:
            with open(encryption_txt, "wb") as text_file:
                text_file.write(self.text)
            logging.info(
                f"Text was successfully written to file {encryption_txt}")
        except OSError as err:
            logging.warning(
                f"Text was not written to file {encryption_txt}\n{err}")
            
    txt = property(get, set)
