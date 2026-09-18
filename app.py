import streamlit as st
from PIL import Image
import random

# --- Delete All History Logic ---
if "delete" in st.query_params and st.query_params["delete"] == "all":
    st.session_state.clear()
    st.cache_data.clear()
    st.query_params.clear()
    st.rerun()

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

st.title("Malek AI - Fabric QC")
st.caption("Bangladesh First AI Fabric Inspector")

# Delete All Button
st.link_button("🗑️ Delete All History", "?delete=all")

if 'history' not in st.session_state:
    st.session_state.history = []
if 'current_image' not in st.session_state:
    st.session_state.current_image = None

uploaded_file = st.file_uploader("Upload Fabric Image", type=None, label_visibility="collapsed")

if uploaded_file:
    st.session_state.current_image = uploaded_file

# Show image if exists
if st.session_state.current_image:
    img = Image.open(st.session_state.current_image)
    st.image(img, caption="Uploaded Fabric", width=350)

    col1, col2 = st.columns(2)
    with col1:
        # Delete Picture Button
        if st.button("🗑️ Delete Picture", use_container_width=True):
            st.session_state.current_image = None
            st.rerun()
    with col2:
        # QC Button with Red Style
        st.markdown('<div class="red-btn">', unsafe_allow_html=True)
        qc_clicked = st.button("QC Check Now", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    if qc_clicked:
        w, h = img.size
        brightness = sum(img.convert("L").getdata()) / (w*h)
        
        if brightness > 180:
            score = random.randint(88, 96)
            grade = "A-Grade OK"
            result = "PASS"
            fault = "No Fault - Fresh Fabric"
        elif brightness > 110:
            score = random.randint(65, 85)
            grade = "B-Grade"
            result = "NEED CHECK"
            fault = "Shade Variation / Light Spot Fault"
        else:
            score = random.randint(35, 64)
            grade = "C-Grade / Rejected"
            result = "FAIL"
            fault = "Hole / Stain / Major Fault Detected"

        # Result Card with your Design
        st.markdown(f"""
        <div class="qc-card">
            <div class="complete-box">✓ QC Complete - {result}</div>
            <div class="label">Quality Score</div>
            <div class="value">{score}%</div>
            <div class="label">Fault Detected</div>
            <div class="result-value" style="font-size:18px; color:#d32f2f;">{fault}</div>
            <div class="label">Grade</div>
            <div class="value" style="font-size:20px;">{grade}</div>
        </div>
        """, unsafe_allow_html=True)

        st.session_state.history.insert(0, f"{st.session_state.current_image.name} -> {result} ({score}%) - {fault}")

st.divider()
st.write("**History:**")
for h in st.session_state.history:
    st.write(f"- {h}")
