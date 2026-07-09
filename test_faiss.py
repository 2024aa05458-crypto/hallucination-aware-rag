from src.artifacts.artifact_manager import ArtifactManager
from src.vectorstore.faiss_store import FAISSVectorStore


artifact = ArtifactManager()

embeddings = artifact.load("embeddings.pkl")


vector_store = FAISSVectorStore()

vector_store.build_index(embeddings)

vector_store.save()

vector_store.load()

print()

print("Vectors in Index")

print(vector_store.index.ntotal)