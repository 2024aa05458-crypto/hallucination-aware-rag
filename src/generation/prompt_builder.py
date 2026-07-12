from src.utils.common import load_yaml
from src.utils.logger import logger


class PromptBuilder:

    def __init__(self):

        prompt = load_yaml("prompt.yaml")

        self.system_prompt = prompt["system_prompt"]

    def build_prompt(self, question, evidence):

        logger.info("Building Prompt")

        context = ""

        for item in evidence:

            context += f"""

Medical Source

Source : {item['source']}

Document : {item['title']}

Evidence

{item['compressed_chunk']}

"""

        prompt = f"""
{self.system_prompt}

You are an expert medical AI assistant specialized in diabetes.

You MUST answer ONLY using the retrieved medical evidence.

Never use outside knowledge.

--------------------------------------------------

QUESTION

{question}

--------------------------------------------------

RETRIEVED MEDICAL EVIDENCE

{context}

--------------------------------------------------

YOUR TASKS

1. Read all retrieved evidence carefully.

2. Combine information from all relevant medical sources.

3. Write a natural, fluent answer in complete English.

4. Explain the answer as if speaking to a patient.

5. NEVER copy the evidence verbatim.

6. If symptoms are mentioned in the evidence,
explicitly list them in natural language.

Example:

"Common symptoms include increased thirst, frequent urination,
increased hunger, fatigue, blurred vision and unexplained weight loss."

Do NOT simply write
"classic symptoms".

7. If diagnosis is mentioned,
explain it naturally.

8. If treatment is mentioned,
explain it naturally.

9. Verify that every statement in your answer is supported by the retrieved evidence.

10. Estimate the percentage of your answer supported by the evidence.

--------------------------------------------------

IMPORTANT

The answer field MUST contain ONLY the medical answer.

DO NOT include

- Sources
- References
- Citations
- Evidence
- Markdown
- JSON explanation
- Notes
- Bullet saying "Sources"

The frontend will display sources separately.

--------------------------------------------------

Return ONLY valid JSON.

Do NOT use markdown.

Do NOT use ```json.

Return EXACTLY this format.

{{
    "answer":"Medical answer only",

    "hallucination_risk":"Very Low",

    "evidence_coverage":95,

    "reason":"Short explanation."
}}
"""

        return prompt