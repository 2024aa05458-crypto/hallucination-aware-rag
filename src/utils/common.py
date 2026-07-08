import yaml
from pathlib import Path

from src.constants import CONFIG_DIR
from src.utils.logger import logger
from src.exception import CustomException

import sys


def load_yaml(file_name: str) -> dict:
    """
    Load a YAML configuration file.

    Args:
        file_name (str): Name of the YAML file.

    Returns:
        dict: Parsed YAML content.
    """

    try:

        file_path = CONFIG_DIR / file_name

        logger.info(f"Loading YAML file: {file_name}")

        with open(file_path, "r", encoding="utf-8") as yaml_file:

            data = yaml.safe_load(yaml_file)

        logger.info(f"{file_name} loaded successfully.")

        return data

    except Exception as e:

        logger.error(e)

        raise CustomException(e, sys)