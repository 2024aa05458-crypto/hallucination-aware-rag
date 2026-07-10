from src.retrieval.retriever import Retriever
from src.generation.evidence_aggregator import EvidenceAggregator
from src.generation.prompt_builder import PromptBuilder
from src.generation.generator import LLMGenerator


class RAGPipeline:

    def __init__(self):

        self.retriever = Retriever()

        self.aggregator = EvidenceAggregator()

        self.prompt_builder = PromptBuilder()

        self.generator = LLMGenerator()

    def ask(self, question):

        retrieved = self.retriever.retrieve(question)

        evidence = self.aggregator.aggregate(retrieved)

        prompt = self.prompt_builder.build_prompt(
            question,
            evidence
        )

        answer = self.generator.generate(prompt)

        return {

            "question": question,

            "answer": answer,

            "evidence": evidence

        }