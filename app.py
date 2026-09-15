import streamlit as st
from PIL import Image

st.set_page_config(page_title="Malek AI", layout="centered")

st.markdown("""
<style>
.qc-card {
    background: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    border: 1px solid #eee;
}
.complete-box {
    background: #e8f5e9;
    padding: 12px;
    border-radius: 8px;
    color: #2e7d32;
    font-weight: bold;
    margin-bottom: 15px;
}
.red-btn>button {
    background: #FF0000 !important;
    color: white !important;
    width: 100%;
    height: 50px;
    border-radius: 8px;
    font-weight: bold;
    border: none;
}
.label { color: #666; font-size: 13px; margin-top: 15px; }
.value { font-size: 32px; font-weight: bold; color: #222; }
.result-value { font-size: 32px; font-weight: bold; color: #222; letter-spacing: 1px; }
</style>
""", unsafe_allow_html=True)

st.title("🏭 Malek AI - Fabric QC")
st.caption("Bangladesh's First AI Fabric Inspector")

# Image Upload
uploaded_file = st.file_uploader("📸 কাপড়ের ছবি আপলোড করুন", type=["jpg","jpeg","png"])

if uploaded_file:
    st.image(Image.open(uploaded_file), use_container_width=True)

# Red Button like screenshot
st.markdown('<div class="red-btn">', unsafe_allow_html=True)
analyze = st.button("🔍 QC Analysis করুন")
st.markdown('</div>', unsafe_allow_html=True)

if analyze and uploaded_file:
    st.markdown("""
    <div class="qc-card">
        <div class="complete-box">✅ Analysis Complete!</div>
        <div class="label">Quality Score</div>
        <div class="value">92%</div>
        <div class="label">4-Point Score</div>
        <div class="value">11</div>
        <div class="label">Defect Status</div>
        <div class="value" style="font-size:26px;">Minor Stain</div>
        <div class="label">Result</div>
        <div class="result-value">PASS</div>
    </div>
    """, unsafe_allow_html=True)
    st.balloons()
    st.success("এই এনালাইসিস দিয়ে আমরা রিপোর্ট জানলাম: 92% Quality PASS ✅")
elif analyze:
    st.warning("আগে ছবি আপলোড করুন মামা!")
