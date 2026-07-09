from src.retrieval.retriever import Retriever
from src.generation.evidence_aggregator import EvidenceAggregator

retriever = Retriever()

aggregator = EvidenceAggregator()

results = retriever.retrieve(

    "What are the symptoms of diabetes?"

)

evidence = aggregator.aggregate(results)

print()

for item in evidence:

    print("=" * 80)

    print(item["source"])

    print(item["combined_score"])

    print()

    print(item["chunk"][:400])