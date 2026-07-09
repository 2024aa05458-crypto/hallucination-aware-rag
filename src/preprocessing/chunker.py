from typing import List

from langchain_text_splitters import RecursiveCharacterTextSplitter

from src.utils.common import load_yaml
from src.utils.logger import logger


class ChunkGenerator:

    def __init__(self):

        config = load_yaml("config.yaml")

        self.chunk_size = config["chunking"]["chunk_size"]

        self.chunk_overlap = config["chunking"]["chunk_overlap"]

        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap
        )

    def generate_chunks(
        self,
        documents: List[dict]
    ) -> List[dict]:

        logger.info("Generating chunks...")

        chunks = []

        chunk_id = 1

        for document in documents:

            split_chunks = self.text_splitter.split_text(
                document["text"]
            )

            for index, chunk in enumerate(split_chunks, start=1):

                chunk_data = {

                    "chunk_id": chunk_id,

                    "document_id": document["document_id"],

                    "file_name": document["file_name"],

                    "title": document["title"],

                    "source": document["source"],

                    "document_type": document["document_type"],

                    "publisher": document["publisher"],

                    "year": document["year"],

                    "reliability_score": document["reliability_score"],

                    "type_weight": document["type_weight"],

                    "chunk_number": index,

                    "character_count": len(chunk),

                    "text": chunk

                }

                chunks.append(chunk_data)

                chunk_id += 1

        logger.info(f"Generated {len(chunks)} chunks.")

        return chunks