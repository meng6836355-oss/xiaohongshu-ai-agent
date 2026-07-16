from openai import OpenAI
from config import OPENAI_API_KEY


client = OpenAI(
    api_key=OPENAI_API_KEY
)


def chat(prompt):

    response = client.chat.completions.create(
        model="gpt-5-mini",
        messages=[
            {
                "role": "system",
                "content": "你是一名专业的小红书运营专家"
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content
