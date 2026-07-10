import faiss
import pickle
import numpy as np
from pathlib import Path

from src.vectorstore.base_vector_store import BaseVectorStore
from src.utils.logger import logger


class FAISSVectorStore(BaseVectorStore):

    def __init__(self):

        self.index = None

        self.index_path = Path("artifacts/faiss.index")

        self.metadata_path = Path("artifacts/faiss_metadata.pkl")


    def build_index(self, embeddings):

        logger.info("Building FAISS index...")

        embeddings = np.array(embeddings).astype("float32")

# Normalize embeddings for cosine similarity
        faiss.normalize_L2(embeddings)

        dimension = embeddings.shape[1]

        self.index = faiss.IndexFlatIP(dimension)

        self.index.add(embeddings)

        logger.info(
            f"FAISS index created with {self.index.ntotal} vectors."
        )


    def save(self):

        faiss.write_index(
            self.index,
            str(self.index_path)
        )

        logger.info("FAISS index saved.")


    def load(self):

        self.index = faiss.read_index(
            str(self.index_path)
        )

        logger.info("FAISS index loaded.")


    def search(
        self,
        query_embedding,
        top_k=3
    ):

        query_embedding = np.array([query_embedding]).astype("float32")

        faiss.normalize_L2(query_embedding)

        scores, indices = self.index.search(
            query_embedding,
            top_k
        )

        return scores, indices