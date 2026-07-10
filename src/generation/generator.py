import os
import time

from dotenv import load_dotenv
from google import genai

from src.utils.logger import logger


class LLMGenerator:

    def __init__(self):

        load_dotenv()

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise Exception("GEMINI_API_KEY not found.")

        self.client = genai.Client(api_key=api_key)

        self.models = [

            "models/gemini-3.5-flash",

            "models/gemini-3.1-flash-lite",

            "models/gemini-flash-latest",

            "models/gemini-2.0-flash"

        ]

        logger.info("Gemini Generator Initialized")

    def generate(self, prompt):

        last_exception = None

        for model in self.models:

            try:

                logger.info(f"Trying model : {model}")

                response = self.client.models.generate_content(

                    model=model,

                    contents=[
                        {
                            "role": "user",
                            "parts": [
                                {
                                    "text": prompt
                                }
                            ]
                        }
                    ]

                )

                if response.text:

                    logger.info(f"Success : {model}")

                    return response.text.strip()

            except Exception as e:

                logger.warning(f"{model} failed : {str(e)}")

                last_exception = e

                time.sleep(2)

        raise last_exception

        return "No response generated."