from src.ingestion.pdf_loader import PDFLoader

loader = PDFLoader("data/raw")

documents = loader.load_documents()

print(f"\nTotal Documents Loaded : {len(documents)}\n")

for document in documents:

    print("=" * 80)

    print(f"Document ID       : {document['document_id']}")

    print(f"File Name         : {document['file_name']}")

    print(f"Title             : {document['title']}")

    print(f"Source            : {document['source']}")

    print(f"Document Type     : {document['document_type']}")

    print(f"Publisher         : {document['publisher']}")

    print(f"Publication Year  : {document['year']}")

    print(f"Reliability Score : {document['reliability_score']}")

    print(f"Pages             : {document['total_pages']}")

    print(f"Characters        : {len(document['text'])}")

    print("=" * 80)