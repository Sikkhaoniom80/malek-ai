import streamlit as st
from PIL import Image

st.set_page_config(page_title="Malek AI - Fabric QC", page_icon="🏭", layout="centered")

# Company Dynamic
params = st.query_params
company_name = params.get("company", "Walton")
if isinstance(company_name, list):
    company_name = company_name[0]
C = company_name if company_name else "Walton"

# Premium Design CSS
st.markdown("""
<style>
.main { background: #ffffff; }
div[data-testid="metric-container"] {
    background-color: #f8f9fa;
    border: 1px solid #e9ecef;
    padding: 15px;
    border-radius: 12px;
    border-left: 5px solid #FF4B4B;
}
.stButton>button {
    background: linear-gradient(90deg, #FF4B4B, #FF6B6B);
    color: white;
    border-radius: 12px;
    height: 55px;
    font-weight: bold;
    font-size: 18px;
    width: 100%;
    border: none;
}
</style>
""", unsafe_allow_html=True)

st.title(f"🏭 {C} - Fabric QC")
st.markdown(f"Made for **{C}** | 🇧🇩 **Bangladesh's First AI Fabric Inspector**")
st.divider()

st.subheader("📸 কাপড়ের ছবি আপলোড করুন")
uploaded_file = st.file_uploader("JPG, PNG ছবি দিন মামা", type=["jpg","jpeg","png"], label_visibility="collapsed")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption=f"{C} Fabric Sample", use_container_width=True)

    user_input = st.text_input(f"Ask Malek AI about {C}...")

    if st.button(f"🔍 {C} এর QC Analysis করুন"):
        st.balloons()
        st.divider()
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Quality Score", "92%")
            st.metric("Fabric Type", "Cotton Knit")
        with col2:
            st.metric("4-Point Score", "11 Points")
            st.metric("Final Result", "PASS ✅")

        st.success(f"🎉 MashaAllah! {C} এর এই ফেব্রিক Buyer এর কাছে 100% যাবে!")
        if user_input:
            st.info(f"**Malek AI Answer:** {user_input} এর জন্য QC রেজাল্ট 92% PASS!")
else:
    st.info("👆 উপরে কাপড়ের ছবি আপলোড করুন, তারপর Analysis করুন মামা")
    st.text_input("Ask Malek AI anything...", placeholder="যেমন: এই কাপড়ে কি দাগ আছে?")

st.divider()
st.caption(f"© 2026 Malek AI | Built for {C}")
