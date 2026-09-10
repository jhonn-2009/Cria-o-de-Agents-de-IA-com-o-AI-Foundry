
import streamlit as st
from groq import Groq


# Configuração da página
st.set_page_config(page_title="Agente de IA - Groq", page_icon="🤖")
st.title("🤖 Chatbot IA")

# Inicializa o cliente da Groq usando a chave das variáveis de ambiente ou secrets
# Certifique-se de configurar a GROQ_API_KEY no seu ambiente
client = Groq(api_key='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')

# Inicializa o histórico de mensagens na sessão do Streamlit
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibe as mensagens anteriores do histórico
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Campo para digitação da pergunta pelo usuário
if pergunta := st.chat_input("Digite sua pergunta..."):
    # Adiciona a mensagem do usuário ao histórico
    st.session_state.messages.append({"role": "user", "content": pergunta})
    with st.chat_message("user"):
        st.markdown(pergunta)

    # Gera a resposta do modelo
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.markdown("Pensando...")

        try:
            # Chamada à API da Groq mantendo o contexto da conversa
            chat_completion = client.chat.completions.create(
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ],
                model="openai/gpt-oss-120b",
            )

            resposta = chat_completion.choices[0].message.content
            message_placeholder.markdown(resposta)

            # Salva a resposta da IA no histórico
            st.session_state.messages.append({"role": "assistant", "content": resposta})

        except Exception as e:
            message_placeholder.error(f"Erro ao conectar com a API: {e}")

# client = Groq(api_key="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")

# pergunta = input('Digite uma pergunta: ')


# chat_completion = client.chat.completions.create(
  #  messages=[
   #     {"role": "user", "content": pergunta}
  #  ],
 # model="openai/gpt-oss-120b",
#)



#print(chat_completion.choices[0].message.content)