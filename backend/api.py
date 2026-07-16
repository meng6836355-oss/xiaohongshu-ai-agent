"""
Xiaohongshu AI Agent API

API entry point for content generation.
"""


from agents.content_agent import ContentAgent


agent = ContentAgent()


def generate_content(product):

    result = agent.generate(
        product
    )

    return result


if __name__ == "__main__":

    product = (
        "迷你吹风机，"
        "便携，"
        "快速干发"
    )

    output = generate_content(
        product
    )

    print(output)
