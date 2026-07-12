from collections import Counter


class ConfidenceCalculator:

    def __init__(self):
        pass

    def calculate(self, evidence):

        semantic = sum(
            chunk["semantic_score"]
            for chunk in evidence
        ) / len(evidence)

        reliability = sum(
            chunk["reliability_score"]
            for chunk in evidence
        ) / len(evidence)

        type_weight = sum(
            chunk["type_weight"]
            for chunk in evidence
        ) / len(evidence)

        unique_sources = len(
            set(
                chunk["source"]
                for chunk in evidence
            )
        )

        agreement = min(unique_sources / 4, 1.0)

        confidence = (

            semantic * 0.35 +

            reliability * 0.25 +

            type_weight * 0.20 +

            agreement * 0.20

        )

        confidence = round(confidence * 100, 2)

        return {

            "semantic_score": round(semantic, 3),

            "reliability_score": round(reliability, 3),

            "type_weight": round(type_weight, 3),

            "source_agreement": round(agreement, 3),

            "confidence": confidence

        }