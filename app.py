import streamlit as st
from datetime import datetime
import time

st.set_page_config(page_title="Malek AI - A-Grade QC", page_icon="🏭", layout="centered")

# --- Delete System ---
if "delete" in st.query_params and st.query_params["delete"] == "all":
    st.session_state.clear()
    st.cache_data.clear()
    st.query_params.clear()
    st.rerun()

if 'qc_history' not in st.session_state:
    st.session_state.qc_history = []
if 'count' not in st.session_state:
    st.session_state.count = 0

st.title("🏭 Fab Inspector")
st.caption("Bangladesh's First AI Fabric Inspector - Malek AI")

st.link_button("🗑️ সব History ডিলিট করুন", "?delete=all")

# --- Upload ---
uploaded_file = st.file_uploader(
    "📸 কাপড়ের ছবি আপলোড করুন (200MB পর্যন্ত)",
    type=['jpg','jpeg','png'],
    key=f"fabric_{st.session_state.count}"
)

if uploaded_file:
    if 'prev_file' not in st.session_state or st.session_state.prev_file != uploaded_file.name:
        st.session_state.prev_file = uploaded_file.name
        st.session_state.count += 1
        st.rerun()

    st.image(uploaded_file, width=300)

    if st.button("🔍 QC Analysis করুন", type="primary", width="stretch"):
        with st.spinner("AI Analysis হচ্ছে..."):
            time.sleep(1)
            # --- এখানে আপনার AI Model বসবে ---
            defects_found = ["Minor Stain"]
            four_point = 11
            
            major_keywords = ["oil", "তেল", "ছেঁড়া", "chera", "tear", "hole", "ফুটা"]
            is_major = any(m in str(defects_found).lower() for m in major_keywords)

            if is_major or four_point > 20:
                result = "❌ FAIL - B-Grade"
                grade = "B-Grade - Reject"
                score = "0%"
            else:
                result = "✅ PASS - A-Grade"
                grade = "A-Grade - Shipment OK"
                score = "92%"

            record = {
                "date": datetime.now().strftime("%d/%m %I:%M %p"),
                "image": uploaded_file.name,
                "score": score,
                "point": four_point,
                "defect": ", ".join(defects_found),
                "result": result,
                "grade": grade
            }
            st.session_state.qc_history.insert(0, record)

        st.success(f"{record['result']} | Score: {score}")
        st.metric("4-Point Score", four
