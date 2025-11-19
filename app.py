import streamlit as st
from agent import criar_agente

st.set_page_config(page_title="Agente Executivo", page_icon="💼")

st.title("💼 Agente Executivo — Streamlit + OpenAI")

user_input = st.text_area("Sua mensagem:", height=120)

if st.button("Enviar"):
    if not user_input.strip():
        st.warning("Digite uma mensagem antes de enviar.")
    else:
        with st.spinner("Gerando resposta..."):
            try:
                agente = criar_agente()
                resposta = agente(user_input)
                st.subheader("📘 Resposta do Agente:")
                st.write(resposta)
            except Exception as e:
                st.error(f"Ocorreu um erro: {e}")
