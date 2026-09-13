import streamlit as st
import pandas as pd
from groq import Groq
from PIL import Image
import os

st.set_page_config(page_title="Malek AI - Fabric QC", layout="wide", page_icon="🧵")

# --- API Key ---
api_key = st.secrets.get("GROQ_API_KEY") or os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key) if api_key else None

# --- Login ---
if "login" not in st.session_state:
    st.session_state.login = False

if not st.session_state.login:
    st.markdown("<h1 style='text-align:center;'>🧵 Malek AI</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>আপনার ফ্যাক্টরির পাহারাদার | Your Factory Guard</p>", unsafe_allow_html=True)
    st.divider()
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.subheader("🔐 Factory Login")
        factory = st.selectbox("Factory Name", ["Gazipur Textile", "Narayanganj Knit", "Ashulia Fabrics", "Demo Factory"])
        password = st.text_input("Password", type="password", value="1234")
        st.info("Demo Password: 1234")
        if st.button("Login to Dashboard", use_container_width=True, type="primary"):
            st.session_state.login = True
            st.session_state.factory = factory
            st.rerun()
else:
    factory_name = st.session_state.factory
    st.sidebar.title(f"🏭 {factory_name}")
    st.sidebar.success("● LIVE - Connected")
    if st.sidebar.button("Logout"):
        st.session_state.login = False
        st.rerun()

    st.title("AI Fabric Inspection Dashboard")
    st.caption(f"Factory: {factory_name} | LIVE Real-time")

    # METRICS
    col1, col2, col3 = st.columns(3)
    col1.metric("আজকের পরীক্ষা", "1250 মিটার", "+120m")
    col2.metric("ত্রুটি / Defects", "14 টা", "2 critical", delta_color="inverse")
    col3.metric("নির্ভুলতা / Accuracy", "94%", "+2.1%")
    st.divider()

    left, right = st.columns([1.2, 1])

    with left:
        st.subheader("📸 কাপড়ের ছবি দিয়ে চেক করুন")
        uploaded = st.file_uploader("ফ্যাব্রিকের ছবি আপলোড করো", type=["jpg","jpeg","png"])
        if uploaded:
            img = Image.open(uploaded)
            st.image(img, caption="Uploaded Fabric", use_container_width=True)
            if st.button("🔍 AI দিয়ে ত্রুটি ধরো", type="primary", use_container_width=True):
                if not client:
                    st.error("GROQ_API_KEY Secrets এ বসাও নাই!")
                else:
                    with st.spinner("AI Scanning Fabric..."):
                        try:
                            response = client.chat.completions.create(
                                model="llama-3.2-11b-vision-preview",
                                messages=[{"role": "user", "content": "You are a textile QC expert. Look at this fabric image and tell if there is any defect like hole, stain, slub, weave gap. Answer in Bangla + English, with confidence % and location."}]
                            )
                            st.success("Result:")
                            st.write(response.choices[0].message.content)
                            st.balloons()
                        except Exception as e:
                            st.error(f"Error: {e}")

        st.divider()
        st.subheader("ত্রুটি তালিকা / Defect List")
        df = pd.DataFrame({
            "সময়": ["10:30 AM", "10:02 AM", "09:45 AM", "09:12 AM"],
            "ধরণ": ["Weave Gap", "Hole", "Stain", "Slub"],
            "অবস্থান": ["Line-A (12.5m)", "Line-C (45.2m)", "Line-B (89m)", "Line-A (102m)"],
            "Status": ["🔴 Flagged", "🟡 Pending", "🟢 Resolved", "🟢 Resolved"]
        })
        st.dataframe(df, use_container_width=True, hide_index=True)

    with right:
        st.subheader("সনাক্তকৃত ত্রুটি / Detected Defect")
        st.error("Hole Detected - 95% confidence")
        st.image("https://images.unsplash.com/photo-1520903924103-00d8a0452a04?q=80&w=600", caption="ID: DEF-1024")
        st.write("Type: Hole / ছিদ্র")
        st.button("✅ Resolve", use_container_width=True, type="primary")
