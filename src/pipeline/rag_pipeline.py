from src.retrieval.retriever import Retriever
from src.generation.evidence_aggregator import EvidenceAggregator
from src.generation.prompt_builder import PromptBuilder
from src.generation.generator import LLMGenerator

from src.confidence.confidence_calculator import ConfidenceCalculator


class RAGPipeline:

    def __init__(self):

        self.retriever = Retriever()

        self.aggregator = EvidenceAggregator()

        self.prompt_builder = PromptBuilder()

        self.generator = LLMGenerator()

        self.confidence = ConfidenceCalculator()

    def ask(self, question):

        retrieved = self.retriever.retrieve(question)

        evidence = self.aggregator.aggregate(retrieved)

        prompt = self.prompt_builder.build_prompt(

            question,

            evidence

        )

        llm_response = self.generator.generate(prompt)

        confidence = self.confidence.calculate(

            evidence

        )

        return {

            "question": question,

            "answer": llm_response["answer"],

            "verification": {

                "hallucination_risk": llm_response["hallucination_risk"],

                "evidence_coverage": llm_response["evidence_coverage"],

                "reason": llm_response["reason"]

            },

            "confidence": confidence,

            "evidence": evidence

        }