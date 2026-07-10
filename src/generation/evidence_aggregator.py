import re

from src.utils.logger import logger


class EvidenceAggregator:

    def __init__(self):
        pass

    def clean_text(self, text):

        text = text.replace("\n", " ")

        text = re.sub(r"\s+", " ", text)

        text = re.sub(r"\[[^\]]*\]", "", text)

        text = re.sub(r"\([0-9,\-\s]+\)", "", text)

        return text.strip()

    def compress_chunk(self, text):

        text = self.clean_text(text)

        sentences = re.split(r'(?<=[.!?])\s+', text)

        selected = []

        keywords = [

            "symptom",
            "symptoms",
            "clinical",
            "diagnosis",
            "treatment",
            "management",
            "prevent",
            "prevention",
            "risk",
            "complication",
            "hba1c",
            "glucose",
            "insulin",
            "diabetes"

        ]

        for sentence in sentences:

            lower = sentence.lower()

            if any(keyword in lower for keyword in keywords):

                selected.append(sentence)

            if len(selected) >= 3:

                break

        if len(selected) == 0:

            selected = sentences[:2]

        return " ".join(selected)

    def aggregate(self, retrieved_chunks):

        retrieved_chunks = sorted(

            retrieved_chunks,

            key=lambda x: x["combined_score"],

            reverse=True

        )

        evidence = []

        seen = set()

        for chunk in retrieved_chunks:

            source_key = chunk["source"] + chunk["title"]

            if source_key in seen:

                continue

            seen.add(source_key)

            chunk["compressed_chunk"] = self.compress_chunk(

                chunk["chunk"]

            )

            evidence.append(chunk)

            if len(evidence) == 4:

                break

        logger.info(f"Evidence Selected : {len(evidence)}")

        return evidence