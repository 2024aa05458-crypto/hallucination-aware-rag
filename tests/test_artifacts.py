from src.ingestion.pdf_loader import PDFLoader
from src.preprocessing.chunker import ChunkGenerator
from src.embeddings.embedder import EmbeddingGenerator

from src.artifacts.artifact_manager import ArtifactManager


loader = PDFLoader("data/raw")

documents = loader.load_documents()


chunker = ChunkGenerator()

chunks = chunker.generate_chunks(documents)


embedder = EmbeddingGenerator()

embeddings = embedder.generate_embeddings(chunks)


artifact = ArtifactManager()

artifact.save("chunks.pkl", chunks)

artifact.save("embeddings.pkl", embeddings)


loaded_chunks = artifact.load("chunks.pkl")

loaded_embeddings = artifact.load("embeddings.pkl")


print()

print(len(loaded_chunks))

print(loaded_embeddings.shape)