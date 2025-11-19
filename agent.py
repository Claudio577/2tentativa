from openai import OpenAI
import os

EXECUTIVE_PROMPT = """
Você é um Executivo Sênior especializado em estratégia corporativa.
Responda de maneira clara, objetiva e estruturada.
"""

def criar_agente():
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def responder(user_input):
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": EXECUTIVE_PROMPT},
                {"role": "user", "content": user_input}
            ],
            temperature=0.1
        )
        return response.choices[0].message["content"]

    return responder
