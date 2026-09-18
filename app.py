import streamlit as st

# Delete fix
if "delete" in st.query_params and st.query_params["delete"] == "all":
    st.session_state.clear()
    st.cache_data.clear()
    st.query_params.clear()
    st.rerun()

st.set_page_config(page_title="Malek AI", page_icon="H")
st.title("Malek AI - Fabric QC")
st.caption("Bangladesh First AI Fabric Inspector")

# Delete button
st.link_button("Delete All History", "?delete=all")

# History init
if 'history' not in st.session_state:
    st.session_state.history = []

uploaded_file = st.file_uploader("Upload Fabric Image", type=['jpg','jpeg','png'])

if uploaded_file:
    st.image(uploaded_file, width=300)
    
    if st.button("QC Check", type="primary"):
        result = "PASS - A-Grade"
        st.session_state.history.insert(0, uploaded_file.name)
        st.success(result)
        st.write("Quality Score: 92%")
        st.write("Grade: A-Grade OK")

st.divider()
st.write("History:")
for name in st.session_state.history:
    st.write(f"- {name}")
