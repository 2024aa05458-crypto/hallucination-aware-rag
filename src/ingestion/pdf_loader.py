from pathlib import Path
from typing import List
import sys

from pypdf import PdfReader

from src.utils.logger import logger
from src.exception import CustomException
from src.preprocessing.text_cleaner import TextCleaner


class PDFLoader:

    def __init__(self, data_path: str):
        self.data_path = Path(data_path)

    def load_documents(self) -> List[dict]:

        documents = []

        try:

            pdf_files = sorted(list(self.data_path.glob("*.pdf")))

            logger.info(f"Found {len(pdf_files)} PDF files.")

            for doc_id, pdf in enumerate(pdf_files, start=1):

                logger.info(f"Reading {pdf.name}")

                reader = PdfReader(pdf)

                text = ""

                for page in reader.pages:

                    extracted = page.extract_text()

                    if extracted:
                        text += extracted + "\n"

                # Clean the extracted text
                cleaned_text = TextCleaner.clean(text)

                # Store document metadata
                document = {
                    "document_id": doc_id,
                    "file_name": pdf.name,
                    "file_path": str(pdf),
                    "total_pages": len(reader.pages),
                    "text": cleaned_text
                }

                documents.append(document)

            logger.info("PDF loading completed successfully.")

            return documents

        except Exception as e:

            logger.error(e)

            raise CustomException(e, sys)