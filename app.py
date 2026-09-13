import streamlit as st
from groq import Groq

st.title("MALEK AI")
st.write("AI Powered Fabric Defect Detection")

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input("Ask Malek AI anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=st.session_state.messages,
        stream=True,
    )
    with st.chat_message("assistant"):
        response = st.write_stream((chunk.choices[0].delta.content for chunk in completion if chunk.choices[0].delta.content))
    st.session_state.messages.append({"role": "assistant", "content": response})
