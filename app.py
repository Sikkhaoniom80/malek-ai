import streamlit as st
from groq import Groq

st.set_page_config(page_title="Malek AI", page_icon="👕")
st.title("Malek AI - Fabric Expert 👕")

if "m" not in st.session_state:
    st.session_state.m=[]

for msg in st.session_state.m:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

prompt=st.chat_input("Ask Malek AI...")

if prompt:
    st.session_state.m.append({"role":"user","content":prompt})
    with st.chat_message("user"):
        st.write(prompt)
    try:
        client=Groq(api_key=st.secrets["GROQ_API_KEY"])
        res=client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role":"system","content":"You are Malek AI fabric expert"}]+st.session_state.m)
        ans=res.choices[0].message.content
    except Exception as e:
        ans=f"Error: {e}"
    st.session_state.m.append({"role":"assistant","content":ans})
    with st.chat_message("assistant"):
        st.write(ans)
