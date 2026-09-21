import streamlit as st
from PIL import Image
import numpy as np
import cv2

st.set_page_config(page_title="Malek AI - 8 Point QC", layout="centered", page_icon="✅")

# --- CSS ---
st.markdown("""
<style>
.qc-card { background: white; padding: 18px; border-radius: 12px; border: 1px solid #e5e7eb; margin-bottom: 10px; box-shadow: 0 2px 8px rgba(0,0,0,0.05); }
.pass { color: #16a34a; font-weight: 800; }
.fail { color: #dc2626; font-weight: 800; }
.check { color: #f59e0b; font-weight: 800; }
</style>
""", unsafe_allow_html=True)

st.title("Malek AI - 8 Point QC Expert")
st.caption("Bangladesh's First AI Fabric Inspector | Made by Malek")

uploaded = st.file_uploader("ফেব্রিকের ছবি আপলোড করো মামা", type=["jpg","jpeg","png"])

if not uploaded:
    st.info("একটা ছবি দাও, আমি ৮ টা পয়েন্ট চেক করে দেবো।")
    st.stop()

# Load
img_pil = Image.open(uploaded).convert("RGB")
img = np.array(img_pil)
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
h, w = gray.shape

st.image(img_pil, caption="Original Fabric", use_container_width=True)

# --- 8 POINT QC LOGIC ---

# 1. Spot / Dag
dark_pixels = np.sum(gray < 35)
spot_percent = (dark_pixels / (h*w)) * 100
spot_status = "PASS" if spot_percent < 0.05 else "FAIL" if spot_percent > 0.3 else "CHECK"

# 2. Shade Variation
std_dev = np.std(gray)
shade_status = "PASS" if std_dev < 18 else "FAIL" if std_dev > 35 else "CHECK"

# 3. Brightness / Dyeing
mean_bright = np.mean(gray)
bright_status = "PASS" if 80 < mean_bright < 180 else "CHECK"

# 4. Holes / Chera
# Adaptive threshold for holes
_, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
holes = cv2.countNonZero(thresh < 10)
hole_status = "PASS" if holes < 50 else "FAIL"

# 5. Crease / Kuckano
edges = cv2.Canny(gray, 50, 150)
crease_density = (np.sum(edges > 0) / (h*w)) * 100
crease_status = "PASS" if crease_density < 8 else "CHECK"

# 6. GSM Uniformity (texture variance)
laplacian = cv2.Laplacian(gray, cv2.CV_64F).var()
gsm_status = "PASS" if laplacian > 100 else "CHECK"

# 7. Color Evenness (split image 4 parts)
parts = [gray[:h//2, :w//2], gray[:h//2, w//2:], gray[h//2:, :w//2], gray[h//2:, w//2:]]
means = [np.mean(p) for p in parts]
color_diff = max(means) - min(means)
color_status = "PASS" if color_diff < 15 else "FAIL" if color_diff > 30 else "CHECK"

# 8. Overall Cleanliness
overall_score = 100 - (spot_percent*10 + (std_dev/2) + (color_diff/2) + (crease_density))
overall_score = int(max(10, min(99, overall_score)))

if overall_score >= 80 and spot_status!="FAIL" and hole_status!="FAIL":
    final_result = "QC PASS"
    final_color = "pass"
else:
    if spot_percent > 0.5 or holes > 100:
        final_result = "QC REJECT"
        final_color = "fail"
    else:
        final_result = "QC HOLD / RE-CHECK"
        final_color = "check"

# --- RESULT UI ---
st.divider()
st.markdown(f"<h1 class='{final_color}' style='text-align:center;'>{final_result} - {overall_score}%</h1>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown(f"""
    <div class="qc-card">1. দাগ (Spots): <span class="{spot_status.lower()}">{spot_status} ({spot_percent:.3f}%)</span></div>
    <div class="qc-card">2. শেড ভ্যারিয়েশন: <span class="{shade_status.lower()}">{shade_status} ({std_dev:.1f})</span></div>
    <div class="qc-card">3. ডাইং / উজ্জ্বলতা: <span class="{bright_status.lower()}">{bright_status} ({mean_bright:.0f})</span></div>
    <div class="qc-card">4. ছিদ্র (Holes): <span class="{hole_status.lower()}">{hole_status}</span></div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown(f"""
    <div class="qc-card">5. কুঁচকানো (Crease): <span class="{crease_status.lower()}">{crease_status} ({crease_density:.1f}%)</span></div>
    <div class="qc-card">6. GSM / টেক্সচার: <span class="{gsm_status.lower()}">{gsm_status} ({laplacian:.0f})</span></div>
    <div class="qc-card">7. কালার ইভেননেস: <span class="{color_status.lower()}">{color_status} ({color_diff:.0f})</span></div>
    <div class="qc-card">8. ফাইনাল স্কোর: <b>{overall_score}%</b></div>
    """, unsafe_allow_html=True)

if final_result == "QC PASS":
    st.success("মামা কাপড় ১০০% ওকে! বায়ারকে পাস দিয়ে দাও।")
elif final_result == "QC REJECT":
    st.error("মামা এইটা বাতিল! দাগ/ছিদ্র আছে, বায়ার রিজেক্ট করবে।")
else:
    st.warning("মামা আরেকবার নিজের চোখে চেক করো, সন্দেহ আছে।")
