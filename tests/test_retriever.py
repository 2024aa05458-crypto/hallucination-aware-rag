from src.retrieval.retriever import Retriever

retriever = Retriever()

results = retriever.retrieve(

    "How can diabetes be prevented?"

)

print()

for result in results:

    print("=" * 100)

    print("Rank :", result["rank"])

    print("Source :", result["source"])

    print("Title :", result["title"])

    print("Combined Score :", result["combined_score"])

    print()

    print(result["chunk"][:700])