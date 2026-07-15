import time

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

        total_start = time.perf_counter()

        retrieval_start = time.perf_counter()

        retrieved = self.retriever.retrieve(question)

        retrieval_time = round(
            time.perf_counter() - retrieval_start,
            3
        )

        aggregation_start = time.perf_counter()

        evidence = self.aggregator.aggregate(
            retrieved
        )

        aggregation_time = round(
            time.perf_counter() - aggregation_start,
            3
        )

        prompt = self.prompt_builder.build_prompt(

            question,

            evidence

        )

        generation_start = time.perf_counter()

        llm_response = self.generator.generate(
            prompt
        )

        generation_time = round(
            time.perf_counter() - generation_start,
            3
        )

        confidence = self.confidence.calculate(
            evidence
        )

        total_latency = round(
            time.perf_counter() - total_start,
            3
        )

        unique_sources = len(

            set(

                f"{item['source']}|{item['title']}"

                for item in evidence

            )

        )

        metrics = {

            "retrieved_chunks": len(retrieved),

            "evidence_chunks": len(evidence),

            "unique_sources": unique_sources,

            "answer_length": len(

                llm_response["answer"]

            ),

            "retrieval_time": retrieval_time,

            "aggregation_time": aggregation_time,

            "generation_time": generation_time,

            "total_latency": total_latency

        }

        return {

            "question": question,

            "answer": llm_response["answer"],

            "verification": {

                "hallucination_risk":

                    llm_response["hallucination_risk"],

                "evidence_coverage":

                    llm_response["evidence_coverage"],

                "reason":

                    llm_response["reason"]

            },

            "confidence": confidence,

            "evidence": evidence,

            "metrics": metrics

        }