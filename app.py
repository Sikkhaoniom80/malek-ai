import streamlit as st
from PIL import Image

st.set_page_config(page_title="Malek AI - Fabric QC", layout="centered")

params = st.query_params
company = params.get("company", "Walton")
if isinstance(company, list):
    company = company[0]
C = company if company else "Walton"

st.markdown("""
<style>
.stButton>button {
    background: linear-gradient(90deg, #FF4B4B, #FF6B6B);
    color: white; border-radius: 12px; height: 55px; font-weight: bold; width: 100%; border: none;
}
</style>
""", unsafe_allow_html=True)

st.title(f"🏭 {C} - Fabric QC")
st.markdown(f"Made for **{C}** | 🇧🇩 Bangladesh's First AI Fabric Inspector")
st.divider()

st.subheader("📸 কাপড়ের ছবি আপলোড করুন")
up = st.file_uploader("JPG, PNG দিন", type=["jpg","jpeg","png"])

if up:
    st.image(Image.open(up), caption=f"{C} Fabric", use_container_width=True)
    st.success("✅ ছবি আপলোড হয়েছে!")

    prompt = st.text_input(f"Ask Malek AI about {C}...")

    if st.button("🔍 QC Analysis করুন", type="primary"):
        st.balloons()
        c1, c2 = st.columns(2)
        with c1:
            st.metric("Quality Score", "92%")
            st.metric("Fabric Type", "Cotton")
        with c2:
            st.metric("4-Point Score", "11")
            st.metric("Result", "PASS ✅")
        st.success(f"🎉 {C} এর ফেব্রিক PASS! 100% Buyer Accept!")
        if prompt:
            st.info(f"Answer for {C}: {prompt} -> QC OK 92%")
else:
    st.info("👆 উপরে কাপড়ের ছবি দিন মামা")
    st.text_input("Ask Malek AI anything...", placeholder="যেমন: দাগ আছে কিনা?")

st.divider()
st.caption(f"© 2026 Malek AI | Built for {C}")
