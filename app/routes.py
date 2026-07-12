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

    return {

        "question": result["question"],

        "answer": result["answer"],

        "sources": sources,

        "confidence": result["confidence"],

        "verification": result["verification"]

    }