from src.ingestion.pdf_loader import PDFLoader
from src.preprocessing.chunker import ChunkGenerator
from src.embeddings.embedder import EmbeddingGenerator
from src.artifacts.artifact_manager import ArtifactManager

from src.utils.logger import logger


class IngestionPipeline:

    def __init__(self):

        self.loader = PDFLoader("data/raw")

        self.chunker = ChunkGenerator()

        self.embedder = EmbeddingGenerator()

        self.artifact = ArtifactManager()

    def run(self):

        logger.info("=" * 60)
        logger.info("Starting Ingestion Pipeline")
        logger.info("=" * 60)

        # Load PDFs
        documents = self.loader.load_documents()

        # Generate Chunks
        chunks = self.chunker.generate_chunks(documents)

        # Generate Embeddings
        embeddings = self.embedder.generate_embeddings(chunks)

        # Save Artifacts
        self.artifact.save("documents.pkl", documents)
        self.artifact.save("chunks.pkl", chunks)
        self.artifact.save("embeddings.pkl", embeddings)

        logger.info("=" * 60)
        logger.info("Pipeline Completed Successfully")
        logger.info("=" * 60)

        return {

            "documents": documents,

            "chunks": chunks,

            "embeddings": embeddings

        }