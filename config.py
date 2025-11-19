import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

def get_llm():
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    # Função interna que envia mensagens ao modelo
    def call(messages):
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=0.1
        )
        return response.choices[0].message["content"]

    return call
