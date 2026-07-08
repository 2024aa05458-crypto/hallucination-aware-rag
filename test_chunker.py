from src.ingestion.pdf_loader import PDFLoader
from src.preprocessing.chunker import ChunkGenerator

loader = PDFLoader("data/raw")

documents = loader.load_documents()

chunker = ChunkGenerator()

chunks = chunker.generate_chunks(documents)

print(f"\nTotal Documents : {len(documents)}")

print(f"Total Chunks    : {len(chunks)}\n")

print("=" * 80)

print("Sample Chunk")

print("=" * 80)

sample = chunks[0]

for key, value in sample.items():

    if key == "text":

        print(f"\n{key}")

        print("-" * 60)

        print(value[:700])

    else:

        print(f"{key:<20}: {value}")