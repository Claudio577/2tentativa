from config import get_llm

EXECUTIVE_PROMPT = """
Você é um Executivo Sênior especializado em estratégia corporativa.
Responda de maneira clara, objetiva e estruturada.
"""

def criar_agente_executivo():
    llm = get_llm()

    def agente(user_input):
        messages = [
            {"role": "system", "content": EXECUTIVE_PROMPT},
            {"role": "user", "content": user_input}
        ]
        return llm(messages)

    return agente
