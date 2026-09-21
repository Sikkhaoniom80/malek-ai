import streamlit as st
from PIL import Image
import numpy as np
import cv2

st.set_page_config(page_title="Malek AI - 8 Point QC", layout="centered")

st.title("✅ Malek AI - 8 Point Fabric QC")
st.caption("Real QC - No AI API, No Random")

uploaded = st.file_uploader("ফেব্রিকের ছবি দাও মামা", type=["jpg","png","jpeg"])

if uploaded:
    img_pil = Image.open(uploaded).convert("RGB")
    img = np.array(img_pil)
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    h,w = gray.shape
    
    st.image(img_pil, use_container_width=True)
    
    dark = np.sum(gray < 35) / (h*w) * 100
    std = np.std(gray)
    mean = np.mean(gray)
    edges = cv2.Canny(gray, 50, 150)
    crease = np.sum(edges>0)/(h*w)*100
    lap = cv2.Laplacian(gray, cv2.CV_64F).var()
    
    score = 100 - (dark*8 + std/2 + crease/2)
    score = int(max(10, min(98, score)))
    
    if dark < 0.05 and std < 20:
        result = "QC PASS"
        st.success(f"{result} - {score}% - মামা কাপড় ওকে!")
    elif dark > 0.3:
        result = "QC REJECT"
        st.error(f"{result} - {score}% - মামা দাগ আছে, বাতিল!")
    else:
        result = "QC HOLD"
        st.warning(f"{result} - {score}% - মামা আরেকবার চেক করো।")
    
    st.write(f"দাগ: {dark:.3f}% | শেড: {std:.1f} | উজ্জ্বলতা: {mean:.0f} | কুঁচকানো: {crease:.1f}%")
else:
    st.info("ছবি আপলোড করো মামা")
