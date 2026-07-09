from src.pipeline.ingestion_pipeline import IngestionPipeline

pipeline = IngestionPipeline()

result = pipeline.run()

print()

print("Pipeline Executed Successfully")

print()

print(f"Documents : {len(result['documents'])}")

print(f"Chunks : {len(result['chunks'])}")

print(f"Embeddings : {result['embeddings'].shape}")