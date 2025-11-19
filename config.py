import os
from openai import OpenAI

def get_llm():
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def call(messages):
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=0.1
        )
        return response.choices[0].message["content"]

    return call
