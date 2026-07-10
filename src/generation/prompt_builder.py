from src.utils.common import load_yaml
from src.utils.logger import logger


class PromptBuilder:

    def __init__(self):

        prompt = load_yaml("prompt.yaml")

        self.system_prompt = prompt["system_prompt"]

    def build_prompt(self, question, evidence):

        logger.info("Building Prompt")

        context = ""

        sources = []

        for item in evidence:

            context += f"""

Medical Source

Source : {item['source']}

Document : {item['title']}

Evidence

{item['compressed_chunk']}

"""

            sources.append(

                f"{item['source']} - {item['title']}"

            )

        unique_sources = list(dict.fromkeys(sources))

        source_text = "\n".join(unique_sources)

        prompt = f"""
{self.system_prompt}

You are answering using a trusted medical knowledge base.

Question

{question}

Medical Evidence

{context}

Instructions

Write a natural answer in complete English.

Do NOT copy the evidence.

Combine information from all sources.

Explain the answer as if speaking to a patient.

If symptoms exist, explain them naturally.

If treatment exists, explain it naturally.

End with:

Sources

{source_text}
"""

        return prompt