import numpy as np
from sentence_transformers import SentenceTransformer

from src.utils.common import load_yaml
from src.utils.logger import logger

from src.vectorstore.faiss_store import FAISSVectorStore
from src.artifacts.artifact_manager import ArtifactManager


class Retriever:

    def __init__(self):

        config = load_yaml("config.yaml")

        self.top_k = config["vector_db"]["top_k"]

        self.embedding_model = SentenceTransformer(
            config["embedding"]["model_name"]
        )

        self.vector_store = FAISSVectorStore()
        self.vector_store.load()

        artifact = ArtifactManager()

        self.chunks = artifact.load("chunks.pkl")

    def retrieve(self, query):

        logger.info(f"Query : {query}")

        query_embedding = self.embedding_model.encode(
            query,
            convert_to_numpy=True
        )

        distances, indices = self.vector_store.search(
            query_embedding,
            self.top_k
        )

        retrieved_chunks = []

        for rank, (distance, index) in enumerate(
            zip(distances[0], indices[0]),
            start=1
        ):

            chunk = self.chunks[index]

            semantic_score = 1 / (1 + float(distance))

            combined_score = (
                semantic_score * 0.7
                + chunk["reliability_score"] * 0.3
            )

            retrieved_chunks.append(

                {

                    "rank": rank,

                    "chunk_id": chunk["chunk_id"],

                    "document_id": chunk["document_id"],

                    "title": chunk["title"],

                    "source": chunk["source"],

                    "document_type": chunk["document_type"],

                    "publisher": chunk["publisher"],

                    "year": chunk["year"],

                    "chunk": chunk["text"],

                    "distance": float(distance),

                    "semantic_score": round(
                        semantic_score,
                        4
                    ),

                    "reliability_score": chunk[
                        "reliability_score"
                    ],

                    "combined_score": round(
                        combined_score,
                        4
                    )

                }

            )

        logger.info(
            f"Retrieved {len(retrieved_chunks)} chunks."
        )

        return retrieved_chunks