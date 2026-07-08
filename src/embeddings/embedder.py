from sentence_transformers import SentenceTransformer
from src.utils.common import load_yaml
from src.utils.logger import logger


class EmbeddingGenerator:

    def __init__(self):

        config = load_yaml("config.yaml")

        self.model_name = config["embedding"]["model_name"]

        logger.info(f"Loading embedding model: {self.model_name}")

        self.model = SentenceTransformer(self.model_name)

        logger.info("Embedding model loaded successfully.")

    def generate_embeddings(self, chunks):

        logger.info("Generating embeddings...")

        texts = [chunk["text"] for chunk in chunks]

        embeddings = self.model.encode(
            texts,
            show_progress_bar=True,
            convert_to_numpy=True
        )

        logger.info(f"Generated embeddings for {len(texts)} chunks.")

        return embeddings