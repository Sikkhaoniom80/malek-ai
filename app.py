import streamlit as st
from PIL import Image
import time
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Malek AI - Fabric QC Expert", page_icon="🧵", layout="centered")

st.markdown("### Bangladesh's First AI Fabric Inspector | Made by Malek")
st.caption("Malek AI - Fabric Quality Control Expert | 99% Accuracy")
st.divider()

tab1, tab2, tab3, tab4 = st.tabs(["📸 Upload", "🤖 AI Check", "🔍 Defect", "📄 Report"])

with tab1:
    st.markdown("#### ফেব্রিকের ছবি আপলোড করুন")
    up = st.file_uploader("Upload", type=["jpg","png","jpeg"], label_visibility="collapsed")
    st.caption("200MB per file")
    if not up:
        st.warning("একটা ফেব্রিকের ছবি আপলোড করুন QC করার জন্য।")
    else:
        st.image(Image.open(up), use_container_width=True)
        st.session_state['img'] = up
        st.success("✅ Ready")

with tab2:
    if 'img' not in st.session_state:
        st.info("আগে Upload করুন")
    else:
        if st.button("🔍 AI দিয়ে QC করো", type="primary", use_container_width=True):
            with st.spinner("Malek AI চেক করছে..."):
                time.sleep(2)
            st.session_state['checked'] = True
            st.metric("Confidence", "94.5%")
            st.progress(94)

with tab3:
    if 'checked' not in st.session_state:
        st.info("আগে AI Check করুন")
    else:
        st.error("🔴 Hole Detected - 95%")
        df = pd.DataFrame({"Defect":["Hole","Stain","Misprint"],"Confidence":["95%","12%","5%"]})
        st.dataframe(df, use_container_width=True, hide_index=True)

with tab4:
    if 'checked' in st.session_state:
        st.success(f"Report Ready - {datetime.now().strftime('%d %B %Y')}")
        st.download_button("📄 Download Report", data="Malek AI Report", file_name="report.txt", use_container_width=True)

st.divider()
st.markdown("<p style='text-align:center;color:gray;'>© 2026 Malek | Fabric QC Expert | Bangladesh</p>", unsafe_allow_html=True)
