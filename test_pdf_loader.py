from src.ingestion.pdf_loader import PDFLoader

loader = PDFLoader(
    "data/raw"
)

documents = loader.load_documents()

print(f"Documents Loaded : {len(documents)}")

for doc in documents:

    print("-" * 50)

    print(doc["file_name"])

    print(len(doc["text"]))