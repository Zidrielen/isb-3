import argparse
import json
import logging

from utils.asymmetric import Asymmetric
from utils.symmetric import Symmetric
from utils.text_transform import Text_transform

SETTING_FILE = "files/settings.json"


def load_settings(settings_file: str) -> dict:
    """Loads a configuration file into the program"""
    settings = None
    try:
        with open(settings_file) as json_file:
            settings = json.load(json_file)
        logging.info(
            f"Settings file successfully loaded from {settings_file}")
    except OSError as err:
        logging.warning(
            f"Settings file wasn't loaded from {settings_file}\n{err}")
    return settings


def console_menu() -> None:
    """
    The function with which you can generate
    keys, encrypt and decrypt messages
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-set",
        "--settings",
        type=str,
        help="Ввод пути к json-файлу")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "-gen",
        "--generation",
        action="store_true",
        help="Запускает режим генерации ключей")
    group.add_argument(
        "-enc",
        "--encryption",
        action="store_true",
        help="Запускает режим шифрования")
    group.add_argument(
        "-dec",
        "--decryption",
        action="store_true",
        help="Запускает режим дешифрования")
    args = parser.parse_args()
    settings = load_settings(args.settings) if args.settings else load_settings(SETTING_FILE)
    if settings:
        if args.generation:
            sym = Symmetric()
            asym = Asymmetric()
            sym.key_generated()
            asym.keys_generated()
            sym.sym_key = asym.asymmetric_encrypt(sym.sym_key)
            asym.save_asymmetric_keys(
                settings["private_key"],
                settings["public_key"])
            sym.save_symmetric_key(
                settings["symmetric_key"],
                settings["extra_parameter"])
            logging.info("Keys generation completed")
        elif args.encryption:
            sym = Symmetric()
            asym = Asymmetric()
            text = Text_transform()
            asym.load_private_key(settings["private_key"])
            sym.load_symmetric_key(
                settings["symmetric_key"],
                settings["extra_parameter"])
            sym.sym_key = asym.asymmetric_decrypt(sym.sym_key)
            text.byte_read_text(settings["initial_file"])
            text.txt = sym.symmetric_encrypt(text.txt)
            text.byte_write_text(settings["encryption_file"])
            logging.info("Encryption completed")
        elif args.decryption:
            sym = Symmetric()
            asym = Asymmetric()
            text = Text_transform()
            asym.load_private_key(settings["private_key"])
            sym.load_symmetric_key(
                settings["symmetric_key"],
                settings["extra_parameter"])
            sym.sym_key = asym.asymmetric_decrypt(sym.sym_key)
            text.byte_read_text(settings["encryption_file"])
            text.txt = sym.symmetric_decrypt(text.txt)
            text.byte_write_text(settings["decryption_file"])
            logging.info("Decryption completed")