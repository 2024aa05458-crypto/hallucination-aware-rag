import yaml
from pathlib import Path

from src.constants import CONFIG_DIR


def load_yaml(file_name: str):

    file_path = CONFIG_DIR / file_name

    with open(file_path, "r", encoding="utf-8") as file:

        return yaml.safe_load(file)