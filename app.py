import streamlit as st
from agents.agente_executivo import criar_agente_executivo
import pkg_resources

st.write("📦 PACOTES INSTALADOS:")
st.code("\n".join(sorted([d.project_name + '==' + d.version for d in pkg_resources.working_set])))

# ⚠️ OBRIGATÓRIO: nada pode vir antes desta linha
st.set_page_config(page_title="Agente Executivo", page_icon="💼")

st.title("💼 Agente Executivo — Streamlit + OpenAI")

st.write("Envie uma pergunta para o agente executivo baseado em GPT-4o-mini:")

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
