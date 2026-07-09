from src.retrieval.retriever import Retriever
from src.generation.evidence_aggregator import EvidenceAggregator
from src.generation.prompt_builder import PromptBuilder


retriever = Retriever()

aggregator = EvidenceAggregator()

builder = PromptBuilder()


results = retriever.retrieve(
    "What are the symptoms of Type 2 diabetes?"
)

evidence = aggregator.aggregate(results)

prompt = builder.build_prompt(
    "What are the symptoms of Type 2 diabetes?",
    evidence
)

print(prompt)