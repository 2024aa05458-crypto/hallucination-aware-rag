import os
import sys
import json
import time
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

sys.path.append(str(PROJECT_ROOT))

import pandas as pd

from src.pipeline.rag_pipeline import RAGPipeline

class RAGEvaluator:

    def __init__(self):

        self.rag = RAGPipeline()

        self.base_dir = Path(__file__).resolve().parent.parent

        self.evaluation_dir = self.base_dir / "evaluation"

        self.results_dir = self.base_dir / "results"

        self.results_dir.mkdir(exist_ok=True)

        (self.results_dir / "charts").mkdir(exist_ok=True)

        self.questions_file = (
            self.evaluation_dir /
            "benchmark_questions.csv"
        )

        self.answers_file = (
            self.results_dir /
            "answers.csv"
        )

        self.report_file = (
            self.results_dir /
            "evaluation_report.csv"
        )

        self.metrics_file = (
            self.results_dir /
            "metrics.json"
        )

        self.response_time_file = (
            self.results_dir /
            "response_times.csv"
        )

    def load_questions(self):

        if not self.questions_file.exists():

            raise FileNotFoundError(

                f"Benchmark file not found : "

                f"{self.questions_file}"

            )

        df = pd.read_csv(

            self.questions_file

        )

        if "question" not in df.columns:

            raise Exception(

                "benchmark_questions.csv "

                "must contain a "

                "'question' column."

            )

        return df

    def evaluate(self):

        questions = self.load_questions()

        answers = []

        response_times = []

        total_questions = len(questions)

        print()

        print("=" * 70)

        print("Hallucination-Aware RAG Evaluation")

        print("=" * 70)

        print()

        print(

            f"Questions Loaded : "

            f"{total_questions}"

        )

        print()

        for index, row in questions.iterrows():

            question = row["question"]

            category = row.get(

                "category",

                "General"

            )

            difficulty = row.get(

                "difficulty",

                "Unknown"

            )

            print(

                f"[{index+1}/{total_questions}] "

                f"{question}"

            )

            start = time.perf_counter()

            result = self.rag.ask(

                question

            )

            elapsed = round(

                time.perf_counter() - start,

                3

            )

            confidence = result["confidence"]

            verification = result["verification"]

            metrics = result["metrics"]

            evidence = result["evidence"]

            sources = []

            for item in evidence:

                source = (

                    f"{item['source']}"

                    f" | "

                    f"{item['title']}"

                )

                if source not in sources:

                    sources.append(source)

            answers.append(

                {

                    "question":

                        question,

                    "category":

                        category,

                    "difficulty":

                        difficulty,

                    "answer":

                        result["answer"],

                    "confidence":

                        confidence["confidence"],

                    "semantic_score":

                        confidence["semantic_score"],

                    "reliability_score":

                        confidence["reliability_score"],

                    "type_weight":

                        confidence["type_weight"],

                    "source_agreement":

                        confidence["source_agreement"],

                    "hallucination_risk":

                        verification["hallucination_risk"],

                    "evidence_coverage":

                        verification["evidence_coverage"],

                    "reason":

                        verification["reason"],

                    "retrieved_chunks":

                        metrics["retrieved_chunks"],

                    "evidence_chunks":

                        metrics["evidence_chunks"],

                    "unique_sources":

                        metrics["unique_sources"],

                    "answer_length":

                        metrics["answer_length"],

                    "retrieval_time":

                        metrics["retrieval_time"],

                    "aggregation_time":

                        metrics["aggregation_time"],

                    "generation_time":

                        metrics["generation_time"],

                    "total_latency":

                        metrics["total_latency"],

                    "overall_runtime":

                        elapsed,

                    "sources":

                        "; ".join(sources)

                }

            )

            response_times.append(

                {

                    "question":

                        question,

                    "retrieval_time":

                        metrics["retrieval_time"],

                    "generation_time":

                        metrics["generation_time"],

                    "total_latency":

                        metrics["total_latency"],

                    "overall_runtime":

                        elapsed

                }

            )

            print(

                f"Confidence : "

                f"{confidence['confidence']}%"

            )

            print(

                f"Hallucination : "

                f"{verification['hallucination_risk']}"

            )

            print(

                f"Latency : "

                f"{metrics['total_latency']} sec"

            )

            print()
            answers_df = pd.DataFrame(

            answers

        )

        response_df = pd.DataFrame(

            response_times

        )

        answers_df.to_csv(

            self.answers_file,

            index=False

        )

        response_df.to_csv(

            self.response_time_file,

            index=False

        )

        average_confidence = round(

            answers_df["confidence"].mean(),

            2

        )

        average_semantic = round(

            answers_df["semantic_score"].mean(),

            3

        )

        average_reliability = round(

            answers_df["reliability_score"].mean(),

            3

        )

        average_type_weight = round(

            answers_df["type_weight"].mean(),

            3

        )

        average_source_agreement = round(

            answers_df["source_agreement"].mean(),

            3

        )

        average_coverage = round(

            answers_df["evidence_coverage"].mean(),

            2

        )

        average_latency = round(

            response_df["total_latency"].mean(),

            3

        )

        average_generation = round(

            response_df["generation_time"].mean(),

            3

        )

        average_retrieval = round(

            response_df["retrieval_time"].mean(),

            3

        )

        average_answer_length = round(

            answers_df["answer_length"].mean(),

            2

        )

        risk_distribution = (

            answers_df["hallucination_risk"]

            .value_counts()

            .to_dict()

        )

        category_summary = (

            answers_df

            .groupby("category")

            .agg(

                {

                    "confidence":"mean",

                    "evidence_coverage":"mean",

                    "total_latency":"mean"

                }

            )

            .round(2)

            .reset_index()

        )

        category_summary.to_csv(

            self.report_file,

            index=False

        )

        metrics = {

            "questions":

                total_questions,

            "average_confidence":

                average_confidence,

            "average_semantic_score":

                average_semantic,

            "average_reliability_score":

                average_reliability,

            "average_type_weight":

                average_type_weight,

            "average_source_agreement":

                average_source_agreement,

            "average_evidence_coverage":

                average_coverage,

            "average_retrieval_time":

                average_retrieval,

            "average_generation_time":

                average_generation,

            "average_total_latency":

                average_latency,

            "average_answer_length":

                average_answer_length,

            "hallucination_distribution":

                risk_distribution

        }

        with open(

            self.metrics_file,

            "w",

            encoding="utf-8"

        ) as f:

            json.dump(

                metrics,

                f,

                indent=4

            )

        print()

        print("=" * 70)

        print("Evaluation Complete")

        print("=" * 70)

        print()

        print(

            f"Questions Evaluated : "

            f"{total_questions}"

        )

        print(

            f"Average Confidence : "

            f"{average_confidence}%"

        )

        print(

            f"Average Evidence Coverage : "

            f"{average_coverage}%"

        )

        print(

            f"Average Retrieval Time : "

            f"{average_retrieval} sec"

        )

        print(

            f"Average Generation Time : "

            f"{average_generation} sec"

        )

        print(

            f"Average Total Latency : "

            f"{average_latency} sec"

        )

        print()

        print(

            "Hallucination Distribution"

        )

        for key, value in risk_distribution.items():

            print(

                f"{key} : {value}"

            )

        print()

        print(

            f"Answers Saved : "

            f"{self.answers_file}"

        )

        print(

            f"Metrics Saved : "

            f"{self.metrics_file}"

        )

        print(

            f"Report Saved : "

            f"{self.report_file}"

        )

        print(

            f"Response Times Saved : "

            f"{self.response_time_file}"

        )

        print()

        return metrics


def main():

    evaluator = RAGEvaluator()

    evaluator.evaluate()


if __name__ == "__main__":

    main()