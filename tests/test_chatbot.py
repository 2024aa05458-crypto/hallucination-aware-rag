from src.pipeline.rag_pipeline import RAGPipeline

rag = RAGPipeline()

while True:

    question = input("\nAsk a Question (type exit to quit): ")

    if question.lower() == "exit":
        break

    result = rag.ask(question)

    print("\n" + "=" * 100)

    print("ANSWER:\n")

    print(result["answer"])

    print("\n" + "=" * 100)

    print("SOURCES:\n")

    for item in result["evidence"]:

        print(f"- {item['source']} | {item['title']}")

    print("=" * 100)