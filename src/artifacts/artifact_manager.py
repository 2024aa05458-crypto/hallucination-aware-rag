import pickle
from pathlib import Path

from src.utils.logger import logger


class ArtifactManager:

    def __init__(self):

        self.artifact_dir = Path("artifacts")

        self.artifact_dir.mkdir(exist_ok=True)

    def save(self, file_name, data):

        path = self.artifact_dir / file_name

        with open(path, "wb") as file:

            pickle.dump(data, file)

        logger.info(f"{file_name} saved successfully.")

    def load(self, file_name):

        path = self.artifact_dir / file_name

        with open(path, "rb") as file:

            data = pickle.load(file)

        logger.info(f"{file_name} loaded successfully.")

        return data