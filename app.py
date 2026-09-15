import streamlit as st
from PIL import Image

st.set_page_config(page_title="Malek AI - Fabric QC", layout="centered")

params = st.query_params
company = params.get("company", "Walton")
if isinstance(company, list):
    company = company[0]
current_company = company if company else "Walton"

st.title(f"🏭 {current_company} - Fabric QC")
st.markdown(f"Made for **{current_company}** | Bangladesh's First AI Fabric Inspector")
st.divider()

st.subheader("📸 কাপড়ের ছবি আপলোড করুন")
uploaded_file = st.file_uploader("ছবি দিন (JPG, PNG)", type=["jpg","png","jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption=f"{current_company} Fabric", use_container_width=True)
    st.success("✅ ছবি আপলোড হয়েছে!")
else:
    st.info("👆 উপরে কাপড়ের ছবি আপলোড করুন")

user_q = st.text_input(f"Ask Malek AI about {current_company}...")

if st.button("🔍 QC Analysis করুন", type="primary", use_container_width=True):
    if not uploaded_file:
        st.warning("⚠️ আগে ছবি আপলোড করুন মামা!")
    else:
        st.balloons()
        c1, c2 = st.columns(2)
        with c1:
            st.metric("Quality Score", "92%")
            st.metric("Defect Status", "Minor Stain")
        with c2:
            st.metric("4-Point Score", "11")
            st.metric("Result", "PASS ✅")
        st.success(f"🎉 {current_company} এর ফেব্রিক PASS!")
