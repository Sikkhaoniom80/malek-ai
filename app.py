import streamlit as st
from groq import Groq
import datetime

st.set_page_config(page_title="MALEK AI - Fabric QC Expert", page_icon="🧵", layout="wide")

VALID_CODES = ["RAHIM-2026", "MALEK-001", "ADMIN-777", "MALEK-TEX"]

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.title("🏭 MALEK SPINNING MILLS - LOGIN")
    code = st.text_input("Factory Access Code:", type="password")
    if st.button("Login"):
        if code in VALID_CODES:
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("ভুল কোড!")
    st.stop()

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

with st.sidebar:
    st.title("🧵 MALEK AI")
    if st.button("Logout"):
        st.session_state.authenticated = False
        st.rerun()

st.title("🧵 MALEK AI - Fabric QC Expert")
st.caption("AI Powered Fabric Defect Detection")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Ask Malek AI anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "system", "content": "You are MALEK AI textile QC expert. Answer in Bangla mix."}, *st.session_state.messages],
        )
        response = completion.choices[0].message.content
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
