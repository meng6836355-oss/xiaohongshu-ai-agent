"""
Xiaohongshu Content Generation Agent

Loads prompt templates and generates marketing content.
"""

from pathlib import Path
from openai_client import chat

class ContentAgent:

    def __init__(self):
        self.prompt = self.load_prompt()


    def load_prompt(self):
def load_prompt(self):

    BASE_DIR = Path(__file__).resolve().parent.parent.parent

    prompt_path = (
        BASE_DIR
        / "prompts"
        / "xhs_writer.md"
    )

    return prompt_path.read_text(
        encoding="utf-8"
    )


    def generate(self, product):

from openai_client import chat


def generate(self, product):

    prompt = self.prompt.replace(
        "{product}",
        product
    )

    result = chat(prompt)

    return result


if __name__ == "__main__":

    agent = ContentAgent()

    result = agent.generate(
        "迷你吹风机，便携，快速干发"
    )

    print(result)
