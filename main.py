import argparse

from utils.system_functions import load_settings

SETTING_FILE = "files/settings.json"


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("-set", "--settings", type=str , help="Ввод пути к json-файлу")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-gen", "--generation", help="Запускает режим генерации ключей")
    group.add_argument("-enc", "--encryption", help="Запускает режим шифрования")
    group.add_argument("-dec", "--decryption", help="Запускает режим дешифрования")

    args = parser.parse_args()

    settings = load_settings(args.settings) if args.settings else load_settings(SETTING_FILE)

    