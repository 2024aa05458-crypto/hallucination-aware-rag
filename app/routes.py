from fastapi import APIRouter

from app.schemas import ChatRequest
from src.pipeline.rag_pipeline import RAGPipeline


router = APIRouter()

rag = RAGPipeline()


@router.post("/chat")
def chat(request: ChatRequest):

    result = rag.ask(request.question)

    sources = []

    for item in result["evidence"]:

        source = f"{item['source']} | {item['title']}"

        if source not in sources:
            sources.append(source)

    confidence = round(
        sum(
            chunk["combined_score"]
            for chunk in result["evidence"]
        ) / len(result["evidence"]),
        2
    )

    return {

        "question": request.question,

        "answer": result["answer"],

        "sources": sources,

        "confidence": confidence

    }