import argparse

from utils.asymmetric import Asymmetric
from utils.symmetric import Symmetric
from utils.system_functions import load_settings
from utils.text_transform import Text_transform

SETTING_FILE = "files/settings.json"


def console_menu():
    """
    A function with which you can generate 
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
        action="store_false",
        help="Запускает режим генерации ключей")
    group.add_argument(
        "-enc",
        "--encryption",
        action="store_false",
        help="Запускает режим шифрования")
    group.add_argument(
        "-dec",
        "--decryption",
        action="store_false",
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
            text.byte_write_text(settings["encrypted_file"])