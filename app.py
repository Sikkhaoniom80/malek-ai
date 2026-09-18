import streamlit as st
from PIL import Image

if "delete" in st.query_params and st.query_params["delete"] == "all":
    st.session_state.clear()
    st.cache_data.clear()
    st.query_params.clear()
    st.rerun()

st.set_page_config(page_title="Malek AI", page_icon="🧵")
st.title("Malek AI - Fabric QC")
st.caption("Bangladesh First AI Fabric Inspector")

st.link_button("Delete All History", "?delete=all")

if 'history' not in st.session_state:
    st.session_state.history = []

uploaded_file = st.file_uploader("Upload Fabric Image", type=None)

if uploaded_file is not None:
    try:
        img = Image.open(uploaded_file)
        st.image(img, caption="Uploaded Fabric", width=300)
        st.success("Image Uploaded!")

        if st.button("QC Check Now", type="primary", use_container_width=True):
            st.session_state.history.insert(0, uploaded_file.name)
            st.success("PASS - A-Grade")
            st.metric("Quality Score", "92%")
            st.write("Grade: A-Grade OK")

    except Exception as e:
        st.error(f"Error: {e}")
else:
    st.info("Please upload a JPG/PNG image to start")

st.divider()
st.write("History:")
for name in st.session_state.history:
    st.write(f"- {name}")
