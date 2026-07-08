from src.ingestion.pdf_loader import PDFLoader
from src.preprocessing.chunker import ChunkGenerator
from src.embeddings.embedder import EmbeddingGenerator

loader = PDFLoader("data/raw")
documents = loader.load_documents()

chunker = ChunkGenerator()
chunks = chunker.generate_chunks(documents)

embedder = EmbeddingGenerator()

embeddings = embedder.generate_embeddings(chunks)

print()

print(f"Chunks : {len(chunks)}")

print(f"Embeddings Shape : {embeddings.shape}")

print()

print("First Embedding")

print(embeddings[0][:15])