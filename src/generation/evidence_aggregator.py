from src.utils.logger import logger


class EvidenceAggregator:

    def __init__(self):
        pass

    def aggregate(self, retrieved_chunks):

        logger.info("Aggregating retrieved evidence...")

        unique_documents = set()

        aggregated = []

        for chunk in retrieved_chunks:

            key = (
                chunk["document_id"],
                chunk["chunk_id"]
            )

            if key not in unique_documents:

                unique_documents.add(key)

                aggregated.append(chunk)

        aggregated = sorted(
            aggregated,
            key=lambda x: x["combined_score"],
            reverse=True
        )

        logger.info(
            f"Evidence aggregated: {len(aggregated)} chunks."
        )

        return aggregated