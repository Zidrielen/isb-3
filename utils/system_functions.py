import logging
import json

logging.getLogger().setLevel(logging.INFO)


def load_settings(settings_file: str) -> dict:
    settings = None

    try:
        with open(settings_file) as json_file:
            settings = json.load(json_file)
        logging.info(f" Settings file successfully loaded from {settings_file}")

    except OSError as err:
        logging.warning(f" Settings file wasn't loaded from {settings_file}\n{err}")

    return settings