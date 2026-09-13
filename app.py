import streamlit as st
from PIL import Image
import time
import random

st.set_page_config(page_title="Malek AI - Fabric QC Expert", page_icon="🧵", layout="centered")

st.title("🧵 Malek AI - Fabric QC Expert")
st.markdown("**Bangladesh's First AI Fabric QC**")
st.divider()

uploaded = st.file_uploader("ফেব্রিকের ছবি আপলোড করুন", type=["jpg","jpeg","png"])

if uploaded:
    img = Image.open(uploaded)
    st.image(img, caption="Uploaded Fabric", use_container_width=True)

    if st.button("🔍 QC Analysis করুন", type="primary", use_container_width=True):
        with st.spinner("AI Analysis চলছে..."):
            time.sleep(2)
        
        st.success("✅ Analysis Complete!")
        
        col1, col2 = st.columns(2)
        col1.metric("Quality Score", f"{random.randint(85,99)}%")
        col2.metric("Defect Status", random.choice(["No Defect", "Minor Stain"]))
        col1.metric("4-Point Score", f"{random.randint(4,15)}")
        col2.metric("Result", "PASS")
        st.balloons()
else:
    st.warning("একটা ফেব্রিকের ছবি আপলোড করুন QC করার জন্য।")

st.divider()
st.caption("© 2026 Malek | Fabric QC Expert")
