import re

from src.utils.logger import logger


class TextCleaner:

    @staticmethod
    def clean(text: str) -> str:

        logger.info("Cleaning document...")

        # Remove multiple spaces
        text = re.sub(r"\s+", " ", text)

        # Remove multiple newlines
        text = re.sub(r"\n+", "\n", text)

        # Remove tabs
        text = text.replace("\t", " ")

        return text.strip()