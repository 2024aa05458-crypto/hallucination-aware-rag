from src.utils.common import load_yaml
from src.utils.logger import logger


class PromptBuilder:

    def __init__(self):

        prompt_config = load_yaml("prompt.yaml")

        self.system_prompt = prompt_config["system_prompt"]

    def build_prompt(
        self,
        question,
        evidence
    ):

        logger.info("Building LLM prompt...")

        context = ""

        for item in evidence:

            context += (
                f"\nSource: {item['source']}"
                f"\nTitle: {item['title']}"
                f"\nEvidence:\n{item['chunk']}\n"
            )

        prompt = f"""
{self.system_prompt}

Context:
{context}

Question:
{question}

Answer:
"""

        return prompt