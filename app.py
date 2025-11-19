import streamlit as st
from config import get_llm

import os
import inspect

st.title("🔍 DEBUG — Qual app.py o Streamlit está executando?")

# 1 — Mostra caminho do arquivo real
st.subheader("📌 Caminho do arquivo em execução:")
st.code(os.path.abspath(__file__))

# 2 — Mostra conteúdo do arquivo
st.subheader("📌 Conteúdo REAL do arquivo em execução:")
with open(__file__, "r") as f:
    st.code(f.read())

# 3 — Lista todos os .py do projeto
st.subheader("📌 Arquivos Python detectados no projeto:")
for root, dirs, files in os.walk("/mount/src"):
    for file in files:
        if file.endswith(".py"):
            st.write(os.path.join(root, file))

st.info("Envie a screenshot desse resultado aqui.")

st.set_page_config(page_title="Agente Executivo", page_icon="💼")

st.title("💼 Agente Executivo — LangChain + Streamlit")

st.write("Envie uma pergunta para o agente executivo baseado em GPT-4o-mini:")

# cria agente simples
def criar_agente_executivo():
    llm = get_llm()

    def agente(user_input):
        messages = [
            {"role": "system", "content": "Você é um executivo sênior especialista em estratégia corporativa."},
            {"role": "user", "content": user_input}
        ]
        return llm(messages)

    return agente


user_input = st.text_area("Sua mensagem:", height=120)

if st.button("Enviar"):
    if not user_input.strip():
        st.warning("Digite uma mensagem antes de enviar.")
    else:
        with st.spinner("Gerando resposta..."):
            try:
                agente = criar_agente_executivo()
                resposta = agente(user_input)

                st.subheader("📘 Resposta do Agente:")
                st.write(resposta)

            except Exception as e:
                st.error(f"Ocorreu um erro ao gerar a resposta: {e}")

st.markdown("---")
st.caption("Aplicação construída com Streamlit + OpenAI")
