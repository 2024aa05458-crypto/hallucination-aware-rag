from pathlib import Path
from typing import List
import sys

from pypdf import PdfReader

from src.preprocessing.text_cleaner import TextCleaner
from src.utils.common import load_yaml
from src.utils.logger import logger
from src.exception import CustomException


class PDFLoader:

    def __init__(self, data_path: str):

        self.data_path = Path(data_path)

        # Load metadata only once
        metadata = load_yaml("document_metadata.yaml")

        self.document_metadata = metadata["documents"]

    def load_documents(self) -> List[dict]:

        documents = []

        try:

            pdf_files = sorted(self.data_path.glob("*.pdf"))

            logger.info(f"Found {len(pdf_files)} PDF files.")

            for doc_id, pdf in enumerate(pdf_files, start=1):

                logger.info(f"Reading PDF : {pdf.name}")

                reader = PdfReader(pdf)

                text = ""

                for page in reader.pages:

                    extracted = page.extract_text()

                    if extracted:

                        text += extracted + "\n"

                cleaned_text = TextCleaner.clean(text)

                metadata = self.document_metadata.get(
                    pdf.name,
                    {
                        "source": "Unknown",
                        "document_type": "Unknown",
                        "title": pdf.stem,
                        "publisher": "Unknown",
                        "year": None,
                        "reliability_score": 0.80
                    }
                )

                document = {

                    "document_id": doc_id,

                    "file_name": pdf.name,

                    "file_path": str(pdf),

                    "total_pages": len(reader.pages),

                    "source": metadata["source"],

                    "document_type": metadata["document_type"],

                    "title": metadata["title"],

                    "publisher": metadata["publisher"],

                    "year": metadata["year"],

                    "reliability_score": metadata["reliability_score"],

                    "text": cleaned_text

                }

                documents.append(document)

                logger.info(f"{pdf.name} loaded successfully.")

            logger.info("All PDF files loaded successfully.")

            return documents

        except Exception as e:

            logger.error(e)

            raise CustomException(e, sys)