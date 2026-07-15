from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import json


class DissertationCharts:

    def __init__(self):

        self.project_root = Path(__file__).resolve().parent.parent

        self.results_dir = self.project_root / "results"

        self.chart_dir = self.results_dir / "charts"

        self.chart_dir.mkdir(exist_ok=True)

        self.answers = pd.read_csv(

            self.results_dir / "answers.csv"

        )

        self.response = pd.read_csv(

            self.results_dir / "response_times.csv"

        )

        with open(

            self.results_dir / "metrics.json",

            "r",

            encoding="utf-8"

        ) as f:

            self.metrics = json.load(f)

    def save_chart(

            self,

            filename

    ):

        plt.tight_layout()

        plt.savefig(

            self.chart_dir / filename,

            dpi=300,

            bbox_inches="tight"

        )

        plt.close()

    #######################################################

    def confidence_distribution(self):

        plt.figure(

            figsize=(8,5)

        )

        plt.hist(

            self.answers["confidence"],

            bins=8,

            edgecolor="black"

        )

        plt.title(

            "Confidence Distribution"

        )

        plt.xlabel(

            "Confidence (%)"

        )

        plt.ylabel(

            "Number of Questions"

        )

        plt.grid(

            alpha=.3

        )

        self.save_chart(

            "confidence_distribution.png"

        )

    #######################################################

    def hallucination_distribution(self):

        counts = (

            self.answers

            ["hallucination_risk"]

            .value_counts()

        )

        plt.figure(

            figsize=(7,7)

        )

        plt.pie(

            counts,

            labels=counts.index,

            autopct="%1.1f%%",

            startangle=90

        )

        plt.title(

            "Hallucination Risk Distribution"

        )

        self.save_chart(

            "hallucination_distribution.png"

        )

    #######################################################

    def response_time(self):

        plt.figure(

            figsize=(10,5)

        )

        plt.plot(

            self.response["overall_runtime"],

            marker="o"

        )

        plt.title(

            "Response Time Per Question"

        )

        plt.xlabel(

            "Question Number"

        )

        plt.ylabel(

            "Seconds"

        )

        plt.grid(

            alpha=.3

        )

        self.save_chart(

            "response_time.png"

        )

    #######################################################

    def category_confidence(self):

        category = (

            self.answers

            .groupby(

                "category"

            )

            ["confidence"]

            .mean()

            .sort_values()

        )

        plt.figure(

            figsize=(10,6)

        )

        plt.barh(

            category.index,

            category.values

        )

        plt.xlabel(

            "Average Confidence"

        )

        plt.title(

            "Category-wise Average Confidence"

        )

        for i,v in enumerate(

                category.values

        ):

            plt.text(

                v+.2,

                i,

                f"{v:.1f}%"

            )

        self.save_chart(

            "category_confidence.png"

        )

    #######################################################

    def evidence_coverage(self):

        coverage = (

            self.answers

            .groupby(

                "category"

            )

            ["evidence_coverage"]

            .mean()

            .sort_values()

        )

        plt.figure(

            figsize=(10,6)

        )

        plt.barh(

            coverage.index,

            coverage.values

        )

        plt.xlabel(

            "Coverage (%)"

        )

        plt.title(

            "Evidence Coverage"

        )

        for i,v in enumerate(

                coverage.values

        ):

            plt.text(

                v+.2,

                i,

                f"{v:.1f}%"

            )

        self.save_chart(

            "evidence_coverage.png"

        )
            #######################################################

    def source_usage(self):

        source_count = {}

        for value in self.answers["sources"]:

            if pd.isna(value):

                continue

            sources = str(value).split(";")

            for source in sources:

                source = source.strip()

                if source == "":

                    continue

                source_count[source] = (

                    source_count.get(source, 0) + 1

                )

        source_df = (

            pd.DataFrame(

                source_count.items(),

                columns=[

                    "Source",

                    "Count"

                ]

            )

            .sort_values(

                "Count",

                ascending=True

            )

        )

        plt.figure(

            figsize=(12,6)

        )

        plt.barh(

            source_df["Source"],

            source_df["Count"]

        )

        plt.xlabel(

            "Usage Count"

        )

        plt.title(

            "Medical Source Usage Frequency"

        )

        for i, value in enumerate(

                source_df["Count"]

        ):

            plt.text(

                value + 0.05,

                i,

                str(value)

            )

        self.save_chart(

            "source_usage.png"

        )

    #######################################################

    def summary_dashboard(self):

        labels = [

            "Confidence",

            "Evidence\nCoverage",

            "Retrieval\nTime",

            "Generation\nTime",

            "Latency"

        ]

        values = [

            self.metrics["average_confidence"],

            self.metrics["average_evidence_coverage"],

            self.metrics["average_retrieval_time"],

            self.metrics["average_generation_time"],

            self.metrics["average_total_latency"]

        ]

        plt.figure(

            figsize=(10,5)

        )

        bars = plt.bar(

            labels,

            values

        )

        plt.title(

            "Overall Evaluation Summary"

        )

        for bar in bars:

            height = bar.get_height()

            plt.text(

                bar.get_x() + bar.get_width()/2,

                height,

                f"{height:.2f}",

                ha="center",

                va="bottom"

            )

        self.save_chart(

            "summary_dashboard.png"

        )

    #######################################################

    def generate_all(self):

        print()

        print("=" * 60)

        print("Generating Dissertation Charts")

        print("=" * 60)

        print()

        self.confidence_distribution()

        print("✓ confidence_distribution.png")

        self.hallucination_distribution()

        print("✓ hallucination_distribution.png")

        self.response_time()

        print("✓ response_time.png")

        self.category_confidence()

        print("✓ category_confidence.png")

        self.evidence_coverage()

        print("✓ evidence_coverage.png")

        self.source_usage()

        print("✓ source_usage.png")

        self.summary_dashboard()

        print("✓ summary_dashboard.png")

        print()

        print("=" * 60)

        print("Charts Generated Successfully")

        print("=" * 60)

        print()

        print(

            "Location :",

            self.chart_dir

        )


###########################################################


def main():

    charts = DissertationCharts()

    charts.generate_all()


if __name__ == "__main__":

    main()